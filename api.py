#!flask/bin/python
from flask import Flask
from flask import request
from sklearn import linear_model
import pickle

# Output is the probability that the given
# input (ex. purchase) belongs to a certain
# class (ex. Fraud or Not Fraud)
logReg = linear_model.LogisticRegression()

# Samples (your features, they should be normalized
# and standardized). Normalization scales the values
# into a range of [0,1]. Standardization scales data
# to have a meanof 0 and standard deviation of 1
X = [[1.0,1.0,2.1], [2.0,2.2,3.3], [3.0,1.1,3.0]]

# Labeled data (Fraud or not)
Y = [1,0,1]

# Build the model
logReg.fit(X, Y)

# Save it to disk
pickle.dump(logReg, open('logReg.pkl', 'wb'))

# API server
app = Flask(__name__)

# Define end point
@app.route('/demo/api/v1.0/predict', methods=['GET'])
def get_prediction():

	# We are using 3 features. For example:
	# purchase amount, country, IP address, etc
	param1 = float(request.args.get('p1'))
	param2 = float(request.args.get('p2'))
	param3 = float(request.args.get('p3'))

	# Load model from disk
	logReg = pickle.load(open('logReg.pkl', 'rb'))

	# Predict
	pred = logReg.predict([[param1, param2, param3]])[0]
	if pred == 0:
		return "Transaction is legit"
	else:
		return "Transaction is Fraud"

# Main app
if __name__ == '__main__':
	app.run(port=7777,host='0.0.0.0')

