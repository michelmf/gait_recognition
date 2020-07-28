##### Ao baixar o CASIA-B, os dados vêm compactados em tar.gz. Esse simples script realiza a descompactação de todos os arquivos
import os
import tarfile
import configparser
from tqdm import tqdm
from glob import glob

# Leitura do arquivo de configuração para extração do root path
cfg = configparser.ConfigParser()
cfg.read('config.cfg')
root_path = cfg.get('PATH','root_path')

# Leitura dos arquivos da pasta
tar_files = glob(os.path.join(root_path,'*.tar.gz'))
os.chdir(root_path) # Altera para a pasta onde se encontram os tar.gz

# extração
with tqdm(total=len(tar_files)) as pbar:
    for tar_file in tar_files:
        tar = tarfile.open(tar_file, 'r:gz')
        tar.extractall()
        tar.close()
        pbar.update(1)

print('Done.')