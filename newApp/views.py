from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from .emails import *
class RecieverViewset(viewsets.ModelViewSet):
    queryset=Receiver.objects.all()
    serializer_class=ReceiverSerializer
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
               serializer.save()
               send_otp(serializer.data['email'])
            return Response({
                "status":200,'message':"donation recieved",'data':serializer.data
            })
            return Response({
                'status':400,
                'message':'something went wrong',
                'data':serializers.error
            })
        except Exception as e:
            print(e)
            
        
# Create your views here.
