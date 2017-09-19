from django.contrib import admin

# Register your models here.

from .models import Promotion, PromotionDetails

admin.site.register(Promotion)
admin.site.register(PromotionDetails)