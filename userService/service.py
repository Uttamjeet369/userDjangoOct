from rest_framework_simplejwt.tokens import RefreshToken

from userService.models import User, Role
from userService.producer import send_email_event


def sign_up_user(email, password, name):
    user = User(email=email, name=name)
    user.set_password(password)
    # user.roles.append(Role.objects.get(name='admin'))
    user.save()

    user_email_data = {
        'to': user.email,
        'from': 'abc@gmail.com',
        'subject': 'welcome',
        'body': 'welcome {}'.format(name)
    }
    send_email_event(user_email_data)


    return user


def login_user(email, password):
    user = User.objects.get(email=email)
    if not user.check_password(password):
        return None, Exception("invalid email or password")

    token = RefreshToken.for_user(user)
    return token, None
