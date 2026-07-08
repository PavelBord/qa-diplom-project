# AQA Diploma Project

![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-9.0-0A9EDC?logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.60-2EAD33?logo=playwright&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-black)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI-2088FF?logo=githubactions&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Report-84C441)
![Pylint](https://img.shields.io/badge/Pylint-passing-brightgreen)

Автоматизированное тестирование веб-приложения **Web Automation Torture Lab**.

Проект выполнен в рамках дипломной работы по автоматизации тестирования и включает UI- и API-тестирование с использованием современных инструментов.

---

# 🚀 Используемые технологии

- Python 3.14
- Pytest
- Playwright
- Requests
- Faker
- Pydantic
- Allure Report
- Docker
- Docker Compose
- GitHub Actions
- Pylint
- Taskipy

---

# 📂 Структура проекта

```text
qa-diplom-project/
│
├── pages/                     # Page Object Model
├── services/                  # API сервисы
├── models/                    # Pydantic модели
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

# ⚙️ Установка проекта

Клонировать репозиторий

```bash
git clone https://github.com/PavelBord/qa-diplom-project.git
```

Перейти в папку проекта

```bash
cd qa-diplom-project
```

Установить зависимости

```bash
uv sync
```

---

# ▶️ Запуск тестов

Все тесты

```bash
uv run pytest
```

Только UI

```bash
uv run pytest tests/ui
```

Только API

```bash
uv run pytest tests/api
```

---

# 🏷️ Запуск по маркерам

UI

```bash
uv run pytest -m ui
```

API

```bash
uv run pytest -m api
```

Home

```bash
uv run pytest -m home
```

Login

```bash
uv run pytest -m login
```

Dashboard

```bash
uv run pytest -m dashboard
```

Boards

```bash
uv run pytest -m boards
```

Tasks

```bash
uv run pytest -m tasks
```

Logout

```bash
uv run pytest -m logout
```

---

# 📊 Allure Report

Запустить тесты

```bash
uv run pytest
```

Открыть отчет

```bash
uv run task report
```

---

# 🐳 Запуск через Docker

Собрать Docker-образ и выполнить тесты

```bash
docker compose up --build
```

Остановить контейнер

```bash
docker compose down
```

После выполнения тестов результаты будут сохранены в папке

```text
allure-results/
```

---

# ✅ Проверка качества кода

Запуск Pylint

```bash
uv run pylint -j 0 --disable=C0114,C0115,C0116,R0902,R0903,W0621 pages services models tests config.py conftest.py
```

---

# 🔄 GitHub Actions

Для автоматической проверки проекта используется GitHub Actions.

При каждом **push** и **pull request** автоматически выполняется:

- запуск Pylint;
- проверка качества кода.

---

# 🏗️ Используемые паттерны

- Page Object Model (POM)
- Service Object
- Fixtures
- Parametrization

---

# 🧪 Реализованные проверки

## UI

- Главная страница
- Авторизация
- Dashboard
- Boards
- Tasks
- Поиск задач
- Поиск досок
- Проверка таблиц
- Проверка фильтрации
- Проверка отображения элементов
- Выход из системы

## API

### Users

- Получение пользователей
- Получение пользователей с параметрами
- Обновление пользователя
- Удаление пользователя
- Проверка авторизации
- Проверка валидации данных

### Tasks

- Получение списка задач
- Создание задачи
- Удаление задачи
- Поиск задач
- Проверка параметров поиска
- Проверка валидации данных
- Позитивные сценарии
- Негативные сценарии

---

# 📈 Статистика проекта

- ✅ 50 автоматизированных тестов
- ✅ 25 UI тестов
- ✅ 25 API тестов
- ✅ Page Object Model
- ✅ Service Object
- ✅ Playwright
- ✅ Requests
- ✅ Docker
- ✅ Docker Compose
- ✅ Allure Report
- ✅ GitHub Actions
- ✅ Pylint (passing)

---

# 👨‍💻 Автор

**Павел Бордуков**

Дипломный проект по автоматизации тестирования на **Python**.