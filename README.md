# DNA Nucleotide Counter

A simple Python project for basic DNA sequence analysis.

## Features

- Validate DNA sequences
- Count nucleotides (A, T, C, G)
- Calculate GC content (%)
- Modular project structure
- Unit testing with pytest

## Project Structure

```
DNA_Nucleotide_Counter/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── dna_tools/
│   ├── __init__.py
│   ├── validator.py
│   ├── counter.py
│   └── gc.py
│
└── tests/
    └── test_counter.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/DNA-Nucleotide-Counter.git
```

Move into the project directory:

```bash
cd DNA-Nucleotide-Counter
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python main.py
```

Example:

Input:

```
AATCGG
```

Output:

```
Nucleotide Counts

A: 2
T: 1
C: 1
G: 2

GC Content: 50.00%
```

## Technologies

- Python 3
- pytest
- Git
- GitHub

## Future Improvements

- Reverse Complement
- DNA → RNA Transcription
- RNA → Protein Translation
- FASTA file reader
- Motif search
- k-mer counting

## License

This project is licensed under the MIT License.