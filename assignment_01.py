Answer 1
Following are the three stages to build a machine learning model:
a) Data Selection which involves identifying the important features/columns in the data set relevant to predict the correct value of target variable
b) Data Preprocessing which can be further subdivided into Formatting, Cleaning and Sampling. Formatting means using the appropriate format of data set.
   Cleaning means finding and fixing/removing missing values in the dataset. Sampling means choosing the right amount of data to train the data.
c) Data Transformation which can be further subdivided into Scaling, Decomposition and Aggregation. Scaling means normalisation or standardization to make 
   sure the data values across the dataset are having same base/units. Decomposition means using a component of data feature as per the requirement in training
   the model. Aggregation means combining multiple attributes of dataset to make a useful feature. 
   
Answer 2
Supervised learning makes use of historical labelled data to help in finding out the  error between predicted value and actual value.
This is useful in improving the training model to minimise error in test dataset.

Answer 3 
Training set refers to the data used to train the machine learning model using parameters and fitting the variation in data.
Test set refers to the data used to validate the ML model and check the error ( predicted value - actual value) 

Answer 4 
Ensemble method is a machine learning technique which combines several base models in order to produce one optimal
predictive model. The idea behind ensemble method is that a group of weak learners come together to form a strong learner.
This makes sure that we don't rely on one particular ML model, instead we try to get the best out of multiple 
ML models. Bagging means Bootstrapping and aggregration to form one ensemble model. Given a sample of data, multiple bootstrapped 
subsamples are pulled and a decision tree is formed on each bootstrapped subsample. An algorithm is used to aggregate over the decision
trees to form the most efficient predictor. Boosting refers to a group of algorithms that utilize weighted average to make weak learners
into strong learners.

Answer 5
Overfitting can be avoided by using cross validation which uses multiple mini train-test splits. Another ways of reducing overfitting this 
is have the right feature selection. Also, bagging method helps in solving the problem of overfittig.

