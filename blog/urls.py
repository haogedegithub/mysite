from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.homehandler,name = 'home'),
    path('index/',views.blog_list,name = 'index'),
    re_path('blog_detail/(.+)',views.blog_detail,name = 'blog_detail'),
    re_path('blogs_with_type/(.+)',views.blog_with_type,name = 'blogs_with_type'),
    path('date/<int:year>/<int:month>',views.blog_with_date,name = 'blog_with_date'),
]