from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import viewsets #  give model viewset which can be used to directly make APIs by default
from .models import Question 
from .serializer import QuestionSerializer
from bs4 import BeautifulSoup
from stackapi import models

import requests
import json

# Create your views here.
def index(request):
  return render(request, 'display/index.html') # Edit 5
  #return HttpResponse("Success")

class QuestionAPI(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

def latest(request):# take a request from us, and it will write all the questions for us by scraping it from stackOverflow
   try:
      res = requests.get("http://stackOverflow.com/questions")

      soup = BeautifulSoup(res.text, "html.parser")

      questions = soup.select(".question-summary")
      delete_all()
      for que in questions:
        q = que.select_one('.question-hyperlink').getText()
        vote_count = que.select_one('.vote-count-post').getText()
        views = que.select_one('.views').attrs['title']
        tags = [i.getText()  for i in (que.select('.post-tag'))]

        question = Question()
        question.question = q
        question.vote_count = vote_count
        question.views = views
        question.tags = tags
        
        question.save() # Save the entry to the database
      return HttpResponseRedirect('/')
   except e as Exception:
    return HttpResponseRedirect('/')

def getUsers(request): # Edit 12
  queryset=models.User.objects.all()[:20]
  return JsonResponse({"users":list(queryset.values())})
def getQuestions(request): # Edit 12
  queryset=models.Question.objects.all()[:10]
  latest(request)
  return JsonResponse({"questions":list(queryset.values())})

def getLatestQuestions(request):
  res = requests.get("http://stackOverflow.com/questions")

  soup = BeautifulSoup(res.text, "html.parser")

  questions = soup.select(".question-summary")
  delete_all()
  for que in questions:
    q = que.select_one('.question-hyperlink').getText()
    vote_count = que.select_one('.vote-count-post').getText()
    views = que.select_one('.views').attrs['title']
    tags = [i.getText()  for i in (que.select('.post-tag'))]

    question = Question()
    question.question = q
    question.vote_count = vote_count
    question.views = views
    question.tags = tags
    #delete_all()
    question.save()
def delete_all():
  Question.objects.all().delete()
  return HttpResponseRedirect('/')