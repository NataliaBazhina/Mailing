from django.urls import path
from mailing_app.views import (
    MailCreateView, MailListView, MailDetailView, MailUpdateView, MailDeleteView,
    MailingCreateView, ScheduledMailingCreateView, ImmediateMailingCreateView,
    MailingListView, MailingDetailView, ActiveMailingListView,
    MailingUpdateView, MailingDeleteView, MailingTryingListView, MailingTryingDetailView
)

app_name = 'mailing_app'

urlpatterns = [
    path('mail/', MailListView.as_view(), name='list_mail'),
    path('mail/create/', MailCreateView.as_view(), name='create_mail'),
    path('mail/view/<int:pk>/', MailDetailView.as_view(), name='view_mail'),
    path('mail/edit/<int:pk>/', MailUpdateView.as_view(), name='update_mail'),
    path('mail/delete/<int:pk>/', MailDeleteView.as_view(), name='delete_mail'),

    path('mailing/', MailingListView.as_view(), name='list_mailing'),
    path('mailing/create/', MailingCreateView.as_view(), name='create_mailing_options'),
    path('mailing/create/scheduled/', ScheduledMailingCreateView.as_view(), name='create_scheduled_mailing'),
    path('mailing/create/immediate/', ImmediateMailingCreateView.as_view(), name='create_immediate_mailing'),
    path('mailing/active/', ActiveMailingListView.as_view(), name='list_active_mailing'),
    path('mailing/view/<int:pk>/', MailingDetailView.as_view(), name='view_mailing'),
    path('mailing/edit/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing/delete/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),

    path('mailing_trying/', MailingTryingListView.as_view(), name='list_mailing_trying'),
    path('mailing_trying/view/<int:pk>/', MailingTryingDetailView.as_view(), name='view_mailing_trying'),
]