from __future__ import print_function
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
        if script_segment:
            is_empty = self.check_is_empty(script_segment)
            if not is_empty:
                is_title = self.check_is_title(script_segment)
            #is_dialog = check_is_dialog()
            print("the script_segment you gave me was: '%s'" % script_segment)
        else:
            raw_input("Must provide a script_segment to parse.")

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

    def check_is_title(self, script_segment):
        '''
            Simplest algorithm that will return True in the naivest of 
            elegance, check if it has (,),[,or  in it. 
            Additional tests to implement in the future:
            - Is the line reasonably similar to a title in a list of titles?
            - Is the line reasonably similar to a title in a season-sepcific
                list of titles?
            - Does the line contain "Air*Date" or have something in a date 
                format?
        '''
        flags = ["(",")","[","]"]
        if any(x in flags for x in script_segment):
            print("Parenthetical string found?")
        else:
            self.commit_output(output=[3,script_segment.strip('\n')])

    def is_dialog(self, script_segment):
        '''
            Check if the line follows the pattern:
            r'^[A-Z].*:" "... or whatever
        '''
        pass


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