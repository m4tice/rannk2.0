from data_extraction import DataExtraction
from match import Match
from table import Table
from helper import export_to_txt

import os


# ======================================================================================================================
input_file = "sample_input.txt"
de = DataExtraction()
de.setFile(input_file)
data = de.getData()

match = Match()
table = Table()

for entry in data:
    t1_info, t2_info = entry
    match.update_match(t1_info, t2_info)
    match_result = match.analyze()
    table.addEntry(match_result)

table.sort_table()
table.rank_table()
table_dict = table.getTableDict()

for item in table_dict.items():
    print(item)

export_to_txt(table_dict)

