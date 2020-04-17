from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=500, null=False, blank=False)
    is_active = models.IntegerField()
    def __unicode__(self):
        return self.question_name