from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.utils import timezone
from .forms import UserForm
from .models import Article, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    all_articles = Article.objects.all().order_by('-id')
    paginator = Paginator(all_articles, 5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render(request, 'articles/index.html', {'articles': articles})


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comment_set.all()
    try:
        previous = Article.objects.get(pk=int(article_id)-1)
    except Article.DoesNotExist:
        previous = Article.objects.all().order_by('-id')[0]
    try:
        nexta = Article.objects.get(pk=int(article_id)+1)
    except Article.DoesNotExist:
        nexta = Article.objects.all().order_by('id')[0]
    return render(request, 'articles/detail.html', {'article': article,
                                                    'previous': previous,
                                                    'nexta': nexta,
                                                    'comments': comments})


class UserFormView(View):
    form_class = UserForm
    template_name = "articles/registration_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('articles:index')
        return render(request, self.template_name, {'form': form})


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('articles:index')


def log_out(request):
    logout(request)
    return redirect('articles:index')


def comment(request, article_id):
    comment = Comment()
    comment.article = Article.objects.get(pk=article_id)
    comment.author = request.user.username
    comment.content = request.POST['comment']
    comment.pub_date = timezone.now()
    comment.save()
    return redirect('articles:detail', article_id)
