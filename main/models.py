from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(_('title'), max_length=50)
    content = models.TextField(_('content'))
    author = models.ForeignKey(User, verbose_name=_('author'), on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(verbose_name=_('created_on'), auto_now_add=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def get_absolute_url(self):
        return reverse('viewpost', args=[str(self.id)])

class Comment(models.Model):
    title = models.CharField(_('title'), max_length=50)
    content = models.TextField(_('content'))
    author = models.ForeignKey(User, verbose_name=_('author'), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_('post'), on_delete=models.CASCADE)
    created_on = models.DateTimeField(_('created_on'), auto_now_add=True)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


