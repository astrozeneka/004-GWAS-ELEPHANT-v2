import pandas as pd

if __name__ == '__main__':
    # Calculate statistics on coverage
    features = ["gene", "exon"]
    individuals = [a for a in range(1, 34)]
    df = pd.DataFrame(columns=features, index=individuals)
    df_stat = pd.DataFrame(columns=features, index=["avg", "std", "med"])
    for feature in features:
        data = open(f"../data/106_annotation_ema/coverage/{feature}.txt").read().strip().split("\n")
        data = [a.split("\t") for a in data]
        for i, indiv in enumerate(individuals):
            sub_data = [int(a[3+i]) for a in data]
            coverage = sum(sub_data) / len(sub_data)
            df[feature][indiv] = coverage

        col = df[feature]
        df_stat[feature]["avg"] = col.mean()
        df_stat[feature]["std"] = col.std()
        df_stat[feature]["med"] = col.median()

    df.to_csv("../prepared_data/106_coverage.csv", sep=",", index=True)
    df_stat.to_csv("../prepared_data/106_coverage_stats.csv", sep=",", index=True)
    print("Done")