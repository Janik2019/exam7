from webapp.models import Poll
from webapp.forms import PollForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class IndexView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'poll/index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        return Poll.objects.all().order_by('-created_at')


class PollView(DetailView):
    template_name = 'poll/poll_view.html'
    model = Poll
    context_object_name = 'poll'


class PollCreateView(CreateView):
    model = Poll
    template_name = 'poll/poll_create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('index')