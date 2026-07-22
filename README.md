# Fashion MNIST Image Classification

## Опис

Веб-застосунок створений за допомогою Streamlit для класифікації предметів одягу з використанням згорткових нейронних мереж.

Проєкт містить дві моделі:

- CNN (власна згорткова нейронна мережа)
- VGG16 (Transfer Learning)

---

## Можливості

- вибір моделі CNN або VGG16;
- завантаження зображення;
- автоматична передобробка;
- прогноз класу;
- відображення впевненості моделі;
- таблиця ймовірностей;
- гістограма ймовірностей;
- графіки Accuracy і Loss.

---

## Структура проєкту

```
Fashion_App/
│
├── app.py
├── models/
├── history/
├── styles/
├── requirements.txt
└── README.md
```

---

## Встановлення

Створіть віртуальне середовище (рекомендовано):

```bash
python -m venv .venv
```

Активуйте його.

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

Встановіть бібліотеки

```bash
pip install -r requirements.txt
```

---

## Запуск

```bash
streamlit run app.py
```

---

## Використані технології

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pandas
- Matplotlib
- Pillow

---

## Автор

Lyubov Nesterchuk