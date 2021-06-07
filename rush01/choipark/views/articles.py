from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from ..forms import CommentForm, ReplyForm
from ..models import ArticleModel, CommentsModel, ReplyModel

class ArticleView(FormView):
    form_comment = CommentForm
    def get(self, request, article_id):
        # article = get_object_or_404(Topic, pk=article_id)
        article = ArticleModel.objects.get(id=article_id)
        comments = CommentsModel.objects.all().filter(id=article_id)
        # reply = Co
        context = {
            'article' : article,
            'form_comment' : self.form_comment,
        }
        return render(request, 'view_article.html', context)
        # return HttpResponseRedirect('login')


class WriteCommentView(FormView):
    def post(self, request, article_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.article = ArticleModel.objects.get(id=article_id)
            temp_form.author = self.request.user
            temp_form.save()

        return redirect('article', article_id)
