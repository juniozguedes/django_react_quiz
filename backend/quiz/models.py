from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    description = models.CharField(max_length=500, null=True)
    isActive = models.BooleanField(default=True)
    quizImg = models.ImageField(upload_to='quiz_img')
    
    def __unicode__(self):
        return self.question_name