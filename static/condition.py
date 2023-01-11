from enum import Enum, unique, auto
from .descriptions import conditions as c

@unique
class selectTypes(Enum):
    singleChoise    = auto()
    multiChoise     = auto()


conditions = {
    "what_happened"     : {
        "select"        : selectTypes.singleChoise,
        "description"   : c.what_happened,
        "choises"       : {
            "ags_rejected"  : {
            },
            "single_day_summon" : {
            },
        },
    },
    "comission_reaction_on_plea"     : {
        "select"        : selectTypes.singleChoise,
        "description"   : c.comission_reaction_on_plea,
        "choises"       : {
            "summoned_to_the_hearing_and_rejected"  : {
            },
            "plea_ignored"                          : {
            },
            "not_summoned_but_deadline_missed"      : {
            },
        },
    },
    "comission_violations"     : {
        "select"        : selectTypes.multiChoise,
        "description"   : c.comission_violations,
        "choises"       : {
            "witnesses_not_heard"  : {
            },
            "no_quorum"            : {
            },
            "less_voices"          : {
            },
        },
    },
    "comission_reason_for_rejection"     : {
        "select"        : selectTypes.singleChoise,
        "description"   : c.comission_reason_for_rejection,
        "choises"       : {
            "rejection_reason_not_believe"     : {
            },
            "rejection_reason_deadline_missed" : {
            },
            "rejection_reason_no_reason"       : {
            },
        }
    },
    "summoned_after_hearing"     : {
        "select"        : selectTypes.singleChoise,
        "description"   : c.summoned_after_hearing,
        "choises"       : {
            "yes_summoned_after_hearing"     : {
            },
            "no_summoned_after_hearing"     : {
            },
        }
    },
    "summoned_after_plea_ignored"     : {
        "select"        : selectTypes.singleChoise,
        "description"   : c.summoned_after_plea_ignored,
        "choises"       : {
            "yes_summoned_after_plea_ignored"     : {
            },
            "no_summoned_after_plead_ingored"     : {
            },
        }
    },
    "summoned_after_missed_deadlines"     : {
        "select"        : selectTypes.singleChoise,
        "description"   : c.summoned_after_missed_deadlines,
        "choises"       : {
            "yes_summoned_after_missed_deadlines"     : {
            },
            "no_summoned_after_missed_deadlines"     : {
            },
        }
    },
    "annexes"     : {
        "select"        : selectTypes.multiChoise,
        "description"   : c.annexes,
        "choises"       : {
            "protocol_copy"     : {
            },
            "comission_decision" : {
            },
            "characteristics"       : {
            },
            "bio"     : {
            },
            "comissariat_response" : {
            },
            "summon_copy"       : {
            },
        }
    },
    "single_day_delivery_method"     : {
        "select"        : selectTypes.singleChoise,
        "description"   : c.single_day_delivery_method,
        "choises"       : {
            "single_day_forcingly_delivered"     : {
            },
            "single_day_came_themselves"     : {
            },
        }
    },
    "single_day_asked_for_ags"     : {
        "select"        : selectTypes.singleChoise,
        "description"   : c.single_day_asked_for_ags,
        "choises"       : {
            "single_day_ags_asked"     : {
            },
            "single_day_ags_not_asked"     : {
            },
        }
    },
    "single_day_ask_ags_copy"     : {
        "select"        : selectTypes.singleChoise,
        "description"   : c.single_day_ask_ags_copy,
        "choises"       : {
            "single_day_yes_ags_copy"     : {
            },
            "single_day_no_ags_copy"     : {
            },
        }
    },
}

