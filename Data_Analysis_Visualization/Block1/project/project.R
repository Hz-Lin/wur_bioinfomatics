# load in the data
skin.df <- read.table(file.choose(),sep=' ', header=TRUE)

# Create a reversed data frame
# Transpose just the gene expression
re.skin.df <- data.frame(t(skin.df[,-2562]))
# Add sample type as column name
colnames(re.skin.df)<-paste0(skin.df$tissue,1:72)
summary(re.skin.df)

range(re.skin.df$tumor1)
range(re.skin.df$tumor2)
range(re.skin.df$tumor3)
range(re.skin.df$normal70)
range(re.skin.df$normal71)
range(re.skin.df$normal72)

# load ggplt2
library(ggplot2)
# Create histogram for tumor1
pl.tumor1 <- ggplot(data=re.skin.df, aes(x=re.skin.df$tumor1))
pl.tumor1 <- pl.tumor1 + geom_histogram(binwidth=5,color="red",fill="red", alpha=0.8) + xlab("tumor1")
print(pl.tumor1)
# Create histogram for tumor2
pl.tumor2 <- ggplot(data=re.skin.df, aes(x=re.skin.df$tumor2))
pl.tumor2 <- pl.tumor2 + geom_histogram(binwidth=5,color="red",fill="red", alpha=0.8) + xlab("tumor2")
print(pl.tumor2)
# Create histogram for tumor3
pl.tumor3 <- ggplot(data=re.skin.df, aes(x=re.skin.df$tumor3))
pl.tumor3 <- pl.tumor3 + geom_histogram(binwidth=5,color="red",fill="red", alpha=0.8) + xlab("tumor3")
print(pl.tumor3)
# Create histogram for normall70
pl.normall70 <- ggplot(data=re.skin.df, aes(x=re.skin.df$normal70))
pl.normall70 <- pl.normall70 + geom_histogram(binwidth=5,color="blue",fill="blue", alpha=0.8) + xlab("normall70")
print(pl.normall70)
# Create histogram for normall71
pl.normall71 <- ggplot(data=re.skin.df, aes(x=re.skin.df$normal71))
pl.normall71 <- pl.normall71 + geom_histogram(binwidth=5,color="blue",fill="blue", alpha=0.8) + xlab("normall71")
print(pl.normall71)
# Create histogram for normall72
pl.normall72 <- ggplot(data=re.skin.df, aes(x=re.skin.df$normal72))
pl.normall72 <- pl.normall72 + geom_histogram(binwidth=5,color="blue",fill="blue", alpha=0.8) + xlab("normall72")
print(pl.normall72)

# Create histogram for tumor samples
pl.tumor <- ggplot(data=re.skin.df, aes(x=rowMeans(re.skin.df[1:43])))
pl.tumor <- pl.tumor + geom_histogram(binwidth=5,color="red",fill="red", alpha=0.8) + xlab("tumor samples")
print(pl.tumor)
# Create histogram for normal samples
pl.normal <- ggplot(data=re.skin.df, aes(x=rowMeans(re.skin.df[44:72])))
pl.normal <- pl.normal + geom_histogram(binwidth=5,color="blue",fill="blue", alpha=0.8) + xlab("normal samples")
print(pl.normal)

pl.scatter <- ggplot(data=re.skin.df, aes(x=rowMeans(re.skin.df[1:43]),y=rowMeans(re.skin.df[44:72])))
pl.scatter <- pl.scatter + geom_point(alpha=0.5,size=4)
pl.scatter <- pl.scatter + xlab("tumor samples") + ylab("nomal samples")
print(pl.scatter)


pl.differ <- ggplot(data=re.skin.df, aes(x=rowMeans(re.skin.df[1:43]) - rowMeans(re.skin.df[44:72])))
pl.differ <- pl.differ + geom_histogram(binwidth=5,color="blue",fill="blue", alpha=0.8)
pl.differ <- pl.differ + xlab("difference in average expression")
print(pl.differ)

differ <- rowMeans(re.skin.df[1:43]) - rowMeans(re.skin.df[44:72])
overexpressed.gene <- 0
underexpressed.gene <- 0
for (dif in differ){
  if (dif>0){overexpressed.gene <- overexpressed.gene+1}
  if (dif<0){underexpressed.gene <- underexpressed.gene+1}
}
print("number of overexpressed.gene =", str(overexpressed.gene))
print(underexpressed.gene)

# Creat a boxplot for gene AMY2B
pl.box1 <- ggplot(data=skin.df, aes(x=factor(skin.df$tissue),y=skin.df$AMY2B))
pl.box1 <- pl.box1 + geom_boxplot() + xlab("tissue sample types") + ylab("expression")
pl.box1 <- pl.box1 + ggtitle("Gene AMY2B expression in tumor and normal tissue")
print(pl.box1)
# Creat a boxplot for gene CLC
pl.box2 <- ggplot(data=skin.df, aes(x=factor(skin.df$tissue),y=skin.df$CLC))
pl.box2 <- pl.box2 + geom_boxplot() + xlab("tissue sample types") + ylab("expression")
pl.box2 <- pl.box2 + ggtitle("Gene CLC expression in tumor and normal tissue")
print(pl.box2)
# Creat a boxplot for gene NAT1
pl.box3 <- ggplot(data=skin.df, aes(x=factor(skin.df$tissue),y=skin.df$NAT1))
pl.box3 <- pl.box3 + geom_boxplot() + xlab("tissue sample types") + ylab("expression")
pl.box3 <- pl.box3 + ggtitle("Gene NAT1 expression in tumor and normal tissue")
print(pl.box3)