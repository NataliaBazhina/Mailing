from django.views.generic import CreateView,UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import now
from mailing_app.forms import MailingForm
from mailing_app.models import Mail, Mailing



class MailCreateView(CreateView):
    model = Mail
    fields = ('topic', 'content',)
    success_url = reverse_lazy("mailing_app:list_mail")


class MailDetailView(DetailView):
    model = Mail


class MailListView(ListView):
    model = Mail


class MailUpdateView(UpdateView):
    model = Mail
    fields = ('topic', 'content',)
    success_url = reverse_lazy('mailing_app:list_mail')


class MailDeleteView(DeleteView):
    model = Mail
    success_url = reverse_lazy('mailing_app:list_mail')


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing_app:list_mailing")

    def form_valid(self, form):
        mailing = form.save(commit=False)
        if mailing.first_mailing:
            mailing.next_mailing = mailing.first_mailing
        else:
            mailing. next_mailing = now()
        mailing.save()
        return super().form_valid(form)



class MailingDetailView(DetailView):
    model = Mailing


class MailingListView(ListView):
    model = Mailing

class ActiveMailingListView(ListView):
    model = Mailing
    template_name = "mailing_app/mailing_active_list.html"
    context_object_name = 'active_mailing_list'

    def get_queryset(self):
        return Mailing.objects.filter(status='RN')

class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('next_mailing', 'frequency','status', 'clients', 'mail',)
    success_url = reverse_lazy('mailing_app:list_mailing')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing_app:list_mailing')

