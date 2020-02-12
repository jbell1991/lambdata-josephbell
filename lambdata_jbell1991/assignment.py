# my_lambdata/assignment.py
import pandas
class DataFrameTransformer(object):
    def __init__(self, df):
        """Param df pandas dataframe with column name "abbrevs" """
        self.df = df
    def inspect_data(self):
        print(self.df.head())
    def add_state_names(self):
        """
        State abbreviation -> Full Name and visa versa.
        FL -> Florida, etc.
        """
        new_df = self.df # don't mutate existing df (just a pref, you could mutate and not return anything if you want)
        names_map = {
            "CA": "Cali",
            "CO": "Colo",
            "CT": "Conn",
            "DC": "Wash DC",
            "TX": "Texas"
        }
        #breakpoint()
        my_col = self.df["abbrevs"]
        other_col = my_col.map(names_map)
        self.df["state_name"] = other_col
        return new_df
if __name__ == "__main__":
    #print("hahahah")
    #input(".............")
    df = pandas.DataFrame({"abbrevs": ["CA", "CO", "CT", "DC", "TX"]})
    #print(type(df))
    #print(df.head())
    transformer = DataFrameTransformer(df)
    transformer.inspect_data()
    #df2 = add_state_names(df)
    #print(df2.head())
    transformer.add_state_names()
    transformer.inspect_data()