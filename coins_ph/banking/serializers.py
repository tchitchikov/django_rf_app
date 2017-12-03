from rest_framework import serializers
from banking.models import Account, Payment, User


class PaymentSerializer(serializers.Serializer):
    # a bunch of constants
    account = serializers.IntegerField()
    to_account = serializers.IntegerField()
    direction = serializers.CharField(max_length=20)
    amount = serializers.FloatField()
    timestamp = serializers.DateTimeField()

    def create(self, validated_data):
        return Payment.objects.create(**validated_data)

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    active = serializers.BooleanField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


class AccountSerializer(serializers.Serializer):
    # a bunch of constants
    user_id = serializers.IntegerField()
    currency = serializers.CharField(max_length=10)
    balance = serializers.FloatField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        """
        Create and return a new Account instance
        """
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Account instance
        """
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.active = validated_data.get('active', instance.balance)
        instance.save()
        return instance