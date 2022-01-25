from rest_framework.serializers import ModelSerializer
from room.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields =