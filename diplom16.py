import streamlit as st

def main():
    # Настройка страницы
    st.set_page_config(page_title="Авторизация", layout="centered")

    # Заголовок страницы
    st.markdown("<h1 style='text-align: center;'>Вход</h1>", unsafe_allow_html=True)

    # Форма авторизации
    with st.form("login_form"):
        st.text_input("Введите никнейм*")  # Поле ввода никнейма
        st.text_input("Введите пароль*", type="password")  # Поле ввода пароля
        st.checkbox("Запомнить меня")  # Чекбокс "Запомнить меня"
        st.markdown("<a href='#' style='text-decoration: none; color: #007BFF;'>Забыли пароль?</a>", unsafe_allow_html=True)  # Ссылка на восстановление пароля

        # Кнопка входа
        col1, col2, col3 = st.columns([2, 4, 2])  # Центрирование кнопки
        with col2:
            submitted = st.form_submit_button("Войти")

        # Ссылка на регистрацию
        st.markdown("<p style='text-align: center;'>Нет аккаунта? <a href='#' style='text-decoration: none; color: #007BFF;'>Зарегистрируйтесь!</a></p>", unsafe_allow_html=True)

    # CSS стили для улучшения внешнего вида
    st.markdown("""
    <style>
        h1 {
            font-family: Arial, sans-serif;
            font-size: 28px;
            color: #333;
        }
        .stTextInput > div {
            margin-bottom: 15px; /* Уменьшение расстояния между полями */
        }
        .stButton button {
            font-size: 18px; /* Увеличение размера текста кнопки */
            padding: 10px 25px; /* Увеличение размера кнопки */
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()





