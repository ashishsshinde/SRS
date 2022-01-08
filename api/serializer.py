from rest_framework import serializers

class LoginSerializer(serializers.Serializer):  
    id = serializers.IntegerField() 
    username = serializers.CharField(max_length=100)   
    password = serializers.CharField(max_length=100)

class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    firstname = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    mobile = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)