document_parts = {
    "ags_rejected"  : {
        "description"   : c.ags_rejected,
        "tags"          : [
            ]
    },
    "single_day_summon"  : {
        "description"   : c.single_day_summon,
        "tags"          : [
            ]
    },
    "summoned_to_the_hearing_and_rejected"  : {
        "description"   : c.summoned_to_the_hearing_and_rejected,
        "tags"          : [
                'petition_provide_denial',
                'petition_provide_personal_case',
                'fact_hearing_happened',
                'plea_cancel_denial',
                'plea_demand_rehearing',
            ]
    },
    "witnesses_not_heard"     : {
        "description"   : c.witnesses_not_heard,
        "tags"          : [
                'fact_witnesses_not_heard',
                'module_witnesses_not_heard',
            ]
    },
    "no_quorum"     : {
        "description"   : c.no_quorum,
        "tags"          : [
                'fact_no_quorum',
                'module_no_quorum',
            ]
    },
    "less_voices"     : {
        "description"   : c.less_voices,
        "tags"          : [
                'fact_less_votes',
                'module_less_votes',
            ]
    },
    "rejection_reason_not_believe"     : {
        "description"   : c.rejection_reason_not_believe,
        "tags"          : [
                'module_no_beliefes',
            ]
    },
    "rejection_reason_deadline_missed": {
        "description"   : c.rejection_reason_deadline_missed,
        "tags"          : [
                'module_deadline_missed_rejection',
            ]
    },
    "rejection_reason_no_reason"     : {
        "description"   : c.rejection_reason_no_reason,
        "tags"          : [
                'module_no_motivation',
            ]
    },
    "protocol_copy"     : {
        "description"   : c.protocol_copy,
        "tags"          : [
                'annex_protocol_copy',
            ]
    },
    "comission_decision"     : {
        "description"   : c.comission_decision,
        "tags"          : [
                'annex_comission_decision',
            ]
    },
    "characteristics"     : {
        "description"   : c.characteristics,
        "tags"          : [
                'annex_characteristics',
            ]
    },
    "bio"     : {
        "description"   : c.bio,
        "tags"          : [
                'annex_bio',
            ]
    },
    "comissariat_response"     : {
        "description"   : c.comissariat_response,
        "tags"          : [
                'annex_comissariat_response',
            ]
    },
    "summon_copy"     : {
        "description"   : c.summon_copy,
        "tags"          : [
                'annex_summon_copy',
            ]
    },

    "yes_summoned_after_hearing"     : {
        "description"   : c.yes_summoned_after_hearing,
        "tags"          : [
            "plea_cancel_summon",
            "block_illegal_summon",
            "fact_illegal_summon",
            ]
    },
    "no_summoned_after_hearing"     : {
        "description"   : c.no_summoned_after_hearing,
        "tags"          : [
            ]
    },
    "yes_summoned_after_plea_ignored"     : {
        "description"   : c.yes_summoned_after_plea_ignored,
        "tags"          : [
            "plea_cancel_summon",
            "block_illegal_summon",
            "block_cancel_illegal_decision",
            "fact_illegal_summon",
            ]
    },
    "no_summoned_after_plead_ingored"     : {
        "description"   : c.no_summoned_after_plead_ingored,
        "tags"          : [
            "petition_forbid_summon",
            ]
    },
    "yes_summoned_after_missed_deadlines"     : {
        "description"   : c.yes_summoned_after_missed_deadlines,
        "tags"          : [
            "plea_cancel_summon",
            "block_illegal_summon",
            "fact_illegal_summon",
            ]
    },
    "no_summoned_after_missed_deadlines"     : {
        "description"   : c.no_summoned_after_missed_deadlines,
        "tags"          : [
            "petition_forbid_summon",
            ]
    },

    "plea_ignored"     : {
        "description"   : c.plea_ignored,
        "tags"          : [
            "module_ignore",
            "plea_inaction",
            "petition_provide_personal_case",
            "fact_incaction",
            'party_inaction',
            'title_inaction',
            ]
    },

    "not_summoned_but_deadline_missed"  : {
        "description"   : c.not_summoned_but_deadline_missed,
        "tags"          : [
                'module_deadline_missed',
                'plea_inaction',
                'petition_provide_personal_case',
                'fact_incaction',
                'fact_deadline_missed',
                'party_inaction',
                'title_inaction',
            ]
    },

    "single_day_forcingly_delivered"  : {
        "description"   : c.single_day_forcingly_delivered,
        "tags"          : [
                'fact_single_day_forcingly_delivered',
            ]
    },
    "single_day_came_themselves"  : {
        "description"   : c.single_day_came_themselves,
        "tags"          : [
            ]
    },

    "single_day_ags_asked"  : {
        "description"   : c.single_day_ags_asked,
        "tags"          : [
                'plea_single_day_asked_for_ags',
                'fact_single_day_asked_for_ags',
                'module_single_day_asked_for_ags',
                'block_single_day_asked_for_ags',
            ]
    },
    "single_day_ags_not_asked"  : {
        "description"   : c.single_day_ags_not_asked,
        "tags"          : [
            ]
    },
    "single_day_yes_ags_copy"  : {
        "description"   : c.single_day_yes_ags_copy,
        "tags"          : [
                'annex_single_day_ags_plea_copy',
            ]
    },
    "single_day_no_ags_copy"  : {
        "description"   : c.single_day_no_ags_copy,
        "tags"          : [
            ]
    },
}

