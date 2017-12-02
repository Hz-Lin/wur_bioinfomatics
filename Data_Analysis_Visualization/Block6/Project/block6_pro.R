# Load libraries
library(ggplot2)
library(chemometrics)
library(rpart)
library(class)
library(tree)
library(randomForest)

# input data
skin <- read.table("get_normal_vs_tumor2_RAW_Skin.out",sep=" ",header=TRUE)
breast <- read.table("get_normal_vs_tumor2_RAW_Breast.out",sep=" ",header=TRUE)
all <- read.table("get_normal_vs_tumor_RAW.out",sep=" ",header=TRUE)
dim(skin)
tail(colnames(skin))
dim(breast)
tail(colnames(breast))
dim(all)
tail(colnames(all))


### k-nearest neighbour
## Skin Tissues
#try cross-validation to find the optiaml k
boxplot(skin[,1:9])
ntrain.skin <- round(nrow(skin)*3/4)
set.seed(30)
train.skin <- sample(1:nrow(skin),ntrain.skin)
res.skin <- knnEval(skin[,-201],skin[,201],train.skin,kfold=10,knnvec=seq(1,25,1),legpos="bottomright")
#on scaled data
nskin <- skin
nskin[,-201] <- scale(skin[,-201])
res.skin <- knnEval(nskin[,-201],nskin[,201],train.skin,kfold=10,knnvec=seq(1,25,1),legpos="bottomright")

# check the accuracy or the results
#onscaled
preds <- knn(skin[train.skin,-201],skin[train.skin,-201],skin[train.skin,201],k=1)
length(which(preds==skin[train.skin,201]))/length(preds)
table(preds,skin[train.skin,201])
preds <- knn(skin[train.skin,-201],skin[-train.skin,-201],skin[train.skin,201],k=1)
length(which(preds==skin[-train.skin,201]))/length(preds)
table(preds,skin[-train.skin,201])
#scaled
preds <- knn(nskin[train.skin,-201],nskin[train.skin,-201],nskin[train.skin,201],k=1)
length(which(preds==nskin[train.skin,201]))/length(preds)
table(preds,nskin[train.skin,201])
preds <- knn(nskin[train.skin,-201],nskin[-train.skin,-201],nskin[train.skin,201],k=1)
length(which(preds==nskin[-train.skin,201]))/length(preds)
table(preds,nskin[-train.skin,201])

### Logistic regression
lr.skin <- glm(tissue~.,data=skin[train.skin,],family="binomial")
summary(lr.skin)
genes.skin <- names(sort(lr.skin$coefficients[-1]))
#on training data
preds <- predict(lr.skin,newdata=skin[train.skin,],type="response")
preds <- ifelse(preds>0.5,"tumor","normal")
length(which(preds==skin[train.skin,2562]))/length(preds)
table(preds,skin[train.skin,2562])
#on test data
preds <- predict(lr.skin,newdata=skin[-train.skin,],type="response")
preds <- ifelse(preds>0.5,"tumor","normal")
length(which(preds==skin[-train.skin,2562]))/length(preds)
table(preds,skin[-train.skin,2562])

### Dicision tree
tree.skin <- tree(tissue~.,data=skin[train.skin,])
plot(tree.skin); text(tree.skin)
#on training data
preds <- predict(tree.skin,newdata=skin[train.skin,],type="class")
length(which(preds==skin[train.skin,2562]))/length(preds)
table(preds,skin[train.skin,2562])
#on test data
preds <- predict(tree.skin,newdata=skin[-train.skin,],type="class")
length(which(preds==skin[-train.skin,2562]))/length(preds)
table(preds,skin[-train.skin,2562])
#Find the optimal size to prune the tree
cv.results <- cv.tree(tree.skin, FUN=prune.misclass)
plot(cv.results$size, cv.results$dev, type="b")
smalltree.skin <- prune.misclass(tree.skin,best=2)
plot(smalltree.skin); text(smalltree.skin)

