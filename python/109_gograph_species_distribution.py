import matplotlib.pyplot as plt

def get_specie(sequence_name):
    return sequence_name.split()[1].split("_")[-1]

if __name__ == '__main__':
    slug = "hair-pot"

    data = open(f"../data/109_GO/{slug}/blast_result.csv").read().strip().split("\n")[1:]
    data = [a.split("\t") for a in data]
    species = [get_specie(a[1]) for a in data]
    species_list = list(set(species))

    bar_data = [(s, species.count(s)) for s in species_list]
    bar_data.sort(key=lambda x:x[1], reverse=False)

    bar_data_lab = [a[0] for a in bar_data]
    bar_data_val = [a[1] for a in bar_data]
    plt.barh(bar_data_lab, bar_data_val)
    plt.ylabel("Species")
    plt.title("Species distribution [blast2go]")
    plt.savefig(f"../data/109_GO/species-distribution-{slug}.png")


    print()