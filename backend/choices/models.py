from django.db import models
from questions.models import Question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=500, null=False, blank=False)
    isCorrect = models.BooleanField(default=False)
    isUserAnswer = models.BooleanField(default=False)
    def __unicode__(self):
        return self.question_name