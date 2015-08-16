'''
Created on Jun 5, 2015

@author: michael
'''
import random
from db import db
from learnChance import learnChance
from processMLresult import processMLresult
from statistic import statistics
 

def RUNhelp(result,trainingData,TIV,machine):
        #teach the net             
        machine.learnNow(TIV.RUN_WINDOW_SIZE,trainingData,TIV)
        res = machine.calcResolts(result)
        MachineRes = processMLresult
        clean = MachineRes().cleanResult(res,TIV.PROCESS_ABS_VAL,TIV.PROCESS_ZERO_CLOSE)  
        #clean = MachineRes().TotCleanResult(res,TIV.PROCESS_ABS_VAL)
        final = MachineRes().showResults(clean)       
        return db().DataStructToList(final)
def RUN(TIV,Mutate):
    '''this is the most important function it controls the program and here we will use our tuning'''
    money = 0
    #create the machine
    machine = learnChance(TIV)
    #create the data base
    DB = db()
    trainingData = DB.trainingData
    Stat=[]
    #iterate over the result array to test the machine
    for index in range(0,len(DB.resultArray)):
        tmp = len(trainingData)
        IOdata = []
        for i in range(0,TIV.RUN_WINDOW_SIZE-1):
            #next part is creating the window data according to which the machine will calculate the result,
            #it is taking the lines in training list in the correct place  
            #********need to check the right order of the data read**********
            IOdata.append(trainingData[(tmp - TIV.RUN_WINDOW_SIZE-1 + i)])#input of the net    
        #add the result current line to the training data 
        IOdata.append( DB.resultArray[index])#output of the net
        IOarray = DB.UnifyLists(IOdata,32)
        List = RUNhelp(IOarray,trainingData,TIV,machine)
        Stat=statistics().calcStat(List,DB.resultArray[index])       
        print "stat",Stat
        raffMoney = Stat[0]
        TIV.Tiv_Db.append([Stat[1],Stat[2],Stat[3],Stat[4]])      
        money+=raffMoney
        trainingData.append(DB.resultArray[index])
        #print "len(trainingData)", len(trainingData)
    #this is the mutation
    rand = random.randrange(0,20,1)
    if((rand <= 1)and(Mutate == True)): 
        TIV.ManipulateMachine(raffMoney,index)
    print "MONEY MADE IN THIS RUN: ", money
    print "TOTAL PREDICTION SUCCESS DATA OF RUNS: ",TIV.Tiv_Db
    TIV.Tiv_Db.append("END OF A RUN")
    return money,TIV 
    
    
    
   

    
    
 
       