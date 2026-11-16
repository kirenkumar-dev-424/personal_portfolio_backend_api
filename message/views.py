from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .service import *
# Create your views here.
class SendMail(APIView):
    class InputSerializer(serializers.Serializer):
        name=serializers.CharField()
        email=serializers.EmailField()
        subject=serializers.CharField()
        message=serializers.CharField()
    def post(self,request):
        serializer=self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send=send_mail(**serializer.validated_data)
        return Response({'message':send},status=status.HTTP_201_CREATED)