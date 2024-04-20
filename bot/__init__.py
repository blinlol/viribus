from .init_model import data_base, model_pipeline
from .UserInfo import UserInfo
from .config import replace_dict, profanities
from .censor import censor

sessions = {}

def answer(question: str):
    if censor(question, profanities):
        return "Пожалуйста будьте Культурными!"
    else:
        return UserInfo(question, 0).correction_answer(data_base, model_pipeline, replace_dict)