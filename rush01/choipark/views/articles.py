from django.shortcuts import render, redirect
from django.views import View
from ..forms import ArticleForm
from ..models import ArticleModel

class ArticleView(View):
    def get(self, request, article_id):
        article = ArticleModel.objects.all().filter(id=article_id)
        return render(request, 'view_article.html', {'article': article[0]})

    def post(self, request, article_id):
        form = ArticleForm(request.POST)
        if request.POST.get('up') or request.POST.get('down'):
            article1 = ArticleModel.objects.all().filter(id=article_id)
            article = ArticleModel.objects.get(pk=request.POST.get('up') or request.POST.get('down'))
            if request.POST.get('up'):
                article.upvote(request.user)
            else:
                article.downvote(request.user)
        if request.POST.get('delete') :
            article1 = ArticleModel.objects.all().filter(id=article_id)
            article = ArticleModel.objects.get(pk=request.POST.get('delete'))
            if not (article.author != request.user and request.user.is_staff == False and request.user.is_superuser == False):
                ArticleModel.objects.get(pk=request.POST.get('delete')).delete()
                return redirect('/')
        tmpform = ArticleForm(request.POST)
        if tmpform.is_valid:
            content=request.POST.get('content')
            if content is not None:
                article = ArticleModel(content=request.POST.get('content'), author=request.user)
                article.save()
        articles = ArticleModel.objects.all()
        return render(request, 'view_article.html', {'form': form, 'article': article1[0]})
