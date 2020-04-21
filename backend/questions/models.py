from django.db import models
from quiz.models import Quiz

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=500, null=False, blank=False)
    isAnswered = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.question_name