### Random forest
forest.skin <- randomForest(tissue~.,data=skin[train.skin,])
#on training data
preds <- predict(forest.skin,newdata=skin[train.skin,],type="class")
length(which(preds==skin[train.skin,2562]))/length(preds)
table(preds,skin[train.skin,2562])
#on test data
preds <- predict(forest.skin,newdata=skin[-train.skin,],type="class")
length(which(preds==skin[-train.skin,2562]))/length(preds)
table(preds,skin[-train.skin,2562])


## Breast Tissues
### k-nearest neighbour
boxplot(breast[,1:9])
nbreast <- breast
nbreast[,-2562] <- scale(breast[,-2562])
#try cross-validation to find the optiaml k
ntrain.breast <- round(nrow(breast)*3/4)
set.seed(30)
train.breast <- sample(1:nrow(breast),ntrain.breast)
res.breast <- knnEval(nbreast[,-2562],nbreast[,2562],train.breast,kfold=10,knnvec=seq(1,25,1),legpos="bottomright")
#accuarcy
preds <- knn(nbreast[train.breast,-2562],nbreast[train.breast,-2562],nbreast[train.breast,2562],k=4)
length(which(preds==nbreast[train.breast,2562]))/length(preds)
table(preds,nbreast[train.breast,2562])
preds <- knn(nbreast[train.breast,-2562],nbreast[-train.breast,-2562],nbreast[train.breast,2562],k=4)
length(which(preds==nbreast[-train.breast,2562]))/length(preds)
table(preds,nbreast[-train.breast,2562])

### Logistic regression
lr.breast <- glm(tissue~.,data=breast[train.breast,],family="binomial")
summary(lr.breast)
genes.breast <- names(sort(lr.breast$coefficients[-1]))
print(length(genes.breast))
#on training data
preds <- predict(lr.breast,newdata=breast[train.breast,],type="response")
preds <- ifelse(preds>0.5,"tumor","normal")
length(which(preds==breast[train.breast,2562]))/length(preds)
table(preds,breast[train.breast,2562])
#on test data
preds <- predict(lr.breast,newdata=breast[-train.breast,],type="response")
preds <- ifelse(preds>0.5,"tumor","normal")
length(which(preds==breast[-train.breast,2562]))/length(preds)
table(preds,breast[-train.breast,2562])


### Dicision tree
tree.breast <- tree(tissue~.,data=breast[train.breast,])
plot(tree.breast); text(tree.breast)

match("GMPPA",genes.breast)
match("NAALADL1",genes.breast)
match("DCK",genes.breast)

#on training data
preds <- predict(tree.breast,newdata=breast[train.breast,],type="class")
length(which(preds==breast[train.breast,2562]))/length(preds)
table(preds,breast[train.breast,2562])
#on test data
preds <- predict(tree.breast,newdata=breast[-train.breast,],type="class")
length(which(preds==breast[-train.breast,2562]))/length(preds)
table(preds,breast[-train.breast,2562])
#Find the optimal size to prune the tree
cv.results <- cv.tree(tree.breast, FUN=prune.misclass)
plot(cv.results$size, cv.results$dev, type="b")
smalltree.breast <- prune.misclass(tree.breast,best=2)
plot(smalltree.breast); text(smalltree.breast)

### Random forest
forest.breast <- randomForest(tissue~.,data=breast[train.breast,])
#on training data
preds <- predict(forest.breast,newdata=breast[train.breast,],type="class")
length(which(preds==breast[train.breast,2562]))/length(preds)
table(preds,breast[train.breast,2562])
#on test data
preds <- predict(forest.breast,newdata=breast[-train.breast,],type="class")
length(which(preds==breast[-train.breast,2562]))/length(preds)
table(preds,breast[-train.breast,2562])




