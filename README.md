# Efficient string matching (Aho-Corasick algorithm)
## Hélène Perée

**Assignment for my master in Bioinformatics and Modelling (ULB)**

**Course**: Algorithms in computational biology (2016-2017)

### Programming language
Python 3 (no libraries)

### Application in biology
Multiple pattern matching enables to look for exact occurrences of multiple known sequences in a genome.

### Input
- A file containing the text (provided example: input.txt)
- A list of keywords/patterns

### Output
Printing of the ending position(s) of these multiple keywords in this text

### Algorithm (combinatorial pattern matching)
1. Creation of a finite state pattern matching machine
2. Processing of the text in a single pass

The pattern matching machine uses a keyword tree: it is a rooted directed tree where the vertices are the states (starting from 0) and the edges are the keywords symbols/characters.

The pattern matching machine is composed of 3 functions:
- Goto (= keyword tree / graph): it links each state and keyword symbol to the next state composing the same keyword. If several keywords have the same prefix, they share the same path in the graph until they differ.
- Failure: it links each state to the previous state with the same symbol or to the start state (0) otherwise.
- Output: it links each state at which we can find the last symbol of at least one keyword to the corresponding keyword(s).

### Example 1 (bibliographic search)
Input:
- text: "ushers"
- keywords: ["he", "she", "his", "hers"]

Output:

4 ['she', 'he']

6 ['hers']

### Example 2 (bioinformatics)
Input:
- text: "ATGGTCGGT"
- keywords: ["GTC", "TC", "GGA", "CGGT"]

Output:

6 ['GTC', 'TC']

9 ['CGGT']

### Complexity
O(N+m) where N = total length of all keywords and m = length of the text

### Source
Alfred V. Aho and Margaret J. Corasick. "Efficient string matching: an aid to bibliographic search." Communications
of the ACM 18.6 (1975): 333‐340

N. C. Jones and A. Pevzner, "Introduction to Bioinformatics Algorithms", Chapter 9, Section 9.4
