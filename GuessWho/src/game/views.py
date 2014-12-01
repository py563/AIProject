from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.template import context
from game.gamelogic import loader
# Create your views here.


def home(request):
    
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))

def GuessWho(request):
    
    ACTIONS = (
     
        ('Yes', 1),
        ('No', -1),
        ('M1', 0),
        ('M2', 0)  
    )
    
    question = loader('start')
    
    for key,value in ACTIONS:
        if key in request.POST:
            question = loader(value)
    
    
    return render_to_response("qstatic.html", {'qtext': question}, context_instance=RequestContext(request))

def addCharacter(request):
    
    return render_to_response("AddCharacter.html", locals(), context_instance=RequestContext(request))

def question(request):
    qtext = Questiondb.objects.all()

  
