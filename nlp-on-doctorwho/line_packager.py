from __future__ import print_function
'''
    The LinePackager class takes as input a single line of a Doctor Who 
    script and converts it to a simple record for the database to compute
    later.
'''

class LinePackager:
    def parseline(self, script_segment=False):
        if script_segment:
            is_empty = self.check_is_empty(script_segment)
            if not is_empty:
                is_title = self.check_is_title(script_segment)
            #is_dialog = check_is_dialog()
            print("the script_segment you gave me was: '%s'" % script_segment)
            return("this is an example of a fake parsed script_segment: %s, %s, %s" %
                                            ("doctor", "writer","season") )
        else:
            raw_input("Must provide a script_segment to parse.")

    def commit_output(self, output=False):
        if output:
            pass
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
            print ("this is a title!")

    def is_dialog(self, script_segment):
        '''
            Check if the line follows the pattern:
            r'^[A-Z].*:" "... or whatever
        '''
        pass


###
#Output Notes: 
#Possible fields in output:
# 1. Message type: (1=spoken line,
#                  2=stage direction,
#                  3=script title
#                  4=undetermined)
# 2. Content: (line (string),
#               stage direction (string? int?),
#               script title (string? int?),
#               unclassified text (string))
# 3. 
###