# read data
skin.df <- read.table('get_normal_vs_tumor2_RAW_Skin.out',sep=' ',header=TRUE,stringsAsFactors=FALSE)
#transpose data
skin.tdf <- data.frame(t(skin.df[,-2562]))
colnames(skin.tdf)<-paste0(skin.df$tissue,1:72)

# Clustering the genes
# K-means clustering
# cluster into 2 groups
dim(skin.tdf)
km.gene <- kmeans(skin.tdf,2,nstart=20)
km.gene$cluster
#elbow method to check the k value
set.seed(6)
wcss <- vector()
for (i in 1:20) wcss[i] <- sum(kmeans(skin.tdf,i)$withinss)
plot(1:20,wcss,type='b')
# we decided to go for 8 clusters
km.gene8 <- kmeans(skin.tdf,8,nstart=20)
km.gene8$cluster
# compare the 2 cluster and 8 cluser
km.gene$tot.withinss
km.gene8$tot.withinss

# hierarchical clustering
dist(skin.tdf)
# use complete linkage
hc.gene.com <- hclust(dist(skin.tdf),method="complete")
# use average linkage
hc.gene.avg <- hclust(dist(skin.tdf),method="average")
#create denrogram
plot(hc.gene.com,main="complete linkage",xlab='',ylab='',cex=.9)
plot(hc.gene.avg,main="average linkage",xlab='',ylab='',cex=.9)

# use a correlation based distance for hc clustering
skin.tdf.cordist <- as.dist(1-cor(skin.df[,1:2561]))
hccor.gene.com <- hclust(skin.tdf.cordist,method="complete")
plot(hccor.gene.com,main="complete linkage",xlab='',ylab='',cex=.9)
hccor.gene.avg <- hclust(skin.tdf.cordist,method="average")
plot(hccor.gene.avg,main="average linkage",xlab='',ylab='',cex=.9)
# cut tree
hc.gene=cutree(hccor.gene.com,5)
hc.gene
table(hc.gene)

# Visualize the gene expression levels in the different samples from genes in at least two clusters
# Visualize the gene expression levels in the different samples in clusters 1
skin.tdf.cordist <- as.dist(1-cor(skin.df[,1:2561]))
hccor.gene.com <- hclust(skin.tdf.cordist,method="complete")

# cut tree
hc.gene=cutree(hccor.gene.com,5)
hc.gene
table(hc.gene)


hcld.hccor <- as.dendrogram(hccor.gene.com)
plot(hcld.hccor, cex=.3)
abline(h=1.6, col="red")
cuthcd = cut(hcld.hccor, h=1.6)
plot(cuthcd$lower[[1]])
# Visualize the gene expression levels in the different samples in clusters 1             
hc1 <- data.matrix(skin.tdf[unlist(cuthcd$lower[[1]]),])
heatmap(hc1,Rowv=NA,Colv=NA,scale='none',col=heat.colors(256),margins=c(5,10))
# Visualize the gene expression levels in the different samples in clusters 2
hc2 <- data.matrix(skin.tdf[unlist(cuthcd$lower[[2]]),])
heatmap(hc2,Rowv=NA,Colv=NA,scale='none',col=heat.colors(256),margins=c(5,10))
# Visualize the gene expression levels in the different samples in clusters 3
hc3 <- data.matrix(skin.tdf[unlist(cuthcd$lower[[3]]),])
heatmap(hc3,Rowv=NA,Colv=NA,scale='none',col=heat.colors(256),margins=c(5,10))

# Clustering the samples
# K-means clustering
# cluster into 2 groups
dim(skin.df)
skin.df.nolab <-skin.df[,1:2561]
km.sample <- kmeans(skin.df.nolab,2,nstart=20)
km.sample$cluster
table(km.sample$cluster)
#elbow method to check the k value
set.seed(6)
wcss <- vector()
for (i in 1:10) wcss[i] <- sum(kmeans(skin.df.nolab,i)$withinss)
plot(1:10,wcss,type='b')
# we decided to go for 6 clusters
km.sample6 <- kmeans(skin.df.nolab,6,nstart=20)
km.sample6$cluster
# compare the 2 cluster and 6 cluser
km.sample$tot.withinss
km.sample6$tot.withinss
table(km.sample$cluster,km.sample6$cluster)
table(km.sample$cluster,skin.df$tissue)
table(km.sample6$cluster,skin.df$tissue)
# cluster in 3 groups
km.sample3 <- kmeans(skin.df.nolab,3,nstart=20)
km.sample3$cluster
table(km.sample3$cluster)
table(km.sample3$cluster,skin.df$tissue)

# hierarchical clustering
dist(skin.df.nolab)
# use complete linkage
hce.sample.com <- hclust(dist(skin.df.nolab),method="complete")
# use average linkage
hce.sample.avg <- hclust(dist(skin.df.nolab),method="average")
#create denrogram
plot(hce.sample.com,main="complete linkage",xlab='',ylab='',cex=.9)
plot(hce.sample.avg,main="average linkage",xlab='',ylab='',cex=.9)

# use a correlation based distance for hc clustering
skin.df.cordist <- as.dist(1-cor(t(skin.df.nolab)))
hccor.sample.com <- hclust(skin.df.cordist,method="complete")
plot(hccor.sample.com,main="complete linkage",xlab='',ylab='',cex=.9)
hccor.sample.avg <- hclust(skin.df.cordist,method="average")
plot(hccor.sample.avg,main="average linkage",xlab='',ylab='',cex=.9)

# cut tree
# Euclidean distance, complete linkage
euc.com=cutree(hce.sample.com,5)
table(euc.com,skin.df$tissue)
# Euclidean distance, average linkage
euc.avg=cutree(hce.sample.avg,3)
table(euc.avg,skin.df$tissue)
# Correlation base distance, complete linkage
cor.com=cutree(hccor.sample.com,5)
table(cor.com,skin.df$tissue)
# Correlation base distance, average linkage
cor.avg=cutree(hccor.sample.avg,4)
table(cor.avg,skin.df$tissue)