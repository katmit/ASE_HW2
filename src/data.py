import csv
import row
import cols


class data():

    ## constructor created for data.py class
    def __init__(self, i, src, fun):
        self.rows = []
        self.col = []

        ## if the src is string then
        ## it reads the file and then calls the add method to add each row
        if str(src) == True :  
            csvreader = csv.reader(src)
            for rows in csvreader:
              self.add(rows);  
        # else:
            # do we need this?

    # def map(t, fun, u):
    #     u ={}
    #     for k,v in pairs(t):
            

    ## add method adds the row read from csv file
    ## It also checks if the col names is being read has already being read or not
    ## if yes then it uses old rows
    ## else add the col rows.
    def add(self, t):
        if(self.cols == True):
            t = t if t == t.cells else row.Row(t) # Can you check one more time unable to understand this
            self.rows.append(t)
            self.col.append(self.add(t))
        else:
            self.col = cols.Cols(t)

    # def clone(self,init ,d):  I think we don't need this we test case already passed.
    #     d = data()