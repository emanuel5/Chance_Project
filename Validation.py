'''
Created on Jul 11, 2015

@author: michael
'''
from db import db
from learnChance import learnChance
from statistic import statistics
import Control
from processMLresult import processMLresult
def ValidRUNhelp(result,trainingData,TIV,machine):
    #machine.learnNow(TIV.RUN_WINDOW_SIZE,trainingData,TIV)
    res = machine.calcResolts(result)
    MachineRes = processMLresult
    clean = MachineRes().cleanResult(res,TIV.PROCESS_ABS_VAL,TIV.PROCESS_ZERO_CLOSE)  
    #clean = MachineRes().TotCleanResult(res,TIV.PROCESS_ABS_VAL)
    final = MachineRes().showResults(clean)       
    return db().DataStructToList(final)
def ValidateMachine(Tiv):
    money = 0
    #create the machine
    machine = learnChance(Tiv)
    #create the data base
    DB = db()
    trainingData = DB.trainingData
    
    Stat=[]
    #iterate over the result array to test the machine
    for index in range(0,len(DB.resultArray)):
        tmp = len(trainingData)
        result = []
        for i in range(0,Tiv.RUN_WINDOW_SIZE-1):
            result.append(trainingData[(tmp - Tiv.RUN_WINDOW_SIZE-1 + i)])    
        result.append( DB.resultArray[index])
        result = DB.UnifyLists(result,32)
        List = Control.RUNhelp(result,trainingData,Tiv,machine)
        Stat=statistics().calcStat(List,DB.resultArray[index])       
        print "stat",Stat
        raffMoney = Stat[0]
        Tiv.Tiv_Db.append([Stat[1],Stat[2],Stat[3],Stat[4]])
        money+=raffMoney
        trainingData.append(DB.resultArray[index])
    #this is the prediction alone part
    for index in range(0,len(DB.vlidationData)):
        tmp = len(trainingData)
        print "len new training data", len(trainingData)
        result = []
        for i in range(0,Tiv.RUN_WINDOW_SIZE-1):
            result.append(trainingData[(tmp - Tiv.RUN_WINDOW_SIZE-1 + i)])    
        result.append( DB.vlidationData[index])
        result = DB.UnifyLists(result,32)
        List = ValidRUNhelp(result,trainingData,Tiv,machine)
        Stat=statistics().calcStat(List,DB.vlidationData[index])       
        print "stat",Stat
        raffMoney = Stat[0]
        Tiv.Tiv_Db.append([Stat[1],Stat[2],Stat[3],Stat[4]])
        money+=raffMoney
        trainingData.append(DB.vlidationData[index])    
        
        
    print "VALIDATION MACHINE MADE TOTAL MONEY: ", money
    print "TOTAL RESULTS: ",len(Tiv.Tiv_Db),Tiv.Tiv_Db
    Tiv.Tiv_Db.append("END OF MACHINE")
    return money
  
    
    
    
    
    
    
    
        
     
    
    
     