#Basic Statistics Operations (Max, Min, Mean, Mode, Median) on Built-in dataset
print("Basic Statistics Operations (Max, Min, Mean, Mode, Median) on Built-in dataset")
x <- c(21,62,10,53,71,55,73,17,24,33)

# finding mean using built-in functions
result.mean <- mean(x)
cat("The mean is:",result.mean)

print("  ")
# finding median using built-in functions
median.result <- median(x)
cat("The median is:",median.result)

# This is function which returns mode.
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}
print("  ")
# finding mode using the function above
result <- getmode(x)
cat("The mode is:",result)
