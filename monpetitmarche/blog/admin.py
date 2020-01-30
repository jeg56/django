from django.contrib import admin
from .models import Post
from .models import TestTable
admin.site.register(Post)
admin.site.register(TestTable)