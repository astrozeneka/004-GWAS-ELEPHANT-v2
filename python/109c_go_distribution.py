import pandas as pd

if __name__ == '__main__':
    path_sig = "../data/109_GO/hair-sig/gograph_biologicalprocess.txt"
    # path_pot1 = "../data/109_GO/hair-pot/CM044023.1_176211135-197257046/gograph_cellularcomponent.txt"
    path_pot2 = "../data/109_GO/hair-pot/CM044026.1_78796413-138054969/gograph_cellularcomponent.txt"
    data = open(path_sig).read().strip().split("\n")

    data = [a.split("\t") for a in data]
    df = pd.DataFrame(data[1:], columns=data[0])

    print()
