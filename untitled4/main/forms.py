
from django.forms import ModelForm

from main.models import Account, Post, Category, Tag, Comment
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = Account.email
    first_name = Account.first_name
    last_name = Account.last_name


    class Meta:
        model = Account
        fields = ['username', 'password1','password2', 'email', 'first_name', 'last_name']


class PostReportingForm(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["reporter", 'like', 'status']


class MakingCategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = "__all__"


class MakingTagForm(ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
