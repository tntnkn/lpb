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
            "region": {
                "prompt"        : p.comissariat_region,
                "description"   : d.comissariat_region,
                "tag"           : "comissariat_region",
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
            "region": {
                "prompt"        : p.comission_region,
                "description"   : d.comission_region,
                "tag"           : "comission_region",
            },
            "address": {
                "prompt"        : p.comission_address,
                "description"   : d.comission_address,
                "tag"           : "comission_address",
            },
        },
    },
}

