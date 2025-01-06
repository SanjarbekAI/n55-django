from django.db import models


class TestFormModel(models.Model):
    file = models.FileField(upload_to='test')
