from aiogram import types

from loader import dp
from aiogram.dispatcher.filters import Text
from pytube import YouTube


@dp.message_handler(Text(startswith="http"))
async def get_audio(message:types.Message):
    link = message.text
    
    from io import BytesIO
    
    buffer = BytesIO()
    url = YouTube(link)

    if url.check_availability() is None:
        video = url.streams.get_highest_resolution()
        video.stream_to_buffer(buffer = buffer)
        buffer.seek(0)
        filename = url.title

        await message.answer_video(video = buffer, caption = filename)

    else:
        await message.answer("Xatolik")