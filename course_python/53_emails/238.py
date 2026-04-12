from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

my_email = EmailMessage()

html_template = Template(Path("/Users/pavel/personal/py_learn/course_python/53_emails/templates/index.html").read_text())
html = html_template.substitute({"name": "Pavel", "date": "tommorow"})

my_email["from"] = "Pavel"
my_email["to"] = "novikevichp@gmail.com"
my_email["subject"] = "Let's go out"
my_email.set_content(html, "html")

with open("/Users/pavel/personal/py_learn/course_python/53_emails/images/aaa.jpg", "rb") as my_img:
    image_data = my_img.read()
    my_email.add_attachment(image_data, maintype="image", subtype="jpg", filename="aaa.jpg")

with smtplib.SMTP(host="localhost", port=2525) as message:
    message.ehlo()
    message.send_message(my_email)
    print("Email was sent")


# class EmailSender:
#     def __init__(self, host: str, port: int):
#         self.localhost = host
#         self.port = port

#     def create_message(self, sender: str, recipient: str, content: str, body: str):
#         message = EmailMessage()
#         message["from"] = sender
#         message["to"] = recipient
#         message["subject"] = content
#         message.set_content(body)
#         return message

#     def send_message(self, message: EmailMessage):
#         with smtplib.SMTP(host=self.localhost, port=self.port) as smtp_server:
#             smtp_server.ehlo()
#             smtp_server.send_message(message)
#             print("Email was sent")

# sender = EmailSender(host="localhost", port=2525)

# email = sender.create_message(
#     sender="Pavel",
#     recipient="Polina",
#     content="Hello message",
#     body="Hello^ my dear. How are you?"
# )

# sender.send_message(email)

