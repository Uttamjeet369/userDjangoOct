import json

from django.http import JsonResponse

from userService.service import sign_up_user, login_user
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = sign_up_user(data['email'], data['password'], data['name'])

        return JsonResponse({
            'user': user.name,
            'email': user.email,
            'user_id': user.id,
            'roles': [roles.role for roles in user.roles.all()]
        }, status=201)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            token, err = login_user(data['email'], data['password'])
            if err:
                return JsonResponse({'token': None}, status=401)
            return JsonResponse({'token': token.value}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'token': None}, status=500)

# TODO: Hello world method which accept a token and print user name...
