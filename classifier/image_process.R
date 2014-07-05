
extractFeatures <- function(path, print=FALSE) {

	# load libraries for IP
	library("EBImage");
	f = readImage(path);

	object_indices = which(binary_image(f,0.9) == 0);

	# really noob way to extract RGB
	red = mean((imageData(f)[,,1])[object_indices]);
	green = mean((imageData(f)[,,2])[object_indices]);
	blue = mean((imageData(f)[,,3])[object_indices]);
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

	bin = binary_image(img, 0.9);
	hbin = high_pass(bin);

	area = sum(bin == 0);
	perimeter = sum(hbin == 0);
	roundness = (4 * pi * area) / (perimeter ^ 2);

	return(roundness);

}

# A function which will perform a high pass filter over an image
high_pass <- function(img) {

	# load libraries for IP
	library("EBImage");

	filter_hi = matrix(1, nc=3, nr=3);
	filter_hi[2,2] = -8;

	img_hi = binary_image(1 - filter2(img, filter_hi));

	return(img_hi);

}

# A function which will perform a binarization of an image
# t - the threshold over which pixels are sorted
binary_image <- function(img, t = 0.5) {

	# load libraries for IP
	library("EBImage");

	img_out = channel(img,"grey");
	
	# round the values
	img_out[img_out >= t] = 1;
	img_out[img_out < t] = 0;

	return(img_out);

}

# To be added
remove_background <- function(img) {

	print("I can't do this yet!")
	return(img);

}

