"""test csv"""
from pathlib import Path
from calc.CSV.csv import Csv
def test_read_csv():
    """test read csv"""
    assert Csv.read_csv(Path("/Users/nayeemkamal/Desktop/calc2/tests/test_data/addition.csv")
                        .absolute())["result"].dtypes=='int64'

def test_write_csv():
    """csv write test"""
    Csv.write_csv(path=str(Path("/Users/nayeemkamal/Desktop/calc2/tests/output/test.csv")
                           .absolute()),
                         dataframe={'name':[0,1,2]})
    assert Csv.read_csv(Path("/Users/nayeemkamal/Desktop/calc2/tests/output/log.csv")
                        .absolute())["name"].dtypes=='int64'
