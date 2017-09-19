from django.contrib import admin
from django.conf.urls import include, url

from .api import PromotionApi, PromotionDetailsApi

urlpatterns = [
    url(r'^promotions$', PromotionApi.as_view()),
    url(r'^promotionDetails$', PromotionDetailsApi.as_view())
    ]