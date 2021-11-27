from rest_framework import status
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth import authenticate
@api_view(['POST',])
def register_apiView(reqeust):
    if reqeust.method=='POST':
        serializer = UserSerializer(data=reqeust.data)
        data ={}
        if serializer.is_valid():
            account = serializer.save()
            data['response']="Successfully registered"
            data['email']= account.email
        else:
            data=serializer.errors
        return Response(data)

@api_view(['POST',])
def loginapiview(request):
    data = {}
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            data['result']=1
        else:
            data['result']=0
        print(data)
        return Response(data)