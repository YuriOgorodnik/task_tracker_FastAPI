Task Tracker App

Приложение "Task Tracker" поможет создать сотрудников и задачи для них, а также отследить своевременность исполнения 
задач сотрудниками.

Описание проекта

Task Tracker - это веб-приложение, которое помогает создавать (редактировать, удалять) сотрудников и различные задачи 
для них, а также контролировать сроки исполнения задач сотрудниками. После назначения новой задачи сотруднику 
приходит оповещение на электронную почту с описанием задачи и сроком её исполнения.

Стек технологий

Проект разработан с использованием следующего технологического стека:

    - Python 3.11
    - FastAPI: веб-фреймворк для создания веб-приложений на основе стандарта OpenAPI
    - SQLAlchemy: библиотека для взаимодействия с базой данных
    - Docker: для контейнеризации приложения

Инструкция по установке

Чтобы развернуть проект и начать его использовать необходимо выполнить следующие шаги:

    1. Склонируйте данный репозиторий: выполните команду git clone для клонирования репозитория 
       на свой локальный компьютер.
    
    2. Установите все необходимые зависимости:
        
        pip install -r requirements.txt

    3. Настройте файл .env: создайте файл .env в корневой директории проекта и добавьте в него переменные среды, 
        например:

        DB_NAME=employee_tasks
        DB_USER=postgres
        DB_PASS=your_database_password
        DB_HOST=localhost
        DB_PORT=5432
        
        DB_HOST_TEST=localhost
        DB_PORT_TEST=5432
        DB_NAME_TEST=employee_tasks_test
        DB_USER_TEST=postgres
        DB_PASS_TEST=your_testdatabase_password
        
        SMTP_HOST=smtp.gmail.com
        SMTP_PORT=465
        SMTP_USER=your_gmail_address
        SMTP_PASS=your_gmail_app_password
        
    4. Выполните миграции для создания базы данных:

        alembic upgrade head
    
    5. Для заполнения базы данных сотрудниками и имеющимися у них задачами запустите команду:

        python -m src.commands.add_data_for_DB

    6. Запустите приложение:

        uvicorn src.main:app --reload

    7. Откройте приложение: перейдите в веб-браузере по адресу http://127.0.0.1:8000/docs и начните 
        использовать приложение.

Краткое описание имеющихся эндпоинтов

В приложении "Task Tracker" есть несколько важных эндпоинтов:

    /employee/list - список сотрудников
    /employee/create - создание сотрудника
    /employee/get/{employee_id} - просмотр сотрудника
    /employee/update/{employee_id} - обновление сотрудника
    /employee/delete/{employee_id} - удаление сотрудника
    /employee/busy_employees - список занятых сотрудников

    /task/list - список задач
    /task/create - создание задачи
    /task/get/{task_id} - просмотр задачи
    /task/update/{task_id} - обновление задачи
    /task/delete/{task_id} - удаление задачи
    /task/important_tasks - список важных задач


Для запуска проекта в Docker необходимо выполнить следующие шаги:

    1. Настройте файл .env-non-dev: Создайте файл .env-non-dev в корневой директории проекта и добавьте в него переменные среды, 
        например:

        DB_NAME=employee_tasks
        DB_USER=postgres
        DB_PASS=your_database_password
        DB_HOST=db
        DB_PORT=5432
        
        POSTGRES_USER=postgres
        POSTGRES_DB=employee_tasks
        POSTGRES_PASSWORD=your_database_password
        
        SMTP_HOST=smtp.gmail.com
        SMTP_PORT=465
        SMTP_USER=your_gmail_address
        SMTP_PASS=your_gmail_app_password

    2. Для создания образа из Dockerfile и запуска контейнеров запустите команду:

        docker-compose up --build 
        или
        docker-compose up -d --build (для запуска в фоновом режиме)

    3. После успешного запуска, ваше приложение должно быть доступно по адресу http://localhost:7777/docs

    4. В терминале, где была запущена команда docker-compose up --build, нажмите Ctrl+C для остановки контейнеров

Автор проекта: Юрий Огородник

Документация проекта: http://127.0.0.1:8000/docs или http://127.0.0.1:8000/redoc