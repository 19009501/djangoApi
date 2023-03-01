from rest_framework import serializers
from .models import *
class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ['id', 'receiver_name', 'description', 'receiver_mail']
    def validate(self,value):
        if not value['receiver_name'].isalpha() and ' ' not in value['receiver_name']:
            print("yes")
            raise serializers.ValidationError("Name must contain only letters and spaces.")
        if '@' not in value['receiver_mail']:
            print("@yes")
            raise serializers.ValidationError("@ not included")
        return value


    
    