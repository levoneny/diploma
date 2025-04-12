import streamlit as st
from datetime import date

def main():
    # Настройка страницы
    st.set_page_config(page_title="Регистрация", layout="centered")

    # Заголовок страницы
    st.markdown("<h1 style='text-align: center;'>Регистрация</h1>", unsafe_allow_html=True)

    # Форма регистрации
    with st.form("registration_form"):
        # Поля формы
        country = st.selectbox(
            "Выберите страну проживания*",
            [
                "Беларусь", "Россия", "Казахстан", "Польша", "Украина", "Германия",
                "Франция", "Италия", "США", "Канада", "Китай", "Япония", "Индия",
                "Австралия", "Испания", "Южная Корея", "Бразилия", "Аргентина", "ЮАР"
            ]
        )
        city = st.text_input("Введите город проживания*")
        name = st.text_input("Введите ваше имя*")
        surname = st.text_input("Введите вашу фамилию*")
        birth = st.date_input("Введите вашу дату рождения*", date.today())
        email = st.text_input("Введите вашу электронную почту*", placeholder="XXXXX@XXX.XXX")
        phone = st.text_input("Введите ваш номер телефона*", placeholder="+3 (XXX) XXX-XX-XX")
        nickname = st.text_input("Придумайте никнейм*")
        password = st.text_input("Придумайте пароль*", type="password")
        password_repeat = st.text_input("Повторите пароль*", type="password")
        st.markdown("<span style='color: green;'>Пароль надежен</span>", unsafe_allow_html=True)
        generated_password = st.checkbox("Использовать сгенерированный браузером пароль")
        
        # Согласие с условиями
        agree_terms = st.checkbox("Согласен/согласна с Условиями предоставления услуг", value=False)
        agree_privacy = st.checkbox("Согласен/согласна с положениями Политики конфиденциальности", value=False)

        # Кнопка регистрации (расположена по центру)
        col1, col2, col3 = st.columns([3, 2, 3])  # Распределение колонок для центрирования
        with col2:
            submitted = st.form_submit_button("Зарегистрироваться")

        # Обработка результатов
        if submitted:
            if agree_terms and agree_privacy:
                st.success(f"Вы успешно зарегистрировались! Добро пожаловать, {nickname}.")
            else:
                st.error("Пожалуйста, примите условия предоставления услуг и положения Политики конфиденциальности.")

    # Стилизация через CSS
    st.markdown("""
    <style>
        h1 {
            font-family: Arial, sans-serif;
            font-size: 28px;
            color: #333;
        }
        .stTextInput > div, .stSelectbox > div, .stCheckbox > div {
            margin-bottom: 15px;
        }
        .stForm .stButton {
            margin-top: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()






