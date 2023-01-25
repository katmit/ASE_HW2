import csv
import row
import cols

from typing import List

class Data():

    ## constructor created for data.py class
    def __init__(self, src):
        self.rows = []
        self.cols =  None

        ## if the src is string then
        ## it reads the file and then calls the add method to add each row
        src_type = type(src)
        if src_type == str :  
            with open(src, 'r') as csv_file:
                 reader = csv.reader(csv_file)
                 for row in reader:
                    self.add(row)
        elif src_type == List[str]: # else we were passed the columns as a string
            self.add(src)
        else:
            raise Exception("Unsupported type in Data constructor")

    ## add method adds the row read from csv file
    ## It also checks if the col names is being read has already being read or not
    ## if yes then it uses old rows
    ## else add the col rows.
    def add(self, t: list[str]):

        if(self.cols is None):
            self.cols = cols.Cols(t)
        else:
            row = row.Row(t)
            self.rows.append(row)
            self.cols.add(row)

    def clone(self):
        new_data = Data({self.cols.names})
        for row in self.rows:
            new_data.add(row)
        return new_data

#todo: main method type stuff