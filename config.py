import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://motorbsoothing03:FXj6wDr6XW4BXTwx@cluster0.2kg1s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
