import argparse
import csv
import json

def process(input_file_name, output_file_name):
    # Process the cardiograms file and convert into .csv format
    with open(input_file_name, 'r') as src_file: # Reading a cardiograms input file 
        with open(output_file_name, 'w', newline='') as out: # Output stream for writing an output file(.csv format)
            src_lines = src_file.readlines() # Read all lines from input file
            header = json.loads(src_lines[0]) # Loading a header 
            
            heartrate_len = len((header['cardiogram']['cards'])[0]['song']['lines']['heartRate']['_line'])
            heartrate = (header['cardiogram']['cards'])[0]['song']['lines']['heartRate']['_line']
            #print(heartrate)
            columns = heartrate[0].keys() # Columns = ['start', 'end', 'value']
            writer = csv.writer(out, delimiter = ',') # declare writer to write a csv file and use delimiter = ',' for .csv format (Input as list and split each data using given delimiter)
            writer.writerow(list(columns)) # write the columns name 
            for i in range(heartrate_len):
                 # parse each record into list for writing into .csv format using
                 heartrate_record = list(heartrate[i].values())
                 print(heartrate_record)
                 writer.writerow(heartrate_record)

if __name__ == '__main__':
    parser = argparse.ArgumentParser() # Adding infile and outfile using AgrumentParser
    parser.add_argument('--infile', required=True, type=str, nargs='+') # Input cardiograms data file
    parser.add_argument('--outfile', type=str, nargs='+') # Output file(If needed)

    args = parser.parse_args()
    for i in range(len(args.infile)): # Iterate over files to process 
        process(args.infile[i], args.infile[i] + '.csv' if args.outfile is None or args.outfile[i] is None else args.outfile[i])
