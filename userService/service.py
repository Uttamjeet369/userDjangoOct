from userService.models import User, Role


def sign_up_user(email, password, name):
    user = User(email=email, name=name)
    user.set_password(password)
    # user.roles.append(Role.objects.get(name='admin'))
    user.save()
    return user


def login_user(email, password):
    user = User.objects.get(email=email)
    if not user.check_password(password):
        return None, Exception("invalid email or password")

    token = user.generate_auth_token()
    return token, None
