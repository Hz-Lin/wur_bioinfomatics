# Lab work Block 4 Regression

# Exercise 1
# A
install.packages("XLConnect")
require(XLConnect)
# failed!!! Then tried to save it as a csv file
theData <- read.csv("lser.csv")
# B
pairs(theData)
# C
model <- lm(tox ~ colour + base + acid, data=theData)
summary(model)
# D
predict(model, data.frame(colour=0.52, base=0.60, acid=0.95))
# E
ypred <- predict(model)
plot(theData$tox,ypred)
abline(a=0,b=1)

# Exercise 2
# A
data <- as.matrix(read.csv("winedata.csv", header=TRUE, row.names=1))
# B
dim(data)
colnames(data)
rownames(data)
colnames(data[,1:17])
# C
install.packages("glmnet")
library(glmnet)
x=data[,-c(1:17)]
y=data[,1]
# D
grid <- 10^seq(10,-10,length=200)
# E
?cv.glmnet
# F
mdl <- cv.glmnet(x=x, y=y, alpha=0, lambda=grid)
plot(mdl)
mdl
# G
ypred <- predict(mdl, newx=x)
plot(y,ypred)
abline(a=0,b=1)
# H
sum((ypred-mean(y))^2)/sum((y-mean(y))^2)
# I
 ## 5
x=data[,-c(1:17)]
y=data[,5]
mdl <- cv.glmnet(x=x, y=y, alpha=0, lambda=grid)
plot(mdl)
ypred <- predict(mdl, newx=x)
plot(y,ypred)
abline(a=0,b=1)
sum((ypred-mean(y))^2)/sum((y-mean(y))^2)
 ## 10
x=data[,-c(1:17)]
y=data[,10]
mdl <- cv.glmnet(x=x, y=y, alpha=0, lambda=grid)
plot(mdl)
ypred <- predict(mdl, newx=x)
plot(y,ypred)
abline(a=0,b=1)
sum((ypred-mean(y))^2)/sum((y-mean(y))^2)
 ## 15
x=data[,-c(1:17)]
y=data[,15]
mdl <- cv.glmnet(x=x, y=y, alpha=0, lambda=grid)
plot(mdl)
ypred <- predict(mdl, newx=x)
plot(y,ypred)
abline(a=0,b=1)
sum((ypred-mean(y))^2)/sum((y-mean(y))^2)
# J
x=data[,-c(1:17)]
y=data[,1]
mdl2 <- cv.glmnet(x=x,y=y,alpha=1,lambda=grid)
plot(mdl2)
ypred2 <- predict(mdl2, newx=x)
R2 <- sum((ypred2-mean(y))^2)/sum((y-mean(y))^2)
plot(y, ypred2, main=sprintf('%s lasso R^2=%.2f', colnames(data)[1],R2))
abline(a=0,b=1)
# K
coef(mdl2)
colnames(x)[which(coef(mdl2) != 0)]
# L
 ## 5
x=data[,-c(1:17)]
y=data[,5]
mdl2 <- cv.glmnet(x=x,y=y,alpha=1,lambda=grid)
plot(mdl2)
ypred2 <- predict(mdl2, newx=x)
R2 <- sum((ypred2-mean(y))^2)/sum((y-mean(y))^2)
plot(y, ypred2, main=sprintf('%s lasso R^2=%.2f', colnames(data)[1],R2))
abline(a=0,b=1)
colnames(x)[which(coef(mdl2) != 0)]
 ## 10
x=data[,-c(1:17)]
y=data[,10]
mdl2 <- cv.glmnet(x=x,y=y,alpha=1,lambda=grid)
plot(mdl2)
ypred2 <- predict(mdl2, newx=x)
R2 <- sum((ypred2-mean(y))^2)/sum((y-mean(y))^2)
plot(y, ypred2, main=sprintf('%s lasso R^2=%.2f', colnames(data)[1],R2))
abline(a=0,b=1)
colnames(x)[which(coef(mdl2) != 0)]
 ## 15
x=data[,-c(1:17)]
y=data[,15]
mdl2 <- cv.glmnet(x=x,y=y,alpha=1,lambda=grid)
plot(mdl2)
ypred2 <- predict(mdl2, newx=x)
R2 <- sum((ypred2-mean(y))^2)/sum((y-mean(y))^2)
plot(y, ypred2, main=sprintf('%s lasso R^2=%.2f', colnames(data)[1],R2))
abline(a=0,b=1)
colnames(x)[which(coef(mdl2) != 0)]
# M
x=data[,-c(1:17)]
y=data[,1]
ypred <- rep(NA, nrow(data))
for (i in 1:nrow(data)) {
  mdl <- cv.glmnet(x=x[-i,],y=y[-i], alpha=1, lambda=grid)
  ypred[i] <- predict(mdl, newx=t(x[i,]))
}
Q2 <- sum((ypred-mean(y))^2)/sum((y-mean(y))^2)
plot(y, ypred, main=sprintf('%s lasso Q^2=%.2f', colnames(data)[1],Q2))
abline(a=0,b=1)
# N
fold <- split(sample(1:nrow(data)), 1:10)
x=data[,-c(1:17)]
y=data[,1]
ypred10 <- rep(NA, nrow(data))
for (i in fold) {
  mdl10 <- cv.glmnet(x=x[-i,], y=y[-i], alpha=1, lambda=grid)
  for (pos in i) {
    ypred10[pos] <- predict(mdl10,newx=t(x[pos,]))
  }
}
Q_square <- sum((ypred10-mean(y))^2)/sum((y-mean(y))^2)
plot(y, ypred10, main=sprintf('%s lasso Q^2=%.2f', colnames(data)[1],Q_square))
abline(a=0,b=1)
