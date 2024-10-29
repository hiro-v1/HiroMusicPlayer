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
from core.queue import Queue
from pyrogram.types import Message
from typing import Any, Dict, Union
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.phone import EditGroupCallTitle


GROUPS: Dict[int, Dict[str, Any]] = {}


def all_groups():
    return GROUPS.keys()


def set_default(chat_id: int) -> None:
    global GROUPS
    GROUPS[chat_id] = {}
    GROUPS[chat_id]["is_playing"] = False
    GROUPS[chat_id]["now_playing"] = None
    GROUPS[chat_id]["stream_mode"] = config.STREAM_MODE
    GROUPS[chat_id]["admins_only"] = config.ADMINS_ONLY
    GROUPS[chat_id]["loop"] = False
    GROUPS[chat_id]["lang"] = config.LANGUAGE
    GROUPS[chat_id]["queue"] = Queue()


def get_group(chat_id) -> Dict[str, Any]:
    if chat_id not in all_groups():
        set_default(chat_id)
    return GROUPS[chat_id]


def set_group(chat_id: int, **kwargs) -> None:
    global GROUPS
    for key, value in kwargs.items():
        GROUPS[chat_id][key] = value


async def set_title(message_or_chat_id: Union[Message, int], title: str, **kw):
    if isinstance(message_or_chat_id, Message):
        client = message_or_chat_id._client
        chat_id = message_or_chat_id.chat.id
    elif isinstance(message_or_chat_id, int):
        client = kw.get("client")
        chat_id = message_or_chat_id
    try:
        peer = await client.resolve_peer(chat_id)
        chat = await client.invoke(GetFullChannel(channel=peer))
        await client.invoke(EditGroupCallTitle(call=chat.full_chat.call, title=title))
    except BaseException:
        pass


def get_queue(chat_id: int) -> Queue:
    return GROUPS[chat_id]["queue"]


def clear_queue(chat_id: int) -> None:
    global GROUPS
    GROUPS[chat_id]["queue"].clear()


def shuffle_queue(chat_id: int) -> Queue:
    global GROUPS
    return GROUPS[chat_id]["queue"].shuffle()
