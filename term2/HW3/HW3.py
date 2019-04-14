import re
import random
import sys

def create_snp(n, seq):
    if n > len(seq):
        print("WARNING: number of SNPs is more than sequence length")
        n = len(seq)
    snp_pos = random.sample(range(0, len(seq)), n)
    answ = []
    for pos in snp_pos:
        answ.append([seq[pos], random.choice(('A', 'C', 'G', 'T')), pos])
    return answ

def process_file(filename, n):
    print("       SEQ_ID            |  MUTATION  |  POSITION-OF-MUTATION")

    with open(filename) as f:
        for line in f:
            seq_id, seq = re.split(r'\s+', line.strip())
            mutations = create_snp(n, seq)
            for mutation in mutations:
                print(f"{seq_id: <22}{mutation[0]: >10}->{mutation[1]}\t{mutation[2]}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: script.py <path-to-seqs> <SNP#>")
        exit()

    filename = sys.argv[1]
    #n = int(sys.argv[2][3:])
    n = int(re.findall(r"([A-Z]+)(\d+)", sys.argv[2])[0][1])
    try:
        process_file(filename, n)
    except FileNotFoundError as error:
        print(f"No such file: {filename}")
        print(error)
