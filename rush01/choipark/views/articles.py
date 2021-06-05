from django.shortcuts import render
from django.views import View
from ..forms import ArticleForm
from ..models import ArticleModel

class ArticleView(View):
    def post(self, request):
        form = ArticleForm(request.POST)
        if request.POST.get('up') or request.POST.get('down'):
            article = ArticleModel.objects.get(pk=request.POST.get('up') or request.POST.get('down'))
            if request.POST.get('up'):
                article.upvote(request.user)
            else:
                article.downvote(request.user)
        if request.POST.get('delete') :
            ArticleModel.objects.get(pk=request.POST.get('delete')).delete()
        tmpform = ArticleForm(request.POST)
        if tmpform.is_valid:
            content=request.POST.get('content')
            if content is not None:
                article = ArticleModel(content=request.POST.get('content'), author=request.user)
                article.save()
        articles = ArticleModel.objects.all()
        return render(request, 'base.html', {'form': form})
