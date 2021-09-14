import random

from django.shortcuts import render

from .models import Health, Food, FoodType


def index(request):
    health_name = {}
    defense = {}

    healths = Health.objects.all()
    for health in healths:
        health_name[health.id] = health.name

        if Food.objects.filter(health_id=health.id).all():
            food = random.choice(Food.objects.filter(health_id=health.id).all())

            if health.replied_id:
                defense[health.replied_id]['value'][health.id] = {'name': health.name, 'value': food.name}
                pass
            else:
                defense[health.id] = {'name': health.name, 'value': food.name}

        else:
            defense[health.id] = {'name': health.name, 'value': {}}

    return render(request, 'index/index.html', {'defense': defense})


def lists(request, health_id):
    food_type = FoodType.objects.all()

    foods = Food.objects.filter(health_id=health_id).all().order_by('food_type')

    return render(request, 'index/list.html', {'food_type': list(food_type), 'foods': foods})
