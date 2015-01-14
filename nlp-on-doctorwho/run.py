from line_packager import *

if __name__ == "__main__":
    obj = LinePackager()
    with open('../resources/raw-scripts/34_1__Deep_Breath.txt') as f:
        obj.parseline(f.readline())
        obj.parseline(f.readline())
        


#with open("script_database.csv", "a") as output_file:
#    output_file.write("\n"+"\t".join(input_file))jkhjk