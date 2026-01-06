# 🎓 Django + Telegram Bot for University Applicants

Open-source проект телеграм-бота для **абитуриентов университета**, построенный на **Django + DRF + aiogram**.

Бот показывает информацию о поступлении (процесс, документы, программы и т.д.)  
Все данные управляются **через Django Admin**, без хардкода в боте.

---

## 🚀 Возможности

- 📌 Telegram-бот для абитуриентов
- 🧠 Backend на Django + DRF
- 🤖 Bot на aiogram
- 🧾 Контент полностью управляется через админку
- ⌨️ ReplyKeyboard (без inline)
- 🧱 Готов к масштабированию (студенты, оплата, справки и т.д.)
- 🔌 Backend и Bot разделены логически

---

## 🏗️ Архитектура

User → Telegram Bot (aiogram) → Django REST API → Database (PostgreSQL / SQLite)


Бот **не хранит данные**, а получает их по API.

---
## 📁 Структура проекта

```text
django-telegrambot-university/
├── backend/
│   ├── manage.py
│   ├── core/
│   ├── apps/
│   │   └── applicants/
│   │       ├── models.py
│   │       ├── admin.py
│   │       ├── serializers.py
│   │       ├── views.py
│   │       └── urls.py
│
├── bot/
│   ├── main.py
│   ├── handlers.py
│   └── keyboards.py
│
├── .env.example
├── requirements.txt
└── README.md
```


---

## ⚙️ Установка и запуск

### 1️⃣ Клонировать репозиторий

```bash
git clone https://github.com/NurbekTech/django-telegrambot-university.git
cd django-telegrambot-university
```

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

```bash
SECRET_KEY=django-secret-key
DEBUG=True
```
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
