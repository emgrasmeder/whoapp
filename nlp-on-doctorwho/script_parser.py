from __future__ import print_function

'''
    script_parser.py is intended to do the preliminary cleaning 
    of the items in the raw-scripts folder. I'm not sure how the 
    database should be structured for NLP projects, but in any case
    I'd like to remove stage directions and speaker attribution.
'''

import nltk
import re
class Analyzer():
    def __init__(self):
        '''
        '''
        print("Instantiating Analyzer class")

        self.cast = []
        self.sentences = nltk.Text(
                    nltk.sent_tokenize(
                    open('../resources/raw-scripts/34_1__Deep_Breath.txt',"r").read()))

    def isolate_speaker(self):
        pass

    def isolate_stage_commands(self):
        '''
            First blush of filtering out parenthetical data about what
            characters are doing. Problematically, this still filters out:
            'DOCTOR: (to dinosaur) I'm not flirting, by the way.'
        '''
        stage_commands = [s 
            for s in self.sentences 
                if re.findall(r"(?=\()(?=.*\))|(?=\[)(?=.*\])",s) and not
                    re.findall(r"^[A-Z]",s)]
                #if re.findall(r"(?=\()(?=.*\))|(?=\[)(?=.*\])",s) and not
                #re.findall(r"(?=^[A-Z]\: \()",s)]
        [print(sc+"\n") for sc in stage_commands]
        