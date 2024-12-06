# Assignment 8: Structurally Similar Sentences

## Overview

In this assignment, the goal is to find structurally similar sentences to a given query sentence. A sentence (say `s1`) is structurally similar to another sentence (say `s2`) if they both have the same named entities as well as a similar parts of speech (POS) sequence.

The similarity between two sentences, `s1` and `s2`, is computed using the following formula:

### Formula:
Score(s1, s2) = (Number of common named entity types between s1 and s2) / |Union of named entity types in s1 and s2|

    POS score(s1, s2)


### POS Score:

POS score(s1, s2) = Sum of Jaccard similarity scores for all n-gram chunks (with overlap length n=2) based on their POS tags.


The task is to compute these similarity scores between a given query sentence and other sentences in a dataset and return the top 5 structurally similar sentences.

## Tasks

1. **Named Entity Recognition (NER)**: Use SpaCy to extract named entities from the sentences.
2. **POS Tagging**: Use SpaCy to extract part-of-speech tags from the sentences.
3. **Compute Similarity Score**: Calculate the similarity between the query sentence and all other sentences based on named entity types and POS sequences.
4. **Return Top 5 Similar Sentences**: Given a query sentence, return the top 5 sentences that are structurally similar.
5. **Jaccard Similarity**: Calculate the Jaccard similarity for POS tag chunks (n-gram overlap length of 2).

## Requirements

To complete the assignment, the following Python libraries are required:

- **SpaCy**: For Named Entity Recognition (NER) and POS tagging.
- **NumPy**: For numerical computations.
- **Pandas**: For organizing and processing the sentences and similarity scores.

### Installation

To install the required libraries, you can run the following commands:

```bash
pip install spacy numpy pandas

Additionally, you need to download the SpaCy model for English:

python -m spacy download en_core_web_sm

Steps
1. Data Input

You will need to input a dataset of sentences (e.g., a list of sentences) along with a query sentence. The input sentences will be compared with the query sentence based on their structural similarity.
2. Named Entity Recognition (NER)

    Extract the named entities from each sentence using SpaCy’s NER functionality.
    For each sentence, store the named entity types.

3. POS Tagging

    For each sentence, extract the part-of-speech tags using SpaCy.
    Generate n-gram chunks (overlap length of 2) from the POS tags.

4. Similarity Calculation

    Named Entity Similarity: Count the number of common named entity types between the query sentence and each candidate sentence. Normalize it by the union of named entity types.
    POS Similarity: Calculate the Jaccard similarity between the POS tag chunks of the query sentence and each candidate sentence.

5. Ranking

    For each sentence, compute the total similarity score as the sum of the named entity similarity and the POS similarity.
    Rank all sentences by their similarity score to the query sentence.

6. Output

Return the top 5 sentences with the highest similarity score to the query sentence.
Example

Given a list of sentences:

sentences = [
    "Apple is looking at buying U.K. startup for $1 billion",
    "San Francisco considers banning sidewalk robots",
    "London is a beautiful city",
    "Amazon is planning to launch new services in 2022",
    "Elon Musk is the CEO of Tesla"
]

And a query sentence:

query_sentence = "Apple is planning to buy a new company"

The program will output the top 5 structurally similar sentences based on named entity recognition and POS similarity.
