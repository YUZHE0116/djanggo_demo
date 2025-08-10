from django.db import models
from account.models import User
from utils.basemodels import BaseModel
# Create your models here.
class Article(BaseModel):
    id = models.IntegerField(primary_key=True)
    title = models.CharField('标题', max_length=100, null=True, blank=True)
    content = models.TextField('内容', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField('发布日期', auto_now_add=True)
    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = '文章'
