import streamlit as st
from datetime import date

def main():
    # Настройка параметров страницы
    st.set_page_config(page_title="Административная панель", layout="wide")

    # Шапка с навигацией и логотипом, растянутая на всю ширину
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
            gap: 20px;
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
    </div>
    """, unsafe_allow_html=True)

    # Заголовок и описание
    st.title("Добавление игры")
    st.write("Заполните форму ниже, чтобы добавить новую игру в систему:")

    # Форма для добавления игры с расположением строго по макету
    with st.form("game_form"):
        # Поля формы
        game_name = st.text_input("Название игры*")
        game_description = st.text_area("Описание игры*", height=120, max_chars=500)
        system_requirements = st.text_area("Системные требования*", height=100, max_chars=300)
        price = st.text_input("Цена игры*", help="Введите цену без счётчика")
        release_date = st.date_input("Дата выхода игры*", date.today())
        genres = st.multiselect("Жанр(ы) игры*", options=["Экшн", "Приключения", "RPG", "Стратегия", "Симуляторы"])
        cover_image = st.file_uploader("Обложка игры*", type=["jpg", "jpeg", "png"])

        # Кнопки внизу формы, расположенные близко друг к другу
        col1, col2 = st.columns([0.8, 0.2])  # Настройка ширины колонок
        with col1:
            submit_button = st.form_submit_button("Добавить", help="Добавить игру в систему")
        with col2:
            cancel_button = st.form_submit_button("Отменить", help="Очистить форму")

    # Обработка отправки формы
    if submit_button:
        st.success(f"Игра '{game_name}' успешно добавлена!")
        if cover_image is not None:
            st.image(cover_image, width=300, caption=game_name)

    # Подвал страницы с логотипом и информацией
    st.markdown("""
    <style>
        .footer {
            text-align: center;
            padding: 10px 20px;
            background-color: #f1f1f1;
            border-top: 2px solid #ddd;
            margin-top: 20px;
        }
        .footer .logo {
            font-weight: bold;
            font-size: 18px;
            color: #333;
        }
    </style>
    <div class="footer">
        <div class="logo">LOGO</div>
        <p>© 2025 Административная панель. Все права защищены.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()



