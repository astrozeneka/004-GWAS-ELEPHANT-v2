
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm

PLINK_FILES="../data/505_plink_extracted/plink_extracted"
LD_FILE="../data/505_plink_extracted/ld-sq-stats.ld"


if __name__ == '__main__':
    snp_list = open(f"{PLINK_FILES}.bim").read().strip().split("\n")
    snp_list = [a.split() for a in snp_list]
    snp_list = [a[1] for a in snp_list]

    ld = pd.read_csv(LD_FILE, sep="\t", header=None)
    ld.columns = snp_list
    ld.index = snp_list

    # ทำให้สามเลียมอันบนเป้น 0.0
    mask = pd.DataFrame(np.triu(np.ones(ld.shape), k=1), columns=ld.columns, index=ld.index)
    ld = ld.where(mask == 0.0, None)

    plt.figure(figsize=(9.5, 8))
    # custom_cmap = sns.diverging_palette(250, 10, as_cmap=True)
    custom_cmap = cm.get_cmap("hot", 1024).reversed()
    sns.heatmap(ld, cmap=custom_cmap, annot=False, fmt=".1f", linewidths=0)
    plt.title('LD heatmap')
    plt.savefig('ld-heatmap.png')
    print()