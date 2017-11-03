# Creat a vector of 50 Fibonacci numbers
fib.seq <- c(1,1)
for (i in c(3:50)){
  fib.seq[i]=fib.seq[i-1]+fib.seq[i-2]
}

# Creat a function to check if the number is odd
is.odd <- function(n){
  remainder <- n%%2
  if(remainder==1){return(TRUE)}else{return(FALSE)}
}

# Creat a vector contains only the odd numbers
odd.fib = fib.seq[sapply(fib.seq,is.odd)]

# Calculate the percentage of odd numbers
percentage = length(odd.fib) / length(fib.seq)
print(percentage)
