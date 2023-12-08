
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.template import context
#from django.http import HttpResponse
#import gamelogic
from gamelogic import DbFunctions
from gamelogic import AnswerGuess
from gamelogic import getCharacters
from gamelogic import getPossibleCharacter

from models import CharacterSet
from models import QuestionDB

# Create your views here.

def home(request):
    request.session['Qcount'] = -1
    request.session['Characters'] = getCharacters()
    return render_to_response("indexgame.html")

'''def reset_game():
   #Kills the session.
      session.kill()
'''
# intial Question loading

def startgame(request):
    questionId = DbFunctions().initialQuestion() #type here code for selecting a random question
    if not 'initial_questions' in request.session :
       request.session['initial_questions'] = questionId
    request.session['current_question'] = questionId 
    request.session['Qcount'] += 1
    request.session['initActorYes'] = getPossibleCharacter(questionId,1) 
    request.session['initActorNo'] = getPossibleCharacter(questionId,-1)
    request.session['initActorUnk'] =getPossibleCharacter(questionId,0)
    return render_to_response("qstatic.html", {'QAsk':DbFunctions().AskQuestion(questionId),'counter':request.session['Qcount']}, context_instance=RequestContext(request))

# choosing the next question      
def guessWho(request):
   ACTIONS = (('Yes', 1),('No', -1),('M1',0),('M2',0))         
   for key,value in ACTIONS:
        if key in request.POST:
            request.session['Qcount'] += 1
            curr=request.session['current_question']
            if key == 'Yes':
               actList = request.session['initActorYes']
            elif key== 'No':
               actList = request.session['initActorNo']
            else:
               actList = request.session['initActorUnk'] 
            responseString,actList = DbFunctions().loader(value,actList,curr)

   if request.session['Qcount'] < 20 and responseString not in request.session['Characters']:
       request.session['current_question']=responseString.QID
       if key == 'Yes':
           request.session['initActorYes']=actList
       elif key== 'No':
           request.session['initActorNo']=actList
       else:
           request.session['initActorUnk']=actList
       return render_to_response("qstatic.html", {'QAsk':responseString,'counter':request.session['Qcount']}, context_instance=RequestContext(request))
   else :
       responseStr = AnswerGuess().guess(actList)
       return render_to_response("AnswerPage.html",{'Guess':responseStr,'counter':request.session['Qcount']}, context_instance=RequestContext(request))

    
def addCharacter(request):
    return render_to_response("AddCharacter.html", locals(), context_instance=RequestContext(request))

def correctGuess(request):
    return render_to_response("correctGuess.html", locals(), context_instance=RequestContext(request))
    
