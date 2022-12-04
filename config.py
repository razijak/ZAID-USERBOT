from os import getenv

API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5699833340").split()))
OWNER_ID = int(getenv("OWNER_ID", "5699833340")) #ur id 
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://razibinraya:razibinraya@cluster0.zli9kam.mongodb.net/?retryWrites=true&w=majority") # an database 
BOT_TOKEN = getenv("BOT_TOKEN", "5726708614:AAE5sRQ5YRVaPM6uqfYGUuoMR6pU4A8IFvY")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER") # I'D if uh want
LOG_GROUP = getenv("LOG_GROUP") #id if uh want to enabled tagalert
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAxD2iNtwZtKZ-Ji9GrLf6PEo6gxfzJ1EihPGPFupcuOAlVXBPL-TEZ37FeW1v4qWYcW8NdKi6z0sMc-tSLtpTVdaMdeFdisYyiZkCCCyOsQaD_AyBt3E1-BbrHpxEz9PRxgjdKknCK2uAqAxJv0xFX_XkS8Ppb5_CbbOBpyU0T_TE7D5cNKipL3lsVV3RpIrOPp8vfLOpmexjq0SuYohhAGkOVj14ISxoKAwf9uhEDSKSLWiF9XZKPAuRRiCZW30TNQeoxWWNJ-22HacCu1cFDbLT6KNIKzHPEkeiCd0dqRwLzS8CNmN_WKUVsU9VVzoMiX29ZpFlD24wM2i30TzwfgAAAAFTvI38AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
