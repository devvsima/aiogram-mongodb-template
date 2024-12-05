from utils.logging import logger

from ..connect import users

async def get_user(id: int):
    try:
        user = await users.find_one({"_id": id})
        logger.info(user['username'])
        return user
    except Exception as e:
        logger.error(f"Error while getting user {id}: {e}")
        return None

async def create_user(id: int, username: str = None, language: str = None):
    await users.insert_one({"_id": id, "username": username, "language": language})
    logger.info(f"New user created: {username} | {id}")
    return await get_user(id)

async def get_or_create_user(id: int, username: str = None, language: str = None):
    user = await get_user(id)
    if not user:
        user = await create_user(id, username, language)
    return user
