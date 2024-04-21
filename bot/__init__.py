from .init_model import data_base, model_pipeline, all_db, filter_ml
from .UserInfo import UserInfo
<<<<<<< Updated upstream
from .config import replace_dict, profanities
from .censor import censor, filter_question
=======
from .config import replace_dict, profanities, dict_links
from .censor import censor, filter_question, new_filter_question
>>>>>>> Stashed changes
from .people_detection import count_people 


def answer(question: str):
    if censor(question, profanities):
        return "Пожалуйста будьте Культурными!"
    else:
<<<<<<< Updated upstream
        label = filter_question(question, filter_emb, filter_ml)
        if label == 0:
            return UserInfo(question, 0).correction_answer(data_base, model_pipeline, replace_dict)
        elif label == 1:
            return "По твоему запросу ничего не нашлось. Попробуй спросить в группе профкома."
        else:
            return "Нет ответа"
=======
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
>>>>>>> Stashed changes

