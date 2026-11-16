from huey.contrib.djhuey import task
from django.conf import settings
from django.core.mail import EmailMessage


@task()
def send_message(name, email, subject, message):

    sender_email = settings.MAILERS['default']['OPTIONS']['username']

    email_subject = f"🏢Portfolio Contact: {subject}"

    email_message = f"""
    You have received a new message from your portfolio.

    Name: {name}
    Email: {email}

    Subject: {subject}

    Message:
    {message}
    """

    mail = EmailMessage(
        subject=email_subject,
        body=email_message,
        from_email=sender_email,
        to=[sender_email],
        reply_to=[email],
        connection=None
    )

    sent_count = mail.send()

    return sent_count == 1