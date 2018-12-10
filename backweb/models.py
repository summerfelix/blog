from django.db import models


class Admin(models.Model):

    username = models.CharField(max_length=20, unique=True)
    realname = models.CharField(max_length=20, default='无')
    password = models.CharField(max_length=64)
    tel = models.CharField(max_length=20, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    operate_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'admin'


class Column(models.Model):

    c_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'column'


class Article(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    content = models.TextField()
    tags = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    operate_time = models.DateTimeField(auto_now=True, null=True)
    icon = models.ImageField(upload_to='article', null=True)
    column = models.ForeignKey(Column, default='公共')

    class Meta:
        db_table = 'article'




