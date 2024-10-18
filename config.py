import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29607719"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1692c3a715a48696d0762d6438a70d33")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://parthaplus5:xIeVwJNkmuco5sc9@cluster0.qv0nk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
