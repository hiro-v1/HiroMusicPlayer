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

import json


def load(lang):
    return json.load(open(f"./lang/{lang}.json", "r"))
