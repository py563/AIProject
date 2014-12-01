from game import models
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
    
    initialQ = "Is your character real?"
    
    return initialQ

def decisionTree():
    
    
    
    return tree