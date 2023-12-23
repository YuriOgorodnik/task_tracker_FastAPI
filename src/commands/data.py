employee_data = [
    {
        "last_name": "Шакура",
        "first_name": "Андрей",
        "patronymic": "Александрович",
        "position": "Главный инженер",
        "phone_number": "+375291186096",
        "email": "andrew@example.com",
        "address": "улица Западная 17-22",
        "city": "город Бобруйск",
        "country": "Республика Беларусь"
    },
    {
        "last_name": "Пяленко",
        "first_name": "Евгений",
        "patronymic": "Александрович",
        "position": "Мастер по сварке",
        "phone_number": "+375259145750",
        "email": "pylenko@example.com",
        "address": "улица Крылова 7-73",
        "city": "город Бобруйск",
        "country": "Республика Беларусь"
    },
    {
        "last_name": "Новикова",
        "first_name": "Оксана",
        "patronymic": "Анатольевна",
        "position": "Инспектор по кадрам",
        "phone_number": "+375291161957",
        "email": "oksana@example.com",
        "address": "улица Ульяновская 100-18",
        "city": "город Бобруйск",
        "country": "Республика Беларусь"
    },
    {
        "last_name": "Леонова",
        "first_name": "Алла",
        "patronymic": "Александровна",
        "position": "Экономист 1 кат.",
        "phone_number": "+375293703595",
        "email": "alla@example.com",
        "address": "улица Советская 23-89",
        "city": "город Бобруйск",
        "country": "Республика Беларусь"
    },
]

task_data = [
    {
        "title": "Оформить документы на стажировку работника",
        "created_at": "2023-12-12T08:20:00",
        "employee_id": 1,
        "deadline": "2023-12-12T15:00:00",
        "is_active": True
    },
    {
        "title": "Провести вводный инструктаж",
        "created_at": "2023-12-12T09:00:00",
        "employee_id": 1,
        "parent_task_id": 1,
        "deadline": "2023-12-12T10:00:00",
        "is_active": True
    },
    {
        "title": "Провести первичный инструктаж",
        "created_at": "2023-12-12T10:10:00",
        "employee_id": 1,
        "parent_task_id": 1,
        "deadline": "2023-12-12T11:00:00",
        "is_active": True
    },
    {
        "title": "Оформить и выдать удостоверение по охране труда",
        "created_at": "2023-12-12T11:20:00",
        "employee_id": 1,
        "parent_task_id": 1,
        "deadline": "2023-12-12T12:00:00",
        "is_active": True
    },
    {
        "title": "Выдать работнику необходимые СИЗ",
        "created_at": "2023-12-12T14:00:00",
        "employee_id": 1,
        "deadline": "2023-12-12T15:00:00",
        "is_active": True
    },
    {
        "title": "Подготовиться к проведению сварочных работ",
        "created_at": "2023-12-13T09:00:00",
        "employee_id": 2,
        "deadline": "2023-12-19T15:00:00",
        "is_active": True
    },
    {
        "title": "Оформить заявку на приобретение сварочных материалов",
        "created_at": "2023-12-14T09:00:00",
        "employee_id": 2,
        "parent_task_id": 6,
        "deadline": "2023-12-14T10:00:00",
        "is_active": True
    },
    {
        "title": "Оформить техническое задание на разработку техинструкции",
        "created_at": "2023-12-14T11:00:00",
        "employee_id": 2,
        "parent_task_id": 6,
        "deadline": "2023-12-15T10:00:00",
        "is_active": True
    },
    {
        "title": "Подготовить и передать Заказчику сварочную документацию",
        "created_at": "2023-12-16T08:20:00",
        "employee_id": 2,
        "deadline": "2023-12-22T12:00:00",
        "is_active": True
    },
    {
        "title": "Подобрать кандидатуру на вакансию 'Электросварщик'",
        "created_at": "2023-12-12T08:20:00",
        "employee_id": 3,
        "deadline": "2023-12-30T12:00:00",
        "is_active": True
    },
    {
        "title": "Разместить объявление в СМИ об имеющейся вакансии",
        "created_at": "2023-12-12T15:00:00",
        "employee_id": 3,
        "parent_task_id": 10,
        "deadline": "2023-12-13T15:00:00",
        "is_active": True
    },
    {
        "title": "Подготовить проект приказа о допуске работника к самостоятельной работе",
        "created_at": "2023-12-19T08:00:00",
        "employee_id": 3,
        "deadline": "2023-12-19T12:00:00",
        "is_active": True
    },
    {
        "title": "Сдать все документы по начислению заработной платы",
        "created_at": "2023-12-28T09:00:00",
        "employee_id": 4,
        "deadline": "2023-12-30T11:00:00",
        "is_active": True
    },
    {
        "title": "Оформить акты выполненных работ по всем объектам",
        "created_at": "2023-12-23T09:00:00",
        "employee_id": 4,
        "deadline": "2023-12-27T10:00:00",
        "is_active": True
    },
    {
        "title": "Предоставить информацию для формирования годового отчёта",
        "created_at": "2023-12-20T15:00:00",
        "deadline": "2023-12-27T15:00:00",
        "is_active": True
    },
    {
        "title": "Подготовить проект приказа о поощрении лучших работников",
        "created_at": "2023-12-22T15:00:00",
        "deadline": "2023-12-24T15:00:00",
        "is_active": True
    },
]
