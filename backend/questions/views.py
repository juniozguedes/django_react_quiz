from django.shortcuts import render
from quiz.models import Quiz
from questions.models import Question
from choices.models import Choice

from django.http import HttpResponse, JsonResponse


def getQuestions(request):
    questions = Question.objects.all()
    data = []
    x = 1
    y = x-1
    while x <= questions.count():
        for question in questions:
            choice = questions[y].choice_set.all()
            choice = list(choice.values("choice"))
            correct = questions[y].choice_set.filter(isCorrect=1)
            correct = list(correct.values("choice"))

            data.append({
                "question" : question.question,
                "choices" : choice,
                "correct": correct
            })
            x+=1
            y+=1    
    return JsonResponse(data, safe=False)

def getQuestionById(request, id):
    quiz = Quiz.objects.get(id=id)
    quizname = quiz.title
    questions = quiz.question_set.all()
    data = []
    data.append({
        "title" : quizname,
    })
    x = 1
    y = x-1
    while x <= questions.count():
        for question in questions:
            choice = questions[y].choice_set.all()
            choice = list(choice.values("choice"))
            correct = questions[y].choice_set.filter(isCorrect=1)
            correct = list(correct.values("choice"))

            data.append({
                "question" : question.question,
                "choices" : choice,
                "correct": correct
            })
            x+=1
            y+=1    
    return JsonResponse(data, safe=False)

#    questions = Question.objects.extra(
#        select={
#            'quest' : 'question'
#        }
#    ).values(
#        'quest'
#    ) #Here I used the extra so I can change the model param Question to quest.