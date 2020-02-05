"""
Script qui recupere les images originales du dataset et qui y applique des transformations de rotation et de
transposition pour demultiplier le dataset original.
"""

from PIL import Image
from os import listdir


def list_files_from_directory(directory="img/", extension="jpg"):
    """
    List les noms des fichiers contenus dans le repertoire directory qui ont l'extension extension.

    :param directory: String chemin vers le repertoire a lister (absolu ou relatif) (par defaut "img/")
    :param extension: String extension des fichiers a lister (par defaut "jpg")
    :return: List de String des noms des fichiers listes
    """
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
