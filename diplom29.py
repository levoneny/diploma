import streamlit as st
from datetime import date

def main():
    # Настройка параметров страницы
    st.set_page_config(page_title="Административная панель", layout="wide")

    # Шапка с навигацией
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
            margin: 0 10px;
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
        <div class="logo">Лого</div>
        <div class="nav-links">
            <a href="#">Игры</a>
            <a href="#">Пользователи</a>
            <a href="#">Платежи</a>
            <a href="#">Аналитика</a>
            <a href="#">Служба поддержки</a>
        </div>
        <div class="profile">
            <a href="#">Профиль</a>
            <div class="divider"></div>
            <a href="#">Выйти</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Заголовок страницы
    st.title("Добавление игры")

    # Форма для добавления игры
    with st.form("game_form"):
        game_name = st.text_input("Введите название игры*")
        game_description = st.text_area("Введите описание к игре*", height=120, max_chars=500)
        system_requirements = st.text_area("Введите системные требования*", height=100, max_chars=300)
        
        # Поле для цены с выбором валюты
        col1, col2 = st.columns([3, 1])  # Настройка колонок
        with col1:
            price = st.text_input("Введите цену игры*", value="0.00")  # Ввод цены
        with col2:
            currency = st.selectbox("Введите валюту*", ["USD", "EUR"])  # Выбор валюты

        release_date = st.date_input("Введите дату выхода игры*", date.today())
        genres = st.multiselect(
            "Выберите жанр(ы) игры*", 
            options=["Экшн", "Приключения", "RPG", "Стратегия", "Симуляторы", "Шутер", "Головоломка", "Хоррор", "Спорт", "Аркада"]
        )
        cover_image = st.file_uploader("Загрузите обложку игры*", type=["jpg", "jpeg", "png"])

        # Кнопки на одной линии справа
        col1, col2 = st.columns([6, 2])  # Ширина колонок настроена так, чтобы разместить кнопки справа
        with col2:
            col2_1, col2_2 = st.columns([1, 1])  # Внутренняя настройка для равного пространства между кнопками
            with col2_1:
                submit_button = st.form_submit_button("Добавить")  # Кнопка "Добавить"
            with col2_2:
                cancel_button = st.form_submit_button("Отменить")  # Кнопка "Отменить"

    # Обработка отправки формы
    if submit_button:
        st.success(f"Игра '{game_name}' успешно добавлена!")
        st.write(f"Цена: {price} {currency}")  # Отображение цены с валютой
        if cover_image:
            st.image(cover_image, width=300, caption=game_name)

    # Подвал страницы
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
        <div class="logo">Лого</div>
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






