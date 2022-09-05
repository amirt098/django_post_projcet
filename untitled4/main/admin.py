from django.contrib import admin
from .models import Test, Post, Tag, Account, Category, Comment
# Register your models here.

admin.site.register(Test)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Account)
admin.site.register(Tag)
admin.site.register(Category)

