import streamlit as st
from datetime import date

# Функция для страницы "Список игр"
def game_list_page():
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
            <!-- Пример данных для таблицы -->
            <tr>
                <td>Игра 1</td>
                <td>Описание игры</td>
                <td>Минимальные требования</td>
                <td>20.00</td>
                <td>USD</td>
                <td>2025-01-01</td>
                <td>Экшн, RPG</td>
                <td><img src="#" alt="Обложка" width="50"></td>
                <td class="action-buttons">
                    <button>Изменить</button>
                    <button>Удалить</button>
                </td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

    # Кнопка перехода к добавлению игры
    if st.button("Добавить игру"):
        st.session_state.page = "add_game_page"

# Функция для страницы "Добавление игры"
def add_game_page():
    st.title("Добавление игры")

    with st.form("game_form"):
        game_name = st.text_input("Введите название игры*")
        game_description = st.text_area("Введите описание к игре*", height=120, max_chars=500)
        system_requirements = st.text_area("Введите системные требования*", height=100, max_chars=300)

        col1, col2 = st.columns([3, 1])
        with col1:
            price = st.text_input("Введите цену игры*", value="0.00")
        with col2:
            currency = st.selectbox("Валюта", ["USD", "EUR", "RUB", "BYN"])

        release_date = st.date_input("Введите дату выхода игры*", date.today())
        genres = st.multiselect(
            "Выберите жанр(ы) игры*",
            options=["Экшн", "Приключения", "RPG", "Стратегия", "Симуляторы", "Шутер", "Головоломка", "Хоррор", "Спорт", "Аркада"]
        )
        cover_image = st.file_uploader("Загрузите обложку игры*", type=["jpg", "jpeg", "png"])

        col1, col2 = st.columns([6, 2])
        with col2:
            submit_button = st.form_submit_button("Добавить")
            cancel_button = st.form_submit_button("Отменить")

    if submit_button:
        st.success(f"Игра '{game_name}' успешно добавлена!")
        st.session_state.page = "game_list_page"  # Возврат на страницу списка игр

    if cancel_button:
        st.session_state.page = "game_list_page"  # Возврат на страницу списка игр

# Основная функция приложения
def main():
    if "page" not in st.session_state:
        st.session_state.page = "game_list_page"

    if st.session_state.page == "game_list_page":
        game_list_page()
    elif st.session_state.page == "add_game_page":
        add_game_page()

if __name__ == '__main__':
    main()







