
from django.urls import path
from user.views import common_views
from django.urls.resolvers import URLPattern
from user.views.common_views import *
from user.views.blogs_views.blog_listing import *
from user.views.blogs_views.single_blog import *

urlpatterns = [
    # All objects
    path('allBlogs', allBlogs, name='allBlogs'),
    path('allBlogs/<int:page>', allBlogs, name='allBlogs'),

    # Single blog
    path('singleBlog/<int:blog_id>', singleBlog, name='singleBlog'),

    # Filtering
    path('blogByTags/<str:tag_name>', blogByTags, name='blogByTags'),
]
