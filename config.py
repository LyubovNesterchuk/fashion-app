from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR / "models"
HISTORY_DIR = BASE_DIR / "history"
STYLE_DIR = BASE_DIR / "styles"
EXAMPLES_DIR = BASE_DIR / "example_images"


CNN_MODEL = MODELS_DIR / "fashion_mnist_cnn.keras"
VGG_MODEL = MODELS_DIR / "fashion_mnist_vgg16.keras"

CNN_HISTORY = HISTORY_DIR / "fashion_mnist_cnn_history.pkl"
VGG_HISTORY = HISTORY_DIR / "fashion_mnist_vgg16_history.pkl"


STYLE_FILE = STYLE_DIR / "style.css"

CNN_SIZE = 28
VGG_SIZE = 96


CLASS_NAMES = [
    "🥾 Ankle boot",
    "👜 Bag",
    "👗 Dress",
    "🧥 Coat", 
    "🧥 Pullover",
    "👡 Sandal",
    "👔 Shirt",
    "👟 Sneaker",
    "👕 T-shirt/top",
    "👖 Trouser",   
    
]

EXAMPLES = [
    "Немає",
    "ankle_boot.png",
    "bag.png",
    "bag2.png",
    "coat.png",
    "dress.png",
    "pullover.png", 
    "sandal.png",
    "shirt.png",
    "sneaker.png",
    "top.png",
    "trouser.png",
    "tshirt.png", 
]