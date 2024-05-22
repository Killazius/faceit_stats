from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsStats(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text != None and len(message.text.split(' ')) == 2
