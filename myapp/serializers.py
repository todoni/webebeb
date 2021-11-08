from rest_framework import serializers
from .models import Users

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'login',
            'mail',
			'last_modified',
        )
        model = Users
