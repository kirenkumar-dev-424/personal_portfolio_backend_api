from .tasks import *
from rest_framework.exceptions import APIException
def send_mail(**data):
    try:
        name=data.get('name')
        email=data.get('email')
        subject=data.get('subject')
        message=data.get('message')
        send_message.schedule(args=(name,email,subject,message,),delay=5)
        return subject
    except:
        raise APIException('Cannot Send mail.')