## All Tissues 
### find informative genes
intersect(genes.skin,genes.breast)
idx <- which(genes.skin %in% genes.breast)
genes.extra <- genes.breast[-idx]
genes <- c(genes.skin,genes.extra[1:147])
# get all the columns of these genes
idx.col <- which(genes %in% colnames(all))
all.small <- all[,c(idx.col,2562)]

### k-nearest neighbour
boxplot(all.small[,1:9])
nall.small <- all.small
nall.small[,-201] <- scale(all.small[,-201])
#try cross-validation to find the optiaml k
ntrain.all.small <- round(nrow(all.small)*3/4)
set.seed(30)
train.all.small <- sample(1:nrow(all.small),ntrain.all.small)
res.all.small <- knnEval(nall.small[,-201],nall.small[,201],train.all.small,kfold=10,knnvec=seq(1,25,1),legpos="bottomright")
#accuarcy
preds <- knn(nall.small[train.all.small,-201],nall.small[train.all.small,-201],nall.small[train.all.small,201],k=1)
length(which(preds==nall.small[train.all.small,201]))/length(preds)
table(preds,nall.small[train.all.small,201])
preds <- knn(nall.small[train.all.small,-201],nall.small[-train.all.small,-201],nall.small[train.all.small,201],k=1)
length(which(preds==nall.small[-train.all.small,201]))/length(preds)
table(preds,nall.small[-train.all.small,201])

### Logistic regression
lr.all.small <- glm(tissue~.,data=all.small[train.all.small,],family="binomial")
summary(lr.all.small)

#on training data
preds <- predict(lr.all.small,newdata=all.small[train.all.small,],type="response")
preds <- ifelse(preds>0.5,"tumor","normal")
length(which(preds==all.small[train.all.small,201]))/length(preds)
table(preds,all.small[train.all.small,201])
#on test data
preds <- predict(lr.all.small,newdata=all.small[-train.all.small,],type="response")
preds <- ifelse(preds>0.5,"tumor","normal")
length(which(preds==all.small[-train.all.small,201]))/length(preds)
table(preds,all.small[-train.all.small,201])


### Dicision tree
tree.all.small <- tree(tissue~.,data=all.small[train.all.small,])
plot(tree.all.small); text(tree.all.small)

#on training data
preds <- predict(tree.all.small,newdata=all.small[train.all.small,],type="class")
length(which(preds==all.small[train.all.small,201]))/length(preds)
table(preds,all.small[train.all.small,201])
#on test data
preds <- predict(tree.all.small,newdata=all.small[-train.all.small,],type="class")
length(which(preds==all.small[-train.all.small,201]))/length(preds)
table(preds,all.small[-train.all.small,201])

#Find the optimal size to prune the tree
cv.results <- cv.tree(tree.all.small, FUN=prune.misclass)
plot(cv.results$size, cv.results$dev, type="b")
smalltree.all.small <- prune.misclass(tree.all.small,best=10)
plot(smalltree.all.small); text(smalltree.all.small)


### Random forest
forest.all.small <- randomForest(tissue~.,data=all.small[train.all.small,])
#on training data
preds <- predict(forest.all.small,newdata=all.small[train.all.small,],type="class")
length(which(preds==all.small[train.all.small,201]))/length(preds)
table(preds,all.small[train.all.small,201])
#on test data
preds <- predict(forest.all.small,newdata=all.small[-train.all.small,],type="class")
length(which(preds==all.small[-train.all.small,201]))/length(preds)
table(preds,all.small[-train.all.small,201])


# apply on each other
preds <- predict(forest.all.small,newdata=skin,type="class")
length(which(preds==skin[,2562]))/length(preds)
table(preds,skin[,2562])
preds <- predict(forest.all.small,newdata=breast,type="class")
length(which(preds==breast[,2562]))/length(preds)
table(preds,breast[,2562])
preds <- predict(forest.breast,newdata=skin,type="class")
length(which(preds==skin[,2562]))/length(preds)
table(preds,skin[,2562])
preds <- predict(forest.breast,newdata=all.small,type="class")