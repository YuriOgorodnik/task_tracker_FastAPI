import smtplib

from src.config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS
from src.tasks.email_sender import create_task_assignment_message


def send_assign_task_email(first_name, email_to, task_title, deadline):
    msg_content = create_task_assignment_message(
        first_name, email_to, task_title, deadline
    )  # Создание содержимого письма

    with smtplib.SMTP_SSL(
        SMTP_HOST, SMTP_PORT
    ) as server:  # Установление защищенного соединения с SMTP сервером
        server.login(
            SMTP_USER, SMTP_PASS
        )  # Аутентификация на сервере с использованием учетных данных
        server.send_message(msg_content)  # Отправка письма через сервер
