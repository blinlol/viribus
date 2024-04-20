from .init_model import data_base, model_pipeline, filter_emb, filter_ml
from .UserInfo import UserInfo
from .config import replace_dict, profanities, dict_links
from .censor import censor, filter_question
from .people_detection import count_people 


def answer(question: str, context: int) -> tuple[str, dict]:
    if censor(question, profanities):
        return "Пожалуйста будьте Культурными!", {}
    else:
        # label = filter_question(question, filter_emb, filter_ml)
        if context < 3:
            return UserInfo(question, context).correction_answer(data_base, model_pipeline, replace_dict, dict_links)
        return "По твоему запросу ничего не нашлось. Попробуй спросить в группе профкома.", {"Профком": "https://vk.com/profcomff"}
        # if label == 0:
        #     return UserInfo(question, 0).correction_answer(data_base, model_pipeline, replace_dict)
        # elif label == 1:
        #     return "По твоему запросу ничего не нашлось. Попробуй спросить в группе профкома.", {}
        # else:
        #     return "Нет ответа", {}

