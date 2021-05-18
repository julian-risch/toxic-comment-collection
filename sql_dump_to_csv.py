# based on https://stackoverflow.com/a/45377207
import pandas as pd
import re
from ast import literal_eval as make_tuple


def find_tables(dump_filename):
    table_list = []
    with open(dump_filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith('create table'):
                table_name = re.findall('create table `([\w_]+)`', line.lower())
                table_list.extend(table_name)
    return table_list


def read_dump(dump_filename, target_table):
    column_names = []
    rows = []
    read_mode = 0 # 0 - skip, 1 - header, 2 - data
    with open(dump_filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith('insert') and target_table in line:
                read_mode = 2
            if line.lower().startswith('create table') and target_table in line:
                read_mode = 1
                continue
            if read_mode == 0:
                continue

            # Filling up the headers
            elif read_mode == 1:
                if line.lower().startswith('primary'):
                    # add more conditions here for different cases 
                    #(e.g. when simply a key is defined, or no key is defined)
                    read_mode = 0
                    continue
                colheader = re.findall('`([\w_]+)`', line)
                #column_names = []
                for col in colheader:
                    column_names.append(col.strip())

            elif read_mode == 2:
                if line.endswith(";"):
                    end_index=-1
                else:
                    end_index=0
                data = make_tuple(line[line.find("VALUES")+7:end_index])
                try:
                    for item in data:
                        row = {}
                        for key, value in zip(column_names, item):
                            row[key]=value
                        rows.append(row)
                except IndexError:
                    pass
                if line.endswith(';'):
                    df = pd.DataFrame(rows, columns=column_names)
                    break
    df.to_csv(dump_filename[:-4]+"_"+target_table+"_df.csv", index=False)
    return


filename = "wow_anonymized.sql" #"lol_anonymized.sql"
table_list = find_tables(filename)
if len(table_list) > 0:
    print('Found tables: ', str(table_list))
    for table in table_list:
        read_dump(filename, table)
