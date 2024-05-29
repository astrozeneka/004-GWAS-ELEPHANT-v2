import glob
import os
from Bio.Align.Applications import ClustalwCommandline
from Bio.Align.Applications import MafftCommandline

from Bio import SeqIO

if __name__ == '__main__':
    snps = ["sig1", "pot1", "pot2", "pot3"]
    individuals = [os.path.basename(a.replace("_1K_sig1.fasta", "") )for a in glob.glob("../data/90x_primers/fasta_sig1/*.fasta")]

    # เตรียม seq ที่ตองใช้ reverse complement
    to_be_reversed = open("../data/90x_primers/to_be_reversed_complement.txt").read().split("\n")
    to_be_reversed = open("../data/90x_primers/to_be_reversed_complement.back.txt").read().split("\n")
    to_be_reversed = [a.split("      ") for a in to_be_reversed if len(a) > 1]
    to_be_reversed = [a for a in to_be_reversed if len(a) > 1] # 27+3 - 50
    to_be_reversed = {a.replace('_', ':'):b for a,b in to_be_reversed}
    ## to_be_reversed = [a for a in to_be_reversed if a[0][0 != "#"]

    for snp in snps[:1]:
        for individual in individuals[:]:
            fasta_file = f"../data/90x_primers/fasta_{snp}/{individual}_1K_{snp}.fasta"
            fasta_revcomp = f"../data/90x_primers/tmp/1_revcomp/{individual}_1K_{snp}_1revcomp.fasta"
            seq_out = []
            for record in SeqIO.parse(fasta_file, "fasta"):
                if record.id[:30] in to_be_reversed and to_be_reversed[record.id[:30]].replace('-', '') in record.seq:
                    record = record.reverse_complement(record.id, record.name)
                seq_out.append(record)

            # ใส่ ref seq เพื่ม
            ref_file = f"../data/90x_primers/refs/{snp}.fasta"
            ref_seq = SeqIO.read(ref_file, "fasta")
            # seq_out.append(ref_seq)
            SeqIO.write(seq_out, open(fasta_revcomp, "w"), "fasta")


            aligned1_fasta_file = f"../data/90x_primers/tmp/2_aligned/{individual}_1K_{snp}_2aligned.fasta"
            clustalw_cline = ClustalwCommandline("clustalw2", infile=fasta_revcomp, outfile=aligned1_fasta_file)
            stdout, stderr = clustalw_cline()

            aligned1_seqs = SeqIO.parse(aligned1_fasta_file, "fasta")
            unaligned_with_ref_seqs = []
            unaligned_with_ref_file = f"../data/90x_primers/tmp/3_unaligned_with_ref/{individual}_1K_{snp}_unalignedwithref.fasta"
            _added = []
            for record in SeqIO.parse(aligned1_fasta_file, "clustal"):
                _added.append(record.id)
                record.id = record.id + "_" + str(_added.count(record.id))
                unaligned_with_ref_seqs.append(record)
            unaligned_with_ref_seqs.append(ref_seq)
            SeqIO.write(unaligned_with_ref_seqs, open(unaligned_with_ref_file, "w"), "fasta")

            # aligned1_seqs.append(ref_seq)
            aligned_with_ref_file = f"../data/90x_primers/tmp/3_with_ref/{individual}_1K_{snp}_withref.fasta"
            clustalw_cline2 = ClustalwCommandline("clustalw2", infile=unaligned_with_ref_file, outfile=aligned_with_ref_file)
            stdout, stderr = clustalw_cline2()
            print("Done")




            print(f"{snp} - {individual}")