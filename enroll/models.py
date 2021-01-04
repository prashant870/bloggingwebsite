from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=300)
    content=RichTextField(null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)