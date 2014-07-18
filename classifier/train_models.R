
source("log_regression.R");

# get feature matrix
training_data <- read.table("bigX.txt");

# establish size of model
num_features <- dim(training_data)[2] - 1;
num_classes <- length(unique(training_data[,num_features + 1]));

# initialize empty set
trained_model <- matrix(0, nr = 1, nc = num_features + 1);

# train model for each distinct class
for (i in 1:num_classes) {

    # create new matrix with binary class
    x <- training_data[,1:4];
    y <- (training_data[,5] == i) + 0; 

    init_theta <- rnorm(4);
    result <- optim(par = init_theta,
	      costFunction,
              x = x,
              y = y,
              lambda = 0.5);

    final_theta <- result$par;
    final_cost <- result$value;

    vec <- c(final_theta, i);
    trained_model <- rbind(trained_model, vec);

}

# Save model values
trained_model <- as.matrix(trained_model[-1,]);
write.table(trained_model, file = "model.txt", row.names = FALSE, col.names = FALSE);


