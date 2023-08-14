import numpy as np

chromosome_data="""1	CM044020.1	NC_064819.1	243,826,021	40	0	
2	CM044021.1	NC_064820.1	236,636,829	40	0	
3	CM044022.1	NC_064821.1	221,642,160	42	2	
4	CM044023.1	NC_064822.1	197,257,046	40	0	
5	CM044024.1	NC_064823.1	166,437,468	39	0	
6	CM044025.1	NC_064824.1	144,996,526	40	0	
7	CM044026.1	NC_064825.1	138,054,969	41	2	
8	CM044027.1	NC_064826.1	134,521,654	39.5	0	
9	CM044028.1	NC_064827.1	127,432,672	41.5	0	
10	CM044029.1	NC_064828.1	120,120,716	40.5	0	
11	CM044030.1	NC_064829.1	117,052,157	41.5	0	
12	CM044031.1	NC_064830.1	110,876,029	42.5	0	
13	CM044032.1	NC_064831.1	106,010,586	41.5	0	
14	CM044033.1	NC_064832.1	100,093,644	40.5	1	
15	CM044034.1	NC_064833.1	96,493,520	40	0	
16	CM044035.1	NC_064834.1	95,037,378	42.5	0	
17	CM044036.1	NC_064835.1	91,502,332	41	0	
18	CM044037.1	NC_064836.1	84,764,919	39.5	2	
19	CM044038.1	NC_064837.1	85,783,627	43.5	1	
20	CM044039.1	NC_064838.1	84,109,276	42	0	
21	CM044040.1	NC_064839.1	83,887,677	42	0	
22	CM044041.1	NC_064840.1	81,976,604	42.5	0	
23	CM044042.1	NC_064841.1	79,875,053	40	0	
24	CM044043.1	NC_064842.1	67,738,374	40.5	1	
25	CM044044.1	NC_064843.1	68,857,337	43	0	
26	CM044045.1	NC_064844.1	48,605,916	40.5	0	
27	CM044046.1	NC_064845.1	38,378,272	41.5	0	
X	CM044047.1	NC_064846.1	181,417,050	40.5	0	
Y	CM044048.1	NC_064847.1	15,906,474	45	6"""
chromosome_data = [a.split() for a in chromosome_data.split("\n")]
chromosome_data = [[a[0], a[1], int(a[3].replace(",", "")), 0] for a in chromosome_data] # The last is the cumulative sum
for i, chr in enumerate(chromosome_data):
    chromosome_data[i][3] = sum([a[2] for a in chromosome_data[:i]])
chromosome_length = {a[1]:a[2] for a in chromosome_data}
chromosome_offset = {a[1]:a[3] for a in chromosome_data}

traits = ["tusk", "hair"]
if __name__ == '__main__':
    for trait in traits:
        snp_data = open(f"../data/101_gemma/{trait}/gemma_lmm1.assoc.txt").read().strip().split("\n")
        snp_data = [a.split("\t") for a in snp_data][1:]
        ## snp_data = [[a[0], int(a[2]), float(a[11])] for a in snp_data if a[0] in chromosome_offset]

        snp_data = [[a[0], a[1], int(a[2]), float(a[11])] for a in snp_data if a[0] in chromosome_offset]
        snp_data.sort(key=lambda x:x[3]) # Sorting the SNP

        sig_thres = 0.05 / len(snp_data)
        pot_thres = 1 / len(snp_data)

        # Make the sig and the pot
        snps = {
            "sig": [a for a in snp_data if a[3] < sig_thres],
            "pot": [a for a in snp_data if a[3] > sig_thres and a[3] < pot_thres]
        }
        bed = {
            "sig": [],
            "pot": []
        }
        FLANKING = 300000
        for type in bed:
            for snp in snps[type]:
                chromosome = snp[0]
                begin = max(0, snp[2] - FLANKING)
                end = max(snp[2] + FLANKING, chromosome_length[snp[0]])
                bed[type].append([chromosome, begin, end])

        # Write it to an outfiles
        for type in bed:
            with open(f"../data/103_bed_files/{trait}-{type}.bed", "w") as f:
                file_content = "\n".join(["\t".join([str(b) for b in a]) for a in bed[type]])
                f.write(file_content)
        print(f"Done for {trait}")
    print("Done")
