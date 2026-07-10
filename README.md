# AQA Diplom Project

Автоматизированное тестирование веб-приложения **Web Automation Torture Lab**.

Проект выполнен в рамках дипломной работы по автоматизации тестирования и включает UI- и API-тесты.

---

# 🚀 Технологии

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
- uv

---

# 📂 Структура проекта

```text
qa-diplom-project/
│
├── .github/
│   └── workflows/
│       └── pylint.yaml
├── core/                  # Базовые классы проекта
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
├── uv.lock
└── README.md
```

---

# ⚙️ Установка

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

UI тесты

```bash
uv run pytest tests/ui
```

API тесты

```bash
uv run pytest tests/api
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

# 🐳 Docker

Запустить проект

```bash
docker compose up --build
```

Остановить контейнер

```bash
docker compose down
```

После выполнения тестов результаты сохраняются в папке

```text
allure-results/
```

---

# 🔍 Pylint

Проверка качества кода

```bash
uv run pylint -j 0 --disable=C0114,C0115,C0116,R0902,R0903,W0621 pages services models tests config.py conftest.py
```

---

# ⚙️ GitHub Actions

При каждом **Push** и **Pull Request** автоматически запускается проверка проекта с помощью **Pylint**.

---

# 🏗 Используемые паттерны

- Page Object Model (POM)
- Service Object
- Fixtures
- Parametrization

---

# ✅ Реализованные проверки

## UI

- Открытие главной страницы
- Авторизация пользователя
- Проверка Dashboard
- Проверка Boards
- Проверка Tasks
- Выход из системы

## API

### Users

- Получение пользователей
- Обновление пользователя
- Удаление пользователя
- Проверка параметров
- Негативные проверки

### Tasks

- Получение задач
- Создание задачи
- Удаление задачи
- Поиск задач
- Проверка параметров
- Негативные проверки

---

# 📈 Статистика проекта

- ✅ 50 автоматизированных тестов
- ✅ UI тестирование
- ✅ API тестирование
- ✅ Docker
- ✅ Allure Report
- ✅ GitHub Actions
- ✅ Pylint

---

# 👨‍💻 Автор

**Павел Бордуков**

Дипломный проект по автоматизации тестирования на Python.