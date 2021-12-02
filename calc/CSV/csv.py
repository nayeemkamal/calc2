"""csv class"""
import pandas

class Csv:
    # pylint: disable=too-few-public-methods

    """csv class"""
    @staticmethod
    def read_csv(path):
        # pylint: disable=redefined-outer-name

        """read csv"""
        return pandas.read_csv(path)

    @staticmethod
    def write_csv(path,dataframe):
        # pylint: disable=unspecified-encoding

        """write csv"""
        with open(path,'w+') as csv:
            csv.write(str(pandas.DataFrame(dataframe).to_csv()))
