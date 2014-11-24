

import web
from databaseConfig import db


'''
 useful functions to obtain
'''

def getObjects():
    return db.select('objects')

def getQuestions():
    return db.select('questions')

def getData():
    return db.select('data')

def getValue(object_id, question_id):
    
    where = 'object_id=%d AND question_id=%d'
    try:
        return db.select('data', vars=locals(), where=where)[0].value
    except IndexError:
        return None
