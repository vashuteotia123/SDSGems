from django.core.paginator import Paginator
from firstapp.models import *
from user.models import *
from django.shortcuts import *
from django.core.exceptions import ObjectDoesNotExist


def singleBlog(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        related_blogs = Blog.objects.filter(
            tags__in=blog.tags.all()).exclude(id=blog_id).distinct()
        message = "Blog found"
    except ObjectDoesNotExist:
        blog = None
        message = "Blog not found"
        related_blogs = None
    context = {
        "blog": blog,
        "message": message,
        "related_blogs": related_blogs,
    }
    return render(request, 'blog_detail.html', context=context)
