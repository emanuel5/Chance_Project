


class db(object):    
    #resultArray = []
    #trainingData = []
    #vlidationData =[]
    
    # constants
    SEVEN  = 0
    EIGHT  = 1
    NINE   = 2
    TEN    = 3
    PRINCE = 4
    QUEEN  = 5
    KING   = 6
    ASS    = 7

    #constructor
    def __init__(self):
        '''constructor'''
        file1 = open("C:\Users\michael\My Documents\LiClipse Workspace\Chance/DATA1.txt")
        lines = file1.readlines()
        file1.close() 
        
        file2 = open("C:\Users\michael\My Documents\LiClipse Workspace\Chance/DATA2.txt")
        resLines = file2.readlines()
        file2.close()
        
        file3 = open("C:\Users\michael\My Documents\LiClipse Workspace\Chance/DATA3.txt")
        valdLines = file3.readlines()
        file3.close()
        
        self.trainingData = self._createDataStruct(lines)    
        self.resultArray = self._createDataStruct(resLines)        
        self.vlidationData = self._createDataStruct(valdLines)

    def _signsToNum(self,Signs):
        Num = 0
        if Signs == 'A':
            Num = self.ASS
        if Signs == 'K':
            Num = self.KING
        if Signs == 'Q':
            Num = self.QUEEN
        if Signs == 'J':
            Num = self.PRINCE
        if Signs == '10':
            Num = self.TEN
        if Signs == '9':
            Num = self.NINE
        if Signs == '8':
            Num = self.EIGHT
        if Signs == '7':
            Num = self.SEVEN           
        return Num    
    
    
    def _numToSigns(self,Num):
        Signs = 0
        
        if Num == 8:
            Signs = 'A'    
        if Num == 7:
            Signs = 'K'    
        if Num == 6:
            Signs = 'Q'        
        if Num == 5:
            Signs = 'J'      
        if Num == 4:
            Signs = '10'
        if Num == 3:
            Signs = '9'
        if Num == 2:
            Signs = '8'   
        if Num == 1:
            Signs = '7'    
                                 
        return Signs
    

    def _createRaffleStruct(self,trefoil,diamond,heart,leaf):
        '''receives 4  numbers and returns array struct of 4 array of all 0 except the incoded place which is 1''' 
        raffleDS={}
        raffleDS["trefoil"] = [0,0,0,0,0,0,0,0]
        raffleDS["diamond"] = [0,0,0,0,0,0,0,0]
        raffleDS["heart"]   = [0,0,0,0,0,0,0,0]
        raffleDS["leaf"]    = [0,0,0,0,0,0,0,0]

        raffleDS["trefoil"][trefoil] = 1
        raffleDS["diamond"][diamond] = 1
        raffleDS["heart"][heart]     = 1
        raffleDS["leaf"][leaf]       = 1     
           
        raffle = raffleDS["trefoil"] + raffleDS["diamond"] + raffleDS["heart"] + raffleDS["leaf"]
        return raffle
    

    def _createDataStruct (self,lines):
        '''recives lines and builds a list of lists, this is the basic data structure '''
        RuffleStructList = []
        i = 0
        for line in lines:
            NewLine = line.split()
            tmp = self._createRaffleStruct (self._signsToNum(NewLine[0]),
                                            self._signsToNum(NewLine[1]),
                                            self._signsToNum(NewLine[2]),
                                            self._signsToNum(NewLine[3]))
            RuffleStructList.insert(i, tmp)   
            i += 1
        return RuffleStructList
    def RaffleStructToList(self,line):
        '''recives ruffle struct and returns the 4 numbes incoded in the struct'''
        x=0;y=0;z=0;w=0
        for i in range(len(line)):
                               
            if line[i] == 1:
                if(i < 8): 
                    x = i
                if((i < 16) and (i >= 8)):
                    y = i-8
                if((i < 24) and (i >= 16)):
                    z = i-16
                if((i < 32) and (i >= 24)):
                    w = i-24
        return [x+1,y+1,z+1,w+1]
    def DataStructToList(self,DataStruct):
        '''recieves the basic data struct and reuturns a list of lists of the numbers not incoded '''
        i = 0
        List = []
        for line in DataStruct:  
            tmp = self.RaffleStructToList(line)
            List.insert(i, tmp)
            i += 1
        return List
    
    def UnifyLists(self,Lists,size):
        retList = []
        for i in range(0,len(Lists)):
            for j in range(0,size):
                index = i*size + j
                retval =Lists[i]
                retList.insert(index,retval[j]) 
        return retList
        
