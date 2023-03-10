from aiogram.utils.markdown import link, hlink

guide_court     = 'Давайте определимся с подсудностью, то есть судом, в который подаём иск.\n\nИск подаётся в городской или районный суд (а не в мировой или областной/краевой).  В нашем случае уполномоченный суд определяется по месту проживания истца. Если человека забрали из хостела, территориальная подсудность будет определяться по адресу хостела. Чтобы определить суд, предлагаем использовать ' + hlink(title='базу данных', url='https://sudrf.ru/index.php?id=300#podsud ') + ' судов, которая работает на базе сайте Верховного суда РФ. Однако иногда эта база данных «лежит» и может быть недоступна по VPN. В этом случае вам придётся самостоятельно определить суд. На сайтах судов посмотрите раздел «территориальная подсудность». Если ваш адрес относится к территориальной подсудности суда, то это и есть суд, куда будете подавать исковое. Если вашего адреса нет, значит, надо искать другой суд.'

guide_how_to_sue    = 'Гайд вышел объёмным -- нажмите ' + hlink(title='сюда', url='https://telegra.ph/gajd-po-podache-iska-12-30') + ' , чтобы его прочитать.'

guide_quorum    = 'Гайд вышел объёмным -- нажмите ' + hlink(title='сюда',
url='https://telegra.ph/kvorum-12-30') + ' , чтобы его прочитать.'

guide_comission = 'Укажите полное название комиссии. Призывные комиссии создаются в каждом муниципальном образовании (МО) решением руководителя региона. То есть для определения Вашей призывной комиссии Вам нужно определить в каком МО Вы проживаете или находились, когда Вас забрали в военкомат/доставили повестку. Зайдите ' + hlink(title='на сайт', url='https://app.raionpoadresu.ru') + ', зарегистрируйтесь, введите в поиск адрес места, куда Вам доставили повестку или откуда Вас насильно забрали в военкомат. Сайт выдаст название МО, например "г. Тверь". Вставьте это МО в название комиссии, чтобы получилось “Призывная комиссия "МО". Например, Призывная комиссия "г. Тверь".'

guide_comissariat = 'Информацию о военном комиссариате можно найти в повестке.  Но если с этим проблемы, то о том, как определить комиссариат, читайте ' + hlink(title='здесь', url='https://docs.google.com/document/d/1Bi0Q0sntboS4McmegvQfUpXIrGKOj6C0M_IK2ML2aL8/edit#)') + '. Пример названия комиссариата: Военный комиссариат Ново-Савиновского и Авиастроительного района Республики Татарстан».'

guide_fee       = 'Как оплатить пошлину? \n\n Оплатить пошлину можно через приложение Сбербанка: Платежи — Государство — Суды — СУДЫ — Выбрать суд по региону (областные/районные). Вам понадобится указать код субъекта РФ, к которому относится ваш суд. Коды субъектов можно посмотреть здесь. Заплатить нужно 300 рублей. Больше информации -- ' + hlink(title='здесь', url='https://base.garant.ru/70175442/62a49222fc82ad8ec3f8d93568e1e7b8/') + '.'

