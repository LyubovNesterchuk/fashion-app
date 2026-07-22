import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from config import CLASS_NAMES


def probability_chart(prediction, predicted_class):

    colors = [
        "green" if i == predicted_class else "skyblue"
        for i in range(len(CLASS_NAMES))
    ]

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.bar(
        CLASS_NAMES,
        prediction[0] * 100,
        color=colors,
    )

    ax.set_ylim(0, 100)

    ax.set_ylabel("Probability (%)")

    plt.xticks(rotation=45, ha="right")

    st.pyplot(fig)

    plt.close(fig)


def probability_table(prediction):

    df = pd.DataFrame(
        {
            "Клас": CLASS_NAMES,
            "Ймовірність (%)": (prediction[0] * 100).round(2),
        }
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )


def history_charts(history):

    col1, col2 = st.columns(2)

    with col1:

        fig, ax = plt.subplots(figsize=(6, 4))

        ax.plot(history["accuracy"], label="Train")

        ax.plot(history["val_accuracy"], label="Validation")

        ax.set_title("Accuracy")

        ax.legend()

        ax.grid()

        st.pyplot(fig)

        plt.close(fig)

    with col2:

        fig, ax = plt.subplots(figsize=(6, 4))

        ax.plot(history["loss"], label="Train")

        ax.plot(history["val_loss"], label="Validation")

        ax.set_title("Loss")

        ax.legend()

        ax.grid()

        st.pyplot(fig)

        plt.close(fig)