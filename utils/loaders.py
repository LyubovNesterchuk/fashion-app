import pickle

import streamlit as st
from tensorflow.keras.models import load_model

from utils.download_model import download_vgg_model
from pathlib import Path

vgg_path = Path(download_vgg_model())
# vgg_path = download_vgg_model()

# vgg_model = load_model(vgg_path)

from config import (
    CNN_HISTORY,
    CNN_MODEL,
    STYLE_FILE,
    VGG_HISTORY,
    # VGG_MODEL,
)


# @st.cache_resource(show_spinner=False)
# def load_model_by_name(model_name: str):
#     """
#     Завантаження нейронної мережі.
#     """

#     if model_name == "CNN":
#         path = CNN_MODEL
#     else:
#         # path = VGG_MODEL
#         path =vgg_model
#     if not path.exists():
#         raise FileNotFoundError(
#             f"Модель не знайдена:\n{path}"
#         )

#     return load_model(path)
@st.cache_resource(show_spinner=False)
def load_model_by_name(model_name: str):
    if model_name == "CNN":
        path = CNN_MODEL
    else:
        path = vgg_path

    if not path.exists():
        raise FileNotFoundError(f"Модель не знайдена:\n{path}")

    return load_model(path)

@st.cache_data(show_spinner=False)
def load_history(model_name: str):
    """
    Завантаження history моделі.
    """

    if model_name == "CNN":
        path = CNN_HISTORY
    else:
        path = VGG_HISTORY

    if not path.exists():
        raise FileNotFoundError(
            f"History не знайдено:\n{path}"
        )

    with open(path, "rb") as file:
        history = pickle.load(file)

    return history


def load_css():
    """
    Підключення CSS.
    """

    if not STYLE_FILE.exists():
        return

    with open(STYLE_FILE, encoding="utf-8") as css:

        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )