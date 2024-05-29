
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm

PLINK_FILES="../data/60x_range"
slugs = ["sig1", "pot1", "pot2", "pot3"]
if __name__ == '__main__':
    for slug in slugs:
        snp_list = open(f"{PLINK_FILES}/{slug}/plink.bim").read().strip().split("\n")
        snp_list = [a.split() for a in snp_list]
        snp_list = [a[1] for a in snp_list]

        ld = pd.read_csv(f"{PLINK_FILES}/{slug}/plink.ld", sep="\t", header=None)
        ld.columns = snp_list
        ld.index = snp_list
        # ทำให้สามเลียมอันบนเป้น 0.0
        mask = pd.DataFrame(np.triu(np.ones(ld.shape), k=1), columns=ld.columns, index=ld.index)
        ld = ld.where(mask == 0.0, None)
        plt.figure(figsize=(19, 16))
        custom_cmap = cm.get_cmap("hot", 1024).reversed()
        custom_cmap = sns.color_palette("viridis", as_cmap=True).reversed()
        sns.heatmap(ld, cmap=custom_cmap, annot=False, fmt=".1f", linewidths=0)
        plt.title(f'LD heatmap {slug}')
        plt.savefig(f"{PLINK_FILES}/{slug}/plink-ld.png")
        print(f"{slug} done")

