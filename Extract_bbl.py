# import bibtexparser

# # Open and parse the .bbl file
# with open('input1.bbl', 'r') as bbl_file:
#     bbl_data = bbl_file.read()
#     bib_database = bibtexparser.loads(bbl_data)

# # Access the extracted information
# entries = bib_database.entries

# for entry in entries:
#     # Access individual fields
#     title = entry.get('title')
#     author = entry.get('author')
#     year = entry.get('year')
#     # ...and so on

#     # Do whatever you want with the extracted information
#     print(f'Title: {title}')
#     print(f'Author: {author}')
#     print(f'Year: {year}')
#     print('---')  # Separator between entries


import bibtexparser

# Open and parse the .bbl file
with open('input2.bbl', 'r') as bbl_file:
    bbl_data = bbl_file.read()
    try:
        bib_database = bibtexparser.loads(bbl_data)
    except bibtexparser.bibdatabase.BibDatabaseError as e:
        print('Error occurred during parsing the .bbl file:')
        print(e)

# Access the extracted information
if bib_database.entries:
    for entry in bib_database.entries:
        # Access individual fields
        title = entry.get('title')
        author = entry.get('author')
        year = entry.get('year')
        # ...and so on

        # Do whatever you want with the extracted information
        print(f'Title: {title}')
        print(f'Author: {author}')
        print(f'Year: {year}')
        print('---')  # Separator between entries
else:
    print('No entries found in the .bbl file.')
