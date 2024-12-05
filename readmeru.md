# 🚀 Давай начнем

## 🛠️ Стек технологий
- `aiogram 2`
- `i18n`
- `Motor`
- `MongoDB`

---

## 📥 Как его установить?

### 1. Клонируем репозиторий
Сначала клонируем репозиторий и переходим в его директорию:

```bash
git clone https://github.com/devvsima/aiogram-mongodb-template.git
cd tgbot
```

### 2. Настройка виртуального окружения ".venv"

#### Linux
Установи зависимости и активируй виртуальное окружение:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
> 💡 Возможно вам прийдется установить apt install python3.10-venv или что-то в этом роде

#### Windows
Аналогичные шаги для Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> 💡 Примечание: Название `.venv` можно изменить на любое другое по твоему желанию.

### 3. Настройка переменных окружения

Сначала скопируй файл `.env.dist` и переименуй его в `.env`:

```bash
cp .env.dist .env
```

Затем отредактируй файл с переменными окружения:

```bash
vim .env
# или
nano .env
```

### 4. Настройки бота

#### `ADMINS` - Идентификаторы администраторов
Добавь ID администраторов, разделяя их запятыми:

```bash
# пример
ADMINS=12345678,12345677,12345676
```

#### `TOKEN` - Токен бота от [@BotFather](https://t.me/BotFather)
Добавь токен своего бота:

```bash
# пример
BOT_TOKEN=123452345243:Asdfasdfasf
```

### 5. Настройка базы данных PostgreSQL

Задай параметры подключения к базе данных:

- `MONGO_HOST` - database host (default = 'localhost')
- `MONGO_PORT` - database port (default = `27017`)
- `MONGO_USER` - database user
- `MONGO_PASS` - database password
- `MONGO_NAME` - database name
  
- `MONGO_URL` - connection url

---

Теперь бот готов к запуску! 🎉