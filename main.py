from telethon import TelegramClient, events
import asyncio
import telegram
import logging

# Конфигурация
API_ID = 'YOUR_API_ID'  # Получите на my.telegram.org
API_HASH = 'YOUR_API_HASH'  # Получите на my.telegram.org
PHONE = 'YOUR_PHONE_NUMBER'  # Ваш номер телефона с кодом страны
CHANNEL_USERNAME = '@channelusername'  # Username канала (с @)
KEYWORDS = ['ключевое слово1', 'ключевое слово2', 'ключевое слово3']  # Ключевые слова
BOT_TOKEN = 'YOUR_BOT_TOKEN'  # Токен от BotFather
CHAT_ID = 'YOUR_CHAT_ID'  # Ваш chat_id (можно получить через @userinfobot)

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание клиентов
client = TelegramClient('session_name', API_ID, API_HASH)
bot = telegram.Bot(token=BOT_TOKEN)

async def send_notification(message):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        logger.info("Уведомление успешно отправлено")
    except Exception as e:
        logger.error(f"Ошибка при отправке уведомления: {e}")

@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def handler(event):
    message_text = event.message.text.lower()
    
    # Проверка наличия ключевых слов
    found_keywords = [kw for kw in KEYWORDS if kw.lower() in message_text]
    
    if found_keywords:
        # Получение ID поста и формирование ссылки
        message_id = event.message.id
        post_link = f"https://t.me/{CHANNEL_USERNAME[1:]}/{message_id}"
        
        # Формирование уведомления
        response = f"Найдены ключевые слова в посте из {CHANNEL_USERNAME}:\n"
        response += f"Ключевые слова: {', '.join(found_keywords)}\n"
        response += f"Текст поста:\n{message_text}\n"
        response += f"Ссылка на пост: {post_link}"
        
        # Отправка уведомления через бот
        await send_notification(response)

async def main():
    await client.start(phone=PHONE)
    logger.info(f"Бот запущен и мониторит канал {CHANNEL_USERNAME}")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())