"""
Script qui recupere les images originales du dataset et qui y applique des transformations de rotation et de
transposition pour demultiplier le dataset original.
"""

from PIL import Image
from os import listdir

import numpy as np
import skimage.io as io
from skimage.transform import rotate, AffineTransform, warp
from skimage.util import random_noise
from skimage.filters import gaussian


def list_files_from_directory(directory="img/", extension="jpg"):
    """
    List les noms des fichiers contenus dans le repertoire directory qui ont l'extension extension.

    :param directory: String chemin vers le repertoire a lister (absolu ou relatif) (par defaut "img/")
    :param extension: String extension des fichiers a lister (par defaut "jpg")
    :return: List de String des noms des fichiers listes
    """u
    return list(f for f in listdir(directory) if f.endswith('.' + extension))


def demultiplier_image(img_name, img_directory, directory_new_dataset, number_of_rotation):
    """
    Ouvre l'image contenue au chemin img_directory+img_name, et applique des transformations a l'image
    qui est sauvegarde dans le repertoire directory_new_dataset.
    On applique number_of_rotation rotations de 360/number_of_rotation a l'image originale et on recommence
    le processus apres avoir creer une image miroir. En utilisant cette fonction, on obtient donc
    number_of_rotation*2 nouvelles images.

    :param img_name: String nom de l'image originale
    :param img_directory: String chemin vers le repertoire de l'image originale (absolu ou relatif)
    :param directory_new_dataset: String chemin vers le repertoire de sauvegarde (absolu ou relatif)
    :param number_of_rotation: nombre de rotation a appliquer
    """
    original_img = Image.open(img_directory + img_name)
    original_img.save(directory_new_dataset + img_name.split(".")[0] + "_1" + ".jpg")

    nb_image = 1

    for i in range(number_of_rotation):
        rotation = (360 / number_of_rotation) * i
        new_im = original_img.rotate(rotation)
        new_im.save(directory_new_dataset + img_name.split(".")[0] + "_" + str(nb_image+1) + ".jpg")
        nb_image += 1

    new_im = new_im.transpose(Image.FLIP_LEFT_RIGHT)

    for i in range(number_of_rotation):
        rotation = (360 / number_of_rotation) * i
        new_im = original_img.rotate(rotation)
        new_im.save(directory_new_dataset + img_name.split(".")[0] + "_" + str(nb_image+1) + ".jpg")
        nb_image += 1

        
# ============ FIXME ================
# How will the dataset param look like: simple list of images or tuple (image, class) ?

# ------------------------------------------------------------------------------------------
# All demultiplication functions are based off a tutorial of image augmentation found here :
# https://www.analyticsvidhya.com/blog/2019/12/image-augmentation-deep-learning-pytorch/
        
def rotate_dataset(dataset, angle):
    """
    Apply a rotation of given angle to all images in the dataset, returning the dataset plus the rotated ones.
    
    :param dataset: list of dataset images
    :param angle: angle of rotation to apply to images
    """
    new_dataset = list()
    for image, label in dataset:
        # Mode as ‘wrap’ fills the points outside the boundaries of the input with the remaining pixels of the image.
        new_image = rotate(image, angle=angle, mode='wrap')
        new_dataset.append((new_image, label))
    return np.concatenate((np.array(new_dataset), dataset))


def flip_dataset(dataset, horizontal=True):
    """
    Flip all images in the dataset, whether horizontally or vertically, returning the dataset plus the flipped ones.
    
    :param dataset: list of dataset images
    :param horizontal: flip images horizontally if True, vertically otherwise
    """
    new_dataset = list()
    if horizontal:
        for image, label in dataset:
            new_image = np.fliplr(image)
            new_dataset.append((new_image, label))
    else:
        for image, label in dataset:
            new_image = np.flipud(image)
            new_dataset.append((new_image, label))
    return np.concatenate((np.array(new_dataset), dataset))


def noising_dataset(dataset):
    """
    Add some random noise to all images in the dataset, returning the dataset plus the noised ones.
    
    :param dataset: list of dataset images
    """
    new_dataset = list()
    sigma = 0.155
    for image, label in dataset:
        new_image = random_noise(image, var=sigma**2)
        new_dataset.append((new_image, label))
    return np.concatenate((np.array(new_dataset), dataset))


def blurring_dataset(dataset):
    """
    Blur images in the dataset, returning the dataset plus the blurred ones.
    
    :param dataset: list of dataset images
    """
    new_dataset = list()
    for image, label in dataset:
        # Setting Multichannel to true ensures that each channel of the image is filtered separately.
        new_image = gaussian(image, sigma=1, multichannel=True)
        new_dataset.append((new_image, label))
    return np.concatenate((np.array(new_dataset), dataset))


def demultiplier(dataset):
    dataset = rotate_dataset(dataset, 90)
    # print("rotate", dataset.shape)
    dataset = flip_dataset(dataset)
    # print("flip", dataset.shape)
    dataset = flip_dataset(dataset, False)
    # print("flip vertical", dataset.shape)
    dataset = rotate_dataset(dataset, 45)
    # print("rotate 45", dataset.shape)
#     dataset = translate_dataset(dataset, #param)
    dataset = noising_dataset(dataset)
    # print("noise", dataset.shape)
    dataset = blurring_dataset(dataset)
    # print("blur", dataset.shape)
    return dataset
    

#On recupere la liste des chemins vers les images du dataset originale
#img_list = list_files_from_directory()
#nb_original_img = len(img_list)

#On itere sur toutes les images pour les chargers et les demultiplier
#index = 0
#for img_path in img_list:
#    print(str(index) + " / " + str(nb_original_img))
#    demultiplier_image(img_path, "img/", "new_img/", 4)
#    index += 1

#index = 0
#img_list = list_files_from_directory(directory="../dataset_calculs", extension="jpg")
#nb_original_img = len(img_list)
#for img_path in img_list:
#    print(str(index) + " / " + str(nb_original_img))
#    original_img = Image.open("../dataset_calculs/" + img_path)
#    original_img = original_img.convert('RGB')
#    original_img.save("../dataset/" + img_path.split('.')[0] + ".jpg")
#    index += 1
