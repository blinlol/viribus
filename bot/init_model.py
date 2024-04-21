import torch
import os
import pickle
from numpy import array
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
from optimum.onnxruntime import ORTModelForQuestionAnswering

from .config import name_emb_model, name_qa_model, data_list, name_filter_emb, path_ml_filter_model 

import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def init_qa_model(name_qa_model: str):
    only_name = name_qa_model[name_qa_model.find("/") + 1:]
    # if name_qa_model in os.listdir("bot/models"):
    #     with open("bot/models/" + only_name, "rb") as f:
    #         return pickle.load(f)
    # model = ORTModelForQuestionAnswering.from_pretrained(name_qa_model, from_transformers=True)
    model = AutoModelForQuestionAnswering.from_pretrained(name_qa_model)
    tokenizer = AutoTokenizer.from_pretrained(name_qa_model)
    tokenizer.model_input_names = ['input_ids', 'attention_mask']

    model_pipeline = pipeline(
        task='question-answering',
        model=model,
        tokenizer=tokenizer,
        device= torch.device("cuda" if torch.cuda.is_available() else "cpu")
        )
    # with open("bot/models/" + only_name, "wb") as f:
    #     pickle.dump(model_pipeline, f, protocol=-1)
    return model_pipeline

def init_emb_model(name_emb_model: str, data_list: list):
    embeddings = HuggingFaceEmbeddings(
        model_name=name_emb_model, 
        encode_kwargs={'normalize_embeddings': True}
        )
    
    data_base = FAISS.from_texts(data_list, embeddings)
    return data_base

def init_filter_emb(name_filter_emb: str):
    embeddings = HuggingFaceEmbeddings(
        model_name=name_filter_emb,
        encode_kwargs={'normalize_embeddings': True}
        )
    return embeddings

def init_cfilter_ml_model(path_ml_filter_model: str):
    with open(path_ml_filter_model, 'rb') as f:
        model = pickle.load(f)
    return model

data_base = init_emb_model(name_emb_model, data_list)
model_pipeline = init_qa_model(name_qa_model)
filter_emb = init_filter_emb(name_filter_emb)
# filter_ml = init_cfilter_ml_model(path_ml_filter_model)
filter_ml = None