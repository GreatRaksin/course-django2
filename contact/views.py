from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from Course_django2.settings import DEFAULT_FROM_EMAIL
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View

from Course_django2 import settings
from .models import ContactForm as ContactModel, Ticket
from .forms import ContactForm, TicketForm


def mail(messages):
    subject = "Новое сообщение"
    messages = messages,
    from_email = DEFAULT_FROM_EMAIL
    recipient_list = ["admin@gmail.com"]
    # send_mail(subject, messages, from_email, recipient_list)


class TicketList(ListView):
    """Список сообщений пользователя"""
    template_name = "contact/ticket-list.html"

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


class TicketCreate(CreateView):
    """Создание тикета"""
    model = Ticket
    form_class = TicketForm
    template_name = 'contact/contact-form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.add_message(self.request, settings.MY_INFO, 'Спасибо!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, settings.MY_INFO, 'Ошибка!')
        return super().form_valid(form)


class TicketUpdate(UpdateView):
    """Редактирование тикетов"""
    model = Ticket
    form_class = TicketForm
    template_name = 'contact/contact-form.html'


class TicketDelete(DeleteView):
    """Удаление тикета"""
    model = Ticket
    template_name = 'contact/ticket-delete.html'
    success_url = reverse_lazy('ticket-list')


class ContactFormView(CreateView):
    """Обработка контактной формы"""
    model = ContactModel
    form_class = ContactForm
    template_name = 'contact/contact-form.html'

    def form_valid(self, form):
        mail("Вам отправили сообщение через контактную форму")
        messages.add_message(self.request, settings.MY_INFO, 'Спасибо!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, settings.MY_INFO, 'Ошибка!')
        return super().form_valid(form)

    # def post(self, request):
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         mail("Вам отправили сообщение через контактную форму")
    #         messages.add_message(request, settings.MY_INFO, 'Спасибо!')
    #     else:
    #         messages.add_message(request, settings.MY_INFO, 'Ошибка!')
    #     return redirect('contact')





