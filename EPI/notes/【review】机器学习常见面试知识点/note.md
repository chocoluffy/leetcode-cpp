Q：
- what is kernel?
- understanding naive bayes
# mini-batch
What is Batch Gradient Descent?
Batch gradient descent is a variation of the gradient descent algorithm that calculates the error for each example in the training dataset, but only updates the model after all training examples have been evaluated.

One cycle through the entire training dataset is called a training epoch. Therefore, it is often said that batch gradient descent performs model updates at the end of each training epoch.

相比于batch Gradient Descent, Mini-batch:
The model update frequency is higher than batch gradient descent which allows for a more robust convergence, avoiding local minima.
The batched updates provide a computationally more efficient process than stochastic gradient descent.
The batching allows both the efficiency of not having all training data in memory and algorithm implementations.

# LDA模型（latent dirichlet /di ri ke late/ allocation）

### *LDA假定每个新文本是这么生成的*
在生成一篇document的时候，两个assumptions:【1】document有一个基于话题的概率分布,【2】每个话题有基于单词的概率分布
首先决定总共单词的数量N，
然后选择一个话题的分布，这个是一个prior先验的概率，比如1/3食物以及2/3动物，pick a topic based on document's multinomial distribution.
然后生成每一个word，通过首先选择话题，然后基于话题选择单词, pick a word based on the topic's multinomial distribution.

> LDA是一个Bag of Words的模型，也就是其实单词出现的顺序以及语法相对位置的模型没有影响。

### 在LDA实际学习的过程中（gibbs sampling）*
给定一个文本，然后反向去学习most likely topic话题的表示。
首先，随机给每个word分配到K个话题，
然后计算两个条件概率：
- 这个文本中被分配到某个话题的概率 p(topic t / whole document d)
- 这个话题里，有多少是由这个单词来贡献的 p(word w / topic t)
通过相乘两个概率，我们可以给每个单词w分配一个新的topic. 
不断重复这个过程，直到达到稳定的状态。

assume：【window size】words appearing in the same context(document) are related.
三个主要参数，document, topic and word. 引入了两个dirichlet变量，

### cons
- 话题数量K是一个先验的knowledge。
- 的到话题分布并不能解释话题之间的关系。

### 实践
- 在实践中，我们尝试结合TF-IDF来希望说减少信息的噪音。也就是去掉出现在超过10%文本里的词，以及少于5篇的词。
- POS tagging，只取动词和名词。

# gibbs sampling
特别对一个latent参数的分布时候。在LDA里面，word是可以被直接观察到的，topic-word和docuemnt-topic的分布是latent的。
当我只知道关于参数的条件概率的时候，钉死其他参数，通过条件概率sample一个参数，然后对每一个参数根据所有数据重复这个过程。

> 实践中，我们常常会尝试比较两篇文章是否在话题分布上相似，用Jensen-Shannon Distance来比较两个概率分布。

- ROC curve
- PCA & SVD （先找到covariance matrix协方差矩阵，再接着PCA）

【update:】
https://blog.csdn.net/John_xyz/article/details/78884425
- bagging和boosting的区别 
我就分别把bagging, Adaboosting, Gradient boosting和gbdt的原理都解释给面试官 

- LSTM的结构
- L1和L2正则惩罚项公式及区别
- 介绍下SVM以及它的核函数 

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

