#!/usr/bin/env python
# coding: utf-8


import os
import datetime
# import re

import pandas as pd
# import skimage as ski
import numpy as np
# import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold

# tf.test.is_gpu_available()


def path(text):
    return os.path.join(*text.split("/"))

def annotate(ax):
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height() / 2 - 1),
                    ha='center', va='bottom', bbox={'color': 'white'})


# Parameters

DATASET_PATH = path("./dataset.csv")
KS_IMAGES_PATH = path("../../ksc-data/images")
FEATURES_PATH = path("./features/old.vgg19.npy")
RUNS_PATH = path("./runs")
RUN_ID = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
RUN_PATH = os.path.join(RUNS_PATH, RUN_ID)
os.makedirs(RUN_PATH, exist_ok=True)

SEED = 42
NKFOLD = 10
TRAIN_TEST_SPLIT_SIZE = 0.7
CLASSES = ['Ia', 'IIb', 'IIIb']
# CLASSES = None
WITH_OTHER = True  # If True, kidney stones which don't fall into preceding 'CLASSES' will be put in an 'Other' class

BATCH_SIZE = 64


# Dataset loading

df = pd.read_csv(DATASET_PATH)

POTENTIAL_CLASSES = df.stone_class.unique().tolist()
if CLASSES is None:
    CLASSES = POTENTIAL_CLASSES
    WITH_OTHER = False
    
LABELS = list(CLASSES)
if WITH_OTHER and not (CLASSES == POTENTIAL_CLASSES):
    LABELS += ['Other']

df['type_image'] = df.SEC.map(lambda x: 'SEC' if x else 'SUR')

filtered_df = df


rng = np.random.default_rng(SEED)
indices = filtered_df.index.values
rng.shuffle(indices)


features = np.load(FEATURES_PATH)
features.shape

X = features[indices]


def classes_mapper(y):
    try:
        return CLASSES.index(y)
    except Exception as e:
        if WITH_OTHER:
            return len(CLASSES)
        raise e


def inverse_class_mapper(pred):
    return (CLASSES + ['Other'] if WITH_OTHER else CLASSES)[pred]


shuffled_df = pd.DataFrame(filtered_df.iloc[indices])
shuffled_df['class_number'] = shuffled_df.stone_class.map(classes_mapper)


Y = shuffled_df.class_number.values

print(Y)


# Dataset spliting

skf = StratifiedKFold(n_splits=NKFOLD, shuffle=True, random_state=SEED)

for fold_idx, (train_indices, test_indices) in enumerate(skf.split(np.zeros(Y.shape), Y)):
    print("=========================================================================================")
    print(f"=================== Run '{RUN_ID}', Fold {fold_idx+1}/{NKFOLD} =========================")
    print("=========================================================================================")

    fig, axes = plt.subplots(figsize=(12, 8), nrows=2)
    shuffled_df.iloc[train_indices].groupby(['type_image', 'class_number']).count().stone_class.rename({i: v for i, v in enumerate(LABELS)}).plot.bar(title='Classes repartition (train set)', rot=0, xlabel='', ax=axes[0]);
    annotate(axes[0])

    shuffled_df.iloc[test_indices].groupby(['type_image', 'class_number']).count().stone_class.rename({i: v for i, v in enumerate(LABELS)}).plot.bar(title='Classes repartition (test set)', rot=0, xlabel='(Stone type, Stone class)', ax=axes[1]);
    annotate(axes[1])

    fig.savefig(os.path.join(RUN_PATH, f'fold_{fold_idx}.dataset_repartition.png'))


    X_train = X[train_indices]
    Y_train = Y[train_indices]

    Y_train = np.reshape(Y_train, (Y_train.shape[0], -1))
    Y_train = np.repeat(Y_train, X_train.shape[1], axis=-1)
    Y_train = np.reshape(Y_train, (-1,))
    print(f"Y_train.shape = {Y_train.shape}")

    X_train = np.reshape(X_train, (-1,) + X_train.shape[2:])
    X_train = np.reshape(X_train, (X_train.shape[0], -1))
    print(f"X_train.shape = {X_train.shape}")


    X_test = X[test_indices]
    Y_test = Y[test_indices]

    X_test = X_test[:, 0, ...]
    X_test = np.reshape(X_test, (-1,) + X_test.shape[1:])
    X_test = np.reshape(X_test, (X_test.shape[0], -1))
    print(f"X_test.shape = {X_test.shape}")

    print(f"Y_test.shape = {Y_test.shape}")


    # Model creation


    hidden_layers = (500,)
    nb_classes = len(LABELS)

    classifier = MLPClassifier(hidden_layers, batch_size=BATCH_SIZE, verbose=True, random_state=SEED)

    classifier.fit(X_train, Y_train)


    fig = plt.figure(figsize=(18,6))
    xticks = np.arange(classifier.n_iter_) + 1
    plt.plot(xticks, classifier.loss_curve_);
    # plt.yscale('log');
    plt.xticks(xticks);
    plt.xlabel('Epochs');
    plt.ylabel('Loss');
    fig.savefig(os.path.join(RUN_PATH, f'fold_{fold_idx}.loss_curve.png'))


    print(f"Classifier score: {classifier.score(X_test, Y_test)}")


    # Test model performances


    Y_pred = classifier.predict(X_test)

    print(classification_report(Y_test, Y_pred, labels=classifier.classes_, target_names=LABELS))

    classification_report_dict = classification_report(Y_test, Y_pred, labels=classifier.classes_, target_names=LABELS, output_dict=True)
    pd.DataFrame(classification_report_dict).to_csv(os.path.join(RUN_PATH, f"fold_{fold_idx}.classification_report.csv"), index=False)

    test_df = pd.DataFrame(shuffled_df.iloc[test_indices])

    test_df['y_pred'] = list(map(inverse_class_mapper, Y_pred))
    test_df['y_true'] = list(map(inverse_class_mapper, Y_test))
    test_df['correct'] = (Y_pred == Y_test).astype('int32')
    test_df.to_csv(os.path.join(RUN_PATH, f"fold_{fold_idx}.results.csv"))


    fig, axes = plt.subplots(figsize=(15,6), nrows=2)
    test_df[test_df.correct == 1].groupby(['type_image', 'y_true']).count().filename.plot.bar(rot=0, ax=axes[0], xlabel='', title='');
    test_df[test_df.correct == 0].groupby(['type_image', 'y_true']).count().filename.plot.bar(rot=0, ax=axes[1], xlabel='', title='');

    fig.savefig(os.path.join(RUN_PATH, f"fold_{fold_idx}.results_plot.png"))

