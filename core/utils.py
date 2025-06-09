import re

async def normalize_phone_number(phone: str) -> str:
    return re.sub(r'\D', '', phone)