# Generated by Django 4.1.2 on 2022-10-09 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothingXX', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingXX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.FloatField(default=0)),
                ('product_number', models.IntegerField(blank=True, null=True)),
                ('product_name', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='clothingXY')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'clothingXX',
            },
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]