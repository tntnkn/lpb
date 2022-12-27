
class userSession():
    def __init__(self, tg_id):
        self.from_id        = tg_id
        self.current_state  = None   
        self.user_info      = userInfo()
        self.user_condition = userCondition()
        self.user_document  = userDocument()
        self.message        = None
        self.ms_text        = None
        self.cb_query       = None
        self.cb_data        = None
        self.left_messages  = list()

class sessionInfo():
    def __init__(self, session):
        self.session    = session
        self.locked     = False
        self.last_action_time = 0  

from static.phrases import info as i
class userInfo():
    def __init__(self):
        self.court_name             = \
            i["court"]["subtypes"]["name"]["description"]
        self.user_name              = \
            i["user"]["subtypes"]["name"]["description"]
        self.user_birthdate         = \
            i["user"]["subtypes"]["birthdate"]["description"]
        self.user_birthplace        = \
            i["user"]["subtypes"]["birthplace"]["description"]
        self.user_address           = \
            i["user"]["subtypes"]["address"]["description"]
        self.user_phone             = \
            i["user"]["subtypes"]["phone"]["description"]
        self.user_email             = \
            i["user"]["subtypes"]["email"]["description"]
        self.ags_plea_date          = \
            i["documents"]["subtypes"]["ags_plea_date"]["description"]
        self.denial_hearing_date    = \
            i["hearings"]["subtypes"]["denial_hearing_date"]["description"]
        self.witnesses              = \
            i["hearings"]["subtypes"]["witnesses"]["description"]
        self.comission_summon_date  = \
            i["hearings"]["subtypes"]["comission_summon_date"]["description"]
        self.comissar_name          = \
            i["comissar"]["subtypes"]["name"]["description"]
        self.comissar_address       = \
            i["comissar"]["subtypes"]["address"]["description"]
        self.comissariat_region     = \
            i["comissariat"]["subtypes"]["region"]["description"]
        self.comissariat_address    = \
            i["comissariat"]["subtypes"]["address"]["description"]
        self.comission_region       = \
            i["comission"]["subtypes"]["region"]["description"]
        self.comission_address      = \
            i["comission"]["subtypes"]["address"]["description"]

class userCondition():
    def __init__(self):
        self.summoned_to_the_hearing_and_rejected   = False
        self.plea_ignored                           = False
        self.not_summoned_but_deadline_missed       = False
        self.witnesses_not_heard                    = False
        self.no_quorum                              = False
        self.less_voices                            = False
        self.rejection_reason_not_believe           = False
        self.rejection_reason_deadline_missed       = False
        self.rejection_reason_no_reason             = False
        self.yes_summoned_after_hearing             = False
        self.no_summoned_after_hearing              = False
        self.yes_summoned_plea_ignored              = False
        self.protocol_copy                          = False
        self.comission_decision                     = False
        self.characteristics                        = False
        self.bio                                    = False
        self.comissariat_response                   = False
        self.summon_copy                            = False

class userDocument():
    def __init__(self):
        self.fact_hearing_happened                  = False
        self.fact_witnesses_not_heard               = False
        self.fact_no_quorum                         = False
        self.fact_less_votes                        = False
        self.fact_deadline_missed                   = False
        self.fact_incaction                         = False
        self.module_witnesses_not_heard             = False
        self.module_no_quorum                       = False
        self.module_less_votes                      = False
        self.module_no_beliefes                     = False
        self.module_deadline_missed                 = False
        self.module_no_motivation                   = False
        self.module_deadline_missed                 = False
        self.module_ignore                          = False
        self.block_cancel_illegal_decision          = False
        self.block_illegal_summon                   = False
        self.petition_forbid_summon                 = False
        self.petition_provide_denial                = False
        self.petition_provide_personal_case         = False
        self.petition_provide_protocol_copy         = False
        self.plea_cancel_denial                     = False
        self.plea_cancel_summon                     = False
        self.plea_incaction                         = False
        self.plea_demand_rehearing                  = False
        self.annex_protocol_copy                    = False
        self.annex_comission_decision               = False
        self.annex_characteristics                  = False
        self.annex_bio                              = False
        self.annex_comissariat_response             = False
        self.annex_summon_copy                      = False
        self.title_inaction                         = False
        self.party_inaction                         = False

