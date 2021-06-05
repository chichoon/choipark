from django.views.generic import FormView
from ..forms import ArticleForm
from ..models import ArticleModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class AddArticle(LoginRequiredMixin, FormView):
    template_name = "add_article.html"
    form_class = ArticleForm
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('login')

    def get(self, request):
        form = self.form_class(initial=self.initial)
        self.form_invalid
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = self.form_class(request.POST)
        self.form_valid(form)
        return render(request, self.template_name, {'form': form,})

    def form_valid(self, form):
        title = form.clean_data['title']
        content = form.clean_data['content']
        try:
            ArticleModel.objects.create(
                title=title,
                content=content,
                author=self.request.user,
            )
        except print(0):
            pass
        return super().form_valid(form)

    def form_invalid(self, form_class):
        return super().form_invalid()
