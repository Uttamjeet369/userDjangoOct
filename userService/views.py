import json

from django.http import JsonResponse
from rest_framework.decorators import permission_classes, api_view

from userService.service import sign_up_user, login_user
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = sign_up_user(data['email'], data['password'], data['name'])

        if user is not None:
            referesh_token = RefreshToken.for_user(user)

            return JsonResponse({
                'user': user.name,
                'email': user.email,
                'user_id': user.id,
                'roles': [roles.role for roles in user.roles.all()],
                'token': str(referesh_token.access_token),
                'refresh_token': str(referesh_token),
            }, status=201)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            token, err = login_user(data['email'], data['password'])
            if err:
                return JsonResponse({'token': None}, status=401)
            return JsonResponse({'token': str(token.access_token), 'refresh_token': str(token)}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'token': None}, status=500)


# TODO: Hello world method which accept a token and print user name...


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sayHello(request):
    return JsonResponse({'hello': 'world'}, status=200)
