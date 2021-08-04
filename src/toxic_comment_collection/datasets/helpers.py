import os
import shutil
import zipfile
from typing import Dict
from urllib.error import URLError

import pandas as pd
import json
import csv
import tarfile
import re
import ast

from io import BytesIO
from urllib.request import urlopen
from twarc import Twarc


def download_from(url : str, destination_file : str) -> str:
    """ Downloads a file to the specified destination.
        
        Keyword arguments:
        url -- url of the file to download
        destination_file -- path to the file to download to

        Returns path to the downloaded file.
    """
    try:
        with urlopen(url) as response:
            os.makedirs(os.path.dirname(destination_file), exist_ok=True)
            with open(destination_file, 'wb') as f:
                shutil.copyfileobj(response, f)
        return destination_file
    except URLError as e:
        print("Additional certificate installation is needed for MacOS. "
              "See https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org "
              "and https://stackoverflow.com/questions/44649449/brew-installation-of-python-3-6-1-ssl-certificate-verify-failed-certificate/44649450#44649450 "
              "for help")
        raise(e)

def convert_excel_to_csv(file_name : str) -> str:
    """ Converts Excel file to CSV file.
        
        Keyword arguments:
        file_name -- path of the Excel file

        Returns path to the converted CSV file
    """
    new_file = file_name + ".csv"
    excel_data = pd.read_excel(file_name)
    excel_data.to_csv(new_file, index=False)
    return new_file

def copy_file(source_file : str, destination_file : str) -> str:
    """ Copies a file to a given path. Creates the path if it doesn't exist.
        
        Keyword arguments:
        source_file -- path of the source file
        destination_file -- path of the destination file
        
        Returns path to the destination file
    """
    os.makedirs(os.path.dirname(destination_file), exist_ok=True)
    shutil.copyfile(source_file, destination_file)
    return destination_file

def convert_json_to_csv(file_name : str) -> str:
    """ Converts JSON file to CSV file
        
        Keyword arguments:
        file_name -- path of the JSON file

        Returns path to the converted CSV file
    """
    new_file = file_name + ".csv"
    json_data = pd.read_json(file_name)
    json_data.to_csv(new_file, index=False)
    return new_file

def convert_jsonl_to_csv(file_name : str) -> str:
    """ Converts JSONL file to CSV file
        
        Keyword arguments:
        file_name -- path of the JSONL file

        Returns path to the converted CSV file
    """
    new_file = file_name + ".json"
    data = []
    with open(file_name, "r") as jsonl_file:
        for line in jsonl_file:
            data.append(json.loads(line))
    df = pd.DataFrame(data)
    df.to_csv(new_file, index=False)
    return new_file

def unzip_file(file_name : str) -> str:
    """ Unpacks a ZIP file
        
        Keyword arguments:
        file_name -- path of the ZIP file

        Returns path to the folder containing the unpacked files.
    """
    extraction_dir = os.path.join(os.path.dirname(file_name), os.path.basename(file_name) + "_extracted")
    os.makedirs(extraction_dir, exist_ok=False)
    with zipfile.ZipFile(file_name) as zip_file:
        zip_file.extractall(extraction_dir)
    return extraction_dir

def untarbz_file(file_name : str):
    """ Unpacks a .tar.bz2 file
        
        Keyword arguments:
        file_name -- path of the .tar.bz2 file
    """
    tar = tarfile.open(file_name, "r:bz2")
    tar.extractall(path=os.path.dirname(file_name))
    tar.close()

def add_column(file_name : str, column_name : str, column_value) -> str:
    """ Inserts a new column into a CSV file.
        
        Keyword arguments:
        file_name -- path of the CSV file
        column_name -- name of the new column
        column_value -- default value that is added in each line

        Returns path to the resulting file.
    """
    new_file = file_name + "_new_column"
    df = pd.read_csv(file_name)
    df.insert(loc=0, column=column_name, value=[column_value] * df.count().max())
    df.to_csv(new_file, index=False)
    return new_file

