# python -m venv .venv
# source .venv/Scripts/activate
# pip install streamlit tensorflow numpy pandas matplotlib pillow scikit-learn
# pip freeze > requirements.txt

# python --version
# pip list


import streamlit as st

from components.sidebar import sidebar
from components.uploader import upload_image
from components.prediction import predict
from components.charts import (
    probability_chart,
    probability_table,
    history_charts,
)

from utils.loaders import (
    load_css,
    load_history,
    load_model_by_name,
)

from utils.preprocess import preprocess_image

st.set_page_config(
    page_title="Fashion MNIST Classifier",
    page_icon="👕",
    layout="wide",
)

load_css()

st.title("👕 Fashion MNIST Image Classifier")

st.write(
    """
Завантажте зображення предмета одягу,
оберіть модель та отримайте прогноз.
"""
)


# Sidebar

selected_model, example = sidebar()


# Load model

with st.spinner("Завантаження моделі..."):

    model = load_model_by_name(selected_model)

    history = load_history(selected_model)


# Upload image

image = upload_image(example)

if image is None:

    st.info("Завантажте або виберіть приклад зображення.")

    st.stop()


# Display

left, right = st.columns(2)

with left:

    st.image(
        image,
        caption="Вхідне зображення",
        use_container_width=True,
    )

with right:

    st.write(f"**Модель:** {selected_model}")

    processed = preprocess_image(
        image,
        selected_model,
    )


# Prediction

with st.spinner("Класифікація..."):

    result = predict(
        model,
        processed,
    )

st.divider()

st.header("Результат")

c1, c2 = st.columns(2)

with c1:

    st.metric(
        "Передбачений клас",
        result["class_name"],
    )

with c2:

    st.metric(
        "Впевненість",
        f"{result['confidence']*100:.2f}%"
    )

st.divider()

probability_table(result["prediction"])

probability_chart(
    result["prediction"],
    result["class_index"],
)

st.divider()

history_charts(history)

# streamlit run app.py

# git init
# git add .
# git status
# git commit -m "Initial Streamlit Fashion MNIST app"
# git remote -v
# git push -u origin main


# ls -lh models
# total 121M
# -rw-r--r-- 1 Admin 197121 5.6M Jul 22 14:25 fashion_mnist_cnn.keras
# -rw-r--r-- 1 Admin 197121 116M Jul 22 18:50 fashion_mnist_vgg16.keras

# GitHub не дозволяє завантажувати файли більші за 100 MB. 
# fashion_mnist_vgg16.keras — 116 MB (перевищує ліміт)
# тому видали файл з Git (але залиш його на комп'ютері)
# git rm --cached models/fashion_mnist_vgg16.keras
# Додай його в .gitignore
# models/fashion_mnist_vgg16.keras
# Перекоміть зміни, знову відправ
# git add .gitignore
# git commit --amend --no-edit
# git push -u origin main

# рішення для розгортання на Streamlit Community Cloud, щоб
# застосунок автоматично завантажував VGG16 з Hugging Face без будь-яких додаткових дій користувача