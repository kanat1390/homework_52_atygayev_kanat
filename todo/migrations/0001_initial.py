# Generated by Django 4.1.1 on 2022-09-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
                ('status', models.CharField(choices=[('N', 'Новая'), ('P', 'В процессе'), ('C', 'Выполнена')], default='N', max_length=1, verbose_name='Статус')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата закрытия')),
            ],
        ),
    ]