from enum import Enum, unique, auto
from .descriptions import conditions as c

@unique
class selectTypes(Enum):
    singleChoise    = auto()
    multiChoise     = auto()


conditions = {
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
    "summoned_plea_ignored"     : {
        "select"        : selectTypes.singleChoise,
        "description"   : c.summoned_plea_ignored,
        "choises"       : {
            "yes_summoned_plea_ignored"     : {
            },
            "no_summoned_after_hearing"     : {
            },
        }
    },
    "annexes"     : {
        "select"        : selectTypes.multiChoise,
        "description"   : c.annexes,
        "choises"       : {
            "annex_protocol_copy"     : {
            },
            "annex_comission_decision" : {
            },
            "annex_characteristics"       : {
            },
            "annex_bio"     : {
            },
            "annex_comissariat_response" : {
            },
            "annex_summon_copy"       : {
            },
        }
    },
}

document_parts = {
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
                'module_deadline_missed',
            ]
    },
    "rejection_reason_no_reason"     : {
        "description"   : c.rejection_reason_no_reason,
        "tags"          : [
                'module_no_motivation',
            ]
    },
    "annex_protocol_copy"     : {
        "description"   : c.protocol_copy,
        "tags"          : [
                'annex_protocol_copy',
            ]
    },
    "annex_comission_decision"     : {
        "description"   : c.comission_decision,
        "tags"          : [
                'annex_comission_decision',
            ]
    },
    "annex_characteristics"     : {
        "description"   : c.characteristics,
        "tags"          : [
                'annex_characteristics',
            ]
    },
    "annex_bio"     : {
        "description"   : c.bio,
        "tags"          : [
                'annex_bio',
            ]
    },
    "annex_comissariat_response"     : {
        "description"   : c.comissariat_response,
        "tags"          : [
                'annex_comissariat_response',
            ]
    },
    "annex_summon_copy"     : {
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
            ]
    },
    "no_summoned_after_hearing"     : {
        "description"   : c.no_summoned_after_hearing,
        "tags"          : [
            "petition_forbid_summon"
            ]
    },

    "plea_ignored"     : {
        "description"   : c.plea_ignored,
        "tags"          : [
            "module_deadline_missed",
            "fact_incaction",
            "plea_incaction",
            "petition_provide_personal_case",
            ]
    },

    "yes_summoned_plea_ignored"     : {
        "description"   : c.yes_summoned_plea_ignored,
        "tags"          : [
            "plea_cancel_summon",
            "block_illegal_summon",
            "block_cancel_illegal_decision",
            ]
    },

    "not_summoned_but_deadline_missed"  : {
        "description"   : c.not_summoned_but_deadline_missed,
        "tags"          : [
                'module_deadline_missed',
                'plea_incaction',
                'petition_provide_personal_case',
                'fact_incaction',
                'party_inaction',
                'title_inaction',
            ]
    },

}

