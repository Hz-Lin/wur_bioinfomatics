# load in the data
skin.df <- read.table(file.choose(),sep=' ', header=TRUE)

# Create a reversed data frame
# Transpose just the gene expression
tdata <- data.frame(t(skin.df[,-2562]))
# Add sample type as column name
colnames(tdata)<-paste0(skin.df$tissue,1:72)
# Inspect the data
dim(tdata)
str(tdata)
names(tdata)
quantile(tdata, na.rm=TRUE)
summary(tdata)

# Task 1
# Generate a heatmap using pheatmap(), for both log-transformed data with the original data.
library(pheatmap)
# for original data
pheatmap(tdata)
# for log-transformed data
pheatmap(log(tdata))
# Also visualize the sample correlation matrix.
cor.matrix.tdata <- cor(tdata)
cor.matrix.log <- cor(log(tdata))
library(corrgram)
corrgram(tdata)
corrgram(log(tdata))
# What do you observe? Are values missing?
any(is.na(tdata))


#Task 2
#visualisation with the help of PCA

# Use prcomp() to generate a PCA and use plot() and summary() to inspect the results
p <- prcomp(tdata,scale=TRUE)
summary(p)
plot(p)
# Generate a biplot
biplot(p)

p.log <- prcomp(log(tdata),scale=TRUE)
summary(p.log)
plot(p.log)
# Generate a biplot
biplot(p.log)

#Task 3 #somuchfun
mn_tdata <- scale(log(tdata), center=TRUE, scale=FALSE)
mvn_tdata <- scale(log(tdata), center=TRUE, scale=TRUE)
boxplot(log(tdata))
boxplot(mn_tdata)
boxplot(mvn_tdata)

#Comparing correlation
cor.matrix.log <- cor(log(tdata))
cor.mn_tdata <- cor(mn_tdata)
pheatmap(cor.matrix.log)
pheatmap(cor.mn_tdata)
change <- cor.matrix.log - cor.mn_tdata
pheatmap(change)

# select first 100 genes out of the tdata
genes <- skin.df[,1:100]
cor.genes <- cor(log(genes))
#normalise the genes data frame 
mn_genes <- scale(log(genes),center=TRUE, scale=FALSE)
cor.mn_genes <- cor(mn_genes)
genes.diff <- cor.genes - cor.mn_genes
summary(genes.diff)
pheatmap(genes.diff)


# Task 4

RAW.all <- read.table("get_normal_vs_tumor_RAW.out", header = TRUE, sep = " ", stringsAsFactors = FALSE)
RAW.breast <- read.table("get_normal_vs_tumor2_RAW_Breast.out", header = TRUE, sep = " ", stringsAsFactors = FALSE)
RAW.FeReSy <- read.table("get_normal_vs_tumor2_RAW_Female.Reproductive.System.out", header = TRUE, sep = " ", stringsAsFactors = FALSE)

tRAW.all <- data.frame(t(RAW.all[,-2562]))
colnames(tRAW.all)<-paste0(RAW.all$tissue,1:2132)
tRAW.breast <- data.frame(t(RAW.breast[,-2562]))
colnames(tRAW.breast)<-paste0(RAW.breast$tissue,1:503)
tRAW.FeReSy <- data.frame(t(RAW.FeReSy[,-2562]))
colnames(tRAW.FeReSy)<-paste0(RAW.FeReSy$tissue,1:130)
