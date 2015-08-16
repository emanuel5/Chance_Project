'''
Created on Jun 8, 2015

@author: michael
'''

import random
class TIV_defs(object):
    '''PROCESS_ZERO_CLOSE = 0
    TRAIN_VERBOSE = 0
    TRAIN_MOMENTUM = 0
    TRAIN_LEARNINGRATE = 0
    TRAIN_WEIGHTDECAY = 0
    TRAIN_LRDECAY = 0
    LEARN_MSE = 0
    RUN_WINDOW_SIZE = 0
    MACHINE_NUM_IN_HIDDEN_LAYER = 0
    LEARN_EPOCH = 0
    LEARN_MSE_DECAY = 0
    Tiv_Db = []
    PROCESS_ABS_VAL = AbsVal
    '''  
    #constructor
    def __init__(self,zeroClose = 6, verbose = False, momentum = 0.00,learningRate = 0.10,
                 weightDecay = 0.0,lrdecay = 1.0,mse = 0.25,windowSize = 3,hiddenLayers = 8,epoch = 3,mseDecay = 0.05,AbsVal = True):
        self.PROCESS_ZERO_CLOSE = zeroClose
        self.TRAIN_VERBOSE = verbose
        self.TRAIN_MOMENTUM = momentum
        self.TRAIN_LEARNINGRATE = learningRate
        self.TRAIN_WEIGHTDECAY = weightDecay
        self.TRAIN_LRDECAY = lrdecay
        self.LEARN_MSE = mse
        self.RUN_WINDOW_SIZE = windowSize
        self.MACHINE_NUM_IN_HIDDEN_LAYER = hiddenLayers
        self.LEARN_EPOCH = epoch
        self.LEARN_MSE_DECAY = mseDecay
        self.Tiv_Db = []
        self.PROCESS_ABS_VAL = AbsVal
         
    def MyPrint(self):
        print [self.PROCESS_ZERO_CLOSE,
                self.TRAIN_VERBOSE,
                self.TRAIN_MOMENTUM,
                self.TRAIN_LEARNINGRATE,
                self.TRAIN_WEIGHTDECAY,
                self.TRAIN_LRDECAY,
                self.LEARN_MSE,
                self.RUN_WINDOW_SIZE,
                self.MACHINE_NUM_IN_HIDDEN_LAYER,
                self.LEARN_EPOCH,
                self.LEARN_MSE_DECAY,
                self.PROCESS_ABS_VAL,
                self.Tiv_Db]
        
    def set_PROCESS_ZERO_CLOSE(self,NewVal):
        self.PROCESS_ZERO_CLOSE = NewVal
    def set_TRAIN_VERBOSE(self,NewVal):
        self.TRAIN_VERBOSE = NewVal
    def set_TRAIN_MOMENTUM(self,NewVal):
        self.TRAIN_MOMENTUM = NewVal 
    def set_TRAIN_LEARNINGRATE(self,NewVal):
        self.TRAIN_LEARNINGRATE = NewVal 
    def set_TRAIN_WEIGHTDECAY(self,NewVal):
        self.TRAIN_WEIGHTDECAY = NewVal 
    def set_TRAIN_LRDECAY(self,NewVal):
        self.TRAIN_LRDECAY = NewVal
    def set_LEARN_MSE(self,NewVal):
        self.LEARN_MSE = NewVal
    def set_RUN_WINDOW_SIZE(self,NewVal):
        self.RUN_WINDOW_SIZE = NewVal 
    def set_MACHINE_NUM_IN_HIDDEN_LAYER(self,NewVal):
        self.MACHINE_NUM_IN_HIDDEN_LAYER = NewVal
    def set_LEARN_EPOCH(self,NewVal):
        self.LEARN_EPOCH = NewVal
    def set_LEARN_MSE_DECAY(self,NewVal):
            self.LEARN_MSE_DECAY
    
    
      
    def _Manipulate(self,index):
        if(self.ProcessType == 1):
            if(index%2 == 0):
                self.set_PROCESS_ZERO_CLOSE(self.PROCESS_ZERO_CLOSE+1)
            else:
                self.set_PROCESS_ZERO_CLOSE(self.PROCESS_ZERO_CLOSE-1)
        if(self.ProcessType == 2):
            if(index%2 == 0):
                if(self.TRAIN_MOMENTUM<1 and self.TRAIN_MOMENTUM>0.1):
                    self.set_TRAIN_MOMENTUM(self.TRAIN_MOMENTUM-0.1)   
            else:
                if(self.TRAIN_MOMENTUM>1):
                    self.set_TRAIN_MOMENTUM(self.TRAIN_MOMENTUM+0.1)
        if(self.ProcessType == 3):
            if(index%2 == 0):
                if(self.TRAIN_LEARNINGRATE<1 and self.TRAIN_LEARNINGRATE>0.1):
                    self.set_TRAIN_LEARNINGRATE(self.TRAIN_LEARNINGRATE-0.1)
            else:
                if(self.TRAIN_LEARNINGRATE>1):
                    self.set_TRAIN_LEARNINGRATE(self.TRAIN_LEARNINGRATE+0.1)
        if(self.ProcessType == 4):
            if(index%2 == 0):
                if(self.TRAIN_WEIGHTDECAY<1 and self.TRAIN_WEIGHTDECAY>0.1):
                    self.set_TRAIN_WEIGHTDECAY(self.TRAIN_WEIGHTDECAY-0.1)
            else:
                if(self.TRAIN_WEIGHTDECAY>1):
                    self.set_TRAIN_WEIGHTDECAY(self.TRAIN_WEIGHTDECAY+0.1)
        if(self.ProcessType == 5):
            if(index%2 == 0):
                if(self.TRAIN_LRDECAY>1):
                    self.set_TRAIN_LRDECAY(self.TRAIN_LRDECAY+0.1)
            else:
                if(self.TRAIN_LRDECAY<1 and self.TRAIN_LRDECAY>0.1):
                    self.set_TRAIN_LRDECAY(self.TRAIN_LRDECAY-0.1)
        if(self.ProcessType == 6):
            if(self.LEARN_MSE>0.25):
                self.set_LEARN_MSE(self.LEARN_MSE-0.01)
        if(self.ProcessType == 7):   
            self.set_LEARN_EPOCH(self.LEARN_EPOCH+1)
        if(self.ProcessType == 8):
            self.set_LEARN_MSE_DECAY(self.LEARN_MSE_DECAY+0.02)
                
                
                            
    def ManipulateMachine(self,raffeleMoney,index):
        if(raffeleMoney <= 0):
            self.ProcessType = random.randrange(1,8,1)    
            self._Manipulate(index)    
    
    def ManpHidnOnMse(self):
        '''this function is supposed to manipulate the machine in tradeoff between MSE and hidden layers,
             these parameters have segnificant influense of run time'''
        TIV_defs.set_MACHINE_NUM_OF_HIDDEN_LAYERS(self,self.MACHINE_NUM_OF_HIDDEN_LAYERS+1)
        TIV_defs.set_LEARN_MSE(self,self.LEARN_MSE+0.05)
    def ManpMseOnHidn(self):
        TIV_defs.set_MACHINE_NUM_OF_HIDDEN_LAYERS(self,self.MACHINE_NUM_OF_HIDDEN_LAYERS-1)
        TIV_defs.set_LEARN_MSE(self,self.LEARN_MSE-0.05)    