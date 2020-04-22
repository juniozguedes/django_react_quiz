from django.shortcuts import render
from quiz.models import Quiz
from questions.models import Question
from choices.models import Choice

from django.http import HttpResponse, JsonResponse

def getQuizById(request, id):
    quiz = Quiz.objects.get(id=id)
    questions = quiz.question_set.all()
    data = []
    data.append({
        "title" : quiz.title,
        "description": quiz.description,
        "img" : quiz.quizImg.name
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