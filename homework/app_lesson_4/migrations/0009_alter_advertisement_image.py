# Generated by Django 4.2.5 on 2023-10-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_4', '0008_alter_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='/advertisements/Default.jpg', upload_to='advertisements/', verbose_name='изображение'),
        ),
    ]
