from game.models import Characterset
from game.models import Attributevalue
from game.models import Questiondb

import random, math




def loader(value):
    
    if value == 'start':
        qtext = InitialQuestion()
    
    elif value == 1:
        qtext = "Yes"
        
    elif value == -1:
        qtext = "Is your character over 50?"
        
    else:
        qtext = "no!!"
        
    return qtext
    
def InitialQuestion():
    
    initialQ = list(Questiondb.objects.filter(qid=1))
    
    return initialQ

def decisionTree():
    
    
    
    return tree

def updateFrequency():

    

    return