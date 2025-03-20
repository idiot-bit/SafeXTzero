import telebot
import random
import os
import sys
import time
import re
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ✅ Bot Token & Owner ID (Replace with actual values)
TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))  
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = telebot.TeleBot(TOKEN)

# ✅ Allowed Users
allowed_users = {OWNER_ID}

# ✅ Ignore Unauthorized Users Completely
def is_authorized(message):
    return message.from_user.id in allowed_users

# ✅ Unauthorized User Handler
@bot.message_handler(func=lambda message: message.from_user.id not in allowed_users)
def handle_unauthorized(message):
    bot.reply_to(message, "🚀𝗪𝗵𝗮𝘁 𝗕𝗿𝘂𝗵 , 𝗜𝘁❜𝘀 𝗩𝗲𝗿𝘆 𝗪𝗿𝗼𝗻𝗴 𝗕𝗿𝗼 😂")

# ✅ Startup Messages
STARTUP_MESSAGES = [
    "👑 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗕𝗮𝗰𝗸, 𝗕𝗼𝘀𝘀.!!",
    "🔥 𝗧𝗵𝗲 𝗞𝗶𝗻𝗴 𝗛𝗮𝘀 𝗔𝗿𝗿𝗶𝘃𝗲𝗱.!!",
    "🚀 𝗥𝗲𝗮𝗱𝘆 𝗳𝗼𝗿 𝗔𝗰𝗧𝗶𝗼𝗻, 𝗠𝗮𝘀𝘁𝗲𝗿.?",
    "⚡ 𝗣𝗼𝘄𝗲𝗿𝗶𝗻𝗴 𝗨𝗽 𝗳𝗼𝗿 𝗬𝗼𝘂!?",
    "💎 𝗬𝗼𝘂𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀, 𝗬𝗼𝘂𝗿 𝗥𝘂𝗹𝗲𝘀.!!",
    "🌟 𝗢𝗻𝗹𝗶𝗻𝗲 & 𝗔𝘁 𝗬𝗼𝘂𝗿 𝗦𝗲𝗿𝘃𝗶𝗰𝗲.!!",
    "🎯 𝗟𝗼𝗰𝗸𝗲𝗱 & 𝗟𝗼𝗮𝗱𝗲𝗱, 𝗕𝗼𝘀𝘀.!!"
]

# ✅ Caption Template
TEMPLATE_CAPTION = """✅ Key Updated Successfully!

♻️Esᴘ - ❕
♻️Tᴏᴜᴄʜ-Aɪᴍʙᴏᴛ Bʀᴜᴛᴛᴛᴀʟ - 👽
♻️Nᴏ ʀᴇᴄᴏɪʟ - ⭕️
♻️Iɢɴᴏʀᴇ Kɴᴏᴄᴋᴇᴅ / Vɪsɪʙɪʟɪᴛʏ Cʜᴇᴄᴋ⚠️
♻️Oɴʟɪɴᴇ Bʏᴘᴀss Sʏsᴛᴇᴍ - 🌀

Key - `{}`

𝗗𝗶𝗿𝗲𝗰𝘁 𝗟𝗼𝗴𝗶𝗻 𝗠𝗮𝗶𝗻 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 ☠

𝗝𝗼𝗶𝗻 𝗦𝗵𝗮𝗿𝗲 & 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 🤩
https://t.me/SafeXT
https://t.me/SafeXT

𝗡𝗼𝘁𝗲 :
    𝗢𝗻𝗹𝘆 𝗦𝗮𝗳𝗲 𝗛𝗮𝗰𝗸𝘀 𝗣𝗿𝗼𝘃𝗶𝗱𝗶𝗻𝗴 ✅
      𝗨𝘀𝗲𝗹𝗲𝘀𝘀 𝗹𝗼𝗮𝗱𝗲𝗿 𝗼𝗿 𝗠𝗼𝗱𝘀🚫
         𝗜𝗮𝗺 𝗡𝗼𝘁 𝗣𝗿𝗼𝘃𝗶𝗱𝗶𝗻𝗴 ❎

   𝗪𝗮𝗻𝘁 𝗕𝘂𝘆 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 ❕
     @LocalxCheats 👽
"""

# ✅ Store Pending APKs & Shares
pending_apks = {}
pending_shares = {}

# ✅ Command: /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, random.choice(STARTUP_MESSAGES), parse_mode="Markdown")

# ✅ Command: /ping (Shows Bot Uptime & Ping)
start_time = time.time()

@bot.message_handler(commands=['ping'])
def ping(message):
    uptime = str(datetime.timedelta(seconds=int(time.time() - start_time)))
    response_time = round(time.time() - message.date, 3)  # Ensure proper subtraction
    bot.reply_to(message, f"🏓 𝗣𝗼𝗻𝗴!\n⏳ 𝗨𝗽𝘁𝗶𝗺𝗲: {uptime}\n⚡ Ping: {response_time}s", parse_mode="Markdown")

