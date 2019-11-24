"""
Script de lancement de l'API pour la classification de cristaux.
"""

from flask import Flask, request, redirect, url_for, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from classifier import Classifier
import json
import random
from PIL import Image

port = 5000

UPLOAD_FOLDER = '/upload'
BD_FOLDER = '/custom-dataset'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['BD_FOLDER'] = BD_FOLDER
CORS(app)

classifier = Classifier()

users = []
with open('users.json') as f:
    users = json.load(f)["users"]


@app.route('/')
def get_index():
    """
    Cette route est la route par defaut, elle permet de renvoyer un micro-page d'acceuil de l'API.

    :return: Un templates HTML d'une micro-page d'acceuil.
    """
    return render_template('index.html')


@app.route('/classification_cristaux/classerCristal/<type_of_image>', methods=['GET', 'POST'])
def get_classe_cristal(type_of_image):
    """
    Cette route permet de recuperer la photo d'un cristal envoye par l'utilisateur et de renvoyer la classe
    du cristal.

    :param: type_of_image: String (SEC = section or SUR = surface)
    :return: String correspondant soit a la classification du cristal soit a un message d'erreur
    """
    if request.method == 'POST':
        image_path = get_image_from_post(request, app.config['UPLOAD_FOLDER'])
        if type_of_image == 'SEC':
            classifier.set_type_of_image("SEC")
        else:
            classifier.set_type_of_image("SUR")
        if image_path != -1:
            prediction = classifier.get_prediction(image_path)
            return prediction
        else:
            return 'No image found'
    else:
        return 'Bad request, POST expected'


@app.route('/classification_cristaux/chargerCristal', methods=['GET', 'POST'])
def upload_cristal():
    """
    Cette route a pour but de recuperer le cristal ainsi que la classification verifiee par l'utilisateur
    dans le but d'agrandir le dataset.

    :return: String correspondant a un message d'acceptation ou d'une erreur
    """
    if request.method == 'POST':
        # Authentification
        if not auth():
            return 'Bad authentification, go back !'

        classe = request.form['classe']
        type = request.form['type']
        image_name = str(classe) + "_" + str(type) + "_" + str(random.randint(0, 10**20)) + ".jpg"
        file_path = get_image_from_post(request, app.config['BD_FOLDER'], filename=image_name)
        if file_path != -1:
            print(image_name)
            return "Thank you for the cristal"
        else:
            return "No image found"
    else:
        return 'Bad request, POST expected'


def get_image_from_post(http_request, directory, filename=None):
    """
    Cette fonction permet de recuperer la requete POST et d'en extraire une image.

    :param http_request: La requete POST qui contient potentiellement une image.
    :param directory: String vers le dossier de sauvegarde de l'image
    :param filename: String pour le nom de l'image
    :return: -1 si il n'y a pas d'image ou String contenant le chemin de sauvegarde de l'image
    """
    # check if the post request has the file part
    if 'image' not in http_request.files:
        return -1
    file = http_request.files['image']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        return -1

    if file:
        img = Image.open(file)
        img = img.convert('RGB')
        if filename is None:
            filename = secure_filename(file.filename)
        img.save(os.path.join(directory, filename.split('.')[0] + '.jpg'))
        return os.path.join(directory, filename.split('.')[0] + '.jpg')


def auth():
    """
    Cette fonction permet de vérifier que le header d'authentification contient bien le bon username et le bon
    mot de passe.

    :return: Boolean selon la reussite de l'euthentification
    """
    username = request.form["username"]
    password = request.form["password"]
    if users.get(username, None) is None:
        return False
    elif users[username] != password:
        return False
    return True


if __name__ == '__main__':
    app.run(port=port)
