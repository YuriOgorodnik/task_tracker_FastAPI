from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import aiosmtplib


async def send_email(employee_email, task_title, deadline):
    sender_email = "yuri.ogorodnik1@gmail.com"
    sender_password = "rjknyimyfeprwahz"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = employee_email
    message["Subject"] = "Новая задача назначена"

    mail_content = f"Здравствуйте, Вам назначена новая задача: {task_title}. Срок выполнения: {deadline}"
    message.attach(MIMEText(mail_content, "plain"))

    async with aiosmtplib.SMTP('smtp.gmail.com', 465) as server:
        await server.starttls()
        await server.login(sender_email, sender_password)
        await server.send_message(message)
