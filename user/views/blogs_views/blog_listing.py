from django.core.paginator import Paginator
from firstapp.models import *
from user.models import *
from django.shortcuts import *


def allBlogs(request, page=1):
    all_objects = Blog.objects.all()
    paginator = Paginator(all_objects, 12)
    try:
        all_objects = paginator.page(page)
    except:
        all_objects = paginator.page(1)
    context = {
        "all_blogs": all_objects,
    }
    return render(request, 'blogs_list.html', context=context)


def blogByTags(request, tag_name, page=1):
    all_objects = Blog.objects.filter(tags__name=tag_name)
    paginator = Paginator(all_objects, 12)
    try:
        all_objects = paginator.page(page)
    except:
        all_objects = paginator.page(1)
    context = {
        "all_blogs": all_objects,
    }
    return render(request, 'blogs_list.html', context=context)
