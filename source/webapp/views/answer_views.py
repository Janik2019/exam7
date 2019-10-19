from webapp.models import Answer, Poll, Choice
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import View


class PollsAnswer(View):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        poll = get_object_or_404(Poll, pk=pk)
        print(poll)
        return render(self.request, 'answer.html', {'poll': poll})


    # def post(self, request,*args, **kwargs):
    #     (request.POST)
    #     return redirect('index')

    # def post(self, request, *args, **kwargs):
    #     pk = request.POST['answer']
    #     answer = get_object_or_404(Choice, pk=pk)
    #     print(answer)
    #     poll = get_object_or_404(Poll, pk=kwargs['pk'])
    #     Answer.objects.create(answer=answer, poll=poll)
    #     return redirect('index')


