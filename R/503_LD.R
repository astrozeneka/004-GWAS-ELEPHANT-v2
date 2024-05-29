
# try to use snp.plotter
install.packages("snp.plotter")
library("snp.plotter")
library(devtools)
install_github(repo="cannin/snp_plotter",
               build_vignette=FALSE,
               dependencies=TRUE,
               subdir="snp.plotter",
               force=TRUE
)
library(snp.plotter)
snp.plotter(config.file="config.txt")
setwd("C:\\Users\\KU\\Desktop\\AGB\\Ryan\\projects\\004-GWAS-ELEPHANT-v2\\data\\503_ld")
data_matrix <- read.table("ld-output.ld", header=FALSE)
# Create a heatmap
heatmap(data_matrix, 
        col = colorRampPalette(c("blue", "white", "red"))(100), # Color palette
        scale = "none",  # No scaling
        Rowv = NA,        # No row clustering
        Colv = NA,        # No column clustering
        xlab = "Columns", # Label for the x-axis
        ylab = "Rows",    # Label for the y-axis
        main = "Heatmap of LD Matrix") # Title for the heatmap
snp.plotter(IMAGE.TYPE = "pdf")

######################################################
## TRY TO USE LDheatmap
######################################################
if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install(version = "3.16")
biocLite(c("snpStats","rtracklayer","GenomicRanges","GenomInfoDb","IRanges"))
devtools::install_github("SFUStatgen/LDheatmap")


