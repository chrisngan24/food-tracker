# A SCRIPT WHICH WILL CREATE THE FEATURE MATRIX 'bigX'

# this script should be called from the root git dir
# expected: each seperate class is placed in a different folder
source("image_process.R");
setwd("training_data");

classes <- list.files();
num.features <- 4;

bigX <- matrix(0, nr = 1, nc = num.features + 1);

for (class_num in 1:length(classes)) {

    # drill down into class files
    setwd(classes[class_num]);
    imagelist <- list.files();

    # iterate over all items
    for (obj in 1:length(imagelist)) {

        vec <- c(extractFeatures(imagelist[obj]), class_num);	
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

