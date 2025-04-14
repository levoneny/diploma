import streamlit as st
from datetime import date

# Функция для страницы регистрации
def registration_page():
    # Настройка страницы
    st.set_page_config(page_title="Регистрация", layout="centered")

    # Заголовок страницы
    st.markdown("<h1 style='text-align: center;'>Регистрация</h1>", unsafe_allow_html=True)

    # Форма регистрации
    with st.form("registration_form"):
        # Поля формы с уменьшенным расстоянием между ними
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

        # Кнопка регистрации (увеличен размер)
        col1, col2, col3 = st.columns([3, 3, 3])  # Центрирование кнопки
        with col2:
            submitted = st.form_submit_button(
                "Зарегистрироваться",
                help="Нажмите для завершения регистрации",
                use_container_width=True  # Увеличение кнопки для избежания переноса текста
            )

        # Обработка результатов
        if submitted:
            if agree_terms and agree_privacy:
                st.success(f"Вы успешно зарегистрировались! Добро пожаловать, {nickname}.")
            else:
                st.error("Пожалуйста, примите условия предоставления услуг и положения Политики конфиденциальности.")

    # Стилизация через CSS для уменьшения отступов
    st.markdown("""
    <style>
        h1 {
            font-family: Arial, sans-serif;
            font-size: 28px;
            color: #333;
        }
        .stTextInput > div, .stSelectbox > div, .stCheckbox > div {
            margin-bottom: 10px; /* Уменьшение расстояния между полями */
        }
        .stButton button {
            font-size: 18px; /* Увеличение размера текста кнопки */
            padding: 10px 25px; /* Увеличение размера кнопки */
        }
    </style>
    """, unsafe_allow_html=True)
    if st.button("Зарегистрироваться"):
        st.session_state.page = "authorization"

