from cmath import log
from django.urls import path
from .views import about_view,  draft, post_publish, user_register_view,login_view,home,logout,postdital,add_post,add_comment_post
from . import views

urlpatterns = [
    
    path('register/',user_register_view,name='register'),
    path('login/',login_view,name='login'),
    path('',home,name='home'),
    path('logout/',logout,name='logout'),
    path('about/',about_view,name='about'),
   
    path('newpost/',add_post,name='newpost'),
    path('postdital/<int:pk>',postdital,name='postdetail'),
    path('post/<int:pk>/edit/',views.UpdatePostView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/',views.PostDeleteView.as_view(),name='post_remove'),
    path('post/<int:pk>/publish/',post_publish,name='post_publish'),
    path('post/<int:pk>/comment/',add_comment_post,name='add_comment_post'),
    
    path('draft/',draft,name='draft'),
]

