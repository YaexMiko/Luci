import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5768949686:AAG7E5FjrUnL99EMfN5dFu5ssPsWYM31y0k")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "19863702"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6d48cb362a97a43cfc944fd5c0f917f9")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002601056342"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "917790252"))

# Port
PORT = os.environ.get("PORT", "8222")

# Database URL
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Bewafa:aloksingh@cluster0.qsrsu.mongodb.net/?retryWrites=true&w=majority")

# Database Name
DB_NAME = os.environ.get("DATABASE_NAME", "fair")

# Join Requests Database
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DB_URI)
JOIN_REQS_DB2 = environ.get("JOIN_REQS_DB2", DB_URI)

# Force sub channel id, if you want to enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002390467697"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002327327171"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002288525306"))

# Bot workers
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\nɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ғʀᴏᴍ ᴀ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ....!</b>.")

# Admins list
try:
    ADMINS = [7533047591]
    for x in (os.environ.get("ADMINS", "6615142034 7207533746").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>sᴏʀʀʏ ᴅᴜᴅᴇ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇsᴇ ᴄʜᴀɴɴᴇʟs</b>\n\n<b>sᴏ ᴘʟᴇᴀss ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 🔥</b>")
# Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Protect content
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

# Disable channel button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ ᴘʟᴇᴀsᴇ  ᴀᴠᴏɪᴅᴇ ᴅɪʀᴇᴄᴛ ᴍᴇssᴀɢᴇs."

# Append owner ID to admins
ADMINS.append(OWNER_ID)
ADMINS.append(7533047591)

# Log file name
LOG_FILE_NAME = "filesharingbot.txt"

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

# Set logging level for Pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Logger function
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
