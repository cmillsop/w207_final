#! python

import os
from zipfile import ZipFile
from glob import glob
import shutil

ARCHIVE_PATH = './data/archived'
EXTRACT_PATH = './data/extracted'

print("Checking directories and cleaning old extracted files...")
if not os.path.exists(ARCHIVE_PATH):
    os.makedirs(ARCHIVE_PATH)
if os.path.exists(EXTRACT_PATH):
    shutil.rmtree(EXTRACT_PATH)
os.makedirs(EXTRACT_PATH)

print("Checking kaggle files for updates...")
os.system(f'kaggle competitions download -c airbnb-recruiting-new-user-bookings -p {ARCHIVE_PATH}')

print("Extracting and collating data files...")
archive_files = glob(f'{ARCHIVE_PATH}/*.zip')
for archive in (archive_files):
    with ZipFile(archive, 'r') as zip_archive:
        zip_archive.extractall(EXTRACT_PATH)
data_files =  glob(f'{EXTRACT_PATH}/*/*.csv')
for file_path in data_files:
    file_name = os.path.basename(file_path)
    os.rename(f'{EXTRACT_PATH}/{file_name}')

print("Clearing empty archive directories...")
dir_names = os.walk(EXTRACT_PATH)
for root, dirs, files in dir_names:
    for dir_name in dirs:
        os.rmdir(dir_name)

print("Complete")