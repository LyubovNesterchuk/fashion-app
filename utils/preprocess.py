import numpy as np

from tensorflow.keras.applications.vgg16 import preprocess_input

from config import CNN_SIZE, VGG_SIZE


# Підготовка зображення

def preprocess_for_cnn(image):

    image = image.convert("L")

    image = image.resize(
        (CNN_SIZE, CNN_SIZE)
    )

    image = np.asarray(
        image,
        dtype=np.float32,
    )

    image /= 255.0

    image = image.reshape(
        1,
        CNN_SIZE,
        CNN_SIZE,
        1,
    )

    return image



def preprocess_for_vgg(image):

    image = image.convert("RGB")

    image = image.resize(
        (VGG_SIZE, VGG_SIZE)
    )

    image = np.asarray(
        image,
        dtype=np.float32,
    )

    image = preprocess_input(image)

    image = np.expand_dims(
        image,
        axis=0,
    )

    return image


# Автоматичний вибір препроцесингу.

def preprocess_image(image, model_name):
  
    if model_name == "CNN":
        return preprocess_for_cnn(image)

    return preprocess_for_vgg(image)