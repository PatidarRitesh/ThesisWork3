



import xml.etree.ElementTree as ET
import re

def init_dict():

    information = {
        'title': '',
        'book': '',
        'publisher': '',
        'pages': '',
        'year': '',
        'ID': '',
        'volume': '',
        'author': list()
    }
    return information

# change 1
root = ET.Element('bibliography')

########################################################################
#-------------- EXTRACT INFORMATION FORM ACL/M FILE ------------------#
def get_information(root, Matched_data, paper_name, paper_format="ACL/M"):
    # root = ET.Element('bibliography')
    # entry_elem = ET.SubElement(root, 'entry', {'label': label})

    information = init_dict()
    # information['author'] = list()
    try: 
        if len(Matched_data['1']):
            for tup in Matched_data['1']:
                if tup[0] == '':
                    information['author'].append(tup[1])
                    # author_elem = ET.SubElement(entry_elem, f'author{len(information["author"])}')
                    # author_elem.text = tup[1]
                else:
                    information['author'].append(tup[0])
                    # author_elem = ET.SubElement(entry_elem, f'author{len(information["author"])}')
                    # author_elem.text = tup[0]
        else:
            print(Matched_data['15'])
            for author in Matched_data['15']:
                information['author'].append("".join(author))
                # author_elem = ET.SubElement(entry_elem, f'author{len(information["author"])}')
                # author_elem.text = author
            # print(information['author'])
            # input()
    except Exception as e:
        print("Error in fetching author name")
    
    try:

        if len(Matched_data['2']):
            information['year'] = Matched_data['2'][0]
            # year_elem = ET.SubElement(entry_elem, 'year')
            # year_elem.text = information['year']

        
        elif len(Matched_data['10']):
            information['year'] = Matched_data['10'][0]
            # year_elem = ET.SubElement(entry_elem, 'year')
            # year_elem.text = information['year']
    except Exception as e:
        print("Error in fetching year")

    try:
    
        if len(Matched_data['3']):
            information['ID'] = Matched_data['3'][0]
            # id_elem = ET.SubElement(entry_elem, 'id')
            # id_elem.text = information['ID']
    except Exception as e:
        print("Error in fetching ID")

    try:

        if len(Matched_data['4']):
            if len(Matched_data['4'][0]):
                information['title'] = Matched_data['4'][0]
                # title_elem = ET.SubElement(entry_elem, 'title')
                # title_elem.text = information['title']
            else:
                information['title'] = Matched_data['4']
                # title_elem = ET.SubElement(entry_elem, 'title')
                # title_elem.text = information['title']
    except Exception as e:
        print("Error in fetching title")

    try:
        if len(Matched_data['5']):
            information['book'] = Matched_data['5'][0]
            # book_elem = ET.SubElement(entry_elem, 'book')
            # book_elem.text = information['book']
    except Exception as e:
        print("Error in fetching book")
        
    try:
        if len(Matched_data['6']):
            information['publisher'] = Matched_data['6'][0]
            # publisher_elem = ET.SubElement(entry_elem, 'publisher')
            # publisher_elem.text = information['publisher']

        else:
            if len(Matched_data['9']):
                if Matched_data['9'][0][0] == '':
                    information['publisher'] = information.get('publisher', '') +  f"Journal: {Matched_data['9'][0][1]}"
                    # publisher_elem = ET.SubElement(entry_elem, 'publisher')
                    # publisher_elem.text = information['publisher']

                else:
                    information['publisher'] = information.get('publisher', '') +  f"Journal: {Matched_data['9'][0][0]}"
                    # publisher_elem = ET.SubElement(entry_elem, 'publisher')
                    # publisher_elem.text = information['publisher']
    except Exception as e:
        print("Error in fetching publisher")

    try:
        if len(Matched_data['11']):
            information['volume'] = Matched_data['11'][0]
            # volume_elem = ET.SubElement(entry_elem, 'volume')
            # volume_elem.text = information['volume']
    except Exception as e:
        print("Error in fetching volume")

    try:
        if len(Matched_data['12']):
            information['pages'] = " ".join(Matched_data['12'][0])
            # pages_elem = ET.SubElement(entry_elem, 'pages')
            # pages_elem.text = information['pages']


        elif len(Matched_data['7']):
            information['pages'] = ' '.join(Matched_data['7'][0])
            # pages_elem = ET.SubElement(entry_elem, 'pages')
            # pages_elem.text = information['pages']
    except Exception as e:
        print("Error in fetching pages")

    
    return information

def get_information2(root, Matched_data, paper_name, data_1):
    # entry_elem = ET.SubElement(root, 'entry', {'label': label})
    information = init_dict()
    # Author-------------------------------------------------------
    try:
        # data_1 = data_1.split(',')  if ',' in data_1 else [data_1.strip()]
        # data_2 = []

        
        # for author in data_1: 
        #     if 'and' in author:
        #         authors = author.strip().split('and')
        #         for auth in authors:
        #             if auth.strip() != '':
        #                 data_2.append(auth.strip())
        #     else:
        #         if author.strip() != '':
        #             data_2.append(author.strip())

        
        # information['author'] = data_2

        ################################## METHOD 2 ########################
        if len(Matched_data['16']):
            information['author'] = Matched_data['16'][0]

        # title_author = ET.SubElement(entry_elem, 'author')
        # title_author.text = information['author']
    except Exception as e:
        print("Error in fetching author name")
        print(e)

    # ID-------------------------------------------------------
    try: 
        if len(Matched_data['20'])and len(Matched_data['20'][0]):
                information['ID'] = Matched_data['20'][0][1]
    except:
        print("Error in fetching ID")
        print(e)
    
    # Title-------------------------------------------------------
    # print("______________________________ MATCHED DATA 8_____________________________")
    # print(Matched_data['8'])
    # input()
    try:
        if len(Matched_data['8'])>=2:
            if len(Matched_data['8'][1]):
                information['title'] = Matched_data['8'][1][2]
                # title_elem = ET.SubElement(entry_elem, 'title')
                # title_elem.text = information['title']
    except Exception as e:
        print("Error in fetching title")
    try:
        if len(Matched_data['8'])>=3:
            if len(Matched_data['8'][2]):
                information['title'] += Matched_data['8'][2][1]
                information['title'] += Matched_data['8'][2][2]
        # if information['title'] != '':
            # title_elem = ET.SubElement(entry_elem, 'title')
            # title_elem.text = information['title']
    except Exception as e:
        print("Error in fetching title")
    try:
        if len(Matched_data['8'])>=5:
            if len(Matched_data['8'][4]):
                information['title'] += Matched_data['8'][4][1]
                information['title'] += Matched_data['8'][4][2]
        # if information['title'] != '':
            # title_elem = ET.SubElement(entry_elem, 'title')
            # title_elem.text = information['title']
    except Exception as e:
        print("Error in fetching title")
    try:
        if len(Matched_data['8'])>=7:
            if len(Matched_data['8'][6]):
                
                information['title'] +=" : "+ Matched_data['8'][6][2]
        # if information['title'] != '':
            # title_elem = ET.SubElement(entry_elem, 'title')
            # title_elem.text = information['title']
    except Exception as e:
        print("Error in fetching title")
    try:
        if len(Matched_data['8'])>=8:
            if len(Matched_data['8'][7]):
                
                information['title'] +=" : "+ Matched_data['8'][7][2]
        # if information['title'] != '':
            # title_elem = ET.SubElement(entry_elem, 'title')
            # title_elem.text = information['title']
    except Exception as e:
        print("Error in fetching title")

    # Page
    # Pages-------------------------------------------------------
    try:

        if len(Matched_data['14']):
            information['pages'] = Matched_data['14'][0]
            # pages_elem = ET.SubElement(entry_elem, 'pages')
            # pages_elem.text = information['pages']
    except Exception as e:
        print("Error in fetching pages")

    # Publisher---------------------------------------------------
    try:
        if len(Matched_data['13']):
            information['publisher'] = Matched_data['13'][0]
            # publisher_elem = ET.SubElement(entry_elem, 'publisher')
            # publisher_elem.text = information['publisher']   
    except Exception as e:
        print("Error in fetching publisher")
    
    return information

