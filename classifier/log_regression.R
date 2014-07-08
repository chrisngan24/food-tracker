
############## 
#
#  Logistic Regression - Based on Coursera Assignment 2
#
############

costFunction <- function(theta, x, y, lambda) {

    # number of examples
    m = length(y);

    # compute the sigmoid for the whole set
    h = sigmoid(x %*% theta);

    # compute cost
    J = sum((t(log(h)) %*% y) + (t(log(1-h)) %*% (1-y))) / (0-m) + (lambda / (2 * m)) %*% sum(theta ^ 2);

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

