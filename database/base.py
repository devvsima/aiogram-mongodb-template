from .connect import db
from datetime import datetime


class BaseDB:
    def __init__(self, db):
        self.db = db
        self.collection = None

    async def get_all(self, query):
        if self.collection is not None:
            return await self.collection.find(query).to_list(None)
        return []
    
    async def get(self, query):
        if self.collection is not None:
            return await self.collection.find_one(query)
        return None

    async def create(self, data):
        if self.collection is not None:
            data['created_at'] = datetime.utcnow()
            return await self.collection.insert_one(data)
        return None

    async def update(self, query, update_data):
        if self.collection is not None:
            return await self.collection.update_one(query, {'$set': update_data})
        return None

    async def delete(self, query):
        if self.collection is not None:
            return await self.collection.delete_one(query)