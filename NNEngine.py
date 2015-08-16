
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
#from pybrain.structure import TanhLayer
from pybrain.structure import SigmoidLayer
#from pybrain.structure import LinearLayer
#hiddenclass = TanhLayer
#hiddenclass = SigmoidLayer
class NNEngine(object):
    
    #constructor
    def __init__(self,numOfInputs,numOfOutputs,TIV):
        self.numOfInputs=numOfInputs
        self.numOfOutputs=numOfOutputs
        self.net = buildNetwork(numOfInputs, TIV.MACHINE_NUM_IN_HIDDEN_LAYER,numOfOutputs,bias = True,hiddenclass = SigmoidLayer,recurrent = True)
        self.dataset = SupervisedDataSet(self.numOfInputs,self.numOfOutputs)
        
    def collectData(self,inputs,outputs):
        '''
        input = [0,0,0,0,0,0,1,0,0,0,0,1,0]
        '''
        #print "inputs ", inputs
        #print "outputs ", outputs
        self.dataset.addSample(inputs, outputs)
        
        
    def train(self,TIV):
        trainer = BackpropTrainer(module=self.net, dataset=self.dataset, verbose=TIV.TRAIN_VERBOSE,
            momentum=TIV.TRAIN_MOMENTUM, learningrate=TIV.TRAIN_LEARNINGRATE,weightdecay=TIV.TRAIN_WEIGHTDECAY,lrdecay=TIV.TRAIN_LRDECAY)
        
        num = []
        mse = TIV.LEARN_MSE
        #pre training
        result_mse = trainer.trainEpochs(10*TIV.LEARN_EPOCH)
        for i in range(0,TIV.LEARN_EPOCH):
            #we change the mse in order for stronger training in the next epoch
            numOfTrains = 0
            result_mse=mse+1
            counter=0
            while (result_mse > mse):
                counter+=1
                if (counter > 20):
                    print "broke trainig loop"
                    break 
                numOfTrains += 1
                result_mse = trainer.train()
                
            num.append(numOfTrains)
            mse-=TIV.LEARN_MSE_DECAY
        return num
    
    def getResult(self,inputs):
        result_dataset= SupervisedDataSet(self.numOfInputs,self.numOfOutputs)
        result_dataset.addSample(inputs,(0,))
        results = self.net.activateOnDataset(result_dataset)
        return results
                
