from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from ..forms import ArticleForm, CommentForm
from ..models import ArticleModel, CommentsModel
from django.http import HttpResponse, HttpResponseRedirect

class ArticleView(FormView):
    commentform = CommentForm
    def get(self, request, article_id):
        # article = get_object_or_404(Topic, pk=article_id)
        article = ArticleModel.objects.get(id=article_id)
        comments = CommentsModel.objects.all().filter(id=article_id)
        # reply = Co
        context = {

            'article' : article,
            'commentform' : self.commentform,
            'comments' : comments,
            #"replies" : ReplyModel.objects.all()
        }
        return render(request, 'view_article.html', context)
        # return HttpResponseRedirect('login')

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

        comment = self.commentform(request.POST)
        comment.instance.author_id = request.user.id
        comment.instance.article_id = article_id
        if comment.is_valid():
            comment.save()
        if request.POST.get('up_c') or request.POST.get('down_c'):
            comment = CommentsModel.objects.get(pk=request.POST.get('up_c') or request.POST.get('down_c'))
            if request.POST.get('up_c'):
                comment.upvote(request.user)
            else:
                comment.downvote(request.user)
        if request.POST.get('delete_c') :
            comment = CommentsModel.objects.get(pk=request.POST.get('delete_c'))
            if not (comment.author != request.user and request.user.is_staff == False and request.user.is_superuser == False):
                CommentsModel.objects.get(pk=request.POST.get('delete_c')).delete()



        # reply = self.replyform(request.POST)
        # reply.instance.author_id = request.user.id
        # reply.instance.comment_id = comment_id
        # if reply.is_valid():
        #     reply.save()
        # if request.POST.get('up_r') or request.POST.get('down_r'):
        #     reply = ReplyModel.objects.get(pk=request.POST.get('up_r') or request.POST.get('down_r'))
        #     if request.POST.get('up_r'):
        #         reply.upvote(request.user)
        #     else:
        #         reply.downvote(request.user)
        # if request.POST.get('delete_r') :
        #     reply = ReplyModel.objects.get(pk=request.POST.get('delete_r'))
        #     if not (reply.author != request.user and request.user.is_staff == False and request.user.is_superuser == False):
        #         ReplyModel.objects.get(pk=request.POST.get('delete_r')).delete()
        
        articles = ArticleModel.objects.all().filter(id=article_id)
        context = {
            "form" : form,
            "article" : articles[0],
            'commentin' : self.commentform,
            "comments" : CommentsModel.objects.all().filter(id=article_id),
            # "replies" : ReplyModel.objects.all()
        }
        return render(request, 'view_article.html', context)
