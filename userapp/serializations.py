from rest_framework import serializers
from userapp.models import Customer
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model:Customer
        fields="__all__"
        