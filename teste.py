# Manipulação de Imagens
from skimage.io import imread, imsave, imshow
from scipy.misc import imresize

# Configuração e Manipulação de arquivos
import os
import configparser
from glob import glob

# Helpers
from functions import utils
from time      import sleep
from tqdm      import tqdm

####################################################################################
### Configuração                                                
####################################################################################

# Configuração dos paths para leitura das imagens
cfg = configparser.ConfigParser()
cfg.read('config.cfg')


# Verificação dos paths
print('####################################################################################################################################################################################')
print(f"Caminho para o CASIA-B    : {cfg.get('PATH','root_path')}")
print(f"Caminho para os resultados: {cfg.get('PATH','output_path')}")

# Execução
print('####################################################################################################################################################################################')
print(f"Caminho para o CASIA-B    : {cfg.get('EXECUTION','execution_subject')}")
print(f"Caminho para os resultados: {cfg.get('EXECUTION','execution_walking_status')}") 
print(f"Caminho para os resultados: {cfg.get('EXECUTION','execution_angle')}")


####################################################################################
### Processamento                                              
####################################################################################

# caminho base para o casia-b
root_path = cfg.get('PATH','root_path')


# Processamento de todos os subjects caso seja all, caso contrário, utiliza o especificado
subjects = utils.SUBJECT if cfg.get('EXECUTION','execution_subject') == 'all' else cfg.get('EXECUTION','execution_subject').split(',')

# Escolha de quais posições serão calculadas. Caso all, todas. Caso contrário, utilizar o atribuído na configuração
execution_walking_status = utils.WALKING_STATUS if cfg.get('EXECUTION','execution_walking_status') == 'all' else cfg.get('EXECUTION','execution_walking_status').split(',')

# Ângulos a serem calculados. Caso all, todas. Caso contrário, utilizar o atribuído na configuração 
execution_angles = utils.ANGLES if cfg.get('EXECUTION','execution_angle') == 'all' else cfg.get('EXECUTION','execution_angle').split(',')

# Gerando todos os paths que devem ser verificados
# for 

print('####################################################################################################################################################################################')
print(f'Subjects considerados      : {subjects}')
print(f'Walking status considerados: {execution_walking_status}')
print(f'Ângulos        considerados: {execution_angles}')
print('####################################################################################################################################################################################')

# Criando os paths necessários. Mais readable...
image_paths = []
for subject in subjects:
    for status in execution_walking_status:
        for angle in execution_angles:
            image_paths.append(os.path.join(root_path, subject, status, angle))

print(f'Quantidade de paths: {len(image_paths)}')
print('####################################################################################################################################################################################')

# Barra de processamento...
for image in tqdm(image_paths):
    pass

####################################################################################
### Processamento de Imagens                                          
####################################################################################