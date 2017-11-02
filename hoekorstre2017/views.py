from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class welcome(Page):

    pass


class instructionsTDhighR(Page):

    # def is_displayed(self):
    #    return self.group.treatment == 'TDhigh'


    # double conditions do not work yet!
    def is_displayed(self):
        return self.group.treatment == 'TDhigh'



class instructionsTDlowD(Page):

    def is_displayed(self):
        return self.group.treatment == 'TDlow'


# class instructions_D_TDlow(Page):
#    def is_displayed(self):
#        return self.player.role == 'D' and self.group.treatment == 'TDlow'
#
#    form_model = models.Player


# class instructions_R_TDhigh(Page):
#    def is_displayed(self):
#        return self.player.role == 'R' and self.group.treatment == 'TDhigh'
#
#     form_model = models.Player


page_sequence = [
    welcome,
    instructionsTDhighR,
    instructionsTDlowD
]
