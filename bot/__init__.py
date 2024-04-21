from .init_model import data_base, model_pipeline, all_db, filter_ml
from .UserInfo import UserInfo
from .config import replace_dict, profanities, dict_links
from .censor import censor, filter_question, new_filter_question
from .people_detection import count_people 


def answer(question: str, context: int) -> tuple[str, dict]:
    if censor(question, profanities):
        return "Пожалуйста будьте Культурными!", {}
    else:
        # label = filter_question(question, filter_emb, filter_ml)
        user = UserInfo(question, context)
        correct_que = user.correction_que(replace_dict)
        if new_filter_question(correct_que, all_db):
            if context < 3:
                return user.correction_answer(data_base, model_pipeline, dict_links)
            return "По твоему запросу ничего не нашлось. Попробуй спросить в группе профкома.", {"Профком": "https://vk.com/profcomff"}
        return "По твоему запросу ничего не нашлось. Попробуй спросить в группе профкома.", {"Профком": "https://vk.com/profcomff"}
        # if label == 0:
        #     return UserInfo(question, 0).correction_answer(data_base, model_pipeline, replace_dict)
        # elif label == 1:
        #     return "По твоему запросу ничего не нашлось. Попробуй спросить в группе профкома.", {}
        # else:
        #     return "Нет ответа", {}