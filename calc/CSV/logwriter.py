"""logwriter"""
from pathlib import Path
from datetime import datetime
from csv import Csv

class Logwriter:

    line = 0
    @staticmethod
    def write(file,record,op,result):
        Csv.write_csv(Path("/Users/nayeemkamal/Desktop/calc2/tests/output/log.csv")
                      ,{"time":datetime.now().strftime("%m/%d/%y %H:%M:%D"),
                        "file":file
                                                                                     })