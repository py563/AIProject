from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.

def home(request):
    
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))

def GuessWho(request):
    
    return render_to_response("qstatic.html",locals(), context_instance=RequestContext(request))

def addCharacter(request):
    
    return render_to_response("AddCharacter.html", locals(), context_instance=RequestContext(request))

