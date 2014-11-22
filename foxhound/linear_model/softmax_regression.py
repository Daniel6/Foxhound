from foxhound.linear_model import LinearModel
from foxhound.utils.updates import Adadelta, Regularizer
from foxhound.neural_network.layers import Dense

class SoftmaxRegression(LinearModel):

    def __init__(self, l1=0.0, l2=1.0, *args, **kwargs):
    	regularizer = Regularizer(l1=l1, l2=l2)
        update = Adadelta()
        layers = [
            Dense(1, activation='softmax')
        ]
        LinearModel.__init__(
            self, 
            layers=layers, 
            cost='cce', 
            update=update, 
            regularizer=regularizer, 
            **kwargs
        )
