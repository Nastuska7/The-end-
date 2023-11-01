# Generated by Django 4.2.5 on 2023-10-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='заголовок')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, max_length=10, verbose_name='цена')),
                ('action', models.BooleanField(help_text='отметьте, если торг уместен', verbose_name='торг')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_up', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
