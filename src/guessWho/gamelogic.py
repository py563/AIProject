from models import CharacterSet
from models import Attributevalue
from models import QuestionDB
import random, math
#questions = QuestionDB.objects.all()
attrList=Attributevalue.objects.all()
actors=CharacterSet.objects.all()
class DbFunctions(object):
    
    def initialQuestion(self):
        i=random.randint(0,5)
        return i
   
    def loader(self,value,actList1,curr):
        chooseNext=curr
        currQActList = getPossibleCharacter(curr)
        for item in actList1:
	  for thing in currQActList:
            if(item.CID==thing.CID):
              item.entropy+=1
        self.qtext = self.AskQuestion(chooseNext)
        return self.qtext,actList1
    
    def AskQuestion(self,best):
        #if 
        initialQ = QuestionDB.objects.all()[best]
        return initialQ

class AnswerGuess(object):
    def guess(self,actList2):
        maxvalue=-99
        ansID=0
        for item in actList2:
            if(maxvalue ==-99):
                ansID=item.Cid
                maxvalue=item.entropy
            elif (maxvalue>item.entropy):
                ansID=item.Cid
                maxvalue=item.entropy
            else:
                pass
        return actors[ansID].Name

#returns all the character names

def getCharacters():
    names = []
    for actor in actors:
        names.append(actor.Name)
    return names
#returns all possible characters in Attribute List for given Question

def getPossibleCharacter(quesId): 
    posActList = []
    for item in attrList:
        if (item.QID == quesId):
            posActList.append(item)
    return posActList
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
