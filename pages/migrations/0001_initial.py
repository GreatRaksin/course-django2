# Generated by Django 2.1.7 on 2019-03-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Текст')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('template', models.CharField(default='pages/index.html', max_length=500, verbose_name='Шаблон')),
                ('slug', models.SlugField(default='', max_length=500, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]
