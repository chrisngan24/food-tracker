
############## 
#
#  Logistic Regression - Based on Coursera Assignment 2
#
############

predict <- function(theta, x) {

    return(sigmoid(theta %*% t(x))); 

}

predict_binary <- function(theta, x) {

    h = sigmoid(theta %*% t(x));
    y = t(h >= 0.5) + 0;

   return (y);

}

costFunction <- function(theta, x, y, lambda) {

    # number of examples
    m = length(y);

    # compute the sigmoid for the whole set
    h = sigmoid(theta %*% t(x));

    # compute cost
    J = sum((log(h) %*% y) + (log(1-h) %*% (1-y))) / (0-m) + (lambda / (2 * m)) * sum(theta ^ 2);

    return(J);

}

# computes the sigmoid fcn over a vector
sigmoid <- function(z) {

    # initialize variable defaults
    g = rep(0, length(z));

    # solve
    g = 1 / (1 + exp(0-z));

    return(g);
}

