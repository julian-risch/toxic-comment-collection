import datasets
import os
import shutil
import sys
import getopt
import logging

TEMPDIR = "./tmp"
FILEDIR = "./files"

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

def main(args):
    try:
        arguments = dict(getopt.getopt(args, "-r -? -o -t: -f:", ['reset', 'help', 'original', 'tempdir', 'filedir'])[0])
    except:
        logging.error("Invalid argument!")
        print_help()
        return -1

    if ("--tempdir" in arguments or "-t" in arguments):
        tempdir = _parse_argument(arguments, "--tempdir", "-t")
    else: 
        tempdir = TEMPDIR

    if ("--filedir" in arguments or "-f" in arguments):
        tempdir = _parse_argument(arguments, "--filedir", "-f")
    else: 
        filedir = FILEDIR

    if ("--help" in arguments or "-?" in arguments):
        print_help()
        exit()
    
    if ("--reset" in arguments or "-r" in arguments):
        clear_all()
        exit()
    
    unify = not ("--original" in arguments or "-o" in arguments)

    fetch_datasets(filedir, tempdir, unify=unify)

def print_help():
    print("""Usage: python3 main.py [-r][-?]
    
-r  --reset         Reset all existing files, deletes everything in folder 'tmp' and 'files'
-?  --help          Show this help
-t  --tempdir XXX   Set the temp directory to XXX (standard: ./tmp)
-f  --filedir XXX   Set the file directory to XXX (standard: ./files""")

def fetch_datasets(filedir, tempdir, unify=True):
    clear_all()
    logging.info("Download Data and perform initial processing")
    max_suffix_length = 0
    for idx, dataset in enumerate(datasets.get_datasets()):
        max_suffix_length = _print_progress_bar(idx *2, len(datasets.get_datasets()) *2, "Download " + dataset.name, max_suffix_length)
        _clear_directory(tempdir)
        file = dataset.download(tempdir)
        max_suffix_length = _print_progress_bar(idx *2 +1, len(datasets.get_datasets()) *2, "Process " + dataset.name, max_suffix_length)
        dataset.valid_hash(file)
        dataset.process(file, os.path.join(filedir, dataset.name), tempdir)
        if unify:
            dataset.unify_format(os.path.join(filedir, dataset.name))
    _print_progress_bar(len(datasets.get_datasets()), len(datasets.get_datasets()), "Done", max_suffix_length)
    logging.info("Done fetching Datasets")

def clear_all():
    logging.info("Clearing all existing Data")
    _clear_directory(TEMPDIR)
    _clear_directory(FILEDIR)
    
def _clear_directory(directory):
    logging.debug("Clearing Directory: " + str(directory))
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.mkdir(directory)

def _parse_argument(args, long_arg_name, short_arg_name):
    if (long_arg_name in args):
        if args[long_arg_name]:
            return args[long_arg_name]
        else:
            logging.error("Invalid arguments!")
            exit()
    elif (short_arg_name in args):
        if args[short_arg_name]:
            return args[short_arg_name]
        else:
            logging.error("Invalid arguments!")
            exit()
    else:
        raise ValueError("Neither long_arg_name nor short_arg_name are present in args!")

def _print_progress_bar(iteration, total, suffix='', max_suffix_length=0):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(50 * iteration // total)
    bar = '█' * filledLength + '-' * (50 - filledLength)
    suffix_string = suffix + (' ' * (max_suffix_length - len(suffix)))
    print(f'\rProgress: [{bar}] {percent}% {suffix_string}', end = '\r')
    if iteration == total: 
        print()
    return len(suffix_string)

if __name__ == '__main__':
    main(sys.argv[1:])
