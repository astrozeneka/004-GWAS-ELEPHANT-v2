import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_style("whitegrid")
# Should build the trait list of each individual

phenotypes = """EMAf10	male	 No Tusk	Normal
EMAf1	male	 No Tusk	Normal
EMAf28	male	 No Tusk	Normal
EMAf2	male	 No Tusk	Normal
EMAf3	male	 No Tusk	Normal
EMAf4	male	 No Tusk	Normal
EMAf5	male	 No Tusk	Normal
EMAf7	male	 No Tusk	Normal
EMAFf20	male	 No Tusk	Long
EMAFf21		 No Tusk	Long
EMAFf2	male	 No Tusk	Long
EMAFf5	male	 No Tusk	Long
EMAFf6	male	 No Tusk	Long
EMAFm2	male	 Tusk	Long
EMAFm6	male	Tusk	Long
EMAFm9	male	 No Tusk	Long
EMAm10	male	 Tusk	Normal
EMAm12	male	 No Tusk	Normal
EMAm13	male	 No Tusk	Normal
EMAm14	male	 No Tusk	Normal
EMAm16	male	 No Tusk	Normal
EMAm17	male	 No Tusk	Normal
EMAm18	male	 No Tusk	Normal
EMAm19	male	 No Tusk	Normal
EMAm1	male	 Tusk	Normal
EMAm20	male	 No Tusk	Normal
EMAm2	male	 Tusk	Normal
EMAm3	male	 Tusk	Normal
EMAm5	male	 Tusk	Normal
EMAm6	male	 Tusk	Normal
EMAm7	male	 Tusk	Normal
EMAm8	male	 Tusk	Normal
EMAm9	male	 Tusk	Normal
"""
phenotypes = phenotypes.strip().split("\n")
phenotypes = [a.split("\t") for a in phenotypes]
phenotypes = {a[0]:a[3] for a in phenotypes}

if __name__ == '__main__':
    eigen_vec = open("../data/1011_mds/pca.eigenvec").read().strip().split("\n")
    eigen_vec = [a.split() for a in eigen_vec]
    eigen_vec = [(a[0].replace("_q20_sorted", ""), float(a[2]), float(a[3])) for a in eigen_vec]
    index = [a[0] for a in eigen_vec]
    eigen_vec = pd.DataFrame([a[1:] for a in eigen_vec], index=index, columns=['x', 'y'])
    eigen_vec['Hair'] = eigen_vec.index.map(lambda x:phenotypes[x])

    p = sns.color_palette("pastel")

    pastel_palette = ["#FF8080", "#FFCF96"]
    sns.scatterplot(data=eigen_vec, x='x', y='y', hue='Hair', palette=pastel_palette)
    plt.xlabel('PCA1')
    plt.ylabel('PCA2')
    plt.savefig("../data/1011_mds/pca.png")
    print()