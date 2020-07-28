# Funções para auxílio da execução da criação dos GEIs
from glob import glob

# Variáveis para auxiliar no processamento das imagens
SUBJECT        = [str(subject).zfill(3) for subject in range(1,125)] # de 001 a 124
WALKING_STATUS = ['bg-01', 'bg-02', 'cl-01', 'cl-02', 'nm-01', 'nm-02', 'nm-03', 'nm-04', 'nm-05', 'nm-06']
ANGLES         = [str(angles).zfill(3) for angles in range(0,181,18)] # de 18 em 18 graus