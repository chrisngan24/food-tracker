###############################
# Installing
###############################
* update .Rprofile

```
r = getOption("repos") 
r["CRAN"] = "http://cran.uk.r-project.org"
options(repos = r)
rm(r)
```

* Install tiff
```
sudo apt-get install libtiff-dev
```

* Open R, and then install package

```
install.package("biOps")
```
#################################
# How to use this package
#################################

> Rscript buildFeatures.R
> Rscript train_models.R

For each object,
> Rscript classify.R image.jpg
    - Output will be the object class




