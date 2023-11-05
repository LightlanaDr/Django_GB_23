from django.http import HttpResponse
import logging

from django.shortcuts import get_object_or_404, render
from django.template.response import TemplateResponse

from .forms import AuthorForm, NewPost, CommentForm
from .models import Author, Post, Comment

logger = logging.getLogger(__name__)


def author_read(request):
    author = Author.objects.all()
    return HttpResponse(author)


def post_read(request):
    posts = Post.objects.all()
    return HttpResponse(posts)


def post_by_authors(request):
    name = request.GET.get('name')
    author_id = Author.objects.filter(f_name=name).first()
    post = Post.objects.filter(author=author_id)
    return HttpResponse(post)


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')
    # posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp_blog/post_of_authors.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.show_content += 1
    post.save()
    return render(request, 'myapp_blog/post_full.html', {'post': post})


def view_all_posts(request):
    posts = Post.objects.all()
    context = {'title': 'Список статей',
               'posts': posts}
    return TemplateResponse(request, 'myapp_blog/posts.html', context)


def post_comm(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post).all()
    post.show_content += 1
    post.save()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.data['comment']
            post_id = form.data['post']
            post = Post.objects.filter(id=post_id).first()
            author = post.author
            comments = Comment(author=author,
                               post=post,
                               publication=True)
            comments.save()
            return render(request, 'myapp_blog/comment.html',
                          {'form': form, 'post': post, 'comments': comment})
        else:
            form = CommentForm()
        return render(request, 'myapp_blog/comment.html',
                       {'post': post, 'comments': comments,'form': form})

    # return render(request, 'myapp_blog/comment.html', {'post': post, 'comments': comments})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            logger.info(f'Получили {f_name=}, {l_name=}, {email=}.')
            author = Author(f_name=f_name, l_name=l_name, email=email,
                            biography=biography, birthday=birthday)
            author.save()
            message = 'Пользователь сохранён'
    else:
        form = AuthorForm()
        message = 'Заполните форму'
    return render(request, 'myapp_blog/author_form.html',
                  {'form': form, 'message': message})


def create_post(request):
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            form.save()
            message = 'Статья добавлена'

    else:
        form = NewPost()
        message = 'Заполните форму'
    return render(request, 'myapp_blog/create_post.html',
                  {'form': form, 'message': message})


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.data['comment']
            post_id = form.data['post']
            post = Post.objects.filter(id=post_id).first()
            author = post.author
            comments = Comment(author=author,
                               post=post,
                               publication=True)
            comments.save()
            return render(request, 'myapp_blog/comment.html',
                          {'form': form})
        else:
            form = CommentForm()
        return render(request, 'myapp_blog/comment.html',
                       {'form': form})
