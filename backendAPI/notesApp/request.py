from rest_framework import serializers 

class createNoteRequest(serializers.Serializer):
    name = serializers.CharField(max_length = 50)
    description = serializers.CharField(max_length = 200)