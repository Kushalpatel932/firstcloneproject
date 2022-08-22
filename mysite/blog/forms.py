from dataclasses import fields
from pyexpat import model
from django import forms

from .models import post,Comment,User_register

class User_register_form(forms.ModelForm):
    class Meta():
        model = User_register
        fields='__all__'



class PostForm(forms.ModelForm):

    class Meta():
        model = post
        fields=('author','title','text')
        
        widgets ={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields =('author','text')
        widgets ={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }