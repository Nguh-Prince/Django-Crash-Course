# Generated by Django 5.0.1 on 2024-05-25 05:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_variant_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
