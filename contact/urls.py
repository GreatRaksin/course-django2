from django.urls import path

from .views import *

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact'),
    path('ticket/', TicketList.as_view(), name='ticket-list'),
    path('ticket/add/', TicketCreate.as_view(), name='ticket-create'),
    path('ticket/update/<int:pk>/', TicketUpdate.as_view(), name='ticket-update'),
    path('ticket/delete/<int:pk>/', TicketDelete.as_view(), name='ticket-delete'),
]