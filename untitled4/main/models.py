from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=200)


class Tag(models.Model):
    title = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=400)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Account(AbstractUser):
    ACCOUNT_POSITION = {('admin', 'Admin'), ('writer', 'Writers'), ('reader', 'Reader')}
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    position = models.CharField(max_length=10, choices=ACCOUNT_POSITION, default='reader')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Post(models.Model):
    POST_STATUS = (('w', 'در انتظار تایید'), ('d', 'تایید شده'))
    headline = models.CharField(max_length=300)
    date = models.DateTimeField()
    status = models.CharField(max_length=25, choices=POST_STATUS, default='w')
    reporter = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)  # reporter account
    text = models.TextField(max_length=5000)
    like = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    isWriter = models.BooleanField(default=False)

    def __str__(self):
        return self.headline


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.account
        # class Meta:
        #   ordering = ['date']
    # writer and tags and category


class Preference(models.Model):
    user = models.ForeignKey(Account, on_delete=False)
    post = models.ForeignKey(Post, on_delete=True)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ':' + str(self.post) + ':' + str(self.value)

    class Meta:
        unique_together = ("user", "post", "value")
