from motor.motor_asyncio import AsyncIOMotorClient

from data.config import MONGO_NAME, MONGO_URL
from utils.logging import logger
# Создаем клиент


client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_NAME]
users = db['users']
