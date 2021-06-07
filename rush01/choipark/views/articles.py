from django.db.models.fields.related import ForeignKey
from django.shortcuts import render, redirect
from django.views import View
from ..forms import ArticleForm, CommentForm
from ..models import ArticleModel, CommentsModel

class ArticleView(View):
    def get(self, request, article_id):
        article = ArticleModel.objects.all().filter(id=article_id)
        comment = CommentForm()
        comments = CommentsModel.objects.all().filter
        # comments = article.comments.all()
        context = {
            'article' : article[0],
            'commentin' : comment,
            'comments' : comments,
        }
        return render(request, 'view_article.html', context)

    def post(self, request, article_id):
        form = ArticleForm(request.POST)
        if request.POST.get('up') or request.POST.get('down'):
            article = ArticleModel.objects.get(pk=request.POST.get('up') or request.POST.get('down'))
            if request.POST.get('up'):
                article.upvote(request.user)
            else:
                article.downvote(request.user)
        if request.POST.get('delete') :
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

        articles = ArticleModel.objects.all().filter(id=article_id)
        comment = CommentForm(request.POST)
        comment.instance.author_id = request.user.id
        comment.instance.article_id = article_id
        if comment.is_valid :
            content=request.POST.get('content')
            if content is not None:
                comment.save()
        comment = CommentForm()
        
        context = {
            "form" : form,
            "article" : articles[0],
            "comment" : comment,
        }
        return render(request, 'view_article.html', context)
