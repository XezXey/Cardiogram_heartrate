import argparse
import csv
import json

def process(input_file_name, output_file_name):
    with open(input_file_name, 'r') as src_file:
        with open(output_file_name, 'w', newline='') as out:
            src_lines = src_file.readlines()
            #print(src_lines)
            header = json.loads(src_lines[0])
            #print(header['cardiogram']['cards']['0']['song']['lines']['heartRate']['_line'])
            #heartrate = header(['cardiogram']['cards'])[0]['song']['lines']['heartRate']['_line']
            #print(heartrate)
            
            heartrate_len = len((header['cardiogram']['cards'])[0]['song']['lines']['heartRate']['_line'])
            heartrate = (header['cardiogram']['cards'])[0]['song']['lines']['heartRate']['_line']
            #write.writerows(map(lambda row : row[:heartrate_len], heartrate[row]))
            print(heartrate)
            columns = heartrate[0].keys()
            writer = csv.writer(out, delimiter = ',')
            writer.writerow(list(columns))
            for i in range(heartrate_len):
                 #print(i)
                 #print(heartrate[i]['start'] + heartrate[i]['end'] + heartrate[i]['value'])
                 heartrate_record = list(heartrate[i].values())
                 #print(heartrate_record)
                 writer.writerow(heartrate_record)
            #print((header['cardiogram']['cards'])[0]['song']['lines']['heartRate']['_line'][1])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', required=True, type=str, nargs='+')
    parser.add_argument('--outfile', type=str, nargs='+')

    args = parser.parse_args()
    for i in range(len(args.infile)):
        process(args.infile[i], args.infile[i] + '.csv' if args.outfile is None or args.outfile[i] is None else args.outfile[i])
