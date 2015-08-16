'''
Created on Jun 8, 2015

@author: michael
'''
import Control
import TIV_defs
import random
import Validation


INITIAL_RUN = 2
SECOND_RUN = 2
THIRED_RUN =  2
FOURTH_RUN = 2

class genetic(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
            '''
        
        
        #self,zeroClose = 6, verbose = False, momentum = 0.00,learningRate = 0.10,weightDecay = 0.0,
        #        lrdecay = 1.0,mse = 0.25,windowSize = 3,hiddenLayers = 8,epoch = 3,mseDecay = 0.05,processAbsVal = False):

        self.L1 = [1,2,3,4,5,6,7,8,9,10,11,12] #zeroClose,how close to highest value we differ 0 and 1
        self.L2 = [False] #verose, this prints the machines work 
        setting = 0
        self.L3 = [0,0,0,0,0,0,0,] #momentum,how much weight has privios node learn
        self.L4 = [0.1] #learnRate, how fast we learn(to high may cause global min/max miss)
        self.L5 = [0,0,0,0,0]  #weightDecay, the decrease in weight each learn has 
        self.L6 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0] #lrdecay, the deacay in the learning rate
        for j in range (0,100):
            self.L3.append(setting) 
            self.L4.append(0.1+setting/2)
            self.L5.append(setting)
            self.L6.append(0.5+setting)
            setting+=0.01
        self.L7 = [0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.4] #mse, how long we train in order to acchive lowe mistake   
        self.L8 = [2,3,4,5] #windowSize, how many last trainnig we include in the run
        self.L9 = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #hiddenLayers, sets the number of hidden layers in the machine (only one layer)
        self.L10 = [1,2,3,4,5] #epoch, how many time we do the mse learning
        self.L11 = [0.03,0.02,0.01,0.04,0.05,0.06,0.07,0.08,0.09,0.1] #mseDecay, in each epoch train we decrease the mse in order to acchieve strong learning  
        self.L12 = [False,True] #processAbsVal, in machine answer negative values swapped to positive if value is False
        
        '''
        L1 = [6]
        L2 = [False]
        L3 = [0,0.05,0.9]
        L4 = [0.1,0.15,0.3]
        L5 = [0.15]
        L6 = [1.0]
        L7 = [0.20]
        L8 = [3]
        L9 = [16]
        L10 = [3]
        L11 = [0.05]
        L12 = [False] 
        '''
    
        self.result = []
        self.FinalList = []
        self.InitialList = []
    def PrintLists(self,machines):
        print "FinalList ",len(self.FinalList)
        for param in self.FinalList: 
            param.MyPrint()
        print "result ",self.result
        print "best machines"
        for param in machines: 
            param.MyPrint()   
    def FindBestMach(self,result,legn):
        AvgRes = []
        BestIndxList = []
        Highest = 0
        tmpIdx = 0
        for i in range(0,len(result)):
            AvgRes.append((result[i][0]+result[i][1]+result[i][2])/3)
        for j in range(0,legn):
            tmpVal = -999999
            tmpIdx = 0    
            for i in range(0,len(AvgRes)):
                if((AvgRes[i]>tmpVal) and (j==0)):
                    tmpVal = AvgRes[i]
                    tmpIdx = i
                else: 
                    if((AvgRes[i]>tmpVal) and (AvgRes[i]<Highest)):
                        tmpVal = AvgRes[i]
                        tmpIdx = i
            Highest = tmpVal
            BestIndxList.append(tmpIdx)
        return BestIndxList
    def ResetL(self):
        self.L1 = []
        self.L2 = []
        self.L3 = []
        self.L4 = []
        self.L5 = []
        self.L6 = []
        self.L7 = []
        self.L8 = []
        self.L9 = []
        self.L10 = []
        self.L11 = []
        self.L12 = []
    def CreateL(self,RunLen,machines):
        for i in range(0,RunLen):
            self.L1.append(machines[i].PROCESS_ZERO_CLOSE)
            self.L2.append(machines[i].TRAIN_VERBOSE)
            self.L3.append(machines[i].TRAIN_MOMENTUM)
            self.L4.append(machines[i].TRAIN_LEARNINGRATE)
            self.L5.append(machines[i].TRAIN_WEIGHTDECAY)
            self.L6.append(machines[i].TRAIN_LRDECAY)
            self.L7.append(machines[i].LEARN_MSE)
            self.L8.append(machines[i].RUN_WINDOW_SIZE)
            self.L9.append(machines[i].MACHINE_NUM_IN_HIDDEN_LAYER)
            self.L10.append(machines[i].LEARN_EPOCH)
            self.L11.append(machines[i].LEARN_MSE_DECAY)
            self.L12.append(machines[i].PROCESS_ABS_VAL)  
    def RandomChoise(self):   
        return [random.choice(self.L1),random.choice(self.L2),random.choice(self.L3),random.choice(self.L4),random.choice(self.L5),random.choice(self.L6),
                random.choice(self.L7),random.choice(self.L8),random.choice(self.L9),random.choice(self.L10),random.choice(self.L11),random.choice(self.L12)]
    
    def GENETIC(self):
        for i in range(0,INITIAL_RUN):          
            L = self.RandomChoise()
            TIV = TIV_defs.TIV_defs(L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9],L[10],L[11]) 
            self.InitialList.append(L)
            #only in first run mutation is allowed
            RetList = Control.RUN(TIV,True)
            self.FinalList.append(RetList[1])
            RetList2 = Control.RUN(TIV,False)
            RetList3 = Control.RUN(TIV,False)
            self.result.append([RetList[0],RetList2[0],RetList3[0]])
            #check the best SECOND_RUN number machines            
        BestIndxList = self.FindBestMach(self.result,SECOND_RUN)
        machines = []
        for i in range(0,SECOND_RUN):
            machines.append(self.FinalList[BestIndxList[i]])
        #print "InitialList",InitialList
        self.PrintLists(machines)               
        self.ResetL()
        self.CreateL(SECOND_RUN,machines)
        
        L = []    
        for i in range(0,SECOND_RUN):
            L = self.RandomChoise()
            print L
            TIV = TIV_defs.TIV_defs(L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9],L[10],L[11]) 
            self.InitialList.append(L)
            RetList = Control.RUN(TIV,True)
            self.FinalList.append(RetList[1])
            RetList2 = Control.RUN(TIV,False)
            RetList3 = Control.RUN(TIV,False)
            self.result.append([RetList[0],RetList2[0],RetList3[0]])
        #check the best THIRED_RUN number of machines
        BestIndxList = self.FindBestMach(self.result,THIRED_RUN)
        machines = []
        for i in range(0,THIRED_RUN):
            machines.append(self.FinalList[BestIndxList[i]])
        #print "InitialList",InitialList
        self.PrintLists(machines)
            
                
        self.ResetL()
        self.CreateL(THIRED_RUN,machines)
        L = []    
        for i in range(0,THIRED_RUN):
            L = self.RandomChoise()
            TIV = TIV_defs.TIV_defs(L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9],L[10],L[11]) 
            self.InitialList.append(L)
            RetList = Control.RUN(TIV,True)
            self.FinalList.append(RetList[1])
            RetList2 = Control.RUN(TIV,False)
            RetList3 = Control.RUN(TIV,False)
            self.result.append([RetList[0],RetList2[0],RetList3[0]])
            #check the best FOURTH_RUN number machines and set Ret to this machines
        BestIndxList = self.FindBestMach(self.result,FOURTH_RUN)
        machines = []
        for i in range(0,FOURTH_RUN):
            machines.append(self.FinalList[BestIndxList[i]])
        self.PrintLists(machines)            
        self.ResetL()
        self.CreateL(FOURTH_RUN,machines)
            
        L = []    
        for i in range(0,FOURTH_RUN/2):
            L =self.RandomChoise()
            print L
            TIV = TIV_defs.TIV_defs(L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9],L[10],L[11]) 
            self.InitialList.append(L)
            RetList = Control.RUN(TIV,True)
            self.FinalList.append(RetList[1])
            RetList2 = Control.RUN(TIV,False)
            RetList3 = Control.RUN(TIV,False)
            self.result.append([RetList[0],RetList2[0],RetList3[0]])             
        self.PrintLists(machines)                      
        #check the best machine
        BestIndxList = self.FindBestMach(self.result,1)
        #make sure the best machine wont give 0s
        print "final"
        for param in self.result:
            print param
        for param in self.FinalList:
            param.MyPrint()
        i = 0
        while((self.result[BestIndxList[i]][0] == 0) and (self.result[BestIndxList[i]][1] == 0) and (self.result[BestIndxList[i]][0] == 0)):
            i+=1
            BestIndxList = self.FindBestMach(self.result,i+1)
            if (i > len(self.result)):
                print "Couldnt find a good machine all machines give 0s"
                return
        print "result selected", self.result[BestIndxList[i]] 
        print "machine selected", 
        self.FinalList[BestIndxList[i]].MyPrint()
        self.FinalList[BestIndxList[i]].Tiv_Db = []
        a1=Validation.ValidateMachine(self.FinalList[BestIndxList[i]])
        a2=Validation.ValidateMachine(self.FinalList[BestIndxList[i]])
        a3=Validation.ValidateMachine(self.FinalList[BestIndxList[i]])
        print "avg machine made ", ((a1+a2+a3)/3)
        
