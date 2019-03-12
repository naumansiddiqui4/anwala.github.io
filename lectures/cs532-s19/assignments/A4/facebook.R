input_data <- read.csv("/home/msiddique/PycharmProjects/Assignment4/acnwala.csv", header=TRUE, sep=",")
mode<- function(x){
  ux <- unique(x)
  ux[which.max(tabulate(match(x,ux)))]
}
y <- 1:nrow(input_data)
labels_x <- c("Mean", "Mode", "S.D.", "acnwala")
y <- c(mean(input_data$FRIENDCOUNT), mode(input_data$FRIENDCOUNT), sqrt(var(input_data$FRIENDCOUNT)), 2014)
x <- c(which.min(abs(input_data$FRIENDCOUNT - mean(input_data$FRIENDCOUNT))), which.min(abs(input_data$FRIENDCOUNT - mode(input_data$FRIENDCOUNT))), which.min(abs(input_data$FRIENDCOUNT - sqrt(var(input_data$FRIENDCOUNT)))), which.min(abs(input_data$FRIENDCOUNT - 2014)))
plot(x, y, col="red",  ylab = "Number of Friends", xlab="Friends for acnwala", ylim = c(0, max(input_data$FRIENDCOUNT)), xlim = c(0, nrow(input_data)), pch=24)
text(x, y, labels = labels_x, pos = 4)
mean(input_data$FRIENDCOUNT)
sqrt(var(input_data$FRIENDCOUNT))
lines(input_data$FRIENDCOUNT,type = "l", col="green")
