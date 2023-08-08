# Generated by Django 4.1.7 on 2023-08-08 20:57

import ExchangeLogistics.exchange.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('offer_type', models.CharField(choices=[('Freight', 'Freight'), ('Truck space', 'Truck space')], default='Freight', max_length=50)),
                ('loading_date', models.DateField()),
                ('loading_country', models.CharField(max_length=50)),
                ('loading_place', models.CharField(max_length=50)),
                ('load_size', models.DecimalField(decimal_places=2, help_text='Value between 0 and 15 meters.', max_digits=4, validators=[ExchangeLogistics.exchange.validators.validate_load_size])),
                ('weight', models.DecimalField(decimal_places=2, help_text='Value between 0 and 28 tons.', max_digits=4, validators=[ExchangeLogistics.exchange.validators.validate_load_weight])),
                ('unloading_date', models.DateField(validators=[ExchangeLogistics.exchange.validators.date_validator])),
                ('unloading_country', models.CharField(max_length=50)),
                ('unloading_place', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[ExchangeLogistics.exchange.validators.validate_price], verbose_name='Price in EURO')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
