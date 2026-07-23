import os
import urllib.request

MODEL_URL = (
    "https://huggingface.co/Lyubovn/"
    "fashion-mnist-vgg16/resolve/main/fashion_mnist_vgg16.keras"
)

MODEL_PATH = "models/fashion_mnist_vgg16.keras"


def download_vgg_model():
    os.makedirs("models", exist_ok=True)

    if not os.path.exists(MODEL_PATH):
        print("Downloading VGG16 model...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("Done!")

    return MODEL_PATH