from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools



author = 'Your name here'

doc = """
Your app description
"""


# variable catalogue
# ==================

# treatment := the randomly assigned treatment
#   values:
#       TDlow --> D plays trust game with R under low incentives
#       TDhigh --> D plays trust game with R under high incentives
#       TAlow --> A plays trust game with R under low incentives
#       TAhigh --> A plays trust game with R under high incentives


class Constants(BaseConstants):
    name_in_url = 'HoeKorStre2017'

    # set the group size
    players_per_group = 3

    # set number of rounds
    num_rounds = 1


class Subsession(BaseSubsession):

    def creating_session(self):
        # group groups randomly at the beginning of the round/subsession
        self.group_randomly()

        # randomize groups to treatments in a balanced way
        treatments = itertools.cycle(['TDlow', 'TDhigh', 'TAlow', 'TAhigh'])
        for group in self.get_groups():
            group.treatment = next(treatments)


class Group(BaseGroup):

    treatment = models.CharField()



class Player(BasePlayer):

    # assign player roles
    # (id_in_group has been randomized above)
    def role(self):
        if self.id_in_group == 1:
            return 'R'
        elif self.id_in_group == 2:
            return 'A'
        else:
            return 'D'