from foxhound.linear_model import SoftmaxRegression
import foxhound.linear_model.tests.utils as utils

def test_train_softmax_regression():
	utils.test_train_model(SoftmaxRegression())
