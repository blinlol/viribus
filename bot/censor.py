from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
from numpy import array, any
from pymorphy3 import MorphAnalyzer

def censor(
    question:str,
    profanities: list
    ) -> bool:
  question = question.lower().translate(str.maketrans('', '', punctuation))

  tokens = word_tokenize(question)
  filtered_tokens = array(tokens)

  morph = MorphAnalyzer()
  lemmatization = lambda w: morph.parse(w)[0].normal_form
  bad_words_in_text_mask = [lemmatization(word) in profanities for word in filtered_tokens]

  check = any(bad_words_in_text_mask)
  return check

def filter_question(question, filter_emb, filter_ml) -> int:
  question_emb = array([filter_emb.embed_query(question)])
  label = filter_ml.predict(question_emb.reshape(1, -1))
  return label

def new_filter_question(question, all_db)->bool:
  score = all_db.similarity_search(question)
  if score < 1.41:
    return True
  return False 
