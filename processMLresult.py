'''
Created on May 29, 2015

@author: michael
'''
'''defines'''

FIRST_RANGE = 8
SECOND_RANGE = 16
THIRED_rang = 24
FOURTH_RANGE = 32
from TIV_defs import TIV_defs
from db import db
class processMLresult(object):
    '''
    responsible for processing the machine learning result  
    '''
    #only 1-2 options returned, the largest in every 8 bits abs value and not abs 
    def TotCleanResult(self,resultList,AbsVal):
        result = []
        for j in range(0,len(resultList)):
            result.append(0)  
            
        largest_jj = 0
        
        for jj in range(0,FIRST_RANGE):
            if(resultList[largest_jj] < resultList[jj]):
                largest_jj = jj
        result[largest_jj] = 1
        largest_jj = FIRST_RANGE
        
        for jj in range(FIRST_RANGE,SECOND_RANGE):
            if(resultList[largest_jj] < resultList[jj]):
                largest_jj = jj
        result[largest_jj] = 1
        largest_jj = SECOND_RANGE
        
        for jj in range(SECOND_RANGE,THIRED_rang):
            if(resultList[largest_jj] < resultList[jj]):
                largest_jj = jj
        result[largest_jj] = 1
        largest_jj = THIRED_rang
       
        for jj in range(THIRED_rang,FOURTH_RANGE):
            if(resultList[largest_jj] < resultList[jj]):
                largest_jj = jj
        result[largest_jj] = 1
       
        for j in range(0,len(resultList)): 
            if(resultList[j] < 0):
                resultList[j] = resultList[j]*(-1)
        largest_jj = 0
        
        for jj in range(0,FIRST_RANGE):
            if(resultList[largest_jj] < resultList[jj]):
                largest_jj = jj
        result[largest_jj] = 1
        largest_jj = FIRST_RANGE
        
        for jj in range(FIRST_RANGE,SECOND_RANGE):
            if(resultList[largest_jj] < resultList[jj]):
                largest_jj = jj
        result[largest_jj] = 1
        largest_jj = SECOND_RANGE
        
        for jj in range(SECOND_RANGE,THIRED_rang):
            if(resultList[largest_jj] < resultList[jj]):
                largest_jj = jj
        result[largest_jj] = 1
        largest_jj = THIRED_rang
       
        for jj in range(THIRED_rang,FOURTH_RANGE):
            if(resultList[largest_jj] < resultList[jj]):
                largest_jj = jj
        result[largest_jj] = 1      
            
        return result  
        
    def cleanResult(self,resultList,AbsVal,zeroClose):
        '''this function is responsible for deciding if a value is 1 or 0 and returns list of 1s and 0s as machine result'''
        result = []
        largest = -1  
        for j in range(0,len(resultList)):            
            tmp = resultList[j]
            if (AbsVal == True):
                if(resultList[j] < 0):
                    tmp = tmp*(-1)
            if(largest < tmp):
                largest = resultList[j] 
        for i in range(0,len(resultList)):
            if((resultList[i] > largest/zeroClose) or (resultList[i] < -largest/zeroClose) ):   
                result.append(1)
            else:
                result.append(0)            
        return result       
    def showResults (self,cleanResList):
        '''this function recieves a list of 1s and 0s and sets all posibble betting options'''
        res = []
        tmpRes = []
        tmp8 = []
        tmp16 = []
        tmp24 = []
        tmp32 = []
        indexes = []
        for j in range(0,len(cleanResList)):
            if(cleanResList[j] == 1):
                indexes.append(j)
        for i in range(0,len(indexes)):                    
            if(indexes[i] < FIRST_RANGE):
                tmp8.append(indexes[i])
            if((indexes[i] < SECOND_RANGE) and (indexes[i] >= FIRST_RANGE)):
                tmp16.append(indexes[i])
            if((indexes[i] < THIRED_rang) and (indexes[i] >= SECOND_RANGE)):
                tmp24.append(indexes[i])
            if((indexes[i] < FOURTH_RANGE) and (indexes[i] >= THIRED_rang)):
                tmp32.append(indexes[i])
        for l in range(0,len(tmp8)):
            for ll in range(0,len(tmp16)):
                for lll in range(0,len(tmp24)):
                    for llll in range(0,len(tmp32)):
                        tmpRes = db()._createRaffleStruct(tmp8[l],tmp16[ll]-8,tmp24[lll]-16,tmp32[llll]-24)       
                        res.append(tmpRes)
        return res
    def __init__(self):
        '''
        Constructor
        '''
        