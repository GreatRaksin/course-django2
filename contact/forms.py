from django import forms

from .models import ContactForm, Ticket


class ContactForm(forms.ModelForm):
    """Форма обратной связи"""
    class Meta:
        model = ContactForm
        fields = ['full_name', 'email', 'text']


class TicketForm(forms.ModelForm):
    """Форма тикетов"""
    class Meta:
        model = Ticket
        fields = ['text', ]