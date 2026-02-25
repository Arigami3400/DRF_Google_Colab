import streamlit as st
import requests

st.title("Предсказание выживания (Titanic)")
api_url = "http://127.0.0.1:8000/predict_titanic/"

Pclass = st.selectbox("Класс билета", [1, 2, 3])
Sex = st.selectbox("Пол", ["male", "female"])
Age = st.number_input("Возраст", 0)
SibSp = st.number_input("Братья/сестры или супруги", 0)
Parch = st.number_input("Родители/дети на борту", 0)
Fare = st.number_input("Стоимость билета", 0.0)
Embarked = st.selectbox("Порт посадки", ["C", "Q", "S"])


data = {
    "Pclass": Pclass,
    "Sex": Sex,
    "Age": Age,
    "SibSp": SibSp,
    "Parch": Parch,
    "Fare": Fare,
    "Embarked": Embarked

}

if st.button("Предсказать"):
    answer = requests.post(api_url, json=data, timeout=10)
    if answer.status_code == 200:
       result = answer.json()
       st.success(f"Результат: {result.get('Predict_survival')}")
    else:
       st.error(f'Ошибка: {answer.status_code}')
