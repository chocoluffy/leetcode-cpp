Q：
- what is kernel?
- understanding naive bayes
- mini-batch
- ROC curve
- PCA & SVD （先找到covariance matrix协方差矩阵，再接着PCA）

# ROC curve

precision: accurate prediction / number of predicts.
recall: the amount of positives your claims / actual number of positives. 

比对true positive rates和false positive rate在不同的threshold。 
例子：
you’ve predicted that there were 10 apples and 5 oranges in a case of 10 apples. You’d have perfect recall (there are actually 10 apples, and you predicted there would be 10) but 66.7% precision because out of the 15 events you predicted, only 10 (the apples) are correct.
precision: 10 / 15
recall: 10 / 10

### typeI and II
Type I error is a false positive, while Type II error is a false negative. Briefly stated, Type I error means claiming something has happened when it hasn’t, while Type II error means that you claim nothing is happening when in fact something is.

The F1 score is a measure of a model’s performance. It is a weighted average of the precision and recall of a model, with results tending to 1 being the best, and those tending to 0 being the worst. You would use it in classification tests where true negatives don’t matter much.

# Naive Bayes
有一个前提是，assume特征之间是相互独立的。

# CNN

### why max pooling?
reduce the data size.

### mini-batch SGD

### use more small convolutional kernel such as `3*3`, rather than a few larger one?
large kernel reduce the image size in large. small kernels reserve more spatial information. 
使用多的kernel可以使用不同的activation function，可以引入更多的非线性去解释数据。

# Decision Tree

a Decision Tree is an intuitive model where by one traverses down the branches of the tree and selects the next branch to go down based on a decision at a node. Tree induction is the task of taking a set of training instances as input, deciding *which attributes are best to split on, splitting the dataset, and recurring on the resulting split datasets until all training instances are categorized*. While building the tree, the goal is to split on the attributes which create the purest child nodes possible, which would keep to a minimum the number of splits that would need to be made in order to classify all instances in our dataset. Purity is measured by the concept of information gain, which relates to how much would need to be known about a previously-unseen instance in order for it to be properly classified. In practice, this is measured by comparing entropy, or the amount of information needed to classify a single instance of a current dataset partition, to the amount of information to classify a single instance if the current dataset partition were to be further partitioned on a given attribute.

Random Forests are simply an ensemble of decision trees. The input vector is run through multiple decision trees. For regression, the output value of all the trees is averaged; for classification a voting scheme is used to determine the final class.

