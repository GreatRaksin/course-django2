# Generated by Django 2.1.7 on 2019-03-15 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=100, verbose_name='url')),
                ('pagination', models.PositiveIntegerField(default=5, verbose_name='Кол. для пагинации')),
                ('template', models.CharField(default='news/post-list.html', max_length=100, verbose_name='Используемый шаблон')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='news.Category')),
            ],
            options={
                'verbose_name': 'Категория статей',
                'verbose_name_plural': 'Категории статей',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('moderation', models.BooleanField(default=False, verbose_name='Разрешено к публикации')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата написания')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('subtitle', models.CharField(default='', max_length=100, verbose_name='Подзаголовок')),
                ('mini_text', models.TextField(default='', max_length=1000, verbose_name='Краткое содержание')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(blank=True, upload_to='post/', verbose_name='Главное изображение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edit_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата редактирования')),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата публикации')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовать?')),
                ('status', models.BooleanField(default=False, verbose_name='Для зарегистрированных')),
                ('slug', models.SlugField(max_length=100, verbose_name='url')),
                ('viewed', models.PositiveIntegerField(default=0, verbose_name='Просмотров')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=100, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='news.Tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Post', verbose_name='Статья'),
        ),
    ]
