"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""



if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    with open('data/SOURCE/SOURCECOLUMNS.txt') as f:
        columns = [column.rstrip().split('|') for column in f]
    with open('data/SOURCE/SOURCEDATA.txt') as f:
        values = [value.rstrip().replace('|',',') for value in f]
    columns = sorted(columns, key=lambda x: int(x[0]))
    values.insert(0, ','.join([l[1] for l in columns]))
    with open('data/DESTINATION/DESTINATIONDATA.csv', 'w+') as f:     
    # write elements of list to destination file
    for rows in values:
        f.write('%s\n' %rows)
    f.close()
