from django.db import models

# Create your models here.
class Promotion(models.Model):

    promotion_id = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Promotions: {}".format(self.promotion_id)


class PromotionDetails(models.Model):
    promotion = models.ForeignKey(Promotion, related_name = "details")
    date_time = models.DateTimeField(null = True,blank=True)
    sales_count = models.IntegerField(null = True,blank=True)
    items_count = models.IntegerField(null = True,blank=True)
    items_quantity = models.IntegerField(null = True,blank=True)
    items_amount = models.FloatField(null = True, blank=True)

    def __str__(self):
        return "Details: {}".format(self.promotion, self.date_time, self.sales_count,
                                    self.items_count, self.items_quantity,
                                    self.items_amount)