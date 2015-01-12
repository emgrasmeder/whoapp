from __future__ import print_function
'''
    The LinePackager class takes as input a single line of a Doctor Who 
    script and converts it to a simple record for the database to compute
    later.
'''

class LinePackager:
    def parseline(self, line=False):
        if line:
            print("We have a line, at least")
            print("---\n\n---\n\n---here's some magic---\n\n---\n\n---")
            print("the line you gave me was: %s" % line)
            return("this is an example of a fake parsed line: %s, %s, %s" %
                                            ("doctor", "writer","season") )
        else:
            raw_input("Must provide a line to parse.")