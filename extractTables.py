import sys

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


reading = False
tables = []
table_data = []
row_elems = []
for line in open(sys.argv[1],'r').readlines():
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
    
    
print "Read " + `len(tables)` + " tables."

ge_tables = []
for table in tables:
    if len(table[0]) > 0 and table[0][0].startswith('General Election'):
        year = table[0][0][17:21]
        
        try:
            if int(year) > 1980:
                print year,table[0][0]
        except:
            # Ignore changing errors
            pass
