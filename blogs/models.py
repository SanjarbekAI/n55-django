from django.db import models


class AuthorsModel(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
    email = models.EmailField(null=True, blank=True)

    def __repr__(self):
        return self.full_name

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class BlogsModel(models.Model):
    author = models.ForeignKey(AuthorsModel, on_delete=models.CASCADE)
    categories = models.ManyToManyField(CategoryModel)

    title = models.CharField(max_length=255, null=True, blank=True, default="default")
    content = models.TextField()
    image = models.ImageField(upload_to='blogs')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"


"""
teachers
groups
students
homeworks
"""
