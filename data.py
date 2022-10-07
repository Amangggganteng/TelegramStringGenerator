from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙᴏᴛ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton(" sᴜᴩᴩᴏʀᴛ ", url="https://t.me/amanqs"),
         InlineKeyboardButton(" ɪɴꜱᴛᴀɢʀᴀᴍ ", url="https://instagram.com/bakuangoreng_"),
        ],
    ]

    START = """

 Haloㅤㅤ
━━━━━━━━━━━━━━━━━━━━━━━━
𝙎𝙩𝙧𝙞𝙣𝙜 𝙈𝙖𝙧𝙮𝙤𝙣𝙤 dibuat untuk 
Mengambil String Session Telegram!
━━━━━━━━━━━━━━━━━━━━━━━━
Privasi vcs,pap tt,chat telegram
anda akan tetap aman.
━━━━━━━━━━━━━━━━━━━━━━━━
By @bakuangoreng   """
