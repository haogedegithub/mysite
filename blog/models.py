from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod
# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length = 15)
    def __str__(self):
        return self.type_name

class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length = 50,verbose_name = '标题')
    blog_type = models.ForeignKey(to = BlogType,on_delete= models.DO_NOTHING,verbose_name = '类型')
    content = RichTextUploadingField()
    author = models.ForeignKey(to = User,on_delete = models.CASCADE,verbose_name = '作者')
    created_time = models.DateTimeField(auto_now_add = True,verbose_name = '创建时间')
    last_updated_time = models.DateTimeField(auto_now = True,verbose_name = '最后修改时间')
    # def read_num(self):
    #     try:
    #         return self.readnum.read_num
    #     except Exception as e:
    #         return 0
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_time']
'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default = 0)
    blog = models.OneToOneField(Blog,on_delete = models.CASCADE)
'''

