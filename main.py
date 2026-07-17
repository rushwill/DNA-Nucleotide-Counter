from dna_tools.validator import validate_dna
from dna_tools.counter import count_nucleotides
from dna_tools.gc import calculate_gc_content
from dna_tools.complement import complement
from dna_tools.reverse import reverse_sequence
from dna_tools.transcription import transcribe_dna
from dna_tools.translation import translate_dna
from dna_tools.orf import find_orf
from dna_tools.fasta import read_fasta
from dna_tools.multi_gc import gc_for_all_sequences
from dna_tools.motif import find_motif



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
    print("4. RNA → Protein Transcription")
    print("5. DNA → Find ORF")
    print("6. GC Content from FASTA")
    print("7. Find Motif")

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
        
        elif choice == "5":

            orf = find_orf(sequence)

            if orf:
                print("\nOpen Reading Frame:")
                print(orf)
            else:
                print("\nNo ORF found.")
        elif choice == "6":

            path = input("Enter FASTA file path: ")

            sequences = read_fasta(path)

            results = gc_for_all_sequences(sequences)

            print()

            for name, gc in results.items():
                        print(f"{name} -> {gc:.2f}%")
        elif choice == "7":

            motif = input("Enter motif: ")

            positions = find_motif(sequence, motif)

            if positions:

                print("\nMotif found at positions:")

                print(*positions)

            else:
                print("\nMotif not found.")

        else:
            print("Invalid option.")

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()