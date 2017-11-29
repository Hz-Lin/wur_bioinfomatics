data <- read.table('get_normal_vs_tumor2_RAW_Female.Reproductive.System.out', header = TRUE, sep = ' ')
logdata <- data
logdata[,1:2561] <- log(logdata[,1:2561])
dim(data)
tail(data)
summary(data)
colnames(data)

#First we try a dummy test on just the first gene of the data set
#the expression results are seperated and assigned to different variables
normal <- data[data$tissue=='normal',]
tumor <- data[data$tissue=='tumor',]
normal.log <- logdata[logdata$tissue=='normal',]     
tumor.log <- logdata[logdata$tissue=='tumor',]   


library(ggplot2)
# histogram of 6 genes from data

library("gridExtra")
library(ggplot2)
library("gridExtra")
pl <- lapply(34:39, function(i){
  ggplot(data=normal,aes(x=normal[,i])) + geom_histogram(binwidth=10) + xlab(sprintf("%s normal sample",colnames(normal)[i]))
}) 
marrangeGrob(pl, nrow=2, ncol=3)
pl <- lapply(34:39, function(i){
  ggplot(data=tumor,aes(x=tumor[,i])) + geom_histogram(binwidth=10) + xlab(sprintf("%s normal sample",colnames(tumor)[i]))
}) 
marrangeGrob(pl, nrow=2, ncol=3)
# Shapiro-Wilk normality test
for (i in 34:39){
  result <- shapiro.test(normal[,i])
  print(result)
}
for (i in 34:39){
  result <- shapiro.test(tumor[,i])
  print(result)
}
# histogram of 6 genes from log-transformed data
pl <- lapply(34:39, function(i){
  ggplot(data=normal.log,aes(x=normal.log[,i])) + geom_histogram(binwidth=0.05) + xlab(sprintf("%s normal sample",colnames(normal.log)[i]))
}) 
marrangeGrob(pl, nrow=2, ncol=3)
pl <- lapply(34:39, function(i){
  ggplot(data=tumor.log,aes(x=tumor.log[,i])) + geom_histogram(binwidth=0.05) + xlab(sprintf("%s normal sample",colnames(tumor.log)[i]))
})
marrangeGrob(pl, nrow=2, ncol=3)
# Shapiro-Wilk normality test
for (i in 34:39){
  result <- shapiro.test(normal.log[,i])
  print(result)
}
for (i in 34:39){
  result <- shapiro.test(tumor.log[,i])
  print(result)
}

# t test!!!
t.test(normal.log[,1], tumor.log[,1], 'two.sided')
pvals <- sapply(1:2561,function(i){
  t.test(normal.log[,i],tumor.log[,i],"two.sided")$p.value
})
hist(pvals)
genes <- colnames(logdata)[-2562]
df.ttest <- data.frame(genes,pvals)
df.ttest = df.ttest[order(df.ttest$pvals),]

df.ttest$Bonferroni <- p.adjust(df.ttest$pvals, method = "bonferroni")
df.ttest$BH <- p.adjust(df.ttest$pvals, method = "BH")
head(df.ttest, n=10)

par(mfrow=c(2,5))
for (i in 1:10){
  gene <- df.ttest[i,1]
  index <- grep(sprintf("^%s$",gene), colnames(normal.log))
  boxplot(normal.log[,index],tumor.log[,index],names=c("normal","tumor"),main=sprintf("%s normal sample",gene))
}

# Mann-Whitney U test!!!
wilcox.test(normal[,1], tumor[,1])
pvals <- sapply(1:2561,function(i){
  wilcox.test(normal[,i],tumor[,i])$p.value
})
hist(pvals)
genes <- colnames(data)[-2562]
df.utest <- data.frame(genes,pvals)
df.utest = df.utest[order(df.utest$pvals),]

df.utest$Bonferroni <- p.adjust(df.utest$pvals, method = "bonferroni")
df.utest$BH <- p.adjust(df.utest$pvals, method = "BH")
head(df.utest, n=10)

par(mfrow=c(2,5))
for (i in 1:10){
  gene <- df.utest[i,1]
  index <- grep(sprintf("^%s$",gene), colnames(normal.log))
  boxplot(normal.log[,index],tumor.log[,index],names=c("normal","tumor"),main=sprintf("%s normal sample",gene))
}