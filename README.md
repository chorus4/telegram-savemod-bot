# Telegram savemod bot

Бот для сохранения удаленных сообщений

Также сохраняет самоудаляющиеся фото

---

### **Важно!**

Для использования бота требуется telegram premium!

## Подготовка и запуск

```
git clone https://github.com/chorus4/telegram-savemod-bot.git
```

**Создание виртуального окружения**

```
python -m venv .venv
```

Активация виртуального окружения

```
.\.venv\Scripts\activate
```

**Установка зависимостей**

```
pip install -r requirements.txt
```

**Конфигурация**

_Переименуйте файл .env.example на .env_

Вместо `YOUR TOKEN` вставьте свой токен с [BotFather](https://t.me/BotFather)

Также создайте в корне проекта папку `media`

---

**Запуск**

```
python main.py
```

После запуска напишите `/start`

На это бот ничего не ответит
так как у бота пока-что не реализован обработчик команды `/start`

После подключите бота к telegram business (перед этим включите [поддержку telegram business](https://sendpulse.ua/ru/knowledge-base/chatbot/telegram/telegram-business) в [BotFather](https://t.me/BotFather)

### ВАЖНО!

Если вам отправили самоудаляющиеся фото вам нужно будет на него ответить

Только после этого бот сможет вам отправить фото
