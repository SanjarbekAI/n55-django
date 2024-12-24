from django.contrib import admin

from blogs.models import BlogsModel, AuthorsModel, CategoryModel

admin.site.register(BlogsModel)
admin.site.register(AuthorsModel)
admin.site.register(CategoryModel)
