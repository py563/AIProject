
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.template import context

from gamelogic import DbFunctions
from gamelogic import AnswerGuess


from models import CharacterSet
from models import QuestionDB

# Create your views here.

def home(request):
    #gamesession = request.session() 
    return render_to_response("indexgame.html")

'''def reset_game():
   #Kills the session.
      session.kill()
'''
def startgame(request):
    question = DbFunctions.initialQuestion() #type here code for selecting a random question
    return render_to_response("qstatic.html", {'QAsk':question}, context_instance=RequestContext(request))
    
def guessWho(request):
   ACTIONS = (('Yes', 1),('No', -1))     
   for key,value in ACTIONS:
        if key in request.POST:
            question = Dbfunctions.loader(value)
   if question !="Answer":
       return render_to_response("qstatic.html", {'QAsk':question}, context_instance=RequestContext(request))
   else :
       return render_to_response("AnswerPage.html",{'Guess':question}, context_instance=RequestContext(request))

    
def AnswerPage(request):
    guess = AnswerGuess.guess()
    return render_to_response("AnswerPage.html",{'Guess':guess},context_instance=RequestContext(request))
    
def addCharacter(request):
    return render_to_response("AddCharacter.html", locals(), context_instance=RequestContext(request))

def question(request):
    qtext = Questiondb.objects.all()

def CharacterSet(request):
    Name = CharacterSet.objects.all()
