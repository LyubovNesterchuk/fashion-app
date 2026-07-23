import streamlit as st


def sidebar():

    st.sidebar.header("⚙️ Налаштування")

    selected_model = st.sidebar.radio(
        "Оберіть модель",
        ["CNN", "VGG16"],
    )

    st.sidebar.divider()

    example = st.sidebar.selectbox(
        "Приклад зображення",
        [
            "Немає",
            "tshirt.png",
            "sneaker.png",
            "bag.png",
            "dress.png",   
            "trouser.png",
            "pullover.png",
            "coat.png",
            "sandal.png",
            "shirt.png",
            "ankle_boot.png"
        ],
    )

    st.sidebar.divider()

    st.sidebar.info(
        """
### CNN

Власна згорткова мережа.

### VGG16

Transfer Learning на основі VGG16.
"""
    )

    return selected_model, example