def clean_csv(file_name : str, names : [str] = None, header : int = 'infer', sep : str = ',', dtype : dict = None ) -> str:
    """ Loads CSV into Dataframe and exports it as CSV again to archive a clean CSV with standard seperators. Can be used to add column names.
        
        Keyword arguments:
        file_name -- path to the file
        names -- list that contains the names for the columns
        header -- set to 0 if an existing header should be overwritten
        sep -- seperator of the CSV file
        dtype -- dict containing the data types of the columns

        Returns path to the resulting file.
    """
    new_file = file_name + "_clean"
    df = pd.read_csv(file_name, names=names, sep=sep, header=header, dtype=dtype)
    df.to_csv(new_file, index=False, quoting=csv.QUOTE_NONNUMERIC)
    return new_file

def join_csvs(file1 : str, column1 : str, file2 : str, column2 : str, how : str = 'inner') -> str:
    """ Joins two CSVs on a given column

        Keyword arguments:
        file1 -- path of the first CSV
        column1 -- name of the column to join on in file1
        file2 -- path of the second CSV
        column2 -- name of the column to join on in file2
        how -- joint type of the pandas DataFrame.merge function

        Returns path to the resulting file.
    """
    new_file = file1 + "_joined"
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df = df1.merge(df2, how=how, left_on=column1, right_on=column2)
    df.to_csv(new_file, index=False)
    return new_file

def drop_duplicates(file_name : str, columns : [str]) -> str:
    """ Drops all duplicates in a CSV file

        Keyword arguments:
        file_name -- path of the CSV file
        columns -- list of columns to perform duplicate checking on

        Returns path to the resulting file.
    """
    new_file = file_name + "_dropped"
    df = pd.read_csv(file_name)
    df = df.drop_duplicates(columns)
    df.to_csv(new_file, index=False)
    return new_file

def merge_csvs(files : dict) -> str:
    """ Merge multiple CSV files into one.

        Keyword arguments:
        files -- dictionary with the filename as a key and a list of attributes that will be added in a label column

        Returns path to the resulting file.
    """
    new_file = list(files.keys())[0] + "_merged"

    merged_df = pd.DataFrame()
    for file in files:
        df = pd.read_csv(file)
        if len(files[file]):
            df.insert(loc=0, column="labels", value=[files[file]] * df.count().max())
        merged_df = merged_df.append(df)
    merged_df.to_csv(new_file, index=False)
    return new_file


def download_tweets_for_csv(file_name : str, column : str, api_data: Dict) -> str:
    """ Replaces the Tweet IDs of a CSV file with the actual tweets.

        Keyword arguments:
        file_name -- path of the CSV file
        column -- name of the column containing the tweet IDs

        Returns path to the resulting file.
    """
    def hydrate(row, translation, columns):
        if str(row[column]) in translation:
            row["text"] = translation[row[column]]
            row = row.drop(column)
            return row
        else:
            ser = pd.Series(index=columns)
            ser = ser.drop(column)
            return ser

    new_file = file_name + "_with_tweets"
    df = pd.read_csv(file_name, dtype={column: str})
    t = Twarc(
        api_data["twitter"]["consumer_key"],
        api_data["twitter"]["consumer_secret"],
        api_data["twitter"]["access_token"],
        api_data["twitter"]["access_token_secret"]
        )
    translation = {}
    for tweet in t.hydrate(df[column]):
        translation[str(tweet["id"])] = tweet["full_text"]
    df = df.apply(hydrate, axis=1, args=(translation,df.columns)).dropna(how='all')
    df.to_csv(new_file, index=False, quoting=csv.QUOTE_NONNUMERIC)
    return new_file

def extract_sql_tables(file_name : str) -> str:
    """ Extracts tables from SQL file and saves them as CSV.

        Keyword arguments:
        file_name -- path of the SQL file

        Returns path of the directory that contains the resulting files.
    """
    def find_tables(dump_filename):
        table_list = []
        with open(dump_filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line.lower().startswith('create table'):
                    table_name = re.findall('create table `([\w_]+)`', line.lower())
                    table_list.extend(table_name)
        return table_list


    def read_dump(dump_filename : str, output_dir : str, target_table : str) -> None:
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
                    data = ast.literal_eval(line[line.find("VALUES")+7:end_index])
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
        df.to_csv(os.path.join(output_dir, target_table+".csv"), index=False)

    output_dir = os.path.join(os.path.dirname(file_name), "extracted")
    os.makedirs(output_dir, exist_ok=False)
    table_list = find_tables(file_name)
    if len(table_list) > 0:
        for table in table_list:
            read_dump(file_name, output_dir, table)
    return output_dir
