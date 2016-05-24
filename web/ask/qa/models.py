from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(default=timezone.now(), null=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes')

    def __unicode__(self):
        return self.title

    def get_url(self):
        return reverse('qa:question', kwargs={'slug': self.pk})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(default=timezone.now(), null=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.text

    def get_url(self):
        return self.question.get_url()
