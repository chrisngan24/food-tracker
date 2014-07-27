# A SCRIPT WHICH WILL CREATE THE FEATURE MATRIX 'bigX'

# this script should be called from the root git dir
# expected: each seperate class is placed in a different folder
source("image_process.R");
setwd("training_data");

classes <- sort(list.files());
num.features <- 4;

# columns is features + 2, because of bias units and class label
bigX <- matrix(0, nr = 1, nc = num.features + 2);

for (class_num in 1:length(classes)) {

    # drill down into class files
    setwd(classes[class_num]);
    imagelist <- list.files();

    # iterate over all items
    for (obj in 1:length(imagelist)) {

        vec <- c(1, extractFeatures(imagelist[obj]), class_num);	
        print(vec)
	bigX <- rbind(bigX, vec);

    }

    # undo drill down
    setwd("..");

}

# remove initialization row
bigX <- bigX[-1,]

# finish output
setwd("..");
write.table(bigX, file="bigX.txt", row.names = FALSE, col.names = FALSE);

print(paste("Done building features for: ", classes));