def get_information3(root, Matched_data, paper_name, data_1):
    information=init_dict()

    # Author-------------------------------------------
    try:
        if len(Matched_data['16']):
            information['author'] = Matched_data['16'][0]

            # title_author = ET.SubElement(entry_elem, 'author')
            # title_author.text = information['author']
    except Exception as e:
        print("Error in fetching author name")
    
    # Title----------------------------------------------
    try:
        # print(Matched_data['17'])
        # input()
        if len(Matched_data['17'])>=1:
           
            information['title'] = Matched_data['17'][0]
                # title_elem = ET.SubElement(entry_elem, 'title')
                # title_elem.text = information['title']
    except Exception as e:
        print("Error in fetching title")

    # Publisher-------------------------------------------
    try:
        if len(Matched_data['18']):
            information['publisher'] = Matched_data['18'][0]
            # publisher_elem = ET.SubElement(entry_elem, 'publisher')
            # publisher_elem.text = information['publisher']
    except Exception as e:
        print("Error in fetching publisher")

    # Volume-------------------------------------------
    try:
        if len(Matched_data['19']):
            information['volume'] = Matched_data['19'][0]
            # volume_elem = ET.SubElement(entry_elem, 'volume')
            # volume_elem.text = information['volume']
    except Exception as e:
        print("Error in fetching volume")

    # ID----------------------------------------------
    try:
        if len(Matched_data['20'])and len(Matched_data['20'][0]):
                information['ID'] = Matched_data['20'][0][1]
            # pages_elem = ET.SubElement(entry_elem, 'pages')
            # pages_elem.text = information['pages']
    except Exception as e:
        print("Error in fetching ID")
    
    # Year---------------------------------------------
    try:
        if information['ID']!='':
            year = re.findall(Patterns["No_new_block_year"], information['ID'])
            print(year)
            if len(year):
                information['year'] = year[0]
    except Exception as e:
        print('Error in fetching year')
    return information

           

    
    

#################################################################
#------------------------PATTERNS------------------------------------
Patterns = { 
    
    'Author_ACM_ACL_2' : r'''{person}{([A-Za-z0-9\s~.]+)({[\\'\w\d\s"-]+}[\d\w\s-]*)*''',
    'Author_ACM_ACL_1' : r'''{person}{([A-Za-z0-9\s~.]+)({[\\'\w\d\s"-]+}[\d\w\s-]*)*''',
    'YEAR_ACM_ACL_1' : r'''{year}{(\d{4})}''',
    'BIB_ACM_ACL_1' : r'''\]% {([\w\d\s:\/-]+)}''',

    'Article_ACM_ACL_2' : r'''\\showarticletitle{([\w\d\s:{}“”;_$%*@!,.?-]*)}''',
    'Book_ACM_ACL_2' : r'''booktitle}{\\emph{([\w\s:,{}*;"'()\/-]+)}}''',
    'Publisher_ACM_ACL_2' : r'''bibinfo{publisher}{{?([\w\s]+)''',
    'Page_ACM_ACL_2' : r'''bibinfo{pages}{(\d+)(-+)?(\d*)''',
    # 'Title_IEEE_ARXIV_CVPR_2' : r'''((\bhttps:.+)}\s{)?|([\w\s,'":\/—- ]+)''',
    'Title_IEEE_ARXIV_CVPR_2' : r'''((\bhttps:.+)}\s{)?|(\w[\w\s,'":~\/—-]*)''',

    'Journal_ACM_3' : r'''journal}{\\emph{([\w\s.]+)|url{([^}]*)}''',
    'Year_ACM_ACL_3' : r'''bibinfo{year}{(\d{4})''',
    'Volumne_ACM_ACL_3' : r'''bibinfo{volume}{(\d+)''',
    'Pages_ACM_ACL_3' : r'''bibinfo{pages}{(\d+)(-+)?(\d*)''',
    'Pages_IEEE_ARXIV_CVPR_3' : r'''(\d+)-+(\d+)''',
    'Publisher_IEEE_aRXIV_CVPR_3' : r'''em[ph{\s]+([^}]+)''',

    'No_new_block_Author_1' : r'''{[\w\d~\s:'^%.,-]*} ([^``]*)''',
    'No_new_block_Title_1' : r'''``([^'']*)''',
    'No_new_block_Publisher_1' : r'''emph{([^}]*)''',
    'No_new_block_Vol_1' : r'''vol.[~\s](\d*)''',
    # 'No_new_block_Id_1': r'''{([^}]*)''',
    'No_new_block_Id_1' : r'''(\[.*\])?{([^}]*)''',
    'No_new_block_year' : r'''\d{4}'''
    

}



