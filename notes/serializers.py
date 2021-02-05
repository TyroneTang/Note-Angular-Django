from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"



class NoteDisplaySerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source="user.username")
    
    class Meta:
        model = Note
        fields = "__all__"