from django.contrib import admin

# Register your models here.
from .models import Category,Post,Cv,JobApplied

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Cv)
admin.site.register(JobApplied)
