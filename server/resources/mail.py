import sys
import uuid
from flask_mail import Message


def send_token_email(user):
    sys.path.append('../')
    from app import mail
    token = uuid.uuid4
    msg = Message('CBS Vote Login Token', sender='femi.blvk@gmail.com', recipients=[user.email])
    msg.body = f'''Here's your login token!, Happy Voting!:
{token}

If you did not make this request then simply ignore this email and no change would be applied
    '''
    mail.send(msg)
    
    return token