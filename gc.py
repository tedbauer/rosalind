import sys

def gc_content(dna_string):
    return (dna_string.count("C") + dna_string.count("G")) / len(dna_string) * 100

fasta = list(sys.stdin)
dna_to_gc = dict()

num_skips = 0
for i, line in enumerate(fasta):
    if num_skips > 0:
        num_skips -= 1
        continue

    if line[0] == ">":
        dna_string = ""
        j = i+1
        while j < len(fasta) and fasta[j][0] != ">":
            num_skips += 1
            dna_string += fasta[j].strip("\n")
            j += 1

        dna_to_gc[line[1:].strip("\n")] = gc_content(dna_string)

l_key, l_val = None, -1
for key, val in dna_to_gc.items():
    if val > l_val:
        l_val = val
        l_key = key

print(l_key)
print(l_val)
