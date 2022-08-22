from django.contrib import admin
from .models import post,User_register,Comment
# Register your models here.

admin.site.register(post)
admin.site.register(User_register)
admin.site.register(Comment)
