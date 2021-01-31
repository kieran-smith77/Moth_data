import csv
import sys
import os

def moth_data_convert(directory, file):
    filename = os.path.join(directory, file).strip('.csv')


    ### LOAD IN NEW DATA FROM CSV ###
    rows = []
    no_code = []
    raw_data = []
    try:
        with open("{}.csv".format(filename), newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                raw_data.append(row)
        headers = raw_data[0]
        raw_data=raw_data[1:]
        for row in raw_data:
            temp_moth_object = {
                "Code": row[0].strip(),
                "Name": row[1],
            }
            for date in range(2, len(row)):
                if row[date]:
                    if temp_moth_object['Code']:
                        rows.append([temp_moth_object["Code"], temp_moth_object['Name'], headers[date], row[date]])
                    else:
                        no_code.append([temp_moth_object["Code"], temp_moth_object['Name'], headers[date], row[date]])
        processed_data = []
        for line in rows:
            processed_data.append(line)
        for line in no_code:
            processed_data.append(line)
    except Exception as e:
        print('Error processing data. Please confirm the structure of the CSV.')
        print('Error: {}'.format(e))
        quit()




    ### LOAD IN REFERENCE DATA ###
    try:
        moths = []
        with open(os.path.join(directory, "british_list.csv"), newline='') as csvfile:
            reader = csv.reader(csvfile)
            for i in reader:
                moths.append(i)
        moths = moths[1:]
        complete = []
        for row in processed_data:
            code = row[0]
            latin_name = ''
            english_name = ''
            for moth in moths:
                if str(moth[0]) == str(code):
                    latin_name = moth[1]
                    english_name = moth[3]
                    break
            if len(english_name) < 1:
                english_name = latin_name
            complete.append(([row[0], latin_name, english_name] + row[1:]))
    except Exception as e:
        print('Unable to import the british moths list. Please got to http://www.staffs-ecology.org.uk/html2015/images/a/a1/British_Checklist.zip and export the file to CSV, saving the document in the same folder as this program')
        print('Error: {}'.format(e))
        quit()


    ### SAVE RESULTS ###
    if not os.path.exists(os.path.join(directory, 'results')):
        os.mkdir(os.path.join(directory, 'results'))
    outfile = os.path.join(directory, 'results', (file.strip('.csv')+ '-output'))

    try:
        with open('{}.csv'.format(outfile), 'w') as final:
            final.write('Code, Latin Name, English Name, My Name, Date, Qty\n')
            for i in complete:
                final.write( str(','.join(i) + '\n') )
    except Exception as e:
        print('Failed to write to output file.')
        print('Error: {}'.format(e))
        quit()



directory = sys.argv[1]

for file in os.listdir(directory):
    if file.endswith(".csv"):
        if file != 'british_list.csv':
            moth_data_convert(directory, file)
