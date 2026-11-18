import unittest
import pandas as pd

from app_refactored import naCleaner
from app_refactored import dateCleaner
from app_refactored import enrich_dateDuration
from app_refactored import duplicateCleaner


class TestFunctions(unittest.TestCase):
    # Functions listed:
    # duplicateCleaner   - drops all rows that match 
    
    # naCleaner   - drops entries that are NA

    # dateCleaner   - converts date columns to datetime

    # enrichDate_Duration   - "    Takes the two datetime input column names
    # and the dataframe to create a new column date_delta which is the 
    # difference, in days, between colA and colB.


    # duplicateCleaner testing not required in this verysion; no dups
    
    def setUp(self):
        self.data = pd.read_csv("./data/03_Library Systembook.csv")

    def test_na(self):
        result = naCleaner(self.data)
        self.assertEqual(len(result),20)
        self.assertFalse(result.isna().any().any(),"NA remains in the dataset")
        self.assertFalse(result["Id"].eq(21).any())

    def test_dataCleaner(self):
        pass

if __name__ == "__main__":
    unittest.main()