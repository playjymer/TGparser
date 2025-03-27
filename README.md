# Telegram Channel Monitor Bot

Простой Telegram-бот для мониторинга канала и уведомления о постах с ключевыми словами.

## ✨ Возможности
- Мониторинг указанного Telegram-канала
- Поиск ключевых слов в новых постах
- Отправка уведомлений через Telegram-бота
- Включение прямой ссылки на пост
- Логирование активности

## 📋 Требования
- Python 3.7+
- Библиотеки:
  - `telethon`
  - `python-telegram-bot`

Установите зависимости:
```bash
pip install telethon python-telegram-bot
```

## ⚙️ Настройка
1. **Получите API ключи:**
   - Зарегистрируйтесь на [my.telegram.org](https://my.telegram.org)
   - Создайте приложение и получите `API_ID` и `API_HASH`

2. **Создайте Telegram-бота:**
   - Напишите [@BotFather](https://t.me/BotFather)
   - Создайте бота командой `/newbot`
   - Скопируйте `BOT_TOKEN`

3. **Получите ваш chat_id:**
   - Напишите [@userinfobot](https://t.me/userinfobot)
   - Отправьте `/start` и получите `CHAT_ID`

4. **Настройте конфигурацию в коде:**
   - `API_ID` — ваш API ID
   - `API_HASH` — ваш API Hash
   - `PHONE` — ваш номер телефона (например, +79991234567)
   - `CHANNEL_USERNAME` — канал для мониторинга (например, @channelusername)
   - `KEYWORDS` — список ключевых слов
   - `BOT_TOKEN` — токен вашего бота
   - `CHAT_ID` — ваш chat_id

## 🚀 Запуск
1. Сохраните код в файл `telegram_monitor_bot.py`
2. Запустите бота:
```bash
python telegram_monitor_bot.py
```
3. При первом запуске введите код подтверждения от Telegram

Бот начнет мониторить канал и отправлять уведомления при обнаружении ключевых слов.

## 📬 Пример уведомления
```
Найдены ключевые слова в посте из @channelusername:
Ключевые слова: слово1, слово2
Текст поста:
Пример текста с ключевыми словами
Ссылка на пост: https://t.me/channelusername/123
```

## 🛠️ Поддержка
Если возникнут вопросы, создайте issue в репозитории или свяжитесь с разработчиком.

---

Сделано с ❤️ для удобного мониторинга Telegram-каналов!
