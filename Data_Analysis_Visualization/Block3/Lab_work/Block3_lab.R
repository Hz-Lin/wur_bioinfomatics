# Lab work Block 3 clustering

# Practical 1: Simulated data
# K-Means Clustering
x <- read.table('makesimdat.txt')
plot(x,col=c(rep(1,25),rep(2,25)))
km.out <- kmeans(x,2,nstart=20)
km.out$cluster
plot(x,col=(km.out$cluster+1),main="K-means Clustering Results with k=2",xlab="",ylab="",pch=20,cex=2)
km.out3 <- kmeans(x,3,nstart=20)
km.out3$cluster
plot(x,col=(km.out3$cluster+1),main="K-means Clustering Results with k=3",xlab="",ylab="",pch=20,cex=2)
set.seed(3)
km.out1 <- kmeans(x,3,nstart=1)
km.out20 <- kmeans(x,3,nstart=20)
km.out1$tot.withinss
km.out20$tot.withinss

# Hierarchical Clustering
dist(x)
hc.complete <- hclust(dist(x),method='complete')
hc.average <- hclust(dist(x),method='average')
plot(hc.complete, main="Complete Linkage", xlab="", sub="", cex=.9)
plot(hc.average, main="Average Linkage", xlab="", sub="", cex=.9)
cutree(hc.complete,2)
cutree(hc.average,2)
xsc <- scale(x)
plot(hclust(dist(xsc),method='complete'), main="Hierarchical Clustering with Scaled Features")
plot(hclust(dist(xsc),method='average'), main="Hierarchical Clustering with Scaled Features")
cutree(hclust(dist(xsc),method='complete'),2)
cutree(hclust(dist(xsc),method='average'),2)


# Practical 2. NCI60 Data Example
library(ISLR)
# extract labels (cancer type)
nci.labs=NCI60$labs
# extract xperimental measurements (microarray data)
nci.data=NCI60$data
# number of rows and columns of nci.data
dim(nci.data)
# examine the cancer types for the cell lines
table(nci.labs)
nci.labs[which(table(nci.labs)==max(table(nci.labs)))]
# hierarchically cluster the cell lines in the NCI60 data
sd.data <- scale(nci.data)
data.dist <- dist(sd.data)
plot(hclust(data.dist), labels=nci.labs , main="Complete Linkage ", xlab="", sub="",ylab="",cex=0.7)
plot(hclust(data.dist , method ="average"), labels=nci.labs, main="Average Linkage ", xlab="", sub="",ylab="",cex=0.7)
# We will use complete linkage hierarchical clustering for the analysis that follows
hc.out <- hclust(dist(sd.data))
hc.clusters <- cutree (hc.out ,4)
table(hc.clusters ,nci.labs)
# plot the cut on the dendrogram that produces these four clusters
plot(hc.out , labels =nci.labs)
# The abline function draws a straight line on top of any existing plot in R
abline(h=139, col="red")
# compare k-means to hc
set.seed(2)
km.out=kmeans(sd.data , 4, nstart =20)
km.clusters =km.out$cluster
table(km.clusters,hc.clusters)
# cluster the genes based on their expression in the various samples
# use the transpose (t) function to swap rows and columns in the expression dataset
tdata <- t(nci.data)
dim(tdata)
# taking the 100 genes with the highest difference between their lowest and their highest expression value
mymin <- apply(tdata,1,min)
mymax <- apply(tdata,1,max)
minmax=mymax-mymin
top100=which(minmax>8.34)
tdata <- tdata[top100,]
# Apply hierarchical clustering using complete linkage, after scaling tdata
tdata.dist=dist(scale(tdata))
thc.out=hclust(tdata.dist,method="complete")
plot(thc.out)
cl=cutree(thc.out,4)
cl
table(cl)
# use a correlation based distance for hc clustering
tdata.cordist=as.dist(1-cor(nci.data[,top100]))
thc.corout=hclust(tdata.cordist,method="complete")
plot(thc.corout)
clcor=cutree(thc.corout,4)
clcor
table(clcor)
# Compare the resulting clusters with the ones obtained above with Euclidean distance
table(clcor,cl)

# Plot the expression of some of the genes
# cluster 1, e-distance
n=which(cl==1)[1]
plot(tdata[n,],type="l")
for (i in 2:length(which(cl==1))) {
  n=which(cl==1)[i]
  points(tdata[n,],type="l")
}
# cluster 2, e-distance
n=which(cl==2)[1]
plot(tdata[n,],type="l",col="red")
for (i in 2:length(which(cl==2))) {
  n=which(cl==2)[i]
  points(tdata[n,],type="l",col="red")
}
# cluster 1, cor-distance
n=which(clcor==1)[1]
plot(tdata[n,],type="l")
for (i in 2:length(which(clcor==1))) {
  n=which(clcor==1)[i]
  points(tdata[n,],type="l")
}
# cluster 2, cor-distance
n=which(clcor==2)[1]
plot(tdata[n,],type="l",col="red")
for (i in 2:length(which(clcor==2))) {
  n=which(clcor==2)[i]
  points(tdata[n,],type="l",col="red")
}