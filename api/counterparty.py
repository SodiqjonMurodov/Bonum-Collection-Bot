import httpx
from core.config import settings
from core.utils import normalize_phone_number

API_TOKEN = settings.get_moysklad_token()
BASE_URL = settings.get_base_url()

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/json"
}

async def check_counterparty_by_phone(phone_number):
    url = f"{settings.BASE_URL}/entity/counterparty"
    clean_phone = await normalize_phone_number(phone_number)

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = await response.json()
        rows = data.get("rows", [])
        for index, row in enumerate(rows):
            row_phone = await normalize_phone_number(row.get("phone", ""))
            print(f"phone{index}", row_phone)
            if row_phone == clean_phone:
                return row
    return None


async def add_counterparty_to_group(counterparty: dict, tag_name: str):
    url = f"{BASE_URL}/entity/counterparty/{counterparty['id']}"
    existing_tags = counterparty.get("tags", [])
    updated_tags = existing_tags + [tag_name] if tag_name not in existing_tags else existing_tags

    data = {
        "tags": updated_tags
    }

    async with httpx.AsyncClient() as client:
        response = await client.put(url, json=data, headers=HEADERS)

    return response.json()


async def create_counterparty(phone: str, name: str):
    url = f"{BASE_URL}/entity/counterparty"
    data = {
        "name": name,
        "phone": phone,
        "tags": ["telebot"]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=HEADERS, json=data)

    if response.status_code not in [200, 201]:
        print(f"Yaratishda xatolik: {response.status_code} - {response.text}")
        return None

    return response.json()


async def get_balance_counterparty(counterparty_id):
    url = f"{BASE_URL}/report/counterparty/{counterparty_id}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return dict(data)

    return None