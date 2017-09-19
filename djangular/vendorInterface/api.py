from rest_framework.generics import ListAPIView

from .serializers import PromotionSerializer, PromotionDetailsSerializer
from .models import Promotion, PromotionDetails

class PromotionApi(ListAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class PromotionDetailsApi(ListAPIView):
    queryset = PromotionDetails.objects.all()
    serializer_class = PromotionDetailsSerializer