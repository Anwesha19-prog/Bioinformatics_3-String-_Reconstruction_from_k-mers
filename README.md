# Bioinformatics_3-String-_Reconstruction_from_k-mers

# README: String Reconstruction from k-mers

## Author: Dr Anwesha Sarkar

---

### Problem Overview

In computational biology, DNA or RNA sequences are often broken into **k-mers** (substrings of length `k`) for analysis. **String Reconstruction from k-mers** is the problem of rebuilding the original sequence using a collection of its overlapping k-length substrings.

This is fundamental in **genome assembly**, where sequencing machines produce small overlapping fragments and the full sequence must be reconstructed.

---

### Why Is This Problem Important?

*  **Bioinformatics:** Used in genome sequencing and assembly
* **Data Reconstruction:** Helps restore sequences from noisy or partial data
* **Graph Algorithms:** Builds understanding of de Bruijn graphs and Eulerian paths

---

### Problem Statement

Given:

* An integer `k`
* A collection of `k`-mers (patterns)

Return:

* A reconstructed string whose `k`-mer composition matches the given patterns

---

### Input Format

A text file (`input.txt`) structured as:

```
k
pattern1 pattern2 pattern3 ...
```

**Example:**

```
4
CTTA ACCA TACC GGCT GCTT TTAC
```

---

### Output Format

* A text file (`output.txt`) with the reconstructed string:

```
GGCTTACCA
```

---

### How to Use

#### Requirements

* Python 3.x

#### Steps

1. Save your k-mer input in `input.txt`:

   ```
   ```

4
CTTA ACCA TACC GGCT GCTT TTAC

````

2. Run the script:
   ```bash
   python string_reconstruction.py
````

3. View the reconstructed string in `output.txt`

---

### How It Works

This solution:

1. Constructs a **de Bruijn graph** from the k-mers.
2. Identifies an **Eulerian path** in the graph.
3. Reconstructs the string from the path by overlapping nodes.

The reconstructed string starts with the prefix of the first node and appends the last character of each subsequent node.

---

### Project Structure

```
string_reconstruction_problem_eulers_theorem.py   # Main Python script


dataset.txt                  # Input k-mers


output.txt                 # Reconstructed string


README.md                  # This file
```

---

### Sample Run

**Input:**

```
4
CTTA ACCA TACC GGCT GCTT TTAC
```

**Output:**

```
GGCTTACCA
```

---

**Notes**

* Input patterns must be valid `k`-mers (all of the same length)
* Only one valid reconstruction is returned, though multiple may exist
* Assumes the input set of k-mers can form a single Eulerian path


