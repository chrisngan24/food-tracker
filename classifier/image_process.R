
#########
#
# important notes: 
# pixels can range from 0-255. 255 is full expression.
# pixels are stored as: [R,G,B]
# [0,0,0] is a black pixel, [255,255,255] is a white one
#
########

extractFeatures <- function(path, print=FALSE) {

	# load libraries for IP
	library("biOps");
	f = readJpeg(path);

	object_indices = which(binary_image(f,220) == 0);

	# really noob way to extract RGB
	red = mean((f[,,1])[object_indices]);
	green = mean((f[,,2])[object_indices]);
	blue = mean((f[,,3])[object_indices]);
	roundness = find_roundness(f);

	if (print) {

		print(paste("Red:", red));
		print(paste("Green:", green));
		print(paste("Blue:", blue));
		print(paste("Roundness:", roundness));

	}

	return(c(red, green, blue, roundness));

}

# A function that approximates the "roundness" of an object
find_roundness <- function(img) {

	bin = binary_cluster(img, 1);
	hbin = imgCanny(bin, 0.8);

	area = sum(bin == 0);
	perimeter = sum(hbin == 0);
	roundness = (4 * pi * area) / (perimeter ^ 2);

	return(roundness);

}

# Edge Detect
binary_cluster <- function(img, class = 1) {

	library("biOps");
	segments <- imagedata(imgEKMeans(img, 3), "grey");
	types <- unique(c(segments));

	edge1 <- segments;
	edge1[which(edge1 != types[class])] = 0;
 	edge1[which(edge1 == types[class])] = 255;

	return(edge1);

}

# A function which will perform a high pass filter over an image
high_pass <- function(img, binary = TRUE) {

	# load libraries for IP
	library("biOps");

	filter_hi = matrix(1, nc=3, nr=3);
	filter_hi[2,2] = -8;

	img_hi = imgConvolve(img, filter_hi, 0);

        if (binary) {
             img_hi = binary_image(255 - img_hi, 220)
        }

	return(img_hi);

}

# A function which will perform a binarization of an image
# t - the threshold over which pixels are sorted
binary_image <- function(img, t = 128) {

	# load libraries for IP
	library("biOps");

	img_out = imagedata(img,"grey");
	
	# round the values
	img_out[which(img_out >= t)] = 255;
	img_out[which(img_out < t)] = 0;

	return(img_out);

}

white_trim <- function(img) {

    # create a binary matrix of filled pixels
    isFilled <- (img != 255);
 
    # determine filtering window
    x1 <- min(which(rowSums(isFilled) > 0)) 
    x2 <- max(which(rowSums(isFilled) > 0)) 
    y1 <- min(which(colSums(isFilled) > 0)) 
    y2 <- max(which(colSums(isFilled) > 0)) 

    # create new image from window
    return(imagedata(img[x1:x2, y1:y2]));

}

# To be added
remove_background <- function(img) {

	print("I can't do this yet!")
	return(img);

}

