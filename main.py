from data_extraction import DataExtraction
from match import Match
from table import Table
from helper import export_to_txt


def main():
    # Define input file
    input_file = "sample_input.txt"

    # Create a Data Extraction object, input the file and extract data from it
    de = DataExtraction()
    de.setFile(input_file)
    data = de.getData()

    # Objects initialisation
    match = Match()
    table = Table()

    # Update entries to table
    for entry in data:
        t1_info, t2_info = entry
        match.update_match(t1_info, t2_info)
        match_result = match.analyze()
        table.addEntry(match_result)

    # Sort and assign teams' ranks to table
    table.sort_table()
    table.rank_table()

    # Export table to text file
    table_dict = table.getTableDict()
    export_to_txt(table_dict)


if __name__ == '__main__':
    main()