# Функция для страницы авторизации
def authorization_page():
    # Настройка страницы
    st.set_page_config(page_title="Авторизация", layout="centered")

    # Заголовок страницы
    st.markdown("<h1 style='text-align: center;'>Вход</h1>", unsafe_allow_html=True)

    # Форма авторизации
    with st.form("login_form"):
        # Поля формы
        st.text_input("Введите никнейм*")  # Поле ввода никнейма
        st.text_input("Введите пароль*", type="password")  # Поле ввода пароля
        st.checkbox("Запомнить меня")  # Чекбокс "Запомнить меня"
        st.markdown("<a href='#' style='text-decoration: none; color: #007BFF;'>Забыли пароль?</a>", unsafe_allow_html=True)  # Ссылка на восстановление пароля

        # Кнопка "Войти" по центру
        col1, col2, col3 = st.columns([3, 3, 3])  # Центрирование кнопки через колонки
        with col2:
            submitted = st.form_submit_button("Войти")  # Кнопка "Войти"

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
        .stCheckbox {
            margin-top: 5px;
        }
    </style>
    """, unsafe_allow_html=True)
    if st.button("Войти"):
        st.session_state.page = "game_list"

# Функция для страницы списка игр
def game_list_page():
    # Настройка страницы
    st.set_page_config(page_title="Список игр", layout="wide")

    # Шапка с навигацией, логотипом и Профиль | Выйти
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
        .profile {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .profile .divider {
            border-left: 1px solid #ddd;
            height: 20px;
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
    st.title("Список игр")

    # Таблица со списком игр
    st.markdown("""
    <style>
        .game-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 16px;
            text-align: left;
        }
        .game-table th, .game-table td {
            border: 1px solid #ddd;
            padding: 10px;
        }
        .game-table th {
            background-color: #007BFF;
            color: white;
        }
        .game-table tbody tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .game-table tbody tr:hover {
            background-color: #f1f1f1;
        }
        .action-buttons button {
            margin-right: 10px;
            padding: 5px 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        .action-buttons button:hover {
            background-color: #0056b3;
        }
    </style>
    <table class="game-table">
        <thead>
            <tr>
                <th>Название</th>
                <th>Описание</th>
                <th>Сист. требования</th>
                <th>Цена</th>
                <th>Валюта</th>
                <th>Дата выхода</th>
                <th>Жанр(ы)</th>
                <th>Обложка</th>
                <th>Действия</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Игра 1</td>
                <td>Описание для первой игры</td>
                <td>Минимальные требования</td>
                <td>15.00</td>
                <td>USD</td>
                <td>2025-01-01</td>
                <td>Экшн, RPG</td>
                <td><img src="#" alt="Обложка" width="50"></td>
                <td class="action-buttons">
                    <button>Изменить</button>
                    <button>Удалить</button>
                </td>
            </tr>
            <tr>
                <td>Игра 2</td>
                <td>Описание для второй игры</td>
                <td>Рекомендуемые требования</td>
                <td>20.00</td>
                <td>EUR</td>
                <td>2024-12-15</td>
                <td>Приключения, Стратегия</td>
                <td><img src="#" alt="Обложка" width="50"></td>
                <td class="action-buttons">
                    <button>Изменить</button>
                    <button>Удалить</button>
                </td>
            </tr>
            <tr>
                <td>Игра 3</td>
                <td>Описание для третьей игры</td>
                <td>Минимальные требования</td>
                <td>10.00</td>
                <td>EUR</td>
                <td>2025-03-10</td>
                <td>Симуляторы, Спорт</td>
                <td><img src="#" alt="Обложка" width="50"></td>
                <td class="action-buttons">
                    <button>Изменить</button>
                    <button>Удалить</button>
                </td>
            </tr>
            <tr>
                <td>Игра 4</td>
                <td>Описание для четвертой игры</td>
                <td>Минимальные требования</td>
                <td>25.00</td>
                <td>USD</td>
                <td>2025-05-10</td>
                <td>Головоломка, Хоррор</td>
                <td><img src="#" alt="Обложка" width="50"></td>
                <td class="action-buttons">
                    <button>Изменить</button>
                    <button>Удалить</button>
                </td>
            </tr>
            <tr>
                <td>Игра 5</td>
                <td>Описание для пятой игры</td>
                <td>Рекомендуемые требования</td>
                <td>30.00</td>
                <td>EUR</td>
                <td>2025-06-15</td>
                <td>Аркада</td>
                <td><img src="#" alt="Обложка" width="50"></td>
                <td class="action-buttons">
                    <button>Изменить</button>
                    <button>Удалить</button>
                </td>
            </tr>
            <tr>
                <td>Игра 6</td>
                <td>Описание для шестой игры</td>
                <td>Минимальные требования</td>
                <td>50.00</td>
                <td>USD</td>
                <td>2025-08-20</td>
                <td>Спорт, Экшн</td>
                <td><img src="#" alt="Обложка" width="50"></td>
                <td class="action-buttons">
                    <button>Изменить</button>
                    <button>Удалить</button>
                </td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

    # Кнопка "Добавить игру" перемещена вправо
    col1, col2 = st.columns([8, 2])  # Колонка справа для кнопки
    with col2:
        if st.button("Добавить игру"):
            st.write("Форма для добавления игры появится здесь")

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
    if st.button("Добавить игру"):
        st.session_state.page = "add_game"

# Функция для страницы добавления игры
def add_game_page():
    # Настройка параметров страницы
    st.set_page_config(page_title="Административная панель", layout="wide")

    # Шапка с навигацией, логотипом и Профиль | Выйти
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
        .profile {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .profile .divider {
            border-left: 1px solid #ddd;
            height: 20px;
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
    if st.button("Добавить"):
        st.session_state.page = "game_list"

# Основная функция
def main():
    # Инициализация состояния страницы
    if "page" not in st.session_state:
        st.session_state.page = "registration"

    # Переходы между страницами
    if st.session_state.page == "registration":
        registration_page()
    elif st.session_state.page == "authorization":
        authorization_page()
    elif st.session_state.page == "game_list":
        game_list_page()
    elif st.session_state.page == "add_game":
        add_game_page()

# Запуск приложения
if __name__ == '__main__':
    main()







