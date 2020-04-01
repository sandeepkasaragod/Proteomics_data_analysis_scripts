#Any queries: sandeep.kolya@gmail.com

import os
import sys
import pip

#Check if the dependency packages are installed
try:
    import xlrd
except:
    #print ("Module does not exist, run command in terminal/command_prompt: pip install xlrd")
    print ("installing module")
    pip.main(["install", "xlrd"])
try:
    import pathlib
except:
    #print ("Modules does not exist, run command in terminal/command_prompt: pip install pathlib")
    print ("installing module")
    pip.main(["install", "pathlib"])

def convert_txt(input_dir, outdir):
    for list_file in os.listdir(input_dir):
        if pathlib.Path(list_file).suffix == '.xlsx': # If the file extension is xlsx
            output_file_path = pathlib.Path(outdir + "/" + list_file)
            write_file = open(str(output_file_path).split('.')[0] + ".txt", 'w') #Create the file with write modeoutp
            file_location = (input_dir + "/" + list_file)
            open_workbook = xlrd.open_workbook(file_location)
            set_sheet = open_workbook.sheet_by_index(0)# Get the first sheet
            for rows in range(set_sheet.nrows):
                each_item = ""
                for items in set_sheet.row_values(rows):
                    each_item = each_item + '\t' + str(items)
                write_file.write(each_item.strip() + '\n')
            write_file.close()
            print "Files Finished: " + list_file

def create_dir(outdir):
    try:
        directory_path = pathlib.Path(outdir + "/")
        if not directory_path.is_dir(): #Check if the directory exist
            directory_path.mkdir(parents=False, mode=511)
        else:
            print ("Directory already exist " + outdir)
            exit(0)
    except IOError as e:
        print (e)
        print ("Could not create a directory, check the admin permission or the drive does not exist")
        exit(0)
             
if __name__ == "__main__":
    if len(sys.argv) == 3:
        create_dir(sys.argv[2])
        convert_txt(sys.argv[1], sys.argv[2])
    else:
        print ("Usage : Excel_to_TSV.py <input directory> <output direcotry>")
        print ("Example in Windows: Excel_to_TSV.py D:\input_folder D:\output_folder")
        print ("Example in Linux: Excel_to_TSV.py mnt/d/input_folder mnt/d/output_folder")
                              
