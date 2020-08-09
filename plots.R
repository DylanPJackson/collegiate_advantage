# Load in all necessary non standard libraries
library(stringr)
library(purrr)
library(lattice)

input <- read.csv("data/sal_degree.csv", header=TRUE, sep = ",")
# Get the index list for the sorted starting median salaries
sort_2 <- order(input[[2]])
# Grab the respective majors and salaries
x_names <- input[[1]][sort_2]
x <- input[[2]][sort_2]
# Clean the data
x <- map(x, ~str_remove_all(., pattern = "[$,]"))
x <- as.numeric(x)
# Name it, for ease of plotting
names(x) <- x_names
barchart(x, xlab = "Median Starting Salary", main = "Median Starting Salary vs. Major")
