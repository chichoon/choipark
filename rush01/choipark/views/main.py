from django.shortcuts import render
from django.views.generic import CreateView 
from django.views.generic import View
from ..models import ArticleModel

class MainView(View):
    def get(self, request) :
        template_name = 'registration/main.html'
        try:
            article = ArticleModel.objects.all().order_by('-date')
        except Exception as e:
            article = []
        context = {
            'article': article,
        }
        return render(request, template_name, context)

