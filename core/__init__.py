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

from core.song import Song
from core.admins import is_sudo, is_admin
from core.stream import app, ytdl, safone, pytgcalls, start_stream
from core.groups import (
    get_group, get_queue, set_group, set_title, all_groups, clear_queue,
    set_default, shuffle_queue)
from core.funcs import (
    search, check_yt_url, extract_args, generate_cover, delete_messages,
    get_spotify_playlist, get_youtube_playlist)
