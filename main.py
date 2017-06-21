import sys
from multiConcordance import *

if  __name__ =='__main__':
    if len(sys.argv) > 1: # Checks thats a parameter exists
        multiConcordance = MultipleConcordance() # Creates MultipleConcordance Object
        parameter = sys.argv[1]
        if (os.path.isdir(parameter)): # If checking directory for files
            path = os.path.dirname(os.path.realpath(__file__))
            os.chdir(path+"/"+parameter)
            path = os.path.dirname(os.path.realpath(__file__))
            for file in os.listdir(path):
                MultipleConcordance.add(multiConcordance, file)
            print MultipleConcordance.writeAllConcordances(multiConcordance)
        else: # Multiple file parameters
            for index in range(1,len(sys.argv)):
                file = sys.argv[index]
                MultipleConcordance.add(multiConcordance, file)
            print MultipleConcordance.writeAllConcordances(multiConcordance)
    else:
        raise ValueError("File name parameter not passed")
