
import os

class Config(object):
	API_ID = 9325118
	API_HASH = "5d3831feb6752d0a6904accac2008250"
	BOT_TOKEN = "5495370777:AAE_wxsdpo5RmDVFbgexUSxVxZnSIMGKeFs"
	BOT_USERNAME = "pwfilestore_bot"
	DB_CHANNEL = "-1001770626286"
	BOT_OWNER = "1123564262"
	DATABASE_URL = "mongodb+srv://LegendBoy:LegendBoy1234@cluster0.1kerb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = ""-1001770626286""
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅File Share Bot🔅**]────⍟
│
├🔸🤖 **My Name:** [File Store Bot](https://t.me/{BOT_USERNAME})
│
├🔸📝 **Language:** [Python3](https://www.python.org)
│
├🔹📚 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹📡 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸👨‍💻 **Developer:** [Deepanshu](https://t.me/LegendDeepanshu) 
│
├🔹👥 **Bot Support:** [Support](https://t.me/lakshyajee12thpw2023discussion)
│
├🔸🔔 **Bot Updates:** [Update](https://t.me/lakshyajeepw2023freeh)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** [LegendDeepanshu](https://t.me/LegendDeepanshu) 

𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐢𝐬 𝐒𝐮𝐩𝐞𝐫 𝐍𝐨𝐨𝐛😅.

𝐈𝐟 𝐘𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐃𝐨𝐧𝐚𝐭𝐞 𝐎𝐮𝐫 𝐇𝐚𝐫𝐝 𝐖𝐨𝐫𝐤. 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐡𝐞 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫.
 
𝐀𝐥𝐬𝐨 𝐫𝐞𝐦𝐞𝐦𝐛𝐞𝐫 𝐭𝐡𝐚𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐰𝐢𝐥𝐥 𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐝𝐮𝐥𝐭 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐟𝐫𝐨𝐦 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞. 𝐒𝐨 𝐛𝐞𝐭𝐭𝐞𝐫 𝐝𝐨𝐧'𝐭 𝐒𝐭𝐨𝐫𝐞 𝐓𝐡𝐨𝐬𝐞 𝐊𝐢𝐧𝐝 𝐨𝐟 𝐓𝐡𝐢𝐧𝐠𝐬.

[Donate Me](https://t.me/LegendDeepanshu) (Contact)
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
