import sys,os

def stripTags(line):
    in_tag = False
    str = ''
    for char in line:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            str += char
    return str

def read(fileIn):
    const = fileIn[0:fileIn.find('(')-1]

    reading = False
    tables = []
    table_data = []
    row_elems = []
    for line in open(fileIn,'r').readlines():
        if line.strip().startswith('<table'):
            reading = True
        elif line.strip().startswith('</table'):
            reading = False
            tables.append(table_data)
            table_data = []
        elif line.strip().startswith('</tr'):
            table_data.append(row_elems)
            row_elems = []
        elif reading:
            nl =  stripTags(line.strip())
            if len(nl) > 0:
                row_elems.append(nl)
    
    ge_tables = []
    for table in tables:
        if len(table[0]) > 0 and table[0][0].startswith('General Election'):
            year = table[0][0][17:21]
            
            try:
                if int(year) > 1980:
                    for row in table[1:]:
                        if len(row) == 5 and row[0] != 'Party':
                            print ",".join([const,year,row[0],row[3]])
            except:
                # Ignore changing errors
                pass


for filename in os.listdir('.'):
    if filename.endswith(')'):
        read(filename)
