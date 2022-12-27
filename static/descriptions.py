import static.commands as c

court           = f"Информация о суде (жми {c.court} для помощи)" 
court_name      = "Название суда"

user            = "Информация о пользователе"
user_name       = "ФИО пользователя"
user_birthdate  = "Дата рождения"
user_birthplace = "Место рождения"
user_address    = "Адрес пользователя"
user_phone      = "Номер телефона пользователя"
user_email      = "Электронная почта пользователя"

documents       = "Информация о документах"
summon_date     = "Дата повестки"
ags_plea_date   = "Дата заявления на АГС"
denial_detail   = "Номер и дата отказа в АГС"

hearings              = "Информация о заседаниях"
denial_hearing_date   = "Дата заседания, на котором был отказ"
witnesses             = "Имена свидетелей"
comission_summon_date = "Дата вынесения комиссией решения о призыве"

comissar        = "Информация о комиссаре"
comissar_name   = "ФИО комиссара"
comissar_address= "Адрес комиссара"

comissariat         = "Информация о комиссариате"
comissariat_region  = "Регион комиссариата"
comissariat_address = "Адрес комиссариата"

comission           = f"Информация о комиссии (жми {c.comission} для помощи)"
comission_region    = "Регион комиссии"
comission_address   = "Адрес комиссии"


class conditions():
    comission_reaction_on_plea              = \
            "Какая была реакция комиссии на заявление?"
    plea_ignored                            = \
            "Заявление проигнорировали"
    summoned_to_the_hearing_and_rejected    = \
            "Вызвали, но отказали"
    not_summoned_but_deadline_missed        = \
            "Не вызвали, но сказали о пропуске сроков"
    comission_violations                    = \
            f"Выберете нарушения со стороны комиссии, если они были\n(жми {c.quorum} для помощи)"
    witnesses_not_heard                     = \
            "Моих свидетелей отказались выслушать"
    no_quorum                               = \
            "Не было кворума"
    less_voices                             = \
            "'За' голосовало меньше половины присутствующих"
    comission_reason_for_rejection          = \
            "На основании чего комиссия проголосовала"
    rejection_reason_not_believe            = \
            "Не убедил в убеждениях"
    rejection_reason_deadline_missed        = \
            "Сказали, что срок пропущен"
    rejection_reason_no_reason              = \
            "Мотивация в решении отсутствует"
    annexes                                 = \
            "Какие документы есть на руках?"
    protocol_copy                           = \
            "Копия выписки из книги протоколов заседания призывной комиссии"
    comission_decision                      = \
            "Заключение призывной комиссии"
    characteristics                         = \
            "Копия характеристика с места работы (учёбы)"
    bio                                     = \
            "Автобиография"
    comissariat_response                    = \
            "Ответ Военного комиссариата на заявление Административного истца"
    summon_copy                             = \
            "Копия повестки для отправки на военную службу"
    summoned_after_hearing                  = \
            "Комиссия Вас призвала?"
    yes_summoned_after_hearing              = \
            "Да"
    no_summoned_after_hearing               = \
            "Нет"
    yes_summoned_plea_ignored   = yes_summoned_after_hearing            
    summoned_plea_ignored       = summoned_after_hearing
