import streamlit as st
from datetime import date

def main():
    # Настройка параметров страницы
    st.set_page_config(page_title="Административная панель", layout="wide")

    # Верхняя панель навигации
    st.markdown("""
    <style>
        .nav-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #f1f1f1;
            border-bottom: 1px solid #ddd;
        }
        .nav-bar a {
            margin-right: 15px;
            text-decoration: none;
            font-weight: bold;
            color: #333;
        }
        .nav-bar a:hover {
            color: #007BFF;
        }
    </style>
    <div class="nav-bar">
        <div>
            <a href="#">Игры</a>
            <a href="#">Пользователи</a>
            <a href="#">Платежи</a>
            <a href="#">Аналитика</a>
            <a href="#">Служба поддержки</a>
        </div>
        <div>
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
        game_name = st.text_input("Введите название игры*")
        game_description = st.text_area("Введите описание к игре*", height=120)
        system_requirements = st.text_area("Введите системные требования*", height=100)
        price = st.number_input("Введите цену игры*", min_value=0.0, step=0.01, format="%.2f")
        release_date = st.date_input("Введите дату выхода игры*", date.today())
        genres = st.multiselect("Выберите жанр(ы) игры*", 
                                options=["Экшн", "Приключения", "RPG", "Стратегия", "Симуляторы"])
        cover_image = st.file_uploader("Загрузите обложку игры*", type=["jpg", "jpeg", "png"])

        # Кнопки отправки и отмены
        col1, col2 = st.columns(2)
        with col1:
            submit_button = st.form_submit_button("Добавить")
        with col2:
            cancel_button = st.form_submit_button("Отменить")

    # Обработка формы
    if submit_button:
        st.success(f"Игра '{game_name}' успешно добавлена!")
        if cover_image is not None:
            st.image(cover_image, width=300, caption=game_name)

if __name__ == '__main__':
    main()


