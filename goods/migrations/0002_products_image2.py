# Generated by Django 4.2.7 on 2024-05-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение2'),
        ),
    ]
