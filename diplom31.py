import streamlit as st

def main():
    # Настройка страницы
    st.set_page_config(page_title="Список игр", layout="wide")

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
                <td>Короткое описание</td>
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
            <!-- Добавьте больше строк для игр -->
        </tbody>
    </table>
    """, unsafe_allow_html=True)

    # Кнопка для добавления игры
    if st.button("Добавить игру"):
        st.write("Форма для добавления игры появится здесь.")

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

if __name__ == '__main__':
    main()





