import numpy as np
from bed_reader import open_bed, sample_file

if __name__ == '__main__':
    # Filter bed files
    bed = open_bed("../data/plink_ema_hair_chr123/snp.hair.bed")
    val = bed.read()
    print()