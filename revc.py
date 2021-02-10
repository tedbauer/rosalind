dna_string = input()
print(
        dna_string
        [::-1]
        .replace("A", "1")
        .replace("T", "2")
        .replace("C", "3")
        .replace("G", "4")

        .replace("1", "T")
        .replace("2", "A")
        .replace("3", "G")
        .replace("4", "C")
)
