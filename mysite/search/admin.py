from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Reply, Tag

class ReplyInline(admin.StackedInline):
  model = Reply
  extra = 5


class CommentAdmin(admin.ModelAdmin):
  inlines = [ReplyInline]


class PostAdmin(admin.ModelAdmin):
  search_fields = ('title', 'text')
  list_display = ['title','thumbnail_preview', 'is_public', 'updated_at', 'created_at', 'title_len']
  list_filter = ['is_public', 'tags']
  ordering = ('-updated_at',)

  def thumbnail_preview(self, obj): 
    return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail.url))

  def title_len(self, obj):
    return len(obj.title)

  title_len.short_description = '제목글자수'
  thumbnail_preview.short_description = '프리뷰'

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply)
admin.site.register(Tag)


