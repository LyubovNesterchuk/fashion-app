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