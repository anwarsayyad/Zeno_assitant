import pandas as pd
import csv
def werite(day,time,task,imp):
    
    header = ('day','time','task','imp')
    data = [
            day,time,task,imp
           ]
    filename = 'myplan.csv' 
    with open(filename,'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        
        
    
