# Generated by Django 3.1.7 on 2021-05-04 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fonda', '0004_restaurant_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='fonda.order'),
        ),
    ]