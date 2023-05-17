import os
import tarfile


path = 'Arxiv_files'
# for extracting files
path_extracted = 'Arxiv_files_extracted'

def rename_file(path):


    folders = os.listdir(path)

    for folder in folders:
        folder_path = os.path.join(path,folder)
        if not os.path.isdir(folder_path):
            continue
        files = os.listdir(folder_path)
        for file in files:
            # print(folder, file)
            # rename file to .tar.gz
            # print(os.path.join(folder, file), os.path.join(folder, file + '.tar.gz'))
            # print(os.getcwd())
            if file.endswith('.tar.gz'):
                continue
                # os.rename(os.path.join(folder_path, file), os.path.join(folder_path, file)[:-7])
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, file + '.tar.gz'))

            # input()



# scp -r -P 2022 patidarritesh@10.0.62.212:/mnt/LACIE/ritesh/partial_sources/050901 ./




def extract_file(path, path_extracted):
    if not os.path.exists(path_extracted):
        os.mkdir(path_extracted)

    folders = os.listdir(path)
    for folder in folders:
        folder_path = os.path.join(path,folder)
        folder_path_extracted = os.path.join(path_extracted,folder) 
        if not os.path.isdir(folder_path):
            continue
        files = os.listdir(folder_path)

        for file in files:
            # print(os.getcwd())
            # print(folder_path, file)
            # print(folder_path)
            # print(folder_path_extracted)
            # os.system('tar -xvzf ' + os.path.join(folder_path, file) + ' -C ' + folder_path)
            if file.endswith('.tar.gz'):
                file_path = os.path.join(folder_path_extracted, file)
                # print(folder_path_extracted)

                # create folder for extracted files
                if not os.path.exists(file_path[:-7]):
                    os.makedirs(file_path[:-7])
                try:
                    # Open the .tar.gz file
                    with tarfile.open(os.path.join(folder_path,file), 'r:gz') as tar:
                        tar.extractall(path=file_path[:-7])  # Replace with the path where you want to extract the contents
                except: 
                    print('error in extracting file: ', os.path.join(folder_path,file))
                    continue



rename_file(path)
extract_file(path, path_extracted)