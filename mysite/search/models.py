from django.db import models
from django.utils import timezone
# Create your models here.

class Tag(models.Model):
  name = models.CharField('태그명', max_length=255,unique=True)
  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField('제목', max_length=32)
  text = models.TextField('본문')
  tags = models.ManyToManyField(Tag, verbose_name='태그', blank=True)
  thumbnail = models.ImageField(verbose_name='썸네일',blank=True, upload_to='images')
  relation_posts = models.ManyToManyField('self', verbose_name='관련기사', blank=True)
  is_public = models.BooleanField('공개', default=True)
  description = models.TextField('게시글설명',max_length=130)
  keywords = models.CharField('게시글의키워드', max_length=255, default='게시글의키워드')
  created_at = models.DateTimeField('작성일', default=timezone.now)
  updated_at = models.DateTimeField('갱신일', default=timezone.now)
  def __str__(self):
      return self.title

class Comment(models.Model):
    """게시글에 대한 댓글"""
    name = models.CharField('이름', max_length=255, default='이름없음')
    text = models.TextField('본문')
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='대상게시글')
    created_at = models.DateTimeField('작성일', default=timezone.now)

    def __str__(self):
        return self.text[:20]

class Reply(models.Model):
    """대댓글"""
    name = models.CharField('이름', max_length=255, default='이름없음')
    text = models.TextField('본문')
    target = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='대상댓글')
    created_at = models.DateTimeField('작성일', default=timezone.now)

    def __str__(self):
        return self.text[:20]

