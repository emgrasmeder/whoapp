from __future__ import print_function
import datetime
'''
    The LinePackager class takes as input a single line of a Doctor Who 
    script and converts it to a simple record for the database to compute
    later.

    Questions:
    - What is the standard protocol for writing a cleaner script?
        - NONE OF THIS MATTERS. DON'T GET CAUGHT IN THE PERFECTION TRAP!
        - Is it "if, elif, elif, elif, elif, else" format?
            - What are the alternatives?
                - "filter1(), filter2(), filter3()..."
                - "Look at first character, do something()
                look at second character, do something()..."
                - Look into Spark NLP MLlib type stuff. 
                Instead of passing a line by line, maybe a lambda function
                is what we want.
                - 
'''

class LinePackager:
    def parseline(self, script_segment=False):
        '''
            Philosophical Question: Should we run every test on every
            line in the script? For now, that makes sense to me to do. 
            Redundancy can be an auto test?
        '''
        self.script_segment = script_segment.strip('\n')
        output = {"message_type":self.get_message_type(),
                    "content":"self.get_content()",
                    "speaker":"self.get_speaker()",
                    "speaker_subcategory":"self.get_speaker_subcategory()",
                    "writer":"self.get_writer()",
                    "year":"self.get_year()",
                    "episode_number":"self.get_episode_number()"}
        raw_input()
        #self.commit_output(output)
        

    def commit_output(self, output=False):
        if output:
            raw_input("This is me pretending to commit the following lines"+
                "to a database/log file:\n %s" % (output))
        else:
            print("The line was apparently a \\n or ''")

    def check_is_empty(self, script_segment):
        '''
            For now, check: Is line =='\n' or ''?
        '''
        flags = ["","\n"]
        for flag in flags:
            if script_segment == flag:
                self.commit_output()
                return True

    def check_is_stage_direction(self, script_segment):
        '''
            Simplest algorithm that will return True in the naivest of 
            elegance, check if it has (,),[,or  in it. 
            Additional tests to implement in the future:
        '''
        flags = ["(",")","[","]"]
        if any(x in flags for x in script_segment):
            print("Parenthetical string found?, may be stage direction")
        else:
            self.commit_output(output=[3,script_segment.strip('\n')])

    def get_message_type(self):
        '''
            Returns the message type, probably coded?

            Possible messages:
            >"\n"
            >"Deep Breath\n"
            >"Original Airdate: 23 Aug 2014\n"
            >"[Albert Embankment]\n"
            >"(On the south side of the River Thames in London, \
                across from Thorney Island and the Houses of Parliament, \
                a crowd is gathered as Big Ben chimes three o'clock and a \
                dinosaur roars at it.) \n"
            >"POLICEMAN: Come on, out of the way. Move yourself, please. \
            Coming through. That's it. Excuse me, sir. \n"
            >"VASTRA: (To Dinosaur) I was there.\n"
        '''
        def detect_date(line):
            try:
                return(datetime.datetime.strptime(line.split(":")[1].strip('\n'),' %d %b %Y'))
            except: return(False)

        print("\n\n---getting message type---\n\n\n---%s---\n\n" % 
            self.script_segment)
        if self.script_segment in ["","\n"]:
            print("the line is EMPTY: %s" % self.script_segment)
        elif not any(x in [":","[","]","(",")"] for x in self.script_segment):
            print("the line is the TITLE: %s" % self.script_segment)
        elif detect_date(self.script_segment):
            print("the line is the DATE: %s" % self.script_segment)
        elif self.script_segment[0] == "[" and self.script_segment[-1]=="]":
            print("the line is the LOCATION(stagedir): %s" 
                                                        % self.script_segment)
        elif self.script_segment[0] == "(": # and self.script_segment[-1]==")":
            print("the line is the STAGE_DIRECTION: %s" 
                                                        % self.script_segment)
        elif ":" in self.script_segment.split(" ")[0]:
            if self.script_segment[1][0] == "(" and \
                                            self.script_segment[1][-1] ==")":
                print("the line is LINE with STAGE_DIR: %s" 
                                                    % self.script_segment)
            else:
                print("This is a SPOKEN LINE: %s " % self.script_segment)


###
#Output Notes: 
#Possible fields in output:
# 1. Message type: (1=line,
#                  2=stage direction,
#                  3=script title
#                  4=undetermined)
# 2. Content: (line (string),
#               stage direction (string? int?),
#               script title (string? int?),
#               unclassified text (string))
# 3. Speaker: (1=DOCTOR, 2=COMPANION)
# 4. Speaker Subcategory (1=David Tennant, 2=Karen Gillian,)
# 5. Shouldn't we alwas include WRITERS, YEAR, and EPISODE NUMBER?
###