from email.message import EmailMessage

from src.config import SMTP_USER


def create_task_assignment_message(first_name, email_to, task_title, deadline):
    email = EmailMessage()  # Создание объекта EmailMessage для формирования письма

    email["Subject"] = "Оповещение о новой задаче"  # Установка темы письма
    email["From"] = SMTP_USER  # Установка адреса отправителя
    email["To"] = email_to  # Установка адреса получателя
    email.set_content(  # Установка содержимого письма с использованием метода set_content
        f"Здравствуйте, {first_name}!\nВам назначена новая задача: {task_title}.\nСрок выполнения: {deadline}"
    )
    return email  # Возврат сформированного объекта EmailMessage, представляющего письмо
