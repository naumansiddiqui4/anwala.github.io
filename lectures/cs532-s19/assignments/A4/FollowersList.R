input_data <- read.csv("/home/msiddique/PycharmProjects/Assignment4/TwitterData.csv", header=TRUE, sep=",")
mode<- function(x){
  ux <- unique(x)
  ux[which.max(tabulate(match(x,ux)))]
}
y <- 1:nrow(input_data)
labels_x <- c("Mean", "Mode", "S.D.", "mln")
y <- c(mean(input_data$Followers), mode(input_data$Followers), sqrt(var(input_data$Followers)), 9.8533095554)
x <- c(which.min(abs(input_data$Followers - mean(input_data$Followers))), which.min(abs(input_data$Followers - mode(input_data$Followers))), which.min(abs(input_data$Followers - sqrt(var(input_data$Followers)))), which.min(abs(input_data$Followers - 9.8533095554)))
plot(x, y, col="red",  ylab = "Number of Followers in log scale", xlab="Followers for phonedude_mln", ylim = c(0, max(input_data$Followers)), xlim = c(0, nrow(input_data)), pch=24)
text(x, y, labels = labels_x, pos = 4)
mean(input_data$Followers)
# input_data$Followers[which((input_data$Followers < mean(input_data$Followers) &(input_data$Followers > mean(input_data$Followers))]
lines(input_data$Followers,type = "l", col="green")
