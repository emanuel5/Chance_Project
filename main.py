'''
Created on Jul 25, 2015

@author: michael
'''
import Genetic
import time
if __name__ == '__main__':
    #MAIN:
    start = time.time()        
    print "Begin Program"        
    Gen = Genetic.genetic()
    Gen.GENETIC()
    print "End Program"
    end = time.time()
    print "total running time", (end - start)