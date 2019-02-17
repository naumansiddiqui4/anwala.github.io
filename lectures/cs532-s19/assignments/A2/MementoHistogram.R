input_data <- read.csv("/home/msiddique/PycharmProjects/Assignment2/Url_timemaps.csv", header=TRUE, sep=",")
input_data$MementoCount
hist(input_data$MementoCount, 
     main="Histogram for Memento Count", 
     xlab="Memento Count",
     ylab = "Number of Urls",
     border="blue", 
     col="green",
     las=1,
     breaks = 5,
     labels = TRUE)