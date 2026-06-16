# QA Diplom Project

Автоматизированное тестирование веб-приложения **Task Management System** с использованием **Playwright**, **Pytest**, **UV** и паттерна **Page Object Model (POM)**.

## Технологии

* Python 3.14
* Playwright
* Pytest
* UV
* Allure Report

## Структура проекта

```text
pages/
├── base_page.py
├── login_page.py
├── home_page.py
├── dashboard_page.py
├── boards_page.py
└── tasks_page.py

tests/
└── test_web.py

conftest.py
pytest.ini
pyproject.toml
README.md
```

## Реализованные Page Object

### LoginPage

Страница авторизации пользователя.

### HomePage

Главная страница Automation Lab.

### DashboardPage

Главная страница после авторизации.

### BoardsPage

Страница управления досками.

### TasksPage

Страница управления задачами.

## Автотесты

### Проверка отображения страницы логина

Проверка отображения полей ввода и кнопки авторизации.

### Проверка отображения главной страницы

Проверка открытия страницы Automation Lab.

### Проверка отображения страницы задач

Проверка открытия страницы "Все задачи".

### Проверка информации о пользователе

Проверка отображения имени авторизованного пользователя.

### Проверка отображения страницы досок

Проверка открытия страницы "Все доски".

### Выход из приложения

Проверка успешного выхода из системы.

## Запуск проекта

Установка зависимостей:

```bash
uv sync
```

Запуск тестов:

```bash
uv run pytest
```

Запуск тестов в браузере Chrome:

```bash
uv run pytest --headed --browser-channel chrome
```

## Allure Report

Генерация результатов:

```bash
uv run pytest --alluredir=allure-results
```

Открытие отчета:

```bash
allure serve allure-results
```

## Используемые практики

* Page Object Model (POM)
* Base Page
* Pytest Fixtures
* Type Hints (аннотации типов)
* Allure Reporting
* Локаторы по `id` и `data-qa`

## Автор

Pavel Bordukov
