from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.template import context
from gamelogic import loader
from models import QuestionDB
# Create your views here.
def home(request):
    return render_to_response("indexgame.html")

def startgame(request):
    ACTIONS = (
     
        ('Yes', 1),
        ('No', -1)
    )
    
    question = loader('start')
   
    for key,value in ACTIONS:
        if key in request.POST:
            question = loader(value)
    if question !="Answer":
        return render_to_response("qstatic.html", {'QAsk':question}, context_instance=RequestContext(request))
    else :
        return render_to_response("AddCharacter.html", locals(), context_instance=RequestContext(request))
def addCharacter(request):
    
    return render_to_response("AddCharacter.html", locals(), context_instance=RequestContext(request))

def question(request):
    qtext = Questiondb.objects.all()
