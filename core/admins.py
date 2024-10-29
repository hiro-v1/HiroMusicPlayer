"""
Pemutar Musik, Bot Obrolan Suara Telegram
HiroMusicPlayer di persembahkan untuk para pecinta demus

Program ini adalah perangkat lunak gratis: Anda dapat mendistribusikan ulang dan/atau memodifikasinya
itu di bawah ketentuan Lisensi Publik Umum GNU Affero yang diterbitkan oleh
Free Software Foundation, baik versi 3 dari Lisensi, atau
(sesuai pilihan Anda) versi apa pun yang lebih baru.

Program ini kami sebarkan dengan harapan dapat bermanfaat,
tapi TANPA JAMINAN APAPUN; bahkan tanpa jaminan tersirat
KELAYAKAN UNTUK DIPERDAGANGKAN atau KESESUAIAN UNTUK TUJUAN TERTENTU.  Lihat
Lisensi Publik Umum GNU Affero untuk lebih jelasnya.

Selamat menikmati, @hiro_v1
"""

from config import config
from pyrogram import enums
from pyrogram.types import Message


async def is_sudo(message: Message):
    if message.from_user and message.from_user.id in config.SUDOERS:
        return True
    else:
        return False


async def is_admin(message: Message):
    if message.from_user:
        user = await message.chat.get_member(message.from_user.id)
        if user.status in [
            enums.ChatMemberStatus.OWNER,
            enums.ChatMemberStatus.ADMINISTRATOR,
        ]:
            return True
        elif message.from_user.id in config.SUDOERS:
            return True
    elif message.sender_chat:
        if message.sender_chat.id == message.chat.id:
            return True
    else:
        return False
