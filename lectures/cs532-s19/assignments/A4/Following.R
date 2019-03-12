input_data <- read.csv("/home/msiddique/PycharmProjects/Assignment4/TwitterDataFollowing.csv", header=TRUE, sep=",")
mode<- function(x){
  ux <- unique(x)
  ux[which.max(tabulate(match(x,ux)))]
}
y <- 1:nrow(input_data)
labels_x <- c("Mean", "Mode", "S.D.", "mln")
y <- c(mean(input_data$Friends), mode(input_data$Friends), sqrt(var(input_data$Friends)), 8.813781191217037)
x <- c(which.min(abs(input_data$Friends - mean(input_data$Friends))), which.min(abs(input_data$Friends - mode(input_data$Friends))), which.min(abs(input_data$Friends - sqrt(var(input_data$Friends)))), which.min(abs(input_data$Friends - 8.813781191217037)))
plot(x, y, col="red",  ylab = "Number of Friends in log scale", xlab="Friends for phonedude_mln", ylim = c(0, max(input_data$Friends)), xlim = c(0, nrow(input_data)), pch=24)
text(x, y, labels = labels_x, pos = 4)
mean(input_data$Friends)
lines(input_data$Friends,type = "l", col="green")
