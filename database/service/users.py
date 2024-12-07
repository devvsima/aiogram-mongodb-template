from utils.logging import logger

from ..connect import db
from ..base import BaseDB

class Users(BaseDB):
    def __init__(self, db):
        super().__init__(db)  # Вызов конструктора базового класса
        self.collection = self.db['users']  # Указание коллекции для пользователей

    async def get_or_create_user(self, user_id: int, username: str = None, language: str = None):
        user = await self.get({'id': user_id})  # Передаем словарь с полем id
        if not user:
            user_data = {'_id': user_id, 'username': username, 'language': language}
            await self.create(user_data)  
            user = user_data  
        return user
    
    
UsersDB = Users(db)