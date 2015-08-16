from NNEngine import NNEngine 
EPOCH = 3
CARDS_SIZE = 32
class learnChance(object):
    '''this class is responsible for teaching the machine'''
    def __init__(self,TIV):
        '''constructor'''
        self.engine = NNEngine(CARDS_SIZE*TIV.RUN_WINDOW_SIZE,CARDS_SIZE,TIV)
        
        
    def _retVal(self,List):
        '''this method recieves a list of 32 values and returns its values seperatly '''
        return (List[0],List[1],List[2],List[3],List[4],List[5],List[6],List[7],
                List[8],List[9],List[10],List[11],List[12],List[13],List[14],List[15],
                List[16],List[17],List[18],List[19],List[20],List[21],List[22],List[23],
                List[24],List[25],List[26],List[27],List[28],List[29],List[30],List[31])
    
    
    def learnNow(self,windowSize,trainingData,TIV):
        '''this method is responsible for teaching the machine it resives the trainig list and window size'''
        arr = trainingData
        #print " arr is" , arr
        inputList = []
        for i in range(0,len(arr)-windowSize):
            outputList = self._retVal(arr[i+windowSize])
            inputList = []
            for j in range(0,windowSize):
                for k in range(0,CARDS_SIZE):
                    index = j*CARDS_SIZE + k
                    retval = self._retVal(arr[i+j])
                    inputList.insert(index,retval[k])
            self.engine.collectData(inputList,outputList)  
        #print "number of trains : "
        #epocs option 1
        #for j in range(0,EPOCH): 
        #    print self.engine.train(TIV,EPOCH)
        print "number of trainning", self.engine.train(TIV)
        #self.engine.train(TIV)
    def calcResolts(self,result):
        '''this method recieves the latest window size inputs and returns the result our machine calculated'''
        res =  self.engine.getResult(result)
        #print "machine calculated ", res
        return res[0]
    



