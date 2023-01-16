import static.commands as c
from aiogram.utils.markdown import link, hlink

court           = f"Информация о суде (нажми {c.court} чтобы понять, как определить)" 
court_name      = "Название суда"

user            = "Информация об истце"
user_name       = "ФИО истца"
user_birthdate  = "Дата рождения истца"
user_birthplace = "Место рождения истца"
user_address    = "Адрес истца"
user_phone      = "Номер телефона истца"
user_email      = "Электронная почта истца"

documents       = "Информация о документах"
summon_date     = "Дата повестки"
ags_plea_date   = "Дата заявления на АГС"
denial_detail   = "Номер и дата отказа в АГС"

hearings              = "Информация о заседаниях"
denial_hearing_date   = "Дата заседания, на котором был отказ"
witnesses             = "Имена свидетелей"
comission_summon_date = "Дата вынесения комиссией решения о призыве"
single_day_hearing_date = "Дата заседания призывной комиссии"
single_day_summon_date  = "Дата призыва одним днём"
single_day_diseases     = "Нерасмотренные заболевания"
single_day_forcingly_delivered_date = "Дата принудительной доставки в военкомат"

comissar        = "Информация о комиссаре"
comissar_name   = "ФИО комиссара"
comissar_address= "Адрес комиссара"

comissariat         = f"Информация о комиссариате (нажми {c.comissariat} чтобы понять, как определить)"
comissariat_name    = "Название комиссариата"
comissariat_address = "Адрес комиссариата"

comission           = f"Информация о комиссии (нажми {c.comission} чтобы понять, как определить)"
comission_name      = "Название комиссии"
comission_address   = "Адрес комиссии"

class pre_messages():
    pre_plaintif_message  = "Сначала мы заполним информацию об истце, то есть о человеке, чьи права были нарушены незаконным призывом, отказом в АГС и т.д.  Если иск подаётся представителем, то истец всё равно тот, чьи права нарушены, а представитель подписывает иск по доверенности. В этом случае от истца нужна доверенность. Представитель должен заполнить контактные данные в сгенерированном иске сам."

    pre_condition_message = "Генератор умеет делать два типа исков: если вам отказали в АГС (не рассмотрели заявление) или если призвали «одним днём».\nЕсли вы оспариваете отказ в АГС или бездействие комиссии при АГС, то выбирайте ответ «отказали в АГС». Если призвали одним днём, то выбирайте второй вариант. Иногда случается, что при призыве «одним днём» призывник умудряется подать заявление на АГС или хотя бы сказать о своём желании перейти на АГС комиссии. В этом случае выбирайте вариант «призвали одним днём». Генератор задаст вопрос про АГС чуть позже."

    pre_diseases_message = "Часто призывники думают, что у них нет болезней. Но не стоит преувеличивать состояние здоровья! Присмотритесь к себе внимательно, может быть, найдётся парочка болезней? Список болезней, которые дают освобождение от службы в армии, найдете " + hlink(title="здесь", url="http://www.consultant.ru/document/cons_doc_LAW_149096/7cd8dde08fc9aff1bf6d22025061d18f55e576e5/") + ".\nЕсли совсем никаких болезней не обнаружите, то из полученного иска надо будет убрать соответствующий пункт."

    pre_annexes_message = "Исковые требования надо обосновать, поэтому запрашиваем документы, которые есть на руках. Они пойдут приложениями в иск."

    pre_making_suit_message = f"На основании ответов генератор формирует исковое -- оно сейчас придёт сюда. Его надо будет проверить и, если будут неточности или ошибки, исправить. Мы работаем над тем, чтобы ошибок было меньше, но они все равно случаются. Мы разработали для вас гид, как правильно подать иск -- нажмите {c.how_to_sue} чтобы его прочитать.\n\n Удачи!\n\n P.S. генератор работает в тестовом режиме, поэтому нам важно получить от вас конструктивный фидбэк. Его и благодарности можно направить в @agsnowarbot в телеграмме"

class conditions():
    what_happened                           = \
            "Что случилось?"
    ags_rejected                            = \
            "Отказали в агс"
    single_day_summon                       = \
            "Призвали одним днём"
    single_day_delivery_method              = \
            "Как оказались в военкомате?"
    single_day_forcingly_delivered          = \
            "Насильно привезли"
    single_day_came_themselves              = \
            "Пришёл сам"
    single_day_asked_for_ags                = \
            "Просили АГС?"
    single_day_ags_asked                    = \
            "Да"
    single_day_ags_not_asked                = \
            "Нет"
    single_day_ask_ags_copy                 = \
            "У вас есть копия заявления на АГС?"
    single_day_yes_ags_copy                 = \
            "Да (приложите его к иску)"
    single_day_no_ags_copy                  = \
            "Нет"
    comission_reaction_on_plea              = \
            "Какая была реакция комиссии на заявление?"
    plea_ignored                            = \
            "Заявление проигнорировали"
    summoned_to_the_hearing_and_rejected    = \
            "Вызвали, но отказали"
    not_summoned_but_deadline_missed        = \
            "Не вызвали, но сказали о пропуске сроков"
    comission_violations                    = \
            f"Выберете нарушения со стороны комиссии, если они были\n(нажми {c.quorum} чтобы понять как)"
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
            "Копия заключения призывной комиссии"
    characteristics                         = \
            "Копия характеристики с места работы (учёбы)"
    bio                                     = \
            "Копия автобиографии"
    comissariat_response                    = \
            "Копия ответа Военного комиссариата на заявление Административного истца"
    summon_copy                             = \
            "Копия повестки Военного комиссариата"
    summoned_after_hearing                  = \
            "Комиссия Вас призвала?"
    yes_summoned_after_hearing              = \
            "Да"
    no_summoned_after_hearing               = \
            "Нет"
    summoned_after_missed_deadlines     = summoned_after_hearing
    summoned_after_plea_ignored         = summoned_after_hearing
    yes_summoned_after_plea_ignored     = yes_summoned_after_hearing
    yes_summoned_after_missed_deadlines = yes_summoned_after_hearing
    no_summoned_after_plead_ingored     = no_summoned_after_hearing
    no_summoned_after_missed_deadlines  = no_summoned_after_hearing





