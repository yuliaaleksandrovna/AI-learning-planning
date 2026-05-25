# AI Learning Planner — Backend

FastAPI-бэкенд для сервиса, который генерирует персональные планы обучения с помощью LLM.

## Статус

MVP готов: API, база данных и LLM-интеграция с LM Studio работают.

## Стек

- **FastAPI** — веб-фреймворк
- **Supabase** — база данных (PostgreSQL)
- **Python 3.11+**

## Запуск локально

### 1. Установить зависимости

```bash
pip install -r requirements.txt
```

### 2. Настроить переменные окружения

Скопировать `.env.example` в `.env` и заполнить:

```bash
cp .env.example .env
```

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

### 3. Создать таблицу в Supabase

Выполнить SQL из файла `supabase_schema.sql` в SQL-редакторе Supabase.

### 4. Запустить сервер

```bash
uvicorn app.main:app --reload
```

Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API

### `POST /plans` — создать план

**Request:**
```json
{
  "goal": "Изучить Python",
  "level": "beginner",
  "duration_weeks": 4,
  "time_per_week": 5,
  "preferred_format": "practice"
}
```

**Response:**
```json
{
  "id": "uuid",
  "title": "План обучения: Изучить Python",
  "duration_weeks": 4,
  "weeks": [
    {
      "week": 1,
      "goal": "...",
      "topics": ["..."],
      "practice": ["..."]
    }
  ],
  "created_at": "2026-..."
}
```

### `GET /plans` — список всех планов

### `GET /plans/{plan_id}` — один план по ID

## Структура проекта

```
app/
  main.py       # роуты FastAPI
  schemas.py    # Pydantic-модели
  db.py         # работа с Supabase
  llm.py        # интеграция с LM Studio
supabase_schema.sql
requirements.txt
.env.example
```

