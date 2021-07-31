import sys
import uuid
from flask_mail import Message

def random_string(string_length=10):
    """Returns a random string of length string_length"""""
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]

def send_token_email(user):
    sys.path.append('../')
    from app import mail
    token = random_string(6)
    msg = Message('CBS Vote Login Token', sender='femi.blvk@gmail.com', recipients=[user.email])
    msg.body = f'''Here's your login token!, Happy Voting!:
{token}

If you did not make this request then simply ignore this email and no change would be applied
    '''
    mail.send(msg)
    
    return token