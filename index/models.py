from django.db import models


class Health(models.Model):

    name = models.CharField(max_length=10)

    replied = models.ForeignKey(
        'Health',
        on_delete=models.CASCADE,
        null=True,
    )


class FoodType(models.Model):
    name = models.CharField(max_length=20)


class Food(models.Model):

    name = models.CharField(max_length=128)

    health = models.ForeignKey(Health, on_delete=models.CASCADE)

    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
