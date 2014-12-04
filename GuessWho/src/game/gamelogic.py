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
    
    """
    ID3 (Examples, Target_Attribute, Attributes)
    Create a root node for the tree
    If all examples are positive, Return the single-node tree Root, with label = +.
    If all examples are negative, Return the single-node tree Root, with label = -.
    If number of predicting attributes is empty, then Return the single node tree Root,
    with label = most common value of the target attribute in the examples.
    Otherwise Begin
        A , The Attribute that best classifies examples.
        Decision Tree attribute for Root = A.
        For each possible value, v_i, of A,
            Add a new tree branch below Root, corresponding to the test A = v_i.
            Let Examples(v_i) be the subset of examples that have the value v_i for A
            If Examples(v_i) is empty
                Then below this new branch add a leaf node with label = most common target value in the examples
            Else below this new branch add the subtree ID3 (Examples(v_i), Target_Attribute, Attributes ? {A})
    End
    Return Root
    """
    
    return tree
