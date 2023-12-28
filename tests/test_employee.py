from httpx import AsyncClient


async def test_create_employee(ac: AsyncClient):
    response = await ac.post(
        "/employee/create",
        json={
            "last_name": "Иванов",
            "first_name": "Иван",
            "patronymic": "Иванович",
            "position": "Инженер по охране труда",
            "phone_number": "+3752911236526",
            "email": "ivanovivan@gmail.com",
            "address": "улица Строителей, 27-17",
            "city": "город Бобруйск",
            "country": "Республика Беларусь",
        },
    )

    assert response.status_code == 200
