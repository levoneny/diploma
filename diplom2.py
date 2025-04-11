import streamlit as st
from datetime import date

def main():
    # Настройка параметров страницы
    st.set_page_config(page_title="Административная панель", layout="wide")

    # Шапка с навигацией и логотипом
    st.markdown("""
    <style>
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #f1f1f1;
            border-bottom: 2px solid #ddd;
        }
        .header .nav-links {
            display: flex;
            flex-grow: 1;
            justify-content: space-around;
        }
        .header a {
            text-decoration: none;
            font-weight: bold;
            color: #333;
        }
        .header a:hover {
            color: #007BFF;
        }
        .logo {
            font-weight: bold;
            font-size: 20px;
            color: #333;
        }
    </style>
    <div class="header">
        <div class="logo">LOGO</div>
        <div class="nav-links">
            <a href="#">Игры</a>
            <a href="#">Пользователи</a>
            <a href="#">Платежи</a>
            <a href="#">Аналитика</a>
            <a href="#">Служба поддержки</a>
        </div>
        <div class="nav-links">
            <a href="#">Профиль</a>
            <a href="#">Выйти</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Заголовок страницы
    st.title("Добавление игры")
    st.write("Заполните форму ниже, чтобы добавить новую игру в систему:")

    # Форма для добавления игры
    with st.form("game_form"):
        game_name = st.text_input("Название игры*")
        game_description = st.text_area("Описание игры*", height=120, max_chars=500)
        system_requirements = st.text_area("Системные требования*", height=100, max_chars=300)
        price = st.text_input("Цена игры*")  # Убрана подсказка
        release_date = st.date_input("Дата выхода игры*", date.today())
        genres = st.multiselect(
            "Жанр(ы) игры*", 
            options=["Экшн", "Приключения", "RPG", "Стратегия", "Симуляторы", 
                     "Шутер", "Головоломка", "Хоррор", "Спорт", "Аркада"]
        )
        cover_image = st.file_uploader("Обложка игры*", type=["jpg", "jpeg", "png"])

        # Кнопки расположены справа
        col1, col2 = st.columns([8, 2])  # Ширина колонок для размещения кнопок справа
        with col2:
            submit_button = st.form_submit_button("Добавить")
            cancel_button = st.form_submit_button("Отменить")

    # Обработка отправки формы
    if submit_button:
        st.success(f"Игра '{game_name}' успешно добавлена!")
        if cover_image is not None:
            st.image(cover_image, width=300, caption=game_name)

    # Подвал с логотипом и ссылками
    st.markdown("""
    <style>
        .footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #f1f1f1;
            border-top: 2px solid #ddd;
            margin-top: 20px;
        }
        .footer .nav-links {
            display: flex;
            flex-grow: 1;
            justify-content: space-around;
        }
        .footer a {
            text-decoration: none;
            font-weight: bold;
            color: #333;
        }
        .footer a:hover {
            color: #007BFF;
        }
        .logo {
            font-weight: bold;
            font-size: 18px;
            color: #333;
        }
    </style>
    <div class="footer">
        <div class="logo">LOGO</div>
        <div class="nav-links">
            <a href="#">О системе</a>
            <a href="#">Политика конфиденциальности</a>
            <a href="#">Условия предоставления услуг</a>
            <a href="#">Правила возврата магазина</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()




