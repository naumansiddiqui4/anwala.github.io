input_data <- read.csv("/home/msiddique/Desktop/Urls_timemap_assignment9.csv", header=TRUE, sep=",")
nrow(input_data)
hist(input_data$Difference, ylab = "Urls",xlab = "Difference between A2 and A9 Memento Count", main="Memento count difference between A2 and A9", col = "green", labels = TRUE)
        