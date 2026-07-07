# QA Diploma Project

Автоматизированное тестирование веб-приложения **Web Automation Torture Lab**.

Проект выполнен в рамках дипломной работы по автоматизации тестирования и включает UI- и API-тесты.

---

# Технологии

- Python 3.14
- Pytest
- Playwright
- Requests
- Faker
- Pydantic
- Allure Report
- Docker
- Docker Compose
- Taskipy

---

# Структура проекта

```
qa-diplom-project/
│
├── pages/                 # Page Object Model
├── services/              # API сервисы
├── models/                # Pydantic модели
├── tests/
│   ├── api/
│   └── ui/
├── conftest.py
├── config.py
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

---

# Установка

Клонировать репозиторий:

```bash
git clone <repository_url>
```

Перейти в папку проекта:

```bash
cd qa-diplom-project
```

Установить зависимости:

```bash
uv sync
```


# Запуск тестов

Все тесты:

```bash
uv run pytest
```

Только UI:

```bash
uv run pytest tests/ui
```

Только API:

```bash
uv run pytest tests/api
```

---

# Allure Report

Запуск тестов:

```bash
uv run pytest
```

Открыть отчет:

```bash
uv run task report
```

---

# Запуск через Docker

Собрать образ и выполнить тесты:

```bash
docker compose up --build
```

После выполнения тестов результаты будут сохранены в папке:

```text
allure-results/
```

Для остановки контейнера:

```bash
docker compose down
```

---

# Используемые паттерны

- Page Object Model (POM)
- Service Object
- Fixtures
- Parametrization

---

# Реализованные проверки

### UI

- Главная страница
- Авторизация
- Dashboard
- Boards
- Tasks
- Поиск
- Таблицы
- Фильтры
- Выход из системы

### API

- Пользователи
- Задачи
- Позитивные сценарии
- Негативные сценарии
- Валидация данных
- Авторизация

---

# Статистика проекта

- ✅ 50 автоматизированных тестов
- ✅ UI тестирование
- ✅ API тестирование
- ✅ Docker
- ✅ Allure Report
- ✅ Playwright
- ✅ Pytest

---

# Автор

Павел Бордуков