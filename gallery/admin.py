# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# model也需要注册
from .models import Gallery

# Register your models here.

admin.site.register(Gallery)
# 注册完要迁移到数据库中去 1.python manage.py makemigration 、2.python manage.py migrate、3.创建超级用户createsuperuser 就可以登陆admin页面
# 账号harry 密码django123
