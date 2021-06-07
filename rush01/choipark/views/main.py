from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import View
from ..models import ArticleModel

class MainView(View):
    template_name = 'registration/main.html'
    def get(self, request) :
        try:
            article = ArticleModel.objects.all().order_by('-date')
        except Exception as e:
            article = []
        context = {
            'articles': article,
        }
        return render(request, self.template_name, context)
    def  post(self, request):
        return render(request, self.template_name)



