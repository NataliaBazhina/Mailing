from django.views.generic import CreateView,UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from mailing_app.forms import MailingForm
from mailing_app.models import Mail, Mailing, MailingTrying


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


@method_decorator(cache_page(60*15), name='dispatch')
class MailingDetailView(DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailing_id = self.object.id
        context['success_count'] = MailingTrying.get_success_count(mailing_id)
        context['failure_count'] = MailingTrying.get_failure_count(mailing_id)
        context['sent_messages_count'] = (context['success_count'] + context['failure_count'])
        return context

@method_decorator(cache_page(60*15), name='dispatch')
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

class MailingTryingListView(ListView):
    model = MailingTrying
    template_name = "mailing_app/mailing_trying_list.html"
    context_object_name = 'list_mailing_trying'

class MailingTryingDetailView(DetailView):
    model = MailingTrying
    template_name = "mailing_app/mailing_trying_detail.html"
    context_object_name = 'view_mailing_trying'