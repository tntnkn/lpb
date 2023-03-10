import static.prompts       as p
import static.descriptions  as d


info = {
    "court": {
        "description"   : d.court,
        "subtypes"      : {
            "name": {
                "prompt"        : p.court_name,
                "description"   : d.court_name,
                "tag"           : "court_name",
            },
        },
    },
    "user": {
        "description"   : d.user,
        "subtypes"      : {
            "name": {
                "prompt"        : p.user_name,
                "description"   : d.user_name,
                "tag"           : "user_name",
            },
            "birthdate": {
                "prompt"        : p.user_birthdate,
                "description"   : d.user_birthdate,
                "tag"           : "user_birthdate",
            },
            "birthplace": {
                "prompt"        : p.user_birthplace,
                "description"   : d.user_birthplace,
                "tag"           : "user_birthplace",
            },
            "address": {
                "prompt"        : p.user_address,
                "description"   : d.user_address,
                "tag"           : "user_address",
            },
            "phone": {
                "prompt"        : p.user_phone,
                "description"   : d.user_phone,
                "tag"           : "user_phone",
            },
            "email": {
                "prompt"        : p.user_email,
                "description"   : d.user_email,
                "tag"           : "user_email",
            },
        },
    },
    "documents": {
        "description"   : d.documents,
        "subtypes"      : {
            "ags_plea_date": {
                "prompt"        : p.ags_plea_date,
                "description"   : d.ags_plea_date,
                "tag"           : "ags_plea_date",
            },
        },
    },
    "hearings": {
        "description"   : d.hearings,
        "subtypes"      : {
            "denial_hearing_date": {
                "prompt"        : p.denial_hearing_date,
                "description"   : d.denial_hearing_date,
                "tag"           : "denial_hearing_date",
            },
            "single_day_hearing_date": {
                "prompt"        : p.single_day_hearing_date,
                "description"   : d.single_day_hearing_date,
                "tag"           : "single_day_hearing_date",
            },
            "single_day_summon_date": {
                "prompt"        : p.single_day_summon_date,
                "description"   : d.single_day_summon_date,
                "tag"           : "single_day_summon_date",
            },
            "single_day_diseases": {
                "prompt"        : p.single_day_diseases,
                "description"   : d.single_day_diseases,
                "tag"           : "single_day_diseases",
            },
            "single_day_forcingly_delivered_date": {
                "prompt"        : p.single_day_forcingly_delivered_date,
                "description"   : d.single_day_forcingly_delivered_date,
                "tag"           : "single_day_forcingly_delivered_date",
            },
            "witnesses": {
                "prompt"        : p.witnesses,
                "description"   : d.witnesses,
                "tag"           : "witnesses",
            },
            "comission_summon_date": {
                "prompt"        : p.comission_summon_date,
                "description"   : d.comission_summon_date,
                "tag"           : "comission_summon_date",
            },
        },
    },
    "comissar": {
        "description"   : d.comissar,
        "subtypes"      : {
            "name": {
                "prompt"        : p.comissar_name,
                "description"   : d.comissar_name,
                "tag"           : "comissar_name",
            },
            "address": {
                "prompt"        : p.comissar_address,
                "description"   : d.comissar_address,
                "tag"           : "comissar_address",
            },
        },
    },
    "comissariat": {
        "description"   : d.comissariat,
        "subtypes"      : {
            "name": {
                "prompt"        : p.comissariat_name,
                "description"   : d.comissariat_name,
                "tag"           : "comissariat_name",
            },
            "address": {
                "prompt"        : p.comissariat_address,
                "description"   : d.comissariat_address,
                "tag"           : "comissariat_address",
            },
        },
    },
    "comission": {
        "description"   : d.comission,
        "subtypes"      : {
            "name": {
                "prompt"        : p.comission_name,
                "description"   : d.comission_name,
                "tag"           : "comission_name",
            },
            "address": {
                "prompt"        : p.comission_address,
                "description"   : d.comission_address,
                "tag"           : "comission_address",
            },
        },
    },
}

