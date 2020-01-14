FROM tensorflow/tensorflow:2.1.0-py3

WORKDIR /code

ENV FLASK_APP=app.py FLASK_RUN_HOST=0.0.0.0

COPY ./api/requirements.txt .

RUN pip install -r requirements.txt

COPY ./api .
COPY ./models/ ./models/

# Define volumes for:
#   - the dataset (used for training),
#   - kidney stone images (uploaded on the API),
#   - kidney stone images (labeled by user to enlarge dataset)
#   - cache for keras model (otherwise it's downloaded every time the image is changed)
VOLUME /dataset /upload /custom-dataset /root/.keras

EXPOSE 5000

CMD ["flask", "run"]
