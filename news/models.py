from django.db import models


class Category(models.Model):
    """Модель категорий статей"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория статей"
        verbose_name_plural = "Категории статей"


class Tag(models.Model):
    """Модель тегов"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Статьи"""
    title = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, verbose_name="Теги")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created"]

