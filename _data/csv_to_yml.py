import csv
ORALS = [5, 9, 31, 42]

print '- id: 1' 
print '  title: session_title' 
print '  papers:' 
with open('papers.csv') as csvf:
    reader = csv.DictReader(csvf)
    for row in reader:
        # print row 
        paper_id = int(row['CMT_Paper_ID'])
        print '  - authors:', row['Authors_Name (comma separated)'].strip() #'Brandon Trabucco, Aviral Kumar, Xinyang Geng, Sergey Levine' 
        print '    id:', paper_id
        if paper_id in ORALS:
            print '    kind:', 'oral' 
        else:
            print '    kind:', 'poster' 
        print '    supplement:', 'false' 
        print '    title:', "'%s'" % row['Paper_Title'].strip()
        print '    url:', row['Link_to_Video'].strip()
