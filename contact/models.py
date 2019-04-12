from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ContactForm(models.Model):
    """Модель формы обратной связи"""
    full_name = models.CharField("ФИО", max_length=30)
    email = models.EmailField("E-Mail", max_length=70)
    text = models.TextField("Сообщение")
    created = models.DateTimeField("Дата сообщения", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.email)

    def get_absolute_url(self):
        return reverse('contact')

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["-created"]


class Ticket(models.Model):
    """Модель тикетов"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение")
    created = models.DateTimeField("Дата сообщения", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.created)

    def get_absolute_url(self):
        return reverse('ticket-list')

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["-created"]
