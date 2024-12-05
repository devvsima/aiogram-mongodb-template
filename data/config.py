from pathlib import Path
from environs import Env

DIR = Path(__file__).absolute().parent.parent

env = Env()
env.read_env()

#  tgbot
TG_TOKEN = env.str("TOKEN", default=None)
ADMINS = env.list("ADMINS", default=None, subcast=int)
RATE_LIMIT = env.int("RATE_LIMIT", default=5)

# db
MONGO_HOST = env.str("MONGO_HOST", default="localhost")
MONGO_PORT = env.int("MONGO_PORT", default=27017)
MONGO_USER = env.str("MONGO_USER", default=None)
MONGO_PASS = env.str("MONGO_PASS", default=None)
MONGO_NAME = env.str("MONGO_NAME", default="template")

MONGO_URL = env.str("MONGO_URL", default="mongodb://{MONGO_HOST}:{MONGO_PORT}/")

if MONGO_NAME and MONGO_PASS:
    MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/"

I18N_DOMAIN = 'bot'
LOCALES_DIR = f'{DIR}/data/locales'

