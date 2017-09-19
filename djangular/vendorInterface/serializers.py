from rest_framework import serializers

from .models import Promotion, PromotionDetails

class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = '__all__'


class PromotionDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PromotionDetails
        fields = '__all__'