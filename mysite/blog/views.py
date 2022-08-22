from ast import List

from django.views.generic import (ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView)
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import post,User_register,Comment
from .forms import CommentForm, PostForm,User_register_form

from django.urls import reverse_lazy




def draft(request):
    if 'user' in request.session:
        dates = post.objects.all()
        return render(request,'blog/draft.html',{'da':dates})


def add_comment_post(request,pk):
    if 'user' in request.session:
        posts = get_object_or_404(post, pk=pk)
        if request.method=="POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                
                comment = form.save(commit=False)
                comment.posts = posts

                comment.save()
                
                return redirect('postdetail',pk=posts.pk)
        else:
            form = CommentForm()
        return render(request,'blog/comment_form.html',{'form':form})


def post_publish(request, pk):
    if 'user' in request.session:

        posts = get_object_or_404(post, pk=pk)
        posts.publish()
        return redirect('postdetail', pk=pk)


class UpdatePostView(UpdateView):
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = post


class PostDeleteView(DeleteView):
    model = post
    success_url = reverse_lazy('home')




    
##########################################3
def postdital(request,pk):

    if 'user' in request.session:
       user_data = post.objects.get(pk=pk)
        
    return render(request,'blog/post_detail.html',{'a':user_data})

def add_post(request):
    if 'user' in request.session:
        form_post = PostForm()
        if request.method=='POST':
            form_post = PostForm(request.POST)
            if form_post.is_valid():
                v = form_post.save(commit=True)
                print(v.id)
                
              

                return redirect('postdetail',pk=v.id)
                
                # return render(request,'post_detail.html',{'form':form_post})

                
    
        return render(request,'blog/post_form.html',{'form':form_post})
    else:
        return redirect('login')

###################################
def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('home')
    return redirect('login')

def login_view(request):
   
    if request.method=='POST':
        user = User_register.objects.get(useremail=request.POST['username'])
        
        if user.userpassword == request.POST['password']:
            login_user = user.username
            request.session['user']= login_user
            return redirect('home')
            
            # return render(request,'base.html',{'login_user':user})
        else:
            return HttpResponse("please enter  the valid username")
        
    return render(request,'login.html')

def user_register_view(request):
    form = User_register_form()
    if request.method =="POST":
        form = User_register_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            print("enter valid informations......")
    return render(request,'register.html',{'form':form})

def home(request):
    if 'user' in request.session:
        user_name= request.session['user']
        publish = post.objects.all()
        return render(request,'home.html',{'publish':publish,'user':user_name})
        
    else:
        return redirect('login')

def about_view(request):
    return render(request,'about.html')











# def new(request):
#     if 'user' in request.session:
#         # form = PostForm()
#         form = get_object_or_404(PostForm)
        
#         if request.method =="POST":
#             form = PostForm(request.POST)
#             if form.is_valid():
#                 form.save()
                
                
#                 return redirect('postView')

#         return render(request,'newpost.html',{'form':form})
#     else:
#         print('kllsfdnkl')




# def post_view(self,request,pk):
#     if 'user' in request.session:
#         publish = get_object_or_404(post,pk=pk)
#         return render(request,'post.html',{'publish':publish})
        
#     else:
#         return redirect('login')


