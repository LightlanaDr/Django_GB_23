from django.http import HttpResponse
import logging

from django.shortcuts import get_object_or_404, render
from django.template.response import TemplateResponse

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


# def view_post(request, id_post):
#     post = get_object_or_404(Post, pk=id_post)
#     # post = Post.objects.get(id=id_post)
#     context = {'title': post.title,
#                'text': post.content}
#     post.show_content += 1
#     post.save()
#     return render(request, 'myapp_blog/post.html', context)

def post_comm(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post).all()
    post.show_content += 1
    post.save()
    return render(request, 'myapp_blog/comment.html', {'post': post, 'comments': comments})
