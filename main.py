from dna_tools.validator import validate_dna
from dna_tools.counter import count_nucleotides
from dna_tools.gc import calculate_gc_content


sequence = input("Enter DNA sequence: ")

try:
    sequence = validate_dna(sequence)

    counts = count_nucleotides(sequence)

    print("\nNucleotide Counts")
    for nucleotide, count in counts.items():
        print(f"{nucleotide}: {count}")
    
    gc_content = calculate_gc_content(sequence)
    print(f"\nGC Content: {gc_content:.2f}%")

except ValueError as e:
    print(e)
