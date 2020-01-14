# Keras
import tensorflow as tf
import tensorflow.compat.v1.keras as keras

# Image libraries
from PIL import Image

# Helper libraries
import numpy as np
import joblib


class Classifier:

    def __init__(self):
        self.sess = tf.compat.v1.Session()
        tf.compat.v1.keras.backend.set_session(self.sess)
        self.vgg16 = keras.applications.vgg16.VGG16(include_top=False, weights='imagenet')
        self.vgg16.trainable = False
        self.vgg16._make_predict_function()
        self.graph = tf.compat.v1.get_default_graph()
        self.model = joblib.load('./0.907_2019-05-11 11-54-50.466169')
        self.class_names = ['IIIb', 'IIb', 'Ia', 'Autre']
        with self.graph.as_default():
            with self.sess.as_default():
                print("neural network initialised")

    def set_type_of_image(self, type_of_image): #FIXME Why models aren't differents?
        if type_of_image == 'SEC':
            self.model = joblib.load('./0.907_2019-05-11 11-54-50.466169')
        else:
            self.model = joblib.load('./0.907_2019-05-11 11-54-50.466169')

    def _preprocess_img(self, img_path):
        with self.graph.as_default():
            with self.sess.as_default():
                img = np.array(Image.open(img_path).resize((500, 500)))
                img_array = [img/255.0]
                img_array = np.array(img_array)
                print(img_array.shape)
                with self.graph.as_default():
                    tf.compat.v1.keras.backend.set_session(self.sess)
                    img_features = self.vgg16.predict(img_array)
                    new_img_features = []
                    for feature in img_features:
                        new_img_features.append(feature.flatten())
                img_features = np.array(new_img_features)
                print("vgg16 done")
        return img_features

    def _classifier_img(self, img_features):
        prediction = self.model.predict(img_features)
        return prediction[0]

    def get_prediction(self, img_path):
        img_features = self._preprocess_img(img_path)
        prediction = self._classifier_img(img_features)
        return self.class_names[prediction]
