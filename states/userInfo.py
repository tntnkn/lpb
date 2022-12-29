from .base import acceptingTextInput
import static.phrases as p


class acceptingUserInfo(acceptingTextInput):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)

    async def doCheckInput(self, inp):
        return True


class askingName(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next            = askingBirthdate
        self.data_prompt     = p.info["user"]["subtypes"]["name"]["prompt"] 

    async def doSaveInput(self, inp):
        self.context.user_info.user_name = inp

class askingBirthdate(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingBirthplace
        self.data_prompt    = p.info["user"]["subtypes"]["birthdate"]["prompt"] 
    async def doSaveInput(self, thing):
        self.context.user_info.user_birthdate = thing

class askingBirthplace(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingAddress
        self.data_prompt    = p.info["user"]["subtypes"]["birthplace"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.user_birthplace = thing

class askingAddress(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingPhone
        self.data_prompt    = p.info["user"]["subtypes"]["address"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.user_address = thing

class askingPhone(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingEmail
        self.data_prompt    = p.info["user"]["subtypes"]["phone"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.user_phone = thing

class askingEmail(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingCourt
        self.data_prompt    = p.info["user"]["subtypes"]["email"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.user_email = thing

class askingCourt(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingSummonDate
        self.data_prompt    = p.info["court"]["subtypes"]["name"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.court_name = thing

class askingSummonDate(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingAGSPleaDate
        self.data_prompt    = p.info["documents"]["subtypes"]["summon_date"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.summon_date = thing

class askingAGSPleaDate(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingDenialDetails
        self.data_prompt    = p.info["documents"]["subtypes"]["ags_plea_date"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.ags_plea_date = thing

class askingDenialDetails(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingComissarName
        self.data_prompt    = p.info["documents"]["subtypes"]["denial_detail"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.denial_detail = thing

class askingComissarName(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingComissarAddress
        self.data_prompt    = p.info["comissar"]["subtypes"]["name"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.comissar_name = thing

class askingComissarAddress(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingComissariatName
        self.data_prompt    = p.info["comissar"]["subtypes"]["address"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.comissar_address = thing

class askingComissariatName(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingComissariatAddress
        self.data_prompt    = p.info["comissariat"]["subtypes"]["name"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.comissariat_name = thing

class askingComissariatAddress(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingComissionRegion
        self.data_prompt    = p.info["comissariat"]["subtypes"]["address"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.comissariat_address = thing

class askingComissionRegion(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = askingComissionAddress
        self.data_prompt    = p.info["comission"]["subtypes"]["region"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.comission_region = thing

class askingComissionAddress(acceptingUserInfo):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next           = None
        self.data_prompt    = p.info["comission"]["subtypes"]["address"]["prompt"] 

    async def doSaveInput(self, thing):
        self.context.user_info.comission_address = thing

