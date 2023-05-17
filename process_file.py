import os
import tarfile


path = 'Arxiv_files'

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
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, file + '.tar.gz'))

            # input()




# scp -r -P 2022 patidarritesh@10.0.62.212:/mnt/LACIE/ritesh/partial_sources/050901 ./


# for extracting files
path_extracted = 'Arxiv_files_extracted'

folders = os.listdir(path)
for folder in folders:
    folder_path = os.path.join(path,folder)
    folder_path_extracted = os.path.join(path_extracted,folder) 
    if not os.path.isdir(folder_path):
        continue
    files = os.listdir(folder_path)
    # create folder for extracted files
    if not os.path.exists(folder_path_extracted):
        os.makedirs(folder_path_extracted)
    for file in files:
        print(os.getcwd())
        print(file)
        print(folder_path)
        print(folder_path_extracted)
        # os.system('tar -xvzf ' + os.path.join(folder_path, file) + ' -C ' + folder_path)
        if file.endswith('.tar.gz'):
            # Open the .tar.gz file
            with tarfile.open(file, 'r:gz') as tar:
                tar.extractall(path=folder_path_extracted)  # Replace with the path where you want to extract the contents
        input()

