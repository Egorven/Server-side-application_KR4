## Установка зависимостей

```bash
python -m venv venv
# На Windows:
venv\Scripts\activate

# На Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt

```
## Тестирование

#  9.1

```bash
cd 9.1

# Создать .env для Alembic
copy .env.example .env

# Применить миграции
alembic upgrade head

python -m uvicorn main:app --reload
```

#  10.1
```bash
python -m uvicorn app10_1:app --reload
# В другом терминале:
curl http://127.0.0.1:8000/items/10/      # CustomExceptionA (404)
curl -X POST http://127.0.0.1:8000/items/1/  # CustomExceptionB (409)
curl -X DELETE http://127.0.0.1:8000/items/1/  # Глобальный обработчик (500)
```

#  10.2
```bash
python -m uvicorn app10_2:app --reload
# В другом терминале:
# age <= 18 -> ошибка валидации (422)
curl -X POST http://127.0.0.1:8000/users/ -H "Content-Type: application/json" -d "{\"username\":\"alex\",\"age\":18,\"email\":\"alex@mail.com\",\"password\":\"password1\"}"

# некорректный email -> ошибка валидации (422)
curl -X POST http://127.0.0.1:8000/users/ -H "Content-Type: application/json" -d "{\"username\":\"alex\",\"age\":20,\"email\":\"not-email\",\"password\":\"password1\"}"

# короткий пароль -> ошибка валидации (422)
curl -X POST http://127.0.0.1:8000/users/ -H "Content-Type: application/json" -d "{\"username\":\"alex\",\"age\":20,\"email\":\"alex@mail.com\",\"password\":\"123\"}"
```

#  11.1 и 11.2

```bash
cd 11.1
pytest -v

cd 11.2
pytest -v
```
