input_data <- read.csv("/home/msiddique/PycharmProjects/Assignment2/Urls_carbondate.csv", header=TRUE, sep=",")
input_data$CarbonDate
hist(input_data$CarbonDate, 
     main="Histogram for Carbon Date", 
     xlab="Number of Days from Carbon Date",
     ylab = "Number of Urls",
     border="blue", 
     col="green",
     las=1,
     breaks = 5,
     labels = TRUE)