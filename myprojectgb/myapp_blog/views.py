from django.http import HttpResponse
import logging
from .models import Author, Post

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
