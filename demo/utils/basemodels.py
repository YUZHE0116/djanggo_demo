from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', editable=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间', editable=True)
    class Meta:
        abstract = True