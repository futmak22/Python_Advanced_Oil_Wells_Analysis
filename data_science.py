#-----------------------------------------------------
# Julio Cesar Galvez Espinosa
#-----------------------------------------------------
import pandas as pd
import os

# 1) - Extracción del path de la data de pozos petroliferos.
oil_wells = os.getcwd() + '/data_sets/Data15_9-19A-CORE_B.xlsx'

core_data = pd.read_excel(oil_wells ,na_values=' ')
