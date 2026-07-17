from dna_tools.validator import validate_dna
from dna_tools.counter import count_nucleotides
from dna_tools.gc import calculate_gc_content
from dna_tools.complement import complement
from dna_tools.reverse import reverse_sequence
from dna_tools.transcription import transcribe_dna
from dna_tools.translation import translate_dna


def nucleotide_counter(sequence):
    counts = count_nucleotides(sequence)
    gc = calculate_gc_content(sequence)

    print("\nNucleotide Counts")
    for nucleotide, count in counts.items():
        print(f"{nucleotide}: {count}")

    print(f"\nGC Content: {gc:.2f}%")


def reverse_complement(sequence):
    comp = complement(sequence)
    rev_comp = reverse_sequence(comp)

    print("\nReverse Complement:")
    print(rev_comp)


def main():

    print("========== DNA Toolkit ==========")
    print("1. Count Nucleotides")
    print("2. Reverse Complement")
    print("3. DNA → RNA Transcription")
    print("4. DNA → Protein Transcription")

    choice = input("\nChoose an option (1-4): ")

    sequence = input("Enter DNA sequence: ")

    try:
        sequence = validate_dna(sequence)

        if choice == "1":
            nucleotide_counter(sequence)

        elif choice == "2":
            reverse_complement(sequence)
        
        elif choice == "3":
            rna = transcribe_dna(sequence)

            print("\nRNA Sequence:")
            print(rna)
        elif choice == "4":

            protein = translate_dna(sequence)

            print("\nProtein Sequence:")
            print(protein)

        else:
            print("Invalid option.")

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()