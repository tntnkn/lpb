from .misc import info_command_text

start       = '/start'
help        = '/help'
info        = '/info'
guides      = '/guides'
court       = '/guide_court'
how_to_sue  = '/guide_how_to_sue'
quorum      = '/guide_quorum'
fee         = '/guide_fee'
comission   = '/guide_comission' 
comissariat = '/guide_comissariat'


class desc():
    start       = 'начать делать иск'
    help        = 'получить список команд'
    info        = 'прочитать детальное описание работы бота'
    guides      = 'посмотреть список гайдов'
    court       = 'получить гайд по определению суда'
    how_to_sue  = 'получить гайд по подаче иска'
    quorum      = 'получить гайд по определению кворума призывной комиссии'
    fee         = 'получить гайд по госпошлине'
    comission   = 'получить гайд по определению названия комиссии' 
    comissariat = 'получить гайд по определению названия комиссариата'

class mess():
    help = f"Нажмите {start}, чтобы {desc.start}, {info}, чтобы {desc.info} или {guides}, чтобы {desc.guides}. Если возникла проблема, то напишите нашим друзьям -- @agsnowarbot."

    guides      = f"Мы сделали для Вас следующие гайды:\n  * {court} - {desc.court},\n  * {how_to_sue} - {desc.how_to_sue},\n  * {quorum} - {desc.quorum},\n  * {fee} - {desc.fee},\n  * {comission} - {desc.comission},\n  * {comissariat} - {desc.comissariat}.\n"

    info  = info_command_text 

