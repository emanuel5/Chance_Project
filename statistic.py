'''
Created on May 29, 2015

@author: michael
'''
from db import db

class statistics(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def _checkCards(self,result1,result2):
        result2 = db().RaffleStructToList(result2)
        res = 0
        if(result1[0] == result2[0]):
            res+=1
        if(result1[1] == result2[1]):
            res+=1
        if(result1[2] == result2[2]):
            res+=1
        if(result1[3] == result2[3]):
            res+=1
        return res                
    def calcStat(self,MachineResultsList,result):
        ret = len(MachineResultsList)*(-5)
        #print "this raffle starts with ",ret," money"
        #add one result option = check largest in every 8...
        #print "THE MACHINE CALCULATED: "
        gess1 = 0
        gess2 = 0
        gess3 = 0
        gess4 = 0
        for i in range(0,len(MachineResultsList)): 
            tmp = self._checkCards(MachineResultsList[i],result)
            if(tmp == 1):
                ret+=2.5
                gess1+=1
            if(tmp == 2):
                ret+=10
                gess2+=1
            if(tmp == 3):
                ret+=100
                gess3+=1
            if(tmp == 4):
                ret+=5000
                gess4+=1
            #print MachineResultsList[i]
        #print "THE REAL RESULT IS: ", db().RaffleStructToList(db().resultArray[curr])    
        #print "this raffle made at the end",ret," money"
        return [ret,gess1,gess2,gess3,gess4]
    