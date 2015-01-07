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
        self.sent_tokens = nltk.sent_tokenize(
                    open('../resources/raw-scripts/34_1__Deep_Breath.txt',"r").read())
        
        #self.sentences = nltk.Text(self.sent_tokens)

    def isolate_scene_notes(self):
        '''
            Best case: make a new self.sent_tokens variable that is broken up 
            properly.

            What I mean to say is that:
            "[Spaceship]
            (Strax is about to fire his weapon before he passes out.)"
            should be viewed as two different senteces. 
            and that 
            "DOCTOR [dream]: Clara!" should be just one sentence. 
        '''
        
        self.trickylines = filter(lambda line: 
            re.findall(r"(?=\[)(?=.*\].*\n)",line),
            self.sent_tokens)
        
        ''' The code just below turns EVERYTHING into a list, which I dont
        love '''
        #trickylines = map(lambda line: 
        #    self.isolate_stage_directions(sentences=line.split("\n")),
        #    trickylines)
        
        #[print(st) for st in self.trickylines]
        

    def isolate_speaker(self):
        '''
            My immediate thoughts is that each line of dialogue should be
            sliced into a two item list, [speaker,line]
            with parenthetical notes stripped out

            There area couple of things to fix about self.spoken_lines.
            Firstly, sentence tokenization means that when someone gives a 
            line that is more than 2 sentences, the speaker and line are 
            dissociated. 

            Also, there is stuff at the end of the script that is just legal
            stuff that I don't want.
        '''
        self.spoken_lines = filter(lambda line: line not in [self.trickylines,
                                            self.stage_directions],
                                            self.sent_tokens)
        #nltk.sent_tokenize(self.spoken_lines)
        fdist1 = nltk.FreqDist(["to do or not to do"])
        print(list(fdist1["to"]))


        #[print("---"+s+"---\n") for s in spoken_lines]

    def isolate_stage_directions(self):
        '''
            Should remove all lines that start with and end with a parenthesis
            or bracket. Doesn't have anything to do with:
            [scene note]\nDOCTOR: Clara! 
            because those are in the same sentence token.
        '''

        self.stage_directions = filter(lambda line: 
            re.findall(r"(?=^\()(?=.*\)$)|(?=^\[)(?=.*\]$)",line),
            self.sent_tokens)
        #[print("---"+sc+"---\n") for sc in self.stage_directions]