
source("log_regression.R");

# Get feature matrix 
bigX <- as.matrix(read.table("bigX.txt"));
model <- as.matrix(read.table("model.txt"));

num.classes <- dim(model)[1];
num.features <- dim(model)[2] - 1;
num.samples <- dim(bigX)[1];

# initialize matrix: rows = num samples, cols = num classes
prob.matrix <- matrix(0, nr = num.samples, nc = num.classes);
class_out <- c();

for (i in 1:num.classes) {

    vec <- predict(model[i,1:num.features], bigX[,1:num.features]);    

    prob.matrix[,i] <- t(vec);

}

for (m in 1:num.samples) {

    class_out <- c(class_out, which.max(prob.matrix[m,]));

}


