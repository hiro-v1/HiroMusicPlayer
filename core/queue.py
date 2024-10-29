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

import random
import asyncio


class Queue(asyncio.Queue):
    def __init__(self) -> None:
        super().__init__()

    def clear(self) -> None:
        self._queue.clear()
        self._init(0)

    def shuffle(self) -> "Queue":
        copy = list(self._queue.copy())
        copy.sort(key=lambda _: random.randint(0, 999999999))
        self.clear()
        self._queue.extend(copy)
        return self

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self):
            raise StopIteration

        item = self._queue[self.__index]
        self.__index += 1
        return item

    def __len__(self):
        return len(self._queue)

    def __getitem__(self, index):
        return self._queue[index]

    def __str__(self):
        queue = list(self._queue)
        string = ""
        for x, item in enumerate(queue):
            if x < 10:
                string += f"**{x+1}. [{item.title}]({item.source})** \n- Requested By: {item.requested_by.mention if item.requested_by else item.request_msg.sender_chat.title}\n"
            else:
                string += f"`\n...{len(queue)-10}`"
                return string
        return string
