from .base import acceptingTextInput, acceptingWrappedKeyboardInput, stateInterface, justSendMessage, acceptingSubsequentTextInput
from .userInfo import acceptingUserInfo
from static.condition import conditions, document_parts
from utils.messaging import send_unsolicited_message
import static.phrases as p
import static.descriptions as d

import bot


class gettingUserConditions(acceptingWrappedKeyboardInput):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.info_type      = None
        self.cond_type      = None
        self.next           = None

    async def doGo(self, callback_data, new_user_info=None):
        if callback_data is None:
            return await super().doGo(callback_data, new_user_info)
        await self.toggleButton(callback_data, new_user_info)
        ret = await self.doGo(None)
        return ret

    def getPageOptions(self):
        page_options = list()
        for choise in conditions[self.cond_type]["choises"].keys():
            page_options.append( 
                (f"{self.getEmoji(choise)} {document_parts[choise]['description']}", 
                 choise) )
        return page_options

    def getPageDescription(self):
        try:
            return conditions[self.cond_type]["description"] 
        except:
            return document_parts[self.cond_type]["description"] 

    async def toggleButton(self, callback_data, new_user_info):
        cond_dict   = vars( self.context.user_condition )
        old_cond    = cond_dict[callback_data]
        await self.reject()

        cond_dict[callback_data] = not old_cond
        if not cond_dict[callback_data]:
            self.next = None
        else:
            self.next = self.nexts[callback_data]

        await self.manageDocParts(callback_data)

    async def reject(self):  
        await super().reject()
        cond_dict   = vars( self.context.user_condition )
        doc_dict    = vars( self.context.user_document )
        choises     = conditions[self.cond_type]["choises"]
        for choise in choises.keys():
            cond_dict[choise] = False
            tags = document_parts[choise]["tags"] 
            for tag in tags:
                doc_dict[tag] = False
             
    def getEmoji(self, choise):
        c = vars(self.context.user_condition)[choise]
        if c:
            return '\/'
        return ''

    async def manageDocParts(self, choise):
        doc_dict  = vars(self.context.user_document)
        cond_dict = vars(self.context.user_condition) 

        boolean   = cond_dict[choise]

        for tag in document_parts[choise]["tags"]:
            doc_dict[tag] = boolean

class acceptingMultiChoiseKeyboardInput(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type   = None
        self.next        = None 

    async def toggleButton(self, callback_data, new_user_info):
        cond_dict = vars( self.context.user_condition )
        cond_dict[callback_data] = not cond_dict[callback_data]
        await self.manageDocParts(callback_data)

class acceptingUserInfoSkipping(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)

    async def go_next(self):
        await self.finish()
        try:
            return await self.next.go()
        except:
            self.next = self.next(self.context, self.prev)
        return await self.next.go()

class acceptingUserInfoSkippingSubsequent(acceptingSubsequentTextInput):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)

    async def go_next(self):
        await self.finish()
        try:
            return await self.next.go()
        except:
            self.next = self.next(self.context, self.prev)
        return await self.next.go()


# ===== Concrete classes


