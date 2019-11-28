from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import NumberForm
from .helpers import to_words


class IndexView(FormView):
    template_name = 'frontend/index.html'
    form_class = NumberForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        number = self.request.POST.get('number')
        if number:
            context['text'] = to_words(number).capitalize()
        return self.render_to_response(context)
