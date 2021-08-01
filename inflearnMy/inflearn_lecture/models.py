from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model

# Create your models here.
class lecture(models.Model) :
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  contents = models.CharField(max_length=200)
  img_url = models.FileField(null=True)
  category = models.CharField(max_length=200,null=True)

  board_text = RichTextUploadingField(null=True)

  def publish(self):
    self.save()

  def __str__(self):
      return self.title

class comment(models.Model) :
  lecture = models.ForeignKey(lecture, on_delete=models.CASCADE)
  author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
  text = models.CharField(max_length=200)

  def publish(self):
    self.save()

  def __str__(self):
      return self.text