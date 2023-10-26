# DNA Similarity

## Overview

The DNA Similarity Calculator is a Python program that allows you to compare DNA sequences and perform various DNA similarity analyses. It provides functions to count the number of matches between two sequences, find the maximum contiguous chain of matches, and align sequences to maximize either matches or the maximum contiguous chain. This tool is useful for bioinformatics and genetic research.

## Prerequisites

- Python 3.x installed on your computer.

## Description

This project comprises a set of functions that handle DNA sequence comparison and alignment. It allows users to find the number of matches, the maximum contiguous chain, and the optimal alignment of two sequences, along with displaying the alignment highlighting matching nucleotides in red. Users can select options from a menu to set the maximum shift, perform calculations, and exit the program. The program guides you through each step and provides an interactive interface for input.

## Hurdles

**User Input Validation**: Validating user inputs is critical to prevent unexpected errors. Handling cases such as invalid input modes or negative shift values necessitates robust error handling and input validation mechanisms.

**User Interface and Experience**: Improving the user interface and experience could enhance the usability of the program. Providing clear instructions and appropriate feedback to the user is important for a seamless user experience.


## Approach

Task 1: Studied the problem statement and designed the basic structure of the program. Implemented the `count_matches` and `max_chain` functions for sequence comparison.

Task 2: Worked on user interface design and implemented the menu-based interface for user interaction.

Task 3: Developed the file handling functionalities for reading sequences from files. 

Task 4: Implemented the sequence alignment functions and tested the program with various examples.


## Usage
1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/EngineerDanny/DNA_similarity.git

2. Run the main.ipynb file in Jupyter Notebook or Jupyter Lab.


## Examples
```python
seq1 = "ATCGGTA"
seq2 = "ATTGGTA"
result = count_matches(seq1, seq2)
print(result)  # Output: 5
```

```python
seq1 = "ATCGGTA"
seq2 = "ATTGGTA"
result = max_chain(seq1, seq2)
print(result)  # Output: 3
```