# ✅ Command: /adduser (Owner Only)
@bot.message_handler(commands=['adduser'])
def add_user(message):
    if message.from_user.id != OWNER_ID:
        return
    try:
        user_id = int(message.text.split()[1])
        allowed_users.add(user_id)
        bot.reply_to(message, f"✅ User `{user_id}` added!", parse_mode="Markdown")
    except:
        bot.reply_to(message, "⚠️ Usage: `/adduser 1234567890`", parse_mode="Markdown")

# ✅ Command: /userlist (Shows All Users in One Message)
@bot.message_handler(commands=['userlist'])
def userlist(message):
    if message.from_user.id != OWNER_ID:
        return  # Only the owner can use this

    if not allowed_users:
        bot.reply_to(message, "⚠️ No users added yet.")
        return

    user_list = "**👥 Registered Users:**\n\n"
    
    for user_id in allowed_users:
        try:
            user = bot.get_chat(user_id)
            username = f"@{user.username}" if user.username else "❌ No Username"
            nickname = user.username if user.username else str(user_id)

            user_info = f"👤 **Username:** {username}\n🆔 **User ID:** `{user_id}`\n🏷 **Nickname:** `{nickname}`\n\n"
            user_list += user_info

            # ✅ Also Print in Termux
            print(f"User: {username} | ID: {user_id} | Nickname: {nickname}")

        except Exception as e:
            error_msg = f"⚠️ Error fetching user `{user_id}`"
            user_list += error_msg + "\n\n"
            print(f"Error fetching user {user_id}: {e}")

    bot.send_message(message.chat.id, user_list, parse_mode="Markdown")

# ✅ Command: /removeuser (Owner Only)
@bot.message_handler(commands=['removeuser'])
def remove_user(message):
    if message.from_user.id != OWNER_ID:
        return
    try:
        user_id = int(message.text.split()[1])
        allowed_users.discard(user_id)
        bot.reply_to(message, f"🚫 User `{user_id}` removed!", parse_mode="Markdown")
    except:
        bot.reply_to(message, "⚠️ Usage: `/removeuser 1234567890`", parse_mode="Markdown")

# ✅ Handle APK Uploads
@bot.message_handler(content_types=['document'])
def handle_apk(message):
    if message.from_user.id not in allowed_users:
        return

    if message.document.mime_type == "application/vnd.android.package-archive":
        key_match = re.search(r'Key - (.+)', message.caption or "")
        
        if key_match:
            send_apk_with_key(message, key_match.group(1))
        else:
            pending_apks[message.chat.id] = message
            bot.reply_to(message, "⏳ Send the key now!")

# ✅ Handle Key Input
@bot.message_handler(func=lambda message: message.text and message.chat.id not in pending_apks)
def handle_unexpected_key(message):
    bot.reply_to(message, "⚠️ Please send the APK first!", parse_mode="Markdown", disable_notification=True)

@bot.message_handler(func=lambda message: message.chat.id in pending_apks and message.text)
def handle_key(message):
    original_apk = pending_apks.pop(message.chat.id)
    send_apk_with_key(original_apk, message.text)

# ✅ Send APK with Key
def send_apk_with_key(apk_message, key):
    if not key.strip():
        bot.reply_to(apk_message, "⚠️ No key provided!")
        return  

    new_caption = TEMPLATE_CAPTION.format(key)
    sent_message = bot.send_document(apk_message.chat.id, apk_message.document.file_id, caption=new_caption, parse_mode="Markdown")

    pending_shares[sent_message.message_id] = (apk_message.document.file_id, key)
    ask_to_share(sent_message)

# ✅ Ask to Share
def ask_to_share(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("✅ Yes", callback_data=f"share_yes|{message.message_id}"),
        InlineKeyboardButton("❌ No", callback_data=f"share_no|{message.message_id}")
    )
    bot.send_message(message.chat.id, "📢 Share to the channel?", reply_markup=keyboard)

# ✅ Handle Share Decision
@bot.callback_query_handler(func=lambda call: call.data.startswith("share_"))
def handle_share_decision(call):
    if call.from_user.id not in allowed_users:
        return

    decision, message_id = call.data.split("|")

    if decision == "share_yes":
        if int(message_id) in pending_shares:
            file_id, key = pending_shares.pop(int(message_id))
            bot.send_document(CHANNEL_ID, file_id, caption=TEMPLATE_CAPTION.format(key), parse_mode="Markdown")
            bot.edit_message_text("✅ Shared Successfully!", call.message.chat.id, call.message.message_id)

    elif decision == "share_no":
        pending_shares.pop(int(message_id), None)
        bot.edit_message_text("❌ Declined!", call.message.chat.id, call.message.message_id)

# ✅ Restart Bot on Crash
def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)

try:
    bot.polling(none_stop=True)
except:
    time.sleep(5)
    restart_bot()