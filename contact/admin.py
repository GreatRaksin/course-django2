from django.contrib import admin

from .models import ContactForm, Ticket


@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    """Форма обратной связи"""
    list_display = ("full_name", "email", "created")


@admin.register(Ticket)
class ContactAdmin(admin.ModelAdmin):
    """Форма тикетов"""
    list_display = ("user", "created")