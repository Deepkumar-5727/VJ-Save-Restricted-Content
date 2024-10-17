import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23011537"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cd59a9fc8cbdca6ae2b405f149cc3c8a")

#Database 
DB_URI = os.environ.get("DB_URI", "")