import time
import os
            
# directory = './BBL_file/BBL_file/'
#directory = './BBL_file/'
root_directory = './Arxiv_files_extracted/1708/'
root_directory_output = './Arxiv_files_extracted/results/1707'
# if not os.path.exists(root_directory_output):
#     os.makedirs(root_directory_output)

for folder in os.listdir(root_directory):
    if "result2" in folder:
        continue
    directory = os.path.join(root_directory, folder)
    output_directory = os.path.join(root_directory_output, folder)
    # output_directory = f'{directory}results2/'
    os.makedirs(output_directory, exist_ok=True)



    for filename in os.listdir(directory):
        if filename.endswith('.bbl'): # if you only want to read bbl files
            paper_name = filename.split('.')[0]
            # if paper_name != 'input49':
            #     continue
            root = ET.Element("bibliography")
            with open(os.path.join(directory, filename), 'r', encoding="utf8") as file:
                bbl_data= file.read()
                print()
                print()
                print()
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                                                                                    
                print("Processing: file:",filename)
            
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print()
                print()
                print()
                

                # split the bbl data into entries
                entries = bbl_data.split('\\bibitem')

                for i, entry in enumerate(entries[1:]):  # ignore the first empty entry
                # for entry in entries[1:]:  # ignore the first empty entry
                    
                    # entry='''\\bibitem{phillips2016industry} R.~L. Phillips and R.~Ormsby, ``Industry classification schemes: An analysis and review,'' \emph{Journal of Business \& Finance Librarianship}, vol.~21, no.~1, pp. 1--25, 2016.'''
                    print("--------Entry original --------------")
                    print(entry)
                    print()
                    fields = entry.split('\\newblock')
                    # if len(fields) < 3:
                    #     print(f"The bibitem {i} of file {filename} does not contain all the three blocks")
                    #     count_error += 1
                    #     continue
                    
                    label = fields[0].strip()
                                    
                    # try:
                    file_type = 'ACL/ACM'

                    # process the fields string by removing newlines and spaces
                    data=[ re.sub('\s+',' ',field.strip().replace('\n', ' ')) for field in fields]
                    # data_1 = re.sub('\s+',' ',fields[0].strip().replace('\n', ' '))
                    # data_2 = re.sub('\s+',' ',fields[1].strip().replace('\n', ' '))
                    # data_3 = re.sub('\s+',' ',fields[2].strip().replace('\n', ' '))






                    # for d in data:
                    #     print(d, end='\n\n')

                    Matched_data = dict()
                    for i in range(1,21):
                        Matched_data[str(i)] = []

                    if len(data) > 0:
                        Matched_data['1'] = re.findall(Patterns["Author_ACM_ACL_1"], data[0])
                        Matched_data['2'] = re.findall(Patterns["YEAR_ACM_ACL_1"], data[0])
                        Matched_data['3'] = re.findall(Patterns["BIB_ACM_ACL_1"], data[0])
                        Matched_data['15'] = re.findall(Patterns["Author_ACM_ACL_2"], data[0])

                        Matched_data['16'] = re.findall(Patterns["No_new_block_Author_1"], data[0])
                        Matched_data['17'] = re.findall(Patterns["No_new_block_Title_1"], data[0])
                        Matched_data['18'] = re.findall(Patterns["No_new_block_Publisher_1"], data[0])
                        Matched_data['19'] = re.findall(Patterns["No_new_block_Vol_1"], data[0])
                        Matched_data['20'] = re.findall(Patterns["No_new_block_Id_1"], data[0])
                        # print("No newblock author match")
                        # print(Matched_data['16'])
                        # # print(Matched_data['17'])
                        # # print(Matched_data['18'])
                        # # print(Matched_data['19'])
                        # print("No newblock Id")
                        # print(Matched_data['20'])
                        # input()
                    if len(data) > 1:
                        Matched_data['4'] = re.findall(Patterns["Article_ACM_ACL_2"], data[1])
                        Matched_data['5'] = re.findall(Patterns["Book_ACM_ACL_2"], data[1])
                        Matched_data['6'] = re.findall(Patterns["Publisher_ACM_ACL_2"], data[1])
                        Matched_data['7'] = re.findall(Patterns["Page_ACM_ACL_2"], data[1])
                        Matched_data['7'] = re.findall(Patterns["Page_ACM_ACL_2"], data[1])
                        Matched_data['8'] = re.findall(Patterns["Title_IEEE_ARXIV_CVPR_2"], data[1])
                        # print(data[1])
                        # print(Matched_data['8'])
                        # input()
                    if len(data) > 2:
                        Matched_data['9'] = re.findall(Patterns["Journal_ACM_3"], data[2])
                        Matched_data['10'] = re.findall(Patterns["Year_ACM_ACL_3"], data[2])
                        Matched_data['11'] = re.findall(Patterns["Volumne_ACM_ACL_3"], data[2])
                        Matched_data['12'] = re.findall(Patterns["Pages_ACM_ACL_3"], data[2])
                        Matched_data['13'] = re.findall(Patterns["Publisher_IEEE_aRXIV_CVPR_3"], data[2])
                        Matched_data['14'] = re.findall(Patterns["Pages_IEEE_ARXIV_CVPR_3"], data[2])
                    # print(Matched_data)
                    # input()
                    paper_format = None
                    if len(Matched_data['4']) or len(Matched_data['5']):
                        paper_format = "ACL/M"
                        information = get_information(root, Matched_data, output_directory + paper_name, paper_format)
                        print("==============================ACM/L=====================================================")
                        print(information)  
                        print("========================================================================================")                   
                    elif(len(Matched_data['17'])):
                        information= get_information3(root, Matched_data, output_directory + paper_name, data[0])
                        print("============================ NO \\newblock IEEE==========================================")
                        print(information)  
                        print("========================================================================================") 

                    else:

                        paper_format = "IEEE/ARXIV/CVPR"
                        information = get_information2(root, Matched_data, output_directory + paper_name, data[0])
                        print("===========================IEEE/ARXIV/CVPR==============================================")
                        print(information)  
                        print("========================================================================================")    
            
                    # add the subelement to the root element of the tree with the information dictionary
                    entry_elem = ET.SubElement(root, 'entry', {'label': label})
                    for key, value in information.items():
                        if key == 'author':
                            author_elem = ET.SubElement(entry_elem, 'author')
                            for i, author in enumerate(value):
                                ET.SubElement(author_elem, f'author{i+1}').text = author
                                # author_elem = ET.SubElement(entry_elem, f'author{i+1}')
                                # author_elem.text = author
                            continue
                        if key == 'pages' and type(value) != str:
                            ET.SubElement(entry_elem, key).text = f'{value[0]}--{value[1]}'
                            continue

                        ET.SubElement(entry_elem, key).text = value


            tree = ET.ElementTree(root)
            ET.indent(tree, space="\t", level=0)
            
            # tree.write('ACL_bbl.xml', encoding='utf-8', xml_declaration=True)
            tree.write(f'{output_directory + paper_name}_bbl.xml', encoding='utf-8', xml_declaration=True)
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print(filename, "Done")
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            input("Press Enter to continue...")
