# Generated by Django 3.2.7 on 2021-09-12 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('replied', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.health')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.foodtype')),
                ('health', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.health')),
            ],
        ),
    ]
