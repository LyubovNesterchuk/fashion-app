import numpy as np

from config import CLASS_NAMES


def predict(model, image):

    prediction = model.predict(image, verbose=0)

    index = int(np.argmax(prediction))

    confidence = float(prediction[0][index])

    return {
        "prediction": prediction,
        "class_index": index,
        "class_name": CLASS_NAMES[index],
        "confidence": confidence,
    }