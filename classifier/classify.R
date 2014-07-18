
source("main.R");
source("image_process.R");
source("log_regression.R");

# Get command line arg of image
feature_vec <- t(rnorm(4));

# Get model 
model <- as.matrix(read.table("model.txt"));

num.classes <- dim(model)[1];
num.features <- dim(model)[2] - 1;

# initialize matrix: rows = num samples, cols = num classes
prob.vec <- vector(length = num.classes);

for (i in 1:num.classes) {
 
    prob.vec[i] <- predict(model[i,1:num.features], feature_vec); 

}

class <- which.max(prob.vec);

print(paste("Predicting: ", num2Name(class)));

