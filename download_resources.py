from decouple import config
import gdown
import zipfile

#1 Descargar wav
url = config("RAW_DATA")
name_raw = config("FOLDER_NAME")
output = config("RAW_FOLDER")+name_raw
gdown.download(url, output, quiet=False)
# Descomprimir 
with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall(config("RAW_FOLDER"))



#2 Descargar csv
url = config("CSV_DATA")
name_raw = config("CSV_FILE")
output = config("CSV_FOLDER")+name_raw
gdown.download(url, output, quiet=False)
# Descomprimir 
with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall(config("CSV_FOLDER"))
