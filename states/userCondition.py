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

    async def reject(self):  
        await super().reject()
        cond_dict   = vars( self.context.user_condition )
        choises     = conditions[self.cond_type]["choises"]
        for choise in choises.keys():
            cond_dict[choise] = False
             
    def getEmoji(self, choise):
        c = vars(self.context.user_condition)[choise]
        if c:
            return '\/'
        return ''

class acceptingMultiChoiseKeyboardInput(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type   = None
        self.next        = None 

    async def toggleButton(self, callback_data, new_user_info):
        cond_dict = vars( self.context.user_condition )
        cond_dict[callback_data] = not cond_dict[callback_data]

class insertDocPartsState(stateInterface):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = None
        self.next           = None

    async def go(self, *args, **kwargs):
        await super().go(*args, **kwargs)

        tags = document_parts[self.cond_type]["tags"] 
        parts_dict = vars( self.context.user_document )
        for tag in tags:
            parts_dict[tag] = True
        return await self.go_next()   

    async def reject(self):  
        await super().reject()
        tags = document_parts[self.cond_type]["tags"] 
        parts_dict = vars( self.context.user_condition )
        for tag in tags:
            parts_dict[tag] = False

    async def go_next(self):
        await self.finish()
        try:
            return await self.next.go()
        except:
            self.next = self.next(self.context, self.prev)
        return await self.next.go()
            
class insertDocPartsMultiChoiseState(stateInterface):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = None

    async def go(self, *args, **kwargs):
        await super().go(*args, **kwargs)
        doc_dict  = vars(self.context.user_document)
        cond_dict = vars(self.context.user_condition) 
        choises = conditions[self.cond_type]["choises"]
        for choise in choises:
            if not cond_dict[choise]:
                continue
            for tag in document_parts[choise]["tags"]:
                doc_dict[tag] = True
        return await self.go_next() 

    async def reject(self):  
        await super().reject()
        doc_dict = vars( self.context.user_document )
        choises = condition[self.cond_type]["choises"]
        for choise in choises:
            for tag in document_parts[choise]["tags"]:
                doc_dict[tag] = False

    async def go_next(self):
        await self.finish()
        try:
            return await self.next.go()
        except:
            self.next = self.next(self.context, self.prev)
        return await self.next.go()

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

class startUserCondition(justSendMessage):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next       = askingWhatHappened
        self.message    = d.pre_messages.pre_condition_message

class askingWhatHappened(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "what_happened"
        self.next       = None 
        self.nexts      = {
          "single_day_summon"                   : singleDaySummon,
          "ags_rejected"                        : agsRejected,
        }


# ----- single_day_summon

class singleDaySummon(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "single_day_summon"
        self.next           = askingSingleDayHearingDate

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
          "single_day_forcingly_delivered": forcinglyDelivered,
          "single_day_came_themselves"    : cameThemSelves,
        }

class forcinglyDelivered(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "single_day_forcingly_delivered"
        self.next           = askingForcinglyDeliveryDate

class cameThemSelves(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "single_day_came_themselves"
        self.next           = singleDayAGS

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
          "single_day_ags_asked"        : agsAsked,
          "single_day_ags_not_asked"    : agsNotAsked,
        }

class agsAsked(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "single_day_ags_asked"
        self.next           = endUserConditions

class agsNotAsked(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "single_day_ags_not_asked"
        self.next           = endUserConditions

# ----- ags_rejected

class agsRejected(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "ags_rejected"
        self.next           = askingAGSPleaDate

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
          "summoned_to_the_hearing_and_rejected": summonedAndRejectedBranch,
          "plea_ignored"                        : pleaIgnored,
          "not_summoned_but_deadline_missed"    : notSummonedButDeadlinesMissed,
        }

# --- summoned_to_the_hearing_and_rejected

class summonedAndRejectedBranch(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "summoned_to_the_hearing_and_rejected"
        self.next           = askingComissionHearingDate

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
        self.next        = insertingComissionViolationsDocParts 

    async def toggleButton(self, callback_data, new_user_info):
        await super().toggleButton(callback_data, new_user_info)
        if self.context.user_condition.witnesses_not_heard:
            self.next = askingForWitnessesNames
        else:
            self.next = insertingComissionViolationsDocParts

class askingForWitnessesNames(acceptingUserInfoSkippingSubsequent):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        print("askingForWitnessesNames")
        self.next           = insertingComissionViolationsDocParts
        self.data_prompt    = p.info["hearings"]["subtypes"]["witnesses"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.witnesses = thing

    def stopInput(self, inp):
        if len(inp) <= 3:
            return True
        return False

class insertingComissionViolationsDocParts(insertDocPartsMultiChoiseState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        print("insertingComissionViolationsDocParts")
        self.cond_type      = "comission_violations"
        self.next           = askingComsissionReasonForRejection

class askingComsissionReasonForRejection(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        print("askingComsissionReasonForRejection")
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "comission_reason_for_rejection"
        self.next       = None 
        self.nexts      = {
          "rejection_reason_not_believe"        : insertNotBelieveRejDocParts,
          "rejection_reason_deadline_missed"    : insertDeadlineRejDocParts,
          "rejection_reason_no_reason"          : insertNoReasonRejDocParts,
        }

class insertNotBelieveRejDocParts(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "rejection_reason_not_believe"
        self.next           = askingIfWasSummonedAfterHearing

class insertDeadlineRejDocParts(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "rejection_reason_deadline_missed"
        self.next           = askingIfWasSummonedAfterHearing

class insertNoReasonRejDocParts(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "rejection_reason_no_reason"
        self.next           = askingIfWasSummonedAfterHearing


# --- not_summoned_but_deadline_missed

class notSummonedButDeadlinesMissed(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "not_summoned_but_deadline_missed"
        self.next           = askingIfWasSummonedAfterMissedDeadlines


# --- plea_ignored

class pleaIgnored(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "plea_ignored"
        self.next           = askingIfWasSummonedAfterIgnore


# --- general


class askingIfWasSummonedAfterHearing(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "summoned_after_hearing"
        self.next       = None
        self.nexts      = {
          "yes_summoned_after_hearing"   : yesSummonedAfterHearing,
          "no_summoned_after_hearing"    : noSummonedAfterHearing,
        }

class yesSummonedAfterHearing(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "yes_summoned_after_hearing"
        self.next           = askingSummonDate

class noSummonedAfterHearing(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "no_summoned_after_hearing"
        self.next           = preAnnexesMessage

class askingIfWasSummonedAfterIgnore(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "summoned_after_plea_ignored"
        self.next       = None
        self.nexts      = {
          "yes_summoned_after_plea_ignored" : yesSummonedPleaIgnored,
          "no_summoned_after_plead_ingored" : noSummonedPleaIgnored,
        }

class yesSummonedPleaIgnored(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "yes_summoned_after_plea_ignored"
        self.next           = askingSummonDate

class noSummonedPleaIgnored(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "no_summoned_after_plead_ingored"
        self.next           = preAnnexesMessage

class askingIfWasSummonedAfterMissedDeadlines(gettingUserConditions):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.cond_type  = "summoned_after_missed_deadlines"
        self.next       = None
        self.nexts      = {
          "yes_summoned_after_missed_deadlines" : yesSummonedDeadlinesMissed,
          "no_summoned_after_missed_deadlines"  : noSummonedDeadlinesMisseded,
        }

class yesSummonedDeadlinesMissed(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "yes_summoned_after_missed_deadlines"
        self.next           = askingSummonDate

class noSummonedDeadlinesMisseded(insertDocPartsState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "no_summoned_after_missed_deadlines"
        self.next           = preAnnexesMessage


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
        self.next        = saveAnnexesChoises  
        self.can_be_done = True
 
class saveAnnexesChoises(insertDocPartsMultiChoiseState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.cond_type      = "annexes"
        self.next           = endUserConditions

class endUserConditions(acceptingWrappedKeyboardInput):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.next = None

    async def go(self, *args, **kwargs):
        await super().go(*args, **kwargs)
        print("USER CONDITIONS ENDED!")
        return await self.done()

