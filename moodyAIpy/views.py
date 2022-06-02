from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

# from .models import User, AIResponse
from .models import AIResponse
from .serializers import *

UserModel = get_user_model()

def index(request):
  return HttpResponse("Hello. You are at the MoodyAI RESTful API. There are no public endpoints to display.")


@api_view(['POST'])
def register(request):
  
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def one_user(request, pk):
  try:
    user_instance = UserModel.objects.get(pk=pk)
  except UserModel.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.user.id == int(pk):
    serializer = UserSerializer(user_instance, context={'request': request})
    return Response(serializer.data)

  else:
    return Response(status=status.HTTP_403_FORBIDDEN)


# @api_view(['GET'])
# def one_user(request, pk):
#   try:
#     user_instance = User.objects.get(pk=pk)
#   except User.DoesNotExist:
#     return Response(status=status.HTTP_404_NOT_FOUND)
  
#   serializer = UserSerializer(user_instance, context={'request': request})
  
#   return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def responses_list(request, fk):
    try:
        data = AIResponse.objects.filter(user = fk)
    except AIResponse.DoesNotExist:
        data = None

    if request.user.id != int(fk):
        return Response(status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'GET':
        serializer = AIResponseSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AIResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def one_response(request, pk):
    try:
        response_instance = AIResponse.objects.get(pk=pk)
    except AIResponse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user.id != int(response_instance.user):
        return Response(status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'PUT':
        serializer = AIResponseSerializer(response_instance, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        response_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)