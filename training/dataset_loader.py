import os
from PIL import Image
import numpy as np
import tensorflow as tf

def load_and_split_dataset(dataset_root, data_types=('.jpg', '.png'), exclude_class_limit=3, image_size=(224, 224), train_size=0.7):
    assert 0 <= train_size <= 1, "train_size should be between 0 (included) and 1.0 (included)"
    
    x, y, excluded_classes = load_images(dataset_root, data_types, exclude_class_limit, image_size)

    # Transformation des labels en entier
    labels = np.unique(y)
    int_y = []
    for value in y:
        int_y.append(np.where(labels == value))
    y = np.array(int_y)
    y = np.reshape(y, (len(y), ))

#     print(x.shape)
#     print(y.shape)
#     print(labels)
    
    # Mélange du dataset
    shuffled_indices = np.arange(len(x))
    np.random.shuffle(shuffled_indices)
    x = x[shuffled_indices]
    y = y[shuffled_indices]

    # Séparation en test et entraînement 30/70
    split_indice = int(train_size * len(x))
    x_train = x[:split_indice]
    y_train = y[:split_indice]
    x_test = x[split_indice:]
    y_test = y[split_indice:]
#     print(x_train.shape)
#     print(x_test.shape)
    
    return x_train, y_train, x_test, y_test, excluded_classes


def load_images(dataset_root, data_types, exclude_class_limit, image_size):
    x = []
    y = []
    excluded_classes = []
    # Récupération des images et des labels
    for dirpath, directories, files in os.walk(dataset_root):
        if len(files) < exclude_class_limit:
            excluded_classes.append((os.path.basename(dirpath), len(files)))
        else:
            for file in files:
                if any(data_type in file for data_type in data_types):
                #if '.jpg' in file or '.png' in file:
                    img = np.array(Image.open(os.path.join(dirpath, file)).resize(image_size).convert("RGB"))
                    x.append(img)
                    label = os.path.basename(dirpath)
                    y.append(label)
    x = np.array(x)
    y = np.array(y)
    
    return x, y, excluded_classes

# class Dataset: