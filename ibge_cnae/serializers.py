from rest_framework import serializers
from .models import IbgeCNAE


class IbgeCNAESerializer(serializers.ModelSerializer):

    class Meta:
        model = IbgeCNAE
        fields = '__all__'
