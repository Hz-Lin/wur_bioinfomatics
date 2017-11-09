# Lab Work for Block 2

# Missing Data
# import the data
mico <- read.table(file.choose(), sep = "\t", header=TRUE, stringsAsFactors = FALSE)
# Inspect the data
dim(mico)
str(mico)
names(mico)
min(mico[c(2:83)], na.rm=TRUE)
max(mico[c(2:83)], na.rm=TRUE)
quantile(mico[c(2:83)], na.rm=TRUE)
summary(mico)
# create an image of the data matrix
image(as.matrix(mico[,-1]))
# range of expression in the data
range(mico[c(2:83)], na.rm=TRUE)
# Find the fraction of missing values
length(which(is.na(as.matrix(mico[,-1]))))
# Load and inspect cleaned and imputed version
imputed <- read.table(file.choose(), sep = "\t", header=TRUE, stringsAsFactors = FALSE)
dim(imputed)
any(is.na(imputed))
heatmap(as.matrix(imputed[,-1]))

# Normalization
#Visualize the expression distributions of all microarrays left in ndata using boxplots
boxplot(data.frame(imputed[,-1]))
# Create a new data frame that contains just  samples taken after alpha factor arrest
# and regenerate the boxplots
names(imputed)
afdata <- imputed[c(1,6:23)]
boxplot(data.frame(afdata[,-1]))
# Mean-normalize the expression distributions and visualize the result.
scale(afdata[,-1],center=TRUE,scale=FALSE)
boxplot(scale(afdata[,-1],center=TRUE,scale=FALSE))
# mean-variance normalization
scale(afdata[,-1],center=TRUE,scale=TRUE)
boxplot(scale(afdata[,-1],center=TRUE,scale=TRUE))
# Create a new matrix that contains the data normalized using the approach you selected
nrmdata <- scale(afdata[,-1],center=TRUE,scale=TRUE)

# Visualization
# For visualization, it helps to work with a subset of the data to avoid too much computation.
# Select 𝑛 genes (say, 𝑛 = 1000) as follows
sds <- apply(nrmdata,1,sd)
ind <- order(sds,decreasing=TRUE)
subdata <- nrmdata[ind[1:1000],]
# Visualize "subdata" using heatmap() and pairs()
heatmap(as.matrix(subdata))
pairs(as.matrix(subdata))
# visualizing the correlation matrix
cor(subdata)
library(corrgram)
corrgram(subdata)
pl <- qplot(x=seq(0,119,7),y=,data=data.frame(subdata),geom="point")
print(pl)
dim(subdata)
# visualize the first few genes (5 or so) as a function of time, in a scatterplot.
# and Add a non-linear trend line
qplot(seq(0,119,7),subdata[1,],geom=c("point","smooth"))
qplot(seq(0,119,7),subdata[2,],geom=c("point","smooth"))
qplot(seq(0,119,7),subdata[3,],geom=c("point","smooth"))
qplot(seq(0,119,7),subdata[4,],geom=c("point","smooth"))
qplot(seq(0,119,7),subdata[5,],geom=c("point","smooth"))
# Use prcomp() to generate a PCA and use plot() and summary() to inspect the results
p <- prcomp(subdata,scale=TRUE)
summary(p)
plot(p)
# Generate a biplot
biplot(p)
# Inspect the first 9 PCs
par(mfrow=c(3,3))
plot(p$rotation[,1])
plot(p$rotation[,2])
plot(p$rotation[,3])
plot(p$rotation[,4])
plot(p$rotation[,5])
plot(p$rotation[,6])
plot(p$rotation[,7])
plot(p$rotation[,8])
plot(p$rotation[,9])
