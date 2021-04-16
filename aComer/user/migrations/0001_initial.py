# Generated by Django 3.1.7 on 2021-04-16 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fonda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('pesimo', 'Pesimo'), ('malo', 'Malo'), ('regular', 'Regular'), ('bueno', 'Bueno'), ('muy bueno', 'Muy Bueno')], default='muy bueno', max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ratings', to='user.client')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ratings', to='fonda.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='ClientAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=75)),
                ('suburb', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('int_number', models.IntegerField()),
                ('ext_number', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to='user.client')),
            ],
        ),
    ]
