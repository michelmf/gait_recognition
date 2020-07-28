####################################################################################
### teste GEI                                                
####################################################################################

# Manipulação de Imagens
from skimage.io import imread, imsave, imshow
from scipy.misc import imresize

# Configuração e Manipulação de arquivos
import os
import configparser
from glob import glob

# Helpers
from functions      import utils
from functions.tool import *
from time           import sleep

####################################################################################
### Configuração                                                
####################################################################################

# Configuração dos paths para leitura das imagens
cfg = configparser.ConfigParser()
cfg.read('config.cfg')

# Verificação dos paths
print('\n\n\n\n\n')
print('####################################################################################################################################################################################')
print(f"Caminho para o CASIA-B    : {cfg.get('PATH','root_path')}")
print(f"Caminho para os resultados: {cfg.get('PATH','output_path')}")
print('####################################################################################################################################################################################')

# caminho base para o casia-b
root_path   = cfg.get('PATH','root_path')
output_path = cfg.get('PATH','output_path')

# Processamento de todos os subjects caso seja all, caso contrário, utiliza o especificado
subjects = utils.SUBJECT if cfg.get('EXECUTION','execution_subject') == 'all' else cfg.get('EXECUTION','execution_subject').split(',')

# Escolha de quais posições serão calculadas. Caso all, todas. Caso contrário, utilizar o atribuído na configuração
execution_walking_status = utils.WALKING_STATUS if cfg.get('EXECUTION','execution_walking_status') == 'all' else cfg.get('EXECUTION','execution_walking_status').split(',')

# Ângulos a serem calculados. Caso all, todas. Caso contrário, utilizar o atribuído na configuração 
execution_angles = utils.ANGLES if cfg.get('EXECUTION','execution_angle') == 'all' else cfg.get('EXECUTION','execution_angle').split(',')

# Paths a serem gerados
print(f'Subjects considerados      : {subjects}')
print(f'Walking status considerados: {execution_walking_status}')
print(f'Ângulos        considerados: {execution_angles}')
print('####################################################################################################################################################################################')

# Criando os paths necessários. Mais readable...
image_paths = []

for subject in subjects:
    for status in execution_walking_status:
        for angle in execution_angles:
            image_paths.append(os.path.join(subject, status, angle))

print(f'Quantidade de paths  : {len(image_paths)}')
print(f'Pasta com imagens    : {image_paths}')
print('####################################################################################################################################################################################')

####################################################################################
### Processamento de Imagens                                          
####################################################################################

# # 1. Função load_image_path_list: Leitura das imagens dada uma pasta específica
print(f'Arquivos encontrados na pasta {os.path.join(root_path, image_paths[0])}')
print(load_image_path_list(os.path.join(root_path, image_paths[0])))
img_files = os.path.join(root_path, image_paths[0])
print('####################################################################################################################################################################################')

# # 2. Função image_path_list_to_image_pic_list: imread das imagens encontradas na função acima
print(f'Arquivos encontrados na pasta {os.path.join(root_path, image_paths[0])}')
print(f'Quantidade de imagens encontradas: {len(image_path_list_to_image_pic_list(img_files))}')
# imgs = image_path_list_to_image_pic_list(img_files)
# print('####################################################################################################################################################################################')

# # 3. Função build_GEI: Crop e sobreposição das imagens
# gei_image = build_GEI(imgs)

# for path in image_paths:
#     os.makedirs(os.path.join(output_path,path),0o666)
#     imsave(os.path.join(output_path,path,'gei_final.bmp'), gei_image)
# #####################################################################################
