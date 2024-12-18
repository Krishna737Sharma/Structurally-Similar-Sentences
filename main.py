# import nessesary libraries
import spacy
from collections import Counter
from itertools import islice

# load model
nlp=spacy.load('en_core_web_sm')

# fun for getting name entities from sent
def get_name_entity(doc):
    name_entity=[]
    print(f"\nName entities in the sentence:")
    for ent in doc.ents:
        name_entity.append(ent.text)
        print(ent)
    return name_entity

# fun for getting POS tag
def get_pos_tag(doc):
    pos_tag=[]
    print(f"\nPOS tags in the sentence:")
    for token in doc:
        pos_tag.append(token.pos_)
        print(token)
    return pos_tag

# fun for similarities
def similarity(set1,set2):
    intersection=len(set(set1).intersection(set(set2)))
    union=len(set(set1).union(set(set2)))
    score= intersection/union if union!=0 else 0
    return score

# POS n-gram generator
def get_ngrams(pos_tag,n):
    ngrams=[]
    for i in range(len(pos_tag)-n+1):
        ngram=pos_tag[i:i+n]
        ngrams.append(ngram)
    print(ngrams)
    return ngrams

# fun for calculate saimilarities
def cal_similarity(sent1,sent2,chunk_size):
  doc1=nlp(sent1)
  doc2=nlp(sent2)

  name_entity1=get_name_entity(doc1)
  name_entity2=get_name_entity(doc2)

  pos_tag1=get_pos_tag(doc1)
  pos_tag2=get_pos_tag(doc2)

  entity_simi=similarity(name_entity1,name_entity2)
  pos_ngram1=get_ngrams(pos_tag1,chunk_size)
  pos_ngram2=get_ngrams(pos_tag2,chunk_size)

  pos_simi=similarity(pos_tag1,pos_tag2)

  total_simi=(entity_simi+pos_simi)
  return total_simi

# Query sentence
Q_sent='Narendra modi is the president of India.'

# Comparision sentence
cam_sent=['Narendra modi was born in the gujrat.','The prime minister gave a speech in red fort.',
          'Krishna is the student of arificial intelligence.','India is my country.',
          'Modi is just a surname.']

# Get chunk size from user
while True:
  try:
    chunk_size=int(input("Enter the chunk size:"))
    break
  except ValueError:
    print("Invalid input. Please enter a valid integer.")
    continue

# calculate similarity
similarities=[]
for sent in cam_sent:
  sim=cal_similarity(Q_sent,sent,chunk_size)
  similarities.append((sent,sim))

print(similarities)

# Sort sentences by similarity
sorted_similarities=sorted(similarities,key=lambda x:x[1],reverse=True)

print(sorted_similarities)

# print top-5 similar sentences
print(f"\nTop-5 similar sentences (Chunk size: {chunk_size}):")
for sentence,score in similarities[:5]:
  print(f"Sentence: {sentence}")
  print(f"Similarity score: {score:.3f}")

