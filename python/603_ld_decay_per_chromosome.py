import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # ในส่วนใหญ๋ sns ต้องการ panda Dataframe format

if __name__ == '__main__':
    # data = open("../data/60x_range/all/all.ld").read().strip().split("\n")

    # ใช้ interchr แทน
    # data = open("../data/60x_range/all/all-interchr.ld").read().strip().split("\n")

    # โดยใช้ --window-size-kb 1000
    data = open("../data/60x_range/all/all-sw1000.ld").read().strip().split("\n")

    data = [a.split() for a in data]
    data = pd.DataFrame(data[1:], columns=data[0])

    # ต้องเปลียชนิข้อมูลก่อน
    data["BP_A"] = data["BP_A"].astype(int)
    data["BP_B"] = data["BP_B"].astype(int)
    data["R2"] = data["R2"].astype(float)

    # คำนวณค่า distance ระหวัง snp pair
    data["distance"] = abs(data["BP_A"] - data["BP_B"])

    # พล็อด LD decay
    # ไม่ต้อง ใช้ colormap

    # ภาค 1 , คำนวณค่าเฉีลยของ 2 ก่อน
    data['distance_interval'] = (data['distance'] // 30000) * 30000
    # average_r2 = data.groupby('distance_interval')['R2'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    # สำหรับแต่ละ chromosome
    data = data[data['CHR_A'] == data['CHR_B']]
    for i, chromosome in enumerate(data['CHR_A'].unique()):
        subset = data[data['CHR_A'] == chromosome]
        subset_average_r2 = subset.groupby('distance_interval')['R2'].mean().reset_index()
        plt.plot(subset_average_r2['distance_interval'], subset_average_r2['R2'], marker='', linestyle='-')
        print()
    # plt.plot(average_r2['distance_interval'], average_r2['R2'], marker='o', linestyle='-')
    plt.title('Average R^2 vs Genetic Distance')
    plt.xlabel('Genetic Distance (bp)')
    plt.ylabel('Average R^2')
    plt.grid(True)
    plt.show()
    plt.savefig("../data/60x_range/all/ld-decay-1000-per-chr.png")

    exit()