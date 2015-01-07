from __future__ import print_function
'''
    make_db.py takes as input all the algorithms that other 
'''

passed=True
input_file = ["test1","test2test3"]
if passed:
    with open("script_database.csv", "a") as output_file:
        output_file.write("\n"+"\t".join(input_file))