# ----- Start
"""
class startUserCondition(justSendMessage):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next       = askingWhatHappened
        self.message    = d.pre_messages.pre_condition_message
"""
class startUserCondition(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "what_happened"
        self.next       = None 
        self.nexts      = {
          "single_day_summon"                   : askingSingleDayHearingDate,
          "ags_rejected"                        : askingAGSPleaDate,
        }


# ----- single_day_summon

class askingSingleDayHearingDate(acceptingUserInfoSkipping):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingSingleDateSummonDate
        self.data_prompt    = p.info["hearings"]["subtypes"]["single_day_hearing_date"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.single_day_hearing_date = thing

class askingSingleDateSummonDate(acceptingUserInfoSkipping):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = preDiseaseMessage
        self.data_prompt    = p.info["hearings"]["subtypes"]["single_day_summon_date"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.single_day_summon_date = thing

class preDiseaseMessage(justSendMessage):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next       = askingSingleDayDiseases
        self.message    = d.pre_messages.pre_diseases_message

class askingSingleDayDiseases(acceptingUserInfoSkippingSubsequent):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingSingleDayDeliveryMethod
        self.data_prompt    = p.info["hearings"]["subtypes"]["single_day_diseases"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.single_day_diseases = thing

    def stopInput(self, inp):
        if len(inp) <= 3:
            return True
        return False

class askingSingleDayDeliveryMethod(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "single_day_delivery_method"
        self.next       = None 
        self.nexts      = {
          "single_day_forcingly_delivered": askingForcinglyDeliveryDate,
          "single_day_came_themselves"    : singleDayAGS,
        }

class askingForcinglyDeliveryDate(acceptingUserInfoSkipping):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = singleDayAGS
        self.data_prompt    = p.info["hearings"]["subtypes"]["single_day_forcingly_delivered_date"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.single_day_forcingly_delivered_date = thing

class singleDayAGS(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "single_day_asked_for_ags"
        self.next       = None 
        self.nexts      = {
          "single_day_ags_asked"        : askingIfHaveAGSCopy,
          "single_day_ags_not_asked"    : endUserConditions,
        }

class askingIfHaveAGSCopy(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "single_day_ask_ags_copy"
        self.next       = None 
        self.nexts      = {
          "single_day_yes_ags_copy"     : endUserConditions,
          "single_day_no_ags_copy"      : endUserConditions,
        }


# ----- ags_rejected

class askingAGSPleaDate(acceptingUserInfoSkipping):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = comissionReactionOnPlea
        self.data_prompt    = p.info["documents"]["subtypes"]["ags_plea_date"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.ags_plea_date = thing

class comissionReactionOnPlea(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "comission_reaction_on_plea"
        self.next       = None 
        self.nexts      = {
          "summoned_to_the_hearing_and_rejected": askingComissionHearingDate,
          "plea_ignored"                        : askingIfWasSummonedAfterIgnore,
          "not_summoned_but_deadline_missed"    : askingIfWasSummonedAfterMissedDeadlines,
        }

# --- summoned_to_the_hearing_and_rejected

class askingComissionHearingDate(acceptingUserInfoSkipping):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingComissionViolations
        self.data_prompt    = p.info["hearings"]["subtypes"]["denial_hearing_date"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.denial_hearing_date = thing

class askingComissionViolations(acceptingMultiChoiseKeyboardInput):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type   = "comission_violations"
        self.next        = askingComsissionReasonForRejection 

    async def toggleButton(self, callback_data, new_user_info):
        await super().toggleButton(callback_data, new_user_info)
        if self.context.user_condition.witnesses_not_heard:
            self.next = askingForWitnessesNames
        else:
            self.next = askingComsissionReasonForRejection

class askingForWitnessesNames(acceptingUserInfoSkippingSubsequent):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        print("askingForWitnessesNames")
        self.next           = askingComsissionReasonForRejection
        self.data_prompt    = p.info["hearings"]["subtypes"]["witnesses"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.witnesses = thing

    def stopInput(self, inp):
        if len(inp) <= 3:
            return True
        return False

class askingComsissionReasonForRejection(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        print("askingComsissionReasonForRejection")
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "comission_reason_for_rejection"
        self.next       = None 
        self.nexts      = {
          "rejection_reason_not_believe"    : askingIfWasSummonedAfterHearing,
          "rejection_reason_deadline_missed": askingIfWasSummonedAfterHearing,
          "rejection_reason_no_reason"      : askingIfWasSummonedAfterHearing,
        }

class askingIfWasSummonedAfterHearing(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "summoned_after_hearing"
        self.next       = None
        self.nexts      = {
          "yes_summoned_after_hearing"   : askingSummonDate,
          "no_summoned_after_hearing"    : preAnnexesMessage,
        }

# --- plea_ignored

class askingIfWasSummonedAfterIgnore(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "summoned_after_plea_ignored"
        self.next       = None
        self.nexts      = {
          "yes_summoned_after_plea_ignored" : askingSummonDate,
          "no_summoned_after_plead_ingored" : preAnnexesMessage,
        }

# --- not_summoned_but_deadline_missed

class askingIfWasSummonedAfterMissedDeadlines(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "summoned_after_missed_deadlines"
        self.next       = None
        self.nexts      = {
          "yes_summoned_after_missed_deadlines" : askingSummonDate,
          "no_summoned_after_missed_deadlines"  : preAnnexesMessage,
        }

# --- general

class askingSummonDate(acceptingUserInfoSkipping):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = preAnnexesMessage
        self.data_prompt    = p.info["hearings"]["subtypes"]["comission_summon_date"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.comission_summon_date = thing

class preAnnexesMessage(justSendMessage):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next       = askingDocumentsForAnnexes
        self.message    = d.pre_messages.pre_annexes_message

class askingDocumentsForAnnexes(acceptingMultiChoiseKeyboardInput):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type   = "annexes"
        self.next        = endUserConditions  
        self.can_be_done = True
 
class endUserConditions(acceptingWrappedKeyboardInput):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.next = None

    async def go(self, *args, **kwargs):
        await super().go(*args, **kwargs)
        print("USER CONDITIONS ENDED!")
        return await self.done()

