from .base import acceptingFormFillingInput
import static.phrases as p
import states.userInfo as userInfo


class fillingUserInfoForm(acceptingFormFillingInput):
    def __init__(self, context, prev=None, keyboard_mes_id=None, 
                 require_user_to_complete_page=True):
        super().__init__(context, prev, keyboard_mes_id, 
                         require_user_to_complete_page)
        self.next       = None
        self.info_type  = None
        self.user_info  = context.user_info
        if self.prev:
            self.require_user_to_complete_page = \
                    self.prev.require_user_to_complete_page

    def getPageOptions(self):
        page_options = list()
        for st in p.info[self.info_type]["subtypes"].values():
            page_options.append(
                ( vars(self.context.user_info)[ st["tag"] ], st["tag"]) )
        return page_options

    def getPageDescription(self):
        return p.info[self.info_type]["description"] 

    def doSetCorrectionPrompt(self, callback_data):
        self.current_state.next = None


class field():
    def __init__(self, state):
        self.state  = state
        self.filled = False

class courtCheckup(fillingUserInfoForm):
    def __init__(self, context, prev=None, keyboard_mes_id=None, 
                 require_user_to_complete_page=True):
        super().__init__(context, prev, keyboard_mes_id, 
                         require_user_to_complete_page)
        self.next       = userCheckup(context, self)
        self.info_type  = "court"
        self.fields     = {
            "court_name"     : field(userInfo.askingCourt) 
        }

class userCheckup(fillingUserInfoForm):
    def __init__(self, context, prev=None, keyboard_mes_id=None, 
                 require_user_to_complete_page=True):
        super().__init__(context, prev, keyboard_mes_id, 
                         require_user_to_complete_page)
        self.next       = comissariatCheckup(context, self)
        self.info_type  = "user"
        self.fields     = {
            "user_name"         : field(userInfo.askingName),
            "user_birthdate"    : field(userInfo.askingBirthdate),
            "user_birthplace"   : field(userInfo.askingBirthplace),
            "user_address"      : field(userInfo.askingAddress),
            "user_phone"        : field(userInfo.askingPhone),
            "user_email"        : field(userInfo.askingEmail),
        }

# the next one is temporarily abandoned.
class documentsCheckup(fillingUserInfoForm):
    def __init__(self, context, prev=None, keyboard_mes_id=None, 
                 require_user_to_complete_page=True):
        super().__init__(context, prev, keyboard_mes_id, 
                         require_user_to_complete_page)
        self.next       = comissariatCheckup(context, self)
        self.info_type  = "documents"
        self.fields     = {
            "ags_plea_date"     : field(userInfo.askingAGSPleaDate),
        }

class comissariatCheckup(fillingUserInfoForm):
    def __init__(self, context, prev=None, keyboard_mes_id=None, 
                 require_user_to_complete_page=True):
        super().__init__(context, prev, keyboard_mes_id, 
                         require_user_to_complete_page)
        self.next       = comissionCheckup(context, self)
        self.info_type  = "comissariat"
        self.fields     = {
            "comissariat_name"     : field(userInfo.askingComissariatName),
            "comissariat_address"  : field(userInfo.askingComissariatAddress),
        }

class comissionCheckup(fillingUserInfoForm):
    def __init__(self, context, prev=None, keyboard_mes_id=None, 
                 require_user_to_complete_page=True):
        super().__init__(context, prev, keyboard_mes_id, 
                         require_user_to_complete_page)
        self.next        = endOfUserCheckup(context, self) 
        self.can_be_done = True
        self.info_type   = "comission"
        self.fields      = {
            "comission_name"        : field(userInfo.askingComissionName),
            "comission_address"     : field(userInfo.askingComissionAddress),
        }

class endOfUserCheckup(fillingUserInfoForm):
    def __init__(self, context, prev=None, keyboard_mes_id=None, 
                 require_user_to_complete_page=True):
        super().__init__(context, prev, keyboard_mes_id, 
                         require_user_to_complete_page)

    async def go(self, *args, **kwargs):
        return await self.done()

    
