from PIL import Image
import streamlit as st

from config import EXAMPLES_DIR


def upload_image(example):

    uploaded = st.file_uploader(
        "Завантажте зображення",
        type=["png", "jpg", "jpeg"],
    )

    if uploaded is not None:
        return Image.open(uploaded)

    if example != "Немає":

        path = EXAMPLES_DIR / example

        if path.exists():
            return Image.open(path)

        st.error(f"Файл {example} не знайдено.")

    return None