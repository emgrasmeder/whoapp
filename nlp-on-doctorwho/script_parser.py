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
        
        sent_tokens = nltk.sent_tokenize(
                    open('../resources/raw-scripts/34_1__Deep_Breath.txt',"r").read())

        [print(sc) for sc in sent_tokens if re.findall(r"(?=\[)(?=.*\].*\n)",sc)]
        
        self.sentences = nltk.Text(sent_tokens)

    def isolate_speaker(self):
        pass

    def isolate_stage_directions(self):
        '''
            Should remove all lines that start with and end with a parenthesis
            or bracket. Doesn't have anything to do with:
            [scene note]\nDOCTOR: Clara! 
            because those are in the same sentence token.
        '''
        stage_directions = [s 
            for s in self.sentences 
                if re.findall(r"(?=^\()(?=.*\)$)|(?=^\[)(?=.*\]$)",s)]
        [print(sc+"---\n---") for sc in stage_directions]
        
