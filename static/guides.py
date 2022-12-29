from aiogram.utils.markdown import link, hlink

guide_court     = 'Давайте определимся с подсудностью, то есть судом, в который подаём иск.\n\nИск подаётся в городской или районный суд (а не в мировой или областной/краевой).  В нашем случае уполномоченный суд определяется по месту проживания истца. Если человека забрали из хостела, территориальная подсудность будет определяться по адресу хостела. Чтобы определить суд, предлагаем использовать ' + hlink(title='базу данных', url='https://sudrf.ru/index.php?id=300#podsud ') + ' судов, которая работает на базе сайте Верховного суда РФ. Однако иногда эта база данных «лежит» и может быть недоступна по VPN. В этом случае вам придётся самостоятельно определить суд. На сайтах судов посмотрите раздел «территориальная подсудность». Если ваш адрес относится к территориальной подсудности суда, то это и есть суд, куда будете подавать исковое. Если вашего адреса нет, значит, надо искать другой суд.'

guide_how_to_sue = 'ССЫЛКА НА ФАЙЛ ДЛЯ СКАЧИВАНИЯ, СЕЙЧАС ГАЙД СЛИШКОМ БОЛЬШОЙ'

guide_quorum    = 'Состав призывной комиссии муниципалитета, которая будет принимать решение по вашему заявлению на АГС, а соответственно и количество ее членов определяется Распоряжением главы субъекта, в котором эта призывная комиссия должна осуществлять свою работу.  В нее точно должны входить следующие лица:\n\n 1. глава муниципального образования или его заместитель - председатель призывной комиссии;\n 2. должностное лицо военного комиссариата - заместитель председателя комиссии;\n 3. секретарь комиссии;\n 4. врач, руководящий работой по медицинскому освидетельствованию граждан, подлежащих призыву на военную службу;\n 5. представитель соответствующего органа внутренних дел;\n 6. представитель соответствующего органа, осуществляющего управление в сфере образования;\n 7. представитель соответствующего органа службы занятости населения (в части вопросов, касающихся альтернативной гражданской службы).\n\n То есть минимум 7 человек, которые будут голосовать по вашему заявлению. И простое большинство при присутствии всех членов комиссии - это от 4 голосов и больше за или против.  Но, что если не все члены комиссии присутствуют? Такое тоже возможно, но тогда их должно быть ⅔ от общего числа членов комиссии, то есть если в нашей комиссии 7 человек, то ⅔ - это не менее 5 членов комиссии должны присутствовать и за или против должны проголосовать 3 и более из них, тогда решение будет принято.\n Что если вы не знаете сколько членов комиссии присутствовало, все ли они имели право голоса и достаточно ли их было для принятия решения. Вы можете запросить копию протокола заседания призывной комиссии с указанием всех членов комиссии, которые присутствовали, и количеством тех кто и как проголосовал. И этот протокол вы можете сравнить с Распоряжением главы субъекта о составе призывной комиссии в вашем муниципалитете и сделать выводы был ли соблюден кворум, а значит была ли соблюдена процедура принятия решения. Если нет, у вас есть большие шансы на отмену такого решения в суде, о чем говорит многочисленная судебная практика.  '

guide_comission = 'Как правильно написать название призывной комиссии?\n\n Призывная комиссия определяется по адресу, где вы живете. Например, если вы живете в московском районе Ясенево, то призывная комиссия будет именоваться «Призывная комиссия муниципального образования Ясенево». Если вы живете в Старом Осколе, то писать нужно «Призывная комиссия Старооскольского городского округа». Больше информации -- ' + hlink(title='здесь', url='https://docs.google.com/document/d/1Bi0Q0sntboS4McmegvQfUpXIrGKOj6C0M_IK2ML2aL8/edit#') + '.'

guide_comissariat = 'Информацию о военном комиссариате можно найти в повестке.  Но если с этим проблемы, то о том, как определить комиссариат, читайте ' + hlink(title='здесь', url='https://docs.google.com/document/d/1Bi0Q0sntboS4McmegvQfUpXIrGKOj6C0M_IK2ML2aL8/edit#)') + '. Пример названия комиссариата: Военный комиссариат Ново-Савиновского и Авиастроительного района Республики Татарстан».'

guide_fee       = 'Как оплатить пошлину? \n\n Оплатить пошлину можно через приложение Сбербанка: Платежи — Государство — Суды — СУДЫ — Выбрать суд по региону (областные/районные). Вам понадобится указать код субъекта РФ, к которому относится ваш суд. Коды субъектов можно посмотреть здесь. Заплатить нужно 300 рублей. Больше информации -- ' + hlink(title='здесь', url='https://base.garant.ru/70175442/62a49222fc82ad8ec3f8d93568e1e7b8/') + '.'

