# Introduction
source("http://www.bioinformatics.nl/bda/plot_classifier.R")
library(ggplot2)
library(chemometrics)
library(class)
library(tree)
library(randomForest)


# k-nearest neighbour classification

##a. Load a simple 2D dataset and visualize it
simple <-read.table(url("http://www.bioinformatics.nl/bda/simple.txt"),sep="\t",header=FALSE)
dim(simple)
pl <- ggplot(data=simple,aes(x=simple$V1,y=simple$V2)) + geom_point(aes(color=factor(simple$V3)))
print(pl)

##b. Use plot_classifier() to try the k-nearest neighbour classifier
plot_classifier(simple,"knn",7)

##c. Try cross-validation to find the optimal k, using knnEval
ntrain <- round(nrow(simple)*3/4)
train <- sample(1:nrow(simple), ntrain)
res <- knnEval(simple[,1:2],simple[,3],train,kfold=10,knnvec=seq(1,25,1),legpos="bottomright")

##d. Repeat b.-c. for the datasets “hard.txt”, “banana.txt” and “spirals.txt”, found on the same server.
hard <-read.table(url("http://www.bioinformatics.nl/bda/hard.txt"),sep="\t",header=FALSE)
dim(hard)
pl <- ggplot(hard,aes(x=hard[,1],y=hard[,2])) + geom_point(aes(color=factor(hard[,3])))
print(pl)
plot_classifier(hard,"knn",11)
ntrain <- round(nrow(hard)*3/4)
train <- sample(1:nrow(hard), ntrain)
res <- knnEval(hard[,1:2],hard[,3],train,kfold=10,knnvec=seq(1,25,1),legpos="bottomright")

banana <-read.table(url("http://www.bioinformatics.nl/bda/banana.txt"),sep="\t",header=FALSE)
dim(banana)
pl <- ggplot(banana,aes(x=banana[,1],y=banana[,2])) + geom_point(aes(color=factor(banana[,3])))
print(pl)
plot_classifier(banana,"knn",11)
ntrain <- round(nrow(banana)*3/4)
train <- sample(1:nrow(banana), ntrain)
res <- knnEval(banana[,1:2],banana[,3],train,kfold=10,knnvec=seq(1,25,1),legpos="bottomright")

spirals <-read.table(url("http://www.bioinformatics.nl/bda/spirals.txt"),sep="\t",header=FALSE)
dim(spirals)
pl <- ggplot(spirals,aes(x=spirals[,1],y=spirals[,2])) + geom_point(aes(color=factor(spirals[,3])))
print(pl)
plot_classifier(spirals,"knn",3)
ntrain <- round(nrow(spirals)*3/4)
train <- sample(1:nrow(spirals), ntrain)
res <- knnEval(spirals[,1:2],spirals[,3],train,kfold=10,knnvec=seq(1,25,1),legpos="bottomright")

##e. Does scaling have an influence on the decision boundary for the hard dataset for the optimal k
nhard <- hard
nhard[,1:2] <- scale(hard[,1:2])
plot_classifier(nhard,"knn",11)
ntrain <- round(nrow(nhard)*3/4)
train <- sample(1:nrow(nhard), ntrain)
res <- knnEval(nhard[,1:2],nhard[,3],train,kfold=10,knnvec=seq(1,25,1),legpos="bottomright")

##f. Find the optimal k for the scaled hard data and calculate the accuracy of the results
training <- hard[train,]
testing <- hard[-train,]
predictions <- knn(training[,-3],testing[,-3],training[,3],k=17)
accuracy <- length(which(predictions==testing[,3]))/length(predictions)
print(accuracy)
table(testing[,3],predictions)


# Other classifiers
##a. Use plot_classifier() to plot the logistic regression decision boundary for the simple dataset
plot_classifier(simple,"lr",9)
##b. Do the same for the hard, banana and spirals datasets. Is logistic regression sensitive to scaling
plot_classifier(hard,"lr",9)
plot_classifier(banana,"lr",9)
plot_classifier(spirals,"lr",9)
plot_classifier(nhard,"lr",9)
##c. Repeat a.-b. for the decision tree and the random forest
plot_classifier(simple,"tree")
plot_classifier(hard,"tree")
plot_classifier(banana,"tree")
plot_classifier(spirals,"tree")
plot_classifier(nhard,"tree")
plot_classifier(simple,"forest",2000)
plot_classifier(hard,"forest",2000)
plot_classifier(banana,"forest",2000)
plot_classifier(spirals,"forest",2000)
plot_classifier(nhard,"forest",2000)


# Multiclass problems
data("iris")

## KNN
ntrain <- round(nrow(iris)*0.75)
train <- sample(1:nrow(iris),ntrain)
training <- iris[train,]
testing <- iris[-train,]
res <- knnEval(iris[,-5],iris[,5],train,kfold=10,knnvec=seq(1,50,by=1),legpos="topleft")
predictions <- knn(training[,-5],testing[,-5],training[,5],k=1)
length(which(predictions==testing[,5]))/length(predictions)
table(testing[,5],predictions)

## tree
mytree <- tree(iris$Species~.,data=iris[,-5])
summary(mytree)
plot(mytree)
text(mytree)
cv.results <- cv.tree(mytree,FUN=prune.misclass)
plot(cv.results$size,cv.results$dev,type="b")
pruned.tree <- prune.misclass(mytree,best=3)
plot(pruned.tree)
text(pruned.tree)
ntrain <- round(nrow(iris)*0.75)
pruned.preds <- predict(pruned.tree,newdata=testing[,-5],type="class")
length(which(pruned.preds==testing[,5]))/length(pruned.preds)
table(testing[,5],pruned.preds)

## forest
myforest <- randomForest(iris$Species[train]~.,data=iris[train,-5],importance=TRUE,ntree=2000,mtry=2)
preds <- predict(myforest)
trainlab <- iris[train,5]
testlab <- iris[-train,5]
length(which(preds==trainlab))/length(preds)
preds <-predict(myforest,newdata=testing)
length(which(preds==testlab))/length(preds)


# Gene expression data
##a. select a (very) small subset of probesets
source("https://bioconductor.org/biocLite.R")
biocLite("ALL")
library(ALL)
data(ALL)
ALLdata <- data.frame(t(exprs(ALL)))
mads <- apply(ALLdata,2,mad)
ind = order(mads,decreasing=TRUE)
n = 10
data <- ALLdata[,ind[1:n]]
data$label <- as.factor(t(substr(ALL@phenoData@data$BT,1,1)))
dim(data)

##b. Select a training set containing 75% of the samples and train a logistic regression classifier
#Hint: translate the predictions into labels using: ifelse(predictions>0.5,"T","B")
ntrain <- round(nrow(data)*0.75)
train <- sample(1:nrow(data),ntrain)
training <- data[train,]
testing <- data[-train,]
trainlab <- data[train,11]
testlab <- data[-train,11]

model <- glm(label~.,data=data[train,],family=binomial)
summary(model)
preds <- predict(model,type="response")
preds <- ifelse(preds>0.5,"T","B")
length(which(preds==trainlab))/length(preds)


