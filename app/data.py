########################################
##librerias

import requests
import pandas as pd
import numpy as np
import json
import plotly.graph_objects as go
import plotly.express as px

import warnings
warnings.filterwarnings("ignore")

########################################
## Conexión Kobo

##### Evaluacion de necesidades

TOKEN = ''
KF_URL = 'kobo.humanitarianresponse.info'
# Evaluacion de necesidades
ASSET_UID = ''
#ASSET_UID = 'azaSuu69RwWhDLpFLx4smT'
QUERY = '{"_submission_time":{"$gt":"2021-01-01T18:34:12.498-08:00"}}'
#QUERY = ''
URL = f'https://{KF_URL}/api/v2/assets/{ASSET_UID}/data/?query={QUERY}&format=json'
#URL = f'https://{KF_URL}/api/v2/assets/{ASSET_UID}/data/format=json'

headers = {"Authorization": f'Token {TOKEN}'}

response = requests.get(URL, headers=headers)
#response

#data = json.loads(response)
data = response.json()

df = pd.DataFrame(data['results'])
# export to xls

df_final = pd.DataFrame()
df_final['_id'] = df['_id']
df_final['_validation_status'] = df['_validation_status']
contar = len(df.index)
contar


########################################
## Depuración base

##################
## Quien diligencia

df['__1/enc'] = df['__1/enc'].replace(np.nan, '')
df['dat_enc/enc'] = df['dat_enc/enc'].replace(np.nan, '')
df["enc"] = df[['__1/enc','dat_enc/enc']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df_final['1. ¿Quién responde la encuesta?/lider'] = 0
df_final['1. ¿Quién responde la encuesta?/organizacion social'] = 0
df_final['1. ¿Quién responde la encuesta?/Miembro de la comunidad'] = 0
df_final['1. ¿Quién responde la encuesta?/Migrante en tránsito con vocación caminante'] = 0
df_final['1. ¿Quién responde la encuesta?/Grupo focal'] = 0
df_final['1. ¿Quién responde la encuesta?/Grupo sectorial'] = 0
df_final['1. ¿Quién responde la encuesta?/Joven / Adolescente'] = 0
df_final['1. ¿Quién responde la encuesta?/Autoridad de la comunidad'] = 0
df_final['1. ¿Quién responde la encuesta?/No sabe'] = 0
df_final['1. ¿Quién responde la encuesta?/Otro'] = 0

for i in range(contar):
    if df['enc'][i] == 'lider':
        df_final['1. ¿Quién responde la encuesta?/lider'][i] = 1
    elif df['enc'][i] == 'org':
        df_final['1. ¿Quién responde la encuesta?/organizacion social'][i] = 1
    elif df['enc'][i] == 'miem_c':
        df_final['1. ¿Quién responde la encuesta?/Miembro de la comunidad'][i] = 1
    elif df['enc'][i] == 'camin':
        df_final['1. ¿Quién responde la encuesta?/Migrante en tránsito con vocación caminante'][i] = 1
    elif df['enc'][i] == 'grup':
        df_final['1. ¿Quién responde la encuesta?/Grupo focal'][i] = 1    
    elif df['enc'][i] == 'sect':
        df_final['1. ¿Quién responde la encuesta?/Grupo sectorial'][i] = 1  
    elif df['enc'][i] == 'jov':
        df_final['1. ¿Quién responde la encuesta?/Joven / Adolescente'][i] = 1  
    elif df['enc'][i] == 'aut_com':
        df_final['1. ¿Quién responde la encuesta?/Autoridad de la comunidad'][i] = 1  
    elif df['enc'][i] == 'no_sabe':
        df_final['1. ¿Quién responde la encuesta?/No sabe'][i] = 1  
    elif df['enc'][i] == 'otro':
        df_final['1. ¿Quién responde la encuesta?/Otro'][i] = 1  


##################
## Tematicas para recolectar información

df['__1/inf'] = df['__1/inf'].replace(np.nan, '')
df['dat_enc/inf'] = df['dat_enc/inf'].replace(np.nan, '')
df['inf'] = df[['__1/inf','dat_enc/inf']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Educación'] = 0
df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Migración'] = 0
df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Protección'] = 0
df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Salud'] = 0
df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Seguridad alimentaria'] = 0
df_final['2. Seleccione las temáticas para las cuales desea recolectar información/WASH'] = 0


for i in range(contar):
    
    if df['inf'][i] != '':
        try:
            if df['inf'][i].count('todos') > 0:
                todos = df['inf'][i].count('todos')

                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Educación'][i] = todos
                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Migración'][i] = todos
                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Protección'][i] = todos
                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Salud'][i] = todos
                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Seguridad alimentaria'][i]= todos
                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/WASH'][i] = todos 
            else:
                educ = df['inf'][i].count('educ')
                migr = df['inf'][i].count('migr')
                prot = df['inf'][i].count('prot')
                salud = df['inf'][i].count('salud')
                seg_alim = df['inf'][i].count('seg_alim')
                wash = df['inf'][i].count('wash')

                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Educación'][i] = educ
                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Migración'][i] = migr
                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Protección'][i] = prot
                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Salud'][i] = salud
                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/Seguridad alimentaria'][i]= seg_alim
                df_final['2. Seleccione las temáticas para las cuales desea recolectar información/WASH'][i] = wash  
        except:
            pass



##################
## Tipo de emergencia


vals_to_replace = {'cronica':'Cronica', 'subita':'Subita'}
df['__1/tipo_em'] = df['__1/tipo_em'].map(vals_to_replace)
df['__1/tipo_em'] = df['__1/tipo_em'].replace(np.nan, '')
df_final['3. Tipo de emergencia'] = df['__1/tipo_em']


##################
## Localización

# Departamento
df['info_gen_g1/departamento'] = df['info_gen_g1/departamento'].replace(np.nan, '')
df['info_gen_g/departamento'] = df['info_gen_g/departamento'].replace(np.nan, '')
df['departamento'] = df[['info_gen_g1/departamento','info_gen_g/departamento']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['departamento'] = df['departamento'].str.replace('_',' ')
df_final['4. Departamento'] = df['departamento']

# Municipio
df['info_gen_g1/municipio'] = df['info_gen_g1/municipio'].replace(np.nan, '')
df['info_gen_g/municipio'] = df['info_gen_g/municipio'].replace(np.nan, '')
df['Municipio'] = df[['info_gen_g1/municipio','info_gen_g/municipio']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['Municipio'] = df['Municipio'].str.replace('_',' ')
df_final['5. Municipio'] = df['Municipio']

# Corregimiento
df['info_gen_g1/corregimiento'] = df['info_gen_g1/corregimiento'].replace(np.nan, '')
df['info_gen_g/corregimiento'] = df['info_gen_g/corregimiento'].replace(np.nan, '')
df['Corregimeinto'] = df[['info_gen_g1/corregimiento','info_gen_g/corregimiento']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['Corregimeinto'] = df['Corregimeinto'].str.replace('_',' ')
df_final['6. Corregimeinto'] = df['Corregimeinto']

# Vereda
df['info_gen_g1/vereda'] = df['info_gen_g1/vereda'].replace(np.nan, '')
df['info_gen_g/vereda'] = df['info_gen_g/vereda'].replace(np.nan, '')
df['Vereda'] = df[['info_gen_g1/vereda','info_gen_g/vereda']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['Vereda'] = df['Vereda'].str.replace('_',' ')
df_final['7. Vereda'] = df['Vereda']

# Barrio
df['info_gen_g1/barr-asent-comu'] = df['info_gen_g1/barr-asent-comu'].replace(np.nan, '')
df['info_gen_g/barr-asent-comu'] = df['info_gen_g/barr-asent-comu'].replace(np.nan, '')
df['Barrio'] = df[['info_gen_g1/barr-asent-comu','info_gen_g/barr-asent-comu']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['Barrio'] = df['Barrio'].str.replace('_',' ')
df_final['8. Barrio, asentamiento, comunidad'] = df['Barrio']

# Ubicacion
df['info_gen_g1/ubi'] = df['info_gen_g1/ubi'].replace(np.nan, '')
df['info_gen_g/ubi'] = df['info_gen_g/ubi'].replace(np.nan, '')
df['Ubicacion'] = df[['info_gen_g1/ubi','info_gen_g/ubi']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df_final['9. Ubicación'] = df['Ubicacion']

# Latitud
df_final['Latitud'] = pd.to_numeric(df_final['9. Ubicación'].str.split().str[0].str.strip(),downcast='float')

# longitud
df_final['Longitud'] = pd.to_numeric(df_final['9. Ubicación'].str.split().str[1].str.strip(),downcast='float')

# Zona
vals_to_replace = {'urbano':'Urbano', 'rural':'Rural', 'periurbano':'Periurbano'}
df['info_gen_g1/rur_urb'] = df['info_gen_g1/rur_urb'].map(vals_to_replace)
df['info_gen_g1/rur_urb'] = df['info_gen_g1/rur_urb'].replace(np.nan, '')
df_final['10. ¿En qué área o zona se ubica la comunidad?'] = df['info_gen_g1/rur_urb']

##################
## Caractersiticas de la comunidad

# caracteristicas
df['_1/carac_asen'] = df['_1/carac_asen'].replace(np.nan, '')
df['info_gen_g/carac_asen'] = df['info_gen_g/carac_asen'].replace(np.nan, '')
df['Caracterizacion'] = df[['_1/carac_asen','info_gen_g/carac_asen']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['Caracterizacion'] = df['Caracterizacion'].replace('', '1')

df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto veredal'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto comunal'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto campesino'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Agua potable'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Alcantarillado'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Energía eléctrica'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Instituciones educativas'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Gas natural'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Hospitales y/o puestos de salud'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Internet'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Presencia de policía y/o ejército'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Saneamiento'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Vías pavimentadas'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Viviendas en ladrillos, concreto, cemento'] = 0
df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Ninguna'] = 0

         
for i in range(contar):
    
    vered = df['Caracterizacion'][i].count('vered')
    comun = df['Caracterizacion'][i].count('comun')
    camp = df['Caracterizacion'][i].count('camp')
    agua = df['Caracterizacion'][i].count('agua')
    alcant = df['Caracterizacion'][i].count('alcant')
    energ = df['Caracterizacion'][i].count('energ')
    escuelas = df['Caracterizacion'][i].count('escuelas')
    gas = df['Caracterizacion'][i].count('gas')
    hosp = df['Caracterizacion'][i].count('hosp')
    intern = df['Caracterizacion'][i].count('intern')
    polic = df['Caracterizacion'][i].count('polic')
    saneam = df['Caracterizacion'][i].count('saneam')
    vias_pav = df['Caracterizacion'][i].count('vias_pav')
    vivi_lad = df['Caracterizacion'][i].count('vivi_lad')
    
    
    if df['Caracterizacion'][i] != '1':
    
        try:
    
            if df['Caracterizacion'][i].count('ninguna') > 0:
                
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Ninguna'][i] = 1
                   
            else:
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto veredal'][i] = vered
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto comunal'][i] = comun
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto campesino'][i] = camp
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Agua potable'][i] = agua
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Alcantarillado'][i] = alcant
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Energía eléctrica'][i] = energ
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Instituciones educativas'][i] = escuelas
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Gas natural'][i] = gas
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Hospitales y/o puestos de salud'][i] = hosp
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Internet'][i] = intern
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Presencia de policía y/o ejército'][i] = polic
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Saneamiento'][i] = saneam
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Vías pavimentadas'][i] = vias_pav
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Viviendas en ladrillos, concreto, cemento'][i] = vivi_lad
                df_final['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Ninguna'][i] = 0
    
        except:
            pass
        
    else:
        pass


# autoreconoce como un grupo étnico
df['_1/indig'] = df['_1/indig'].replace(np.nan, '')
df['info_gen_g/indig'] = df['info_gen_g/indig'].replace(np.nan, '')
df['auto_etnico'] = df[['_1/indig','info_gen_g/indig']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
vals_to_replace = {'si':'Si', 'no':'No', 'nose':'No sabe', 'ns':'No sabe'}
df['auto_etnico'] = df['auto_etnico'].map(vals_to_replace)
df['auto_etnico'] = df['auto_etnico'].replace(np.nan, '')

df_final['12. ¿La comunidad se autoreconoce como un grupo étnico?'] = df['auto_etnico']

# censos o caracterizaciones poblacionales
df['_1/censos'] = df['_1/censos'].replace(np.nan, '')
df['info_gen_g/censos'] = df['info_gen_g/censos'].replace(np.nan, '')
df['censos'] = df[['_1/censos','info_gen_g/censos']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
vals_to_replace = {'si':'Si', 'no':'No', 'nose':'No sabe', 'ns':'No sabe'}
df['censos'] = df['censos'].map(vals_to_replace)
df['censos'] = df['censos'].replace(np.nan, '')
df_final['13. ¿En la comunidad se han realizado censos o caracterizaciones poblacionales?'] = df['censos']

# ¿Qué entidad los ha realizado?
df['_1/censos_quien'] = df['_1/censos_quien'].replace(np.nan, '')
df['info_gen_g/censos_quien'] = df['info_gen_g/censos_quien'].replace(np.nan, '')
df['censos_quien'] = df[['_1/censos_quien','info_gen_g/censos_quien']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df_final['¿Qué entidad los ha realizado?'] = df['censos_quien']

# ¿Cuándo se realizó el último censo o caracterización?
df['_1/censos_cuando'] = df['_1/censos_cuando'].replace(np.nan, '')
df['info_gen_g/censos_cuando'] = df['info_gen_g/censos_cuando'].replace(np.nan, '')
df['censos_cuando'] = df[['_1/censos_cuando','info_gen_g/censos_cuando']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df_final['¿Cuándo se realizó el último censo o caracterización?'] = df['censos_cuando']

# ¿En la comunidad se han realizado evaluaciones de necesidades previas?
df['_1/ev_nec'] = df['_1/ev_nec'].replace(np.nan, '')
df['eva_previas'] = df['_1/ev_nec']
vals_to_replace = {'si':'Si', 'no':'No', 'nose':'No sabe', 'ns':'No sabe'}
df['eva_previas'] = df['eva_previas'].map(vals_to_replace)
df['eva_previas'] = df['eva_previas'].replace(np.nan, '')
df_final['14. ¿En la comunidad se han realizado evaluaciones de necesidades previas?'] = df['eva_previas']

# ¿Qué organización o entidad ha realizado evaluaciones de necesidades en la comunidad?
df['_1/ev_nec_quien'] = df['_1/ev_nec_quien'].replace(np.nan, '')
df_final['¿Qué organización o entidad ha realizado evaluaciones de necesidades en la comunidad?'] = df['_1/ev_nec_quien']

# 15. Indique aproximadamente cuantas familias habitan en el Barrio, asentamiento o comunidad
df['_1/fam'] = df['_1/fam'].replace(np.nan, '')
df['info_gen_g/fam'] = df['info_gen_g/fam'].replace(np.nan, '')
df['familias'] = df[['_1/fam','info_gen_g/fam']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['familias'] = df['familias'].replace('', 0)
df['familias'] = pd.to_numeric(df['familias'], downcast='integer')
df_final['15. Indique aproximadamente cuantas familias habitan en el Barrio, asentamiento o comunidad'] = df['familias']

# 18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?
df['_1/necesidades'] = df['_1/necesidades'].replace(np.nan, '')
df['info_basica_g/necesidades'] = df['info_basica_g/necesidades'].replace(np.nan, '')
df['necesidades_NNA'] = df[['_1/necesidades','info_basica_g/necesidades']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a agua potable'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a alimentación básica'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a asistencia en salud'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a educación'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a instalaciones sanitarias'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Alojamiento deficitario'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Asistencia a primera infancia'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia física'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia sexual'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Deserción escolar'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Embarazo adolescente'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Escasez de elementos de higiene y desinfección'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Espacios de recreación y esparcimiento'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Falta de oportunidades laborales de los cuidadores'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Hacinamiento'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Incremento de enfermedades o epidemias'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Saneamiento básico (Acueducto, alcantarillado y recolección de basuras)'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Situación de migración'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Trabajo infantil'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Otra'] = 0
df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/No sabe (Está en fase de investigación)'] = 0

         
for i in range(contar):
    
    agua = df['necesidades_NNA'][i].count('agua')
    alim = df['necesidades_NNA'][i].count('alim')
    saud = df['necesidades_NNA'][i].count('saud')
    educacion = df['necesidades_NNA'][i].count('educacion')
    instalacio_san = df['necesidades_NNA'][i].count('instalacio_san')
    alojam = df['necesidades_NNA'][i].count('alojam')
    prim_inf = df['necesidades_NNA'][i].count('prim_inf')
    viol_fisica = df['necesidades_NNA'][i].count('viol_fisica')
    viol_sexual = df['necesidades_NNA'][i].count('viol_sexual')
    desercion = df['necesidades_NNA'][i].count('desercion')
    embarazo_adol = df['necesidades_NNA'][i].count('embarazo_adol')
    esc_higi = df['necesidades_NNA'][i].count('esc_higi')
    espacios_recre = df['necesidades_NNA'][i].count('espacios_recre')
    trabajo_cuid = df['necesidades_NNA'][i].count('trabajo_cuid')
    hacinam = df['necesidades_NNA'][i].count('hacinam')
    salud_enferm = df['necesidades_NNA'][i].count('salud_enferm')
    reclutam = df['necesidades_NNA'][i].count('reclutam')
    saneam = df['necesidades_NNA'][i].count('saneam')
    migrac = df['necesidades_NNA'][i].count('migrac')
    trabajo_inf = df['necesidades_NNA'][i].count('trabajo_inf')
    otra = df['necesidades_NNA'][i].count('otra')
    
    
    try:
        if df['necesidades_NNA'][i].count('no_sabe') > 0:
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/No sabe (Está en fase de investigación)'][i] = 1
                   
        else:
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a agua potable'][i] = agua
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a alimentación básica'][i] = alim
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a asistencia en salud'][i] = saud
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a educación'][i] = educacion
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a instalaciones sanitarias'][i] = instalacio_san
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Alojamiento deficitario'][i] = alojam
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Asistencia a primera infancia'][i] = prim_inf
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia física'][i] = viol_fisica
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia sexual'][i] = viol_sexual
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Deserción escolar'][i] = desercion
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Embarazo adolescente'][i] = embarazo_adol
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Escasez de elementos de higiene y desinfección'][i] = esc_higi
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Espacios de recreación y esparcimiento'][i] = espacios_recre
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Falta de oportunidades laborales de los cuidadores'][i] = trabajo_cuid
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Hacinamiento'][i] = hacinam
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Incremento de enfermedades o epidemias'][i] = salud_enferm
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.'][i] = reclutam
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Saneamiento básico (Acueducto, alcantarillado y recolección de basuras)'][i] = saneam
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Situación de migración'][i] = migrac
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Trabajo infantil'][i] = trabajo_inf
            df_final['18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Otra'][i] = otra

    except:
        pass


## 19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?
df['_1/asent_informal'] = df['_1/asent_informal'].replace(np.nan, '')
df['info_basica_g/asent_informal'] = df['info_basica_g/asent_informal'].replace(np.nan, '')
df['asentamiento humano informal'] = df[['_1/asent_informal','info_basica_g/asent_informal']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['asentamiento humano informal'] = df['asentamiento humano informal'].replace('si', 'Si').replace('no', 'No').replace('', 'No responde').replace('no_sabe', 'No sabe')
df_final['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'] = df['asentamiento humano informal']

# 23. ¿Cómo es el terreno donde está asentada la comunidad?
df['_1/terreno'] = df['_1/terreno'].replace(np.nan, '')
df['desastres_nat_g/terreno'] = df['desastres_nat_g/terreno'].replace(np.nan, '')
df['terreno'] = df[['_1/terreno','desastres_nat_g/terreno']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Bosque'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a bahia, estuario, lagunas'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a los cauces de ríos, quebradas, arroyos'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca de volcanes'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte alta de una montaña'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte baja de una montaña'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Humedales'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Isla'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Paramo'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Terreno desértico'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Zona costera'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Ninguna de las anteriores'] = 0
df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Otro'] = 0


for i in range(contar):
    
    bosque = df['terreno'][i].count('bosque')
    bahia = df['terreno'][i].count('bahia')
    rios = df['terreno'][i].count('rios')
    volcanes = df['terreno'][i].count('volcanes')
    montana_alta = df['terreno'][i].count('montana_alta')
    montana_baja = df['terreno'][i].count('montana_baja')
    humed = df['terreno'][i].count('humed')
    isla = df['terreno'][i].count('isla')
    paramo = df['terreno'][i].count('paramo')
    terr_des = df['terreno'][i].count('terr_des')
    zona_cost = df['terreno'][i].count('zona_cost')
    otro = df['terreno'][i].count('otro')
    
    
    try:
        if df['terreno'][i].count('ninguna') > 0:
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Ninguna de las anteriores'][i] = 1
                   
        else:
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Bosque'][i] = bosque
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a bahia, estuario, lagunas'][i] = bahia
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a los cauces de ríos, quebradas, arroyos'][i] = rios
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca de volcanes'][i] = volcanes
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte alta de una montaña'][i] = montana_alta
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte baja de una montaña'][i] = montana_baja
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Humedales'][i] = humed
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Isla'][i] = isla
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Paramo'][i] = paramo
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Terreno desértico'][i]= terr_des
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Zona costera'][i] = zona_cost
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Ninguna de las anteriores'][i] = 0
            df_final['23. ¿Cómo es el terreno donde está asentada la comunidad?/Otro'][i] = otro

    except:
        pass

##################
## Migración

## ¿En la comunidad viven personas migrantes?

df['migrac1/viven_migrantes'] = df['migrac1/viven_migrantes'].replace(np.nan, '')
df['migrac/viven_migrantes'] = df['migrac/viven_migrantes'].replace(np.nan, '')
df['viven_migracaión'] = df[['migrac1/viven_migrantes','migrac/viven_migrantes']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['viven_migracaión'] = df['viven_migracaión'].replace('si', 'Si').replace('no','No').replace('no_sabe','No Sabe').replace('nosabe','No Sabe').replace('nose','No Sabe').replace('','No responde')
df_final['¿En la comunidad viven personas migrantes?'] = df['viven_migracaión']



## Nacionalidad

df['migrac1/viven_migrantes_si1/nacionalidad'] = df['migrac1/viven_migrantes_si1/nacionalidad'].replace(np.nan, '')
df['migrac/viven_migrantes_si/nacionalidad'] = df['migrac/viven_migrantes_si/nacionalidad'].replace(np.nan, '')


df['nacionalidad_migracaión'] = df[['migrac1/viven_migrantes_si1/nacionalidad','migrac/viven_migrantes_si/nacionalidad']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df_final['Nacionalidad Migrante/Venezuela'] = 0
df_final['Nacionalidad Migrante/Haiti'] = 0
df_final['Nacionalidad Migrante/Cuba'] = 0
df_final['Nacionalidad Migrante/Chile'] = 0
df_final['Nacionalidad Migrante/Brasil'] = 0
df_final['Nacionalidad Migrante/Panamá'] = 0
df_final['Nacionalidad Migrante/Ecuador'] = 0
df_final['Nacionalidad Migrante/Otro'] = 0

for i in range(contar):
    
    ven = df['nacionalidad_migracaión'][i].count('ven')
    hai = df['nacionalidad_migracaión'][i].count('hai')
    cuba = df['nacionalidad_migracaión'][i].count('cuba')
    chile = df['nacionalidad_migracaión'][i].count('chile')
    bras = df['nacionalidad_migracaión'][i].count('bras')
    panam = df['nacionalidad_migracaión'][i].count('panam')
    ecuad = df['nacionalidad_migracaión'][i].count('ecuad')
    otro = df['nacionalidad_migracaión'][i].count('otro')
    
    try:
        df_final['Nacionalidad Migrante/Venezuela'][i] = ven
        df_final['Nacionalidad Migrante/Haiti'][i] = hai
        df_final['Nacionalidad Migrante/Cuba'][i] = cuba
        df_final['Nacionalidad Migrante/Chile'][i] = chile
        df_final['Nacionalidad Migrante/Brasil'][i] = bras
        df_final['Nacionalidad Migrante/Panamá'][i] = panam
        df_final['Nacionalidad Migrante/Ecuador'][i] = ecuad
        df_final['Nacionalidad Migrante/Otro'][i] = otro    
                
    except:
        pass

## ¿Qué porcentaje de la población que vive en la comunidad es migrante?

df['migrac1/viven_migrantes_si1/porc_pob_mig'] = df['migrac1/viven_migrantes_si1/porc_pob_mig'].replace(np.nan, '')
df['migrac/viven_migrantes_si/porc_pob_mig'] = df['migrac/viven_migrantes_si/porc_pob_mig'].replace(np.nan, '')
df['porcentaje_migracaión'] = df[['migrac1/viven_migrantes_si1/porc_pob_mig','migrac/viven_migrantes_si/porc_pob_mig']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['porcentaje_migracaión'] = df['porcentaje_migracaión'].replace('0_10', 'Entre el 0% y el 10%').replace('10_30','Entre el 11% y el 30%').replace('31_60','Entre el 31% y el 60%').replace('61_','Más del 61%').replace('nosabe','No sabe').replace('','No Responde')
df['porcentaje_migracaión']
df_final['¿Qué porcentaje de la población que vive en la comunidad es migrante?'] = df['porcentaje_migracaión']


##################
## Salud

# 79. ¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes debido a la situación generada por las limitaciones de refugio, abrigo, alimentación, agua y saneamiento, así como la aparición de brotes epidémicos?

df['Afectaciones salud'] = df['sal/casos_enferm'].replace('si', 'Si').replace('no','No').replace('no_sabe','No Sabe').replace('nosabe','No Sabe').replace('nose','No Sabe').replace(np.nan,'No responde')
df_final['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'] = df['Afectaciones salud']
df['sal/enferm'] = df['sal/enferm'].replace(np.nan,'')

df_final['Casos afectaciones salud/Anemia'] = 0
df_final['Casos afectaciones salud/Afecciones en la piel'] = 0
df_final['Casos afectaciones salud/Chikunguna'] = 0
df_final['Casos afectaciones salud/COVID19'] = 0
df_final['Casos afectaciones salud/Dengue'] = 0
df_final['Casos afectaciones salud/Deshidratación'] = 0
df_final['Casos afectaciones salud/Desnutrición'] = 0
df_final['Casos afectaciones salud/Enfermedad Diarreíca Aguda - EDA'] = 0
df_final['Casos afectaciones salud/Infección Respiratoria Aguda - IRA'] = 0
df_final['Casos afectaciones salud/Malaria'] = 0
df_final['Casos afectaciones salud/Meningitis'] = 0
df_final['Casos afectaciones salud/Rubeola'] = 0
df_final['Casos afectaciones salud/Sarampión'] = 0
df_final['Casos afectaciones salud/Vómito'] = 0
df_final['Casos afectaciones salud/Zika'] = 0
df_final['Casos afectaciones salud/Otro'] = 0



for i in range(contar):
    
    anemia = df['sal/enferm'][i].count('anemia')
    af_piel = df['sal/enferm'][i].count('af_piel')
    chik = df['sal/enferm'][i].count('chik')
    covid = df['sal/enferm'][i].count('covid')
    deng = df['sal/enferm'][i].count('deng')
    desh = df['sal/enferm'][i].count('desh')
    desnut = df['sal/enferm'][i].count('desnut')
    eda = df['sal/enferm'][i].count('eda')
    ira = df['sal/enferm'][i].count('ira')
    mal = df['sal/enferm'][i].count('mal')
    mening = df['sal/enferm'][i].count('mening')
    rub = df['sal/enferm'][i].count('rub')
    saramp = df['sal/enferm'][i].count('saramp')
    vomi = df['sal/enferm'][i].count('vomi')
    zika = df['sal/enferm'][i].count('zika')
    otro = df['sal/enferm'][i].count('otro')

    
    try:
        df_final['Casos afectaciones salud/Anemia'][i] = anemia
        df_final['Casos afectaciones salud/Afecciones en la piel'][i] = af_piel
        df_final['Casos afectaciones salud/Chikunguna'][i] = chik
        df_final['Casos afectaciones salud/COVID19'][i] = covid
        df_final['Casos afectaciones salud/Dengue'][i] = deng
        df_final['Casos afectaciones salud/Deshidratación'][i] = desh
        df_final['Casos afectaciones salud/Desnutrición'][i] = desnut
        df_final['Casos afectaciones salud/Enfermedad Diarreíca Aguda - EDA'][i] = eda
        df_final['Casos afectaciones salud/Infección Respiratoria Aguda - IRA'][i] = ira
        df_final['Casos afectaciones salud/Malaria'][i] = mal
        df_final['Casos afectaciones salud/Meningitis'][i] = mening
        df_final['Casos afectaciones salud/Rubeola'][i] = rub
        df_final['Casos afectaciones salud/Sarampión'][i] = saramp
        df_final['Casos afectaciones salud/Vómito'][i] = vomi
        df_final['Casos afectaciones salud/Zika'][i] = zika
        df_final['Casos afectaciones salud/Otro'][i] = otro
                
    except:
        pass

## Acceso a la salud

df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con recursos para el pago de tratamientos médicos'] = 0
df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay centro de salud funcional cerca'] = 0
df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay suficiente capacidad médica para la atención'] = 0
df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con documentos de identidad'] = 0
df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud  (EPS)'] = 0
df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud por condición irregular de migración'] = 0
df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Tiempo de espera para la atención'] = 0
df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Transporte'] = 0
df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Otro'] = 0

# barreras para acceder a la salud


df['sal/barrera_cron'] = df['sal/barrera_cron'].replace(np.nan, '')
df['sal/barrera'] = df['sal/barrera'].replace(np.nan, '')
df['barreras salud'] = df[['sal/barrera_cron','sal/barrera']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['barreras salud']
         
for i in range(contar):
    
    no_rec = df['barreras salud'][i].count('no_rec')
    no_centr_salud = df['barreras salud'][i].count('no_centr_salud')
    capac_med = df['barreras salud'][i].count('capac_med')
    doc = df['barreras salud'][i].count('doc')
    acc_salud = df['barreras salud'][i].count('acc_salud')
    # variables muy parecidas, van a sumar
    acc_salud_mig = df['barreras salud'][i].count('acc_salud_mig')
    tiemp_atenc = df['barreras salud'][i].count('tiemp_atenc')
    transporte = df['barreras salud'][i].count('transporte')
    otro = df['barreras salud'][i].count('otro')
    
    try:
        if df['barreras salud'][i].count('todas') > 0:
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con recursos para el pago de tratamientos médicos'][i] = 1
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay centro de salud funcional cerca'][i] = 1
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay suficiente capacidad médica para la atención'][i] = 1
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con documentos de identidad'][i] = 1
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud  (EPS)'][i] = 1
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud por condición irregular de migración'][i] = 1
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Tiempo de espera para la atención'][i] = 1
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Transporte'][i] = 1
                   
        else:
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con recursos para el pago de tratamientos médicos'][i] = no_rec
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay centro de salud funcional cerca'][i] = no_centr_salud
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay suficiente capacidad médica para la atención'][i] = capac_med
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con documentos de identidad'][i] = doc
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud  (EPS)'][i] = acc_salud
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud por condición irregular de migración'][i] = acc_salud_mig
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Tiempo de espera para la atención'][i] = tiemp_atenc
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Transporte'][i] = transporte
            df_final['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Otro'][i] = otro
    except:
        pass

##################
## Educación

# 73. ¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?

df['educ1/tiempo_esc'] = df['educ1/tiempo_esc'].replace(np.nan, '')
df['educ/tiempo_esc'] = df['educ/tiempo_esc'].replace(np.nan, '')
df['tiempo educacion'] = df[['educ1/tiempo_esc','educ/tiempo_esc']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df['tiempo educacion'] = df['tiempo educacion'].replace('5_30', '5 - 30 minutos').replace('30_60','Entre 30 - 60 minutos').replace('61_','Mas de 60 minutos').replace('5_15','5 - 30 minutos').replace('16_30','5 - 30 minutos').replace('31_','Entre 30 - 60 minutos').replace('','No responde')
df_final['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'] = df['tiempo educacion']

# ¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?

df['educ1/nna_noacc_edu'] = df['educ1/nna_noacc_edu'].replace(np.nan, '')
df['educ/nna_noacc_edu'] = df['educ/nna_noacc_edu'].replace(np.nan, '')
df['sin estudiar'] = df[['educ1/nna_noacc_edu','educ/nna_noacc_edu']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['sin estudiar'] = df['sin estudiar'].replace('si', 'Si').replace('no','No').replace('ns','No sabe').replace('nose','No sabe').replace('nosabe','No sabe').replace('','No Responde')
df_final['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'] = df['sin estudiar']

# Principales razones de no estudiar

df['educ1/acc_edu_no'] = df['educ1/acc_edu_no'].replace(np.nan, '')
df['educ/acc_edu_no'] = df['educ/acc_edu_no'].replace(np.nan, '')
df['razones sin estudiar'] = df[['educ1/acc_edu_no','educ/acc_edu_no']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df_final['Razón no estudio/Afectación en la comunidad por conflicto'] = 0
df_final['Razón no estudio/Afectación en la infraestructura de las instituciones'] = 0
df_final['Razón no estudio/Climas extremos (Temporadas de lluvias)'] = 0
df_final['Razón no estudio/Desastres naturales'] = 0
df_final['Razón no estudio/Falta de Cupos'] = 0
df_final['Razón no estudio/Hacinamiento en las aulas'] = 0
df_final['Razón no estudio/Los entornos no son seguros'] = 0
df_final['Razón no estudio/No hay docentes'] = 0
df_final['Razón no estudio/No hay dotación suficiente (tableros, pupitres, etc)'] = 0
df_final['Razón no estudio/No los pueden llevar o recoger del colegio'] = 0
df_final['Razón no estudio/Por falta de recursos económicos'] = 0
df_final['Razón no estudio/Por largas distancias entre el colegio y la vivienda'] = 0
df_final['Razón no estudio/Por su estatus migratorio'] = 0
df_final['Razón no estudio/Trabajo infantil (dentro o fuera del hogar)'] = 0
df_final['Razón no estudio/Otro'] = 0

for i in range(contar):
    
    conflic = df['razones sin estudiar'][i].count('conflic')
    inst = df['razones sin estudiar'][i].count('inst')
    clima = df['razones sin estudiar'][i].count('clima')
    desast = df['razones sin estudiar'][i].count('desast')
    falta_cupos = df['razones sin estudiar'][i].count('falta_cupos')
    hacinam = df['razones sin estudiar'][i].count('hacinam')
    ento_ins = df['razones sin estudiar'][i].count('ento_ins')
    no_doc = df['razones sin estudiar'][i].count('no_doc')
    dotac = df['razones sin estudiar'][i].count('dotac')
    padres_trabajan = df['razones sin estudiar'][i].count('padres_trabajan')
    rec_migrat = df['razones sin estudiar'][i].count('rec_migrat')
    largas_dist = df['razones sin estudiar'][i].count('largas_dist')
    estatus_migrat = df['razones sin estudiar'][i].count('estatus_migrat')
    trab = df['razones sin estudiar'][i].count('trab')
    otro = df['razones sin estudiar'][i].count('otro')

    try:
        df_final['Razón no estudio/Afectación en la comunidad por conflicto'][i] = conflic
        df_final['Razón no estudio/Afectación en la infraestructura de las instituciones'][i] = inst
        df_final['Razón no estudio/Climas extremos (Temporadas de lluvias)'][i] = clima
        df_final['Razón no estudio/Desastres naturales'][i] = desast
        df_final['Razón no estudio/Falta de Cupos'][i] = falta_cupos
        df_final['Razón no estudio/Hacinamiento en las aulas'][i] = hacinam
        df_final['Razón no estudio/Los entornos no son seguros'][i] = ento_ins
        df_final['Razón no estudio/No hay docentes'][i] = no_doc
        df_final['Razón no estudio/No hay dotación suficiente (tableros, pupitres, etc)'][i] = dotac
        df_final['Razón no estudio/No los pueden llevar o recoger del colegio'][i] = padres_trabajan
        df_final['Razón no estudio/Por falta de recursos económicos'][i] = rec_migrat
        df_final['Razón no estudio/Por largas distancias entre el colegio y la vivienda'][i] = largas_dist
        df_final['Razón no estudio/Por su estatus migratorio'][i] = estatus_migrat
        df_final['Razón no estudio/Trabajo infantil (dentro o fuera del hogar)'][i] = trab
        df_final['Razón no estudio/Otro'][i] = otro

    except:
        pass

##################
## WASH

# ¿Cuál es la principal fuente de agua que usa la comunidad actualmente?

df['wash_1/agua_consum'] = df['wash_1/agua_consum'].replace(np.nan, '')
df['wash_/agua_consum'] = df['wash_/agua_consum'].replace(np.nan, '')
df['Fuente de agua'] = df[['wash_1/agua_consum','wash_/agua_consum']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df_final['Principal fuente de agua/Acueducto por tubería'] = 0
df_final['Principal fuente de agua/Agua embotellada o en bolsa'] = 0
df_final['Principal fuente de agua/Aguas lluvias'] = 0
df_final['Principal fuente de agua/Aguatero'] = 0
df_final['Principal fuente de agua/Carro tanque o agua en camión cisterna'] = 0
df_final['Principal fuente de agua/No hay servicio'] = 0
df_final['Principal fuente de agua/Otra fuente por tubería'] = 0
df_final['Principal fuente de agua/Pila pública o de suministro comunitario'] = 0
df_final['Principal fuente de agua/Pozo con bomba'] = 0
df_final['Principal fuente de agua/Pozo sin bomba, aljibe, jagüey o barreno'] = 0
df_final['Principal fuente de agua/Río, quebrada, nacimiento o manantial'] = 0
df_final['Principal fuente de agua/Tanque de agua'] = 0
df_final['Principal fuente de agua/Tecnologías alternativas (puntos de suministro o de abasto)'] = 0
df_final['Principal fuente de agua/Otra'] = 0
df_final['Principal fuente de agua/No sabe'] = 0

for i in range(contar):
    
    acued = df['Fuente de agua'][i].count('acued')
    bolsa = df['Fuente de agua'][i].count('bolsa')
    agua_lluvias = df['Fuente de agua'][i].count('agua_lluvias')
    aguatero = df['Fuente de agua'][i].count('aguatero')
    carrotanque = df['Fuente de agua'][i].count('carrotanque')
    ninguno = df['Fuente de agua'][i].count('ninguno')
    tuberias = df['Fuente de agua'][i].count('tuberias')
    pila = df['Fuente de agua'][i].count('pila')
    pozo_bomba = df['Fuente de agua'][i].count('pozo_bomba')
    pozo_sinbomba = df['Fuente de agua'][i].count('pozo_sinbomba')
    rio = df['Fuente de agua'][i].count('rio')
    tanque = df['Fuente de agua'][i].count('tanque')
    tecnologias_alt = df['Fuente de agua'][i].count('tecnologias_alt')
    otro = df['Fuente de agua'][i].count('otro')
    no_sabe = df['Fuente de agua'][i].count('no_sabe')
        

    try:
        df_final['Principal fuente de agua/Acueducto por tubería'][i] = acued
        df_final['Principal fuente de agua/Agua embotellada o en bolsa'][i] = bolsa
        df_final['Principal fuente de agua/Aguas lluvias'][i] = agua_lluvias
        df_final['Principal fuente de agua/Aguatero'][i] = aguatero
        df_final['Principal fuente de agua/Carro tanque o agua en camión cisterna'][i] = carrotanque
        df_final['Principal fuente de agua/No hay servicio'][i] = ninguno
        df_final['Principal fuente de agua/Otra fuente por tubería'] = tuberias
        df_final['Principal fuente de agua/Pila pública o de suministro comunitario'][i] = pila
        df_final['Principal fuente de agua/Pozo con bomba'][i]= pozo_bomba
        df_final['Principal fuente de agua/Pozo sin bomba, aljibe, jagüey o barreno'][i] = pozo_sinbomba
        df_final['Principal fuente de agua/Río, quebrada, nacimiento o manantial'][i] = rio
        df_final['Principal fuente de agua/Tanque de agua'][i] = tanque
        df_final['Principal fuente de agua/Tecnologías alternativas (puntos de suministro o de abasto)'][i] = tecnologias_alt
        df_final['Principal fuente de agua/Otra'][i] = otro
        df_final['Principal fuente de agua/No sabe'][i] = no_sabe

    except:
        pass

# ¿Cuál es la modalidad de recolección de basuras en la comunidad?

df['wash_1/disp_basura'] = df['wash_1/disp_basura'].replace(np.nan, '')
df['wash_/disp_basura'] = df['wash_/disp_basura'].replace(np.nan, '')
df['Recoleccion de basuras'] = df[['wash_1/agua_consum','wash_/disp_basura']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df_final['Modalidad de recolección de basuras en la comunidad/Por recolección pública, privada o comunitaria'] = 0
df_final['Modalidad de recolección de basuras en la comunidad/Se arroja a un río, quebrada, cano o laguna'] = 0
df_final['Modalidad de recolección de basuras en la comunidad/Se arroja a un patio, lote, zanja o baldío'] = 0
df_final['Modalidad de recolección de basuras en la comunidad/Se quema o se entierra'] = 0
df_final['Modalidad de recolección de basuras en la comunidad/Se elimina de otra forma'] = 0
df_final['Modalidad de recolección de basuras en la comunidad/Se clasifica la basura entre orgánicos y reciclaje, aprovechando todos los residuos'] = 0
df_final['Modalidad de recolección de basuras en la comunidad/Otro'] = 0
df_final['Modalidad de recolección de basuras en la comunidad/No sabe'] = 0

for i in range(contar):
    
    rec_pub = df['Recoleccion de basuras'][i].count('rec_pub')
    arroja_rio = df['Recoleccion de basuras'][i].count('arroja_rio')
    arroja_pat = df['Recoleccion de basuras'][i].count('arroja_pat')
    quema = df['Recoleccion de basuras'][i].count('quema')
    elima = df['Recoleccion de basuras'][i].count('elima')
    clasif = df['Recoleccion de basuras'][i].count('clasif')
    otro = df['Recoleccion de basuras'][i].count('otro')
    no_sabe = df['Recoleccion de basuras'][i].count('no_sabe')

    try:
        df_final['Modalidad de recolección de basuras en la comunidad/Por recolección pública, privada o comunitaria'][i] = rec_pub
        df_final['Modalidad de recolección de basuras en la comunidad/Se arroja a un río, quebrada, cano o laguna'][i] = arroja_rio
        df_final['Modalidad de recolección de basuras en la comunidad/Se arroja a un patio, lote, zanja o baldío'][i] = arroja_pat
        df_final['Modalidad de recolección de basuras en la comunidad/Se quema o se entierra'][i] = quema
        df_final['Modalidad de recolección de basuras en la comunidad/Se elimina de otra forma'][i] = elima
        df_final['Modalidad de recolección de basuras en la comunidad/Se clasifica la basura entre orgánicos y reciclaje, aprovechando todos los residuos'][i] = clasif
        df_final['Modalidad de recolección de basuras en la comunidad/Otro'][i] = otro
        df_final['Modalidad de recolección de basuras en la comunidad/No sabe'][i] = no_sabe

    except:
        pass

# Focos de contaminación

df['wash_1/focos_contam'] = df['wash_1/focos_contam'].replace(np.nan, '')
df['wash_/focos_contam'] = df['wash_/focos_contam'].replace(np.nan, '')
df['Focos contaminacion'] = df[['wash_1/focos_contam','wash_/focos_contam']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df_final['Focos de contaminación/Agua estancada'] = 0
df_final['Focos de contaminación/Animales muertos'] = 0
df_final['Focos de contaminación/Basureros clandestinos'] = 0
df_final['Focos de contaminación/Corrientes de aguas negras'] = 0
df_final['Focos de contaminación/Defecación al aire libre'] = 0
df_final['Focos de contaminación/Desechos químicos'] = 0
df_final['Focos de contaminación/Disposición de basura al aire libre'] = 0
df_final['Focos de contaminación/Disposición de excretas inadecuada'] = 0
df_final['Focos de contaminación/Ninguno'] = 0
df_final['Focos de contaminación/Plantas de tratamiento de aguas residuales'] = 0
df_final['Focos de contaminación/Roedores'] = 0
df_final['Focos de contaminación/Transmisión de enfermedades por vectores'] = 0
df_final['Focos de contaminación/Zonas de basuras permanentes'] = 0
df_final['Focos de contaminación/Otro'] = 0
df_final['Focos de contaminación/No sabe'] = 0

for i in range(contar):
    
    agua_Est = df['Focos contaminacion'][i].count('agua_Est')
    anim_m = df['Focos contaminacion'][i].count('anim_m')
    basurer = df['Focos contaminacion'][i].count('basurer')
    corr_as = df['Focos contaminacion'][i].count('corr_as')
    defec_aire = df['Focos contaminacion'][i].count('defec_aire')
    desech_quim = df['Focos contaminacion'][i].count('desech_quim')
    basura_aire = df['Focos contaminacion'][i].count('basura_aire')
    excreta_inad = df['Focos contaminacion'][i].count('excreta_inad')
    ninguno = df['Focos contaminacion'][i].count('ninguno')
    plant_trat = df['Focos contaminacion'][i].count('plant_trat')
    roed = df['Focos contaminacion'][i].count('roed')
    vect = df['Focos contaminacion'][i].count('vect')
    bas = df['Focos contaminacion'][i].count('bas')
    otro = df['Focos contaminacion'][i].count('otro')
    no_sabe = df['Focos contaminacion'][i].count('no_sabe')
    
    try:
        df_final['Focos de contaminación/Agua estancada'][i] = agua_Est
        df_final['Focos de contaminación/Animales muertos'][i] = anim_m
        df_final['Focos de contaminación/Basureros clandestinos'][i] = basurer
        df_final['Focos de contaminación/Corrientes de aguas negras'][i] = corr_as
        df_final['Focos de contaminación/Defecación al aire libre'][i] = defec_aire
        df_final['Focos de contaminación/Desechos químicos'][i] = desech_quim
        df_final['Focos de contaminación/Disposición de basura al aire libre'][i] = basura_aire
        df_final['Focos de contaminación/Disposición de excretas inadecuada'][i] = excreta_inad
        df_final['Focos de contaminación/Ninguno'][i] = ninguno
        df_final['Focos de contaminación/Plantas de tratamiento de aguas residuales'][i] = plant_trat
        df_final['Focos de contaminación/Roedores'][i]= roed
        df_final['Focos de contaminación/Transmisión de enfermedades por vectores'][i] = vect
        df_final['Focos de contaminación/Zonas de basuras permanentes'][i] = bas
        df_final['Focos de contaminación/Otro'][i] = otro
        df_final['Focos de contaminación/No sabe'][i] = no_sabe

    except:
        pass


##################
## Protección

# Trabajo infantil

df['prot_g1/nna_trab'] = df['prot_g1/nna_trab'].replace(np.nan, '')
df['trab_inf/nna_trab'] = df['trab_inf/nna_trab'].replace(np.nan, '')
df['Tabajo infantil'] = df[['prot_g1/nna_trab','trab_inf/nna_trab']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['Tabajo infantil'] = df['Tabajo infantil'].replace('si', 'Si').replace('no','No').replace('ns','No sabe').replace('nose','No sabe').replace('nosabe','No sabe').replace('','No Responde')
df_final['¿Existen casos de trabajo infantil en la comunidad?'] = df['Tabajo infantil']

# Existen casos de mendicidad

df['prot_g1/nna_don'] = df['prot_g1/nna_don'].replace(np.nan, '')
df['trab_inf/nna_don'] = df['trab_inf/nna_don'].replace(np.nan, '')
df['Casos mendicidad'] = df[['prot_g1/nna_don','trab_inf/nna_don']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['Casos mendicidad'] = df['Casos mendicidad'].replace('si', 'Si').replace('no','No').replace('ns','No sabe').replace('nose','No sabe').replace('nosabe','No sabe').replace('','No Responde')
df_final['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'] = df['Casos mendicidad']

# ¿Se han presentado apoyo o ayudas económicas a las familias?

df['prot_g1/subsid_gub'] = df['prot_g1/subsid_gub'].replace(np.nan, '')
df['fam_g/subsid_gub'] = df['fam_g/subsid_gub'].replace(np.nan, '')
df['Ayudas economicas'] = df[['prot_g1/subsid_gub','fam_g/subsid_gub']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['Ayudas economicas'] = df['Ayudas economicas'].replace('si', 'Si').replace('no','No').replace('ns','No sabe').replace('nose','No sabe').replace('nosabe','No sabe').replace('','No Responde')
df_final['¿Se han presentado apoyo o ayudas económicas a las familias?'] = df['Ayudas economicas']

##################
## SAN

##¿En la comunidad, los niños, niñas y adolescentes reciben algún apoyo alimentario?

df['nutric_1/subs_alim'] = df['nutric_1/subs_alim'].replace(np.nan, '')
df['nutric_/subs_alim'] = df['nutric_/subs_alim'].replace(np.nan, '')
df['apoyo alimentario'] = df[['nutric_1/subs_alim','nutric_/subs_alim']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

df_final['Apoyo alimentario/Subsidio económico'] = 0
df_final['Apoyo alimentario/Comedores comunitarios'] = 0
df_final['Apoyo alimentario/Kits o bonos alimentarios'] = 0
df_final['Apoyo alimentario/Ninguno'] = 0
df_final['Apoyo alimentario/No sabe'] = 0
df_final['Apoyo alimentario/Otra'] = 0

for i in range(contar):
    
    subs_econm = df['apoyo alimentario'][i].count('subs_econm')
    comed_comun = df['apoyo alimentario'][i].count('comed_comun')
    kits = df['apoyo alimentario'][i].count('kits')
    ninguno = df['apoyo alimentario'][i].count('ninguno')
    no_sabe = df['apoyo alimentario'][i].count('no_sabe')
    otra = df['apoyo alimentario'][i].count('otra')

    try:
        df_final['Apoyo alimentario/Subsidio económico'][i] = subs_econm
        df_final['Apoyo alimentario/Comedores comunitarios'][i] = comed_comun
        df_final['Apoyo alimentario/Kits o bonos alimentarios'][i] = kits
        df_final['Apoyo alimentario/Ninguno'][i] = ninguno
        df_final['Apoyo alimentario/No sabe'][i] = no_sabe
        df_final['Apoyo alimentario/Otra'][i] = otra

    except:
        pass

# Indique el nivel aproximado de consumo de alimentos por parte de los niños, niñas y adolescentes de la comunidad

df['nutric_1/niv_alim'] = df['nutric_1/niv_alim'].replace(np.nan, '')
df['nutric_/niv_alim'] = df['nutric_/niv_alim'].replace(np.nan, '')
df['consumo alimentario NNA'] = df[['nutric_1/niv_alim','nutric_/niv_alim']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['consumo alimentario NNA'] = df['consumo alimentario NNA'].replace('acept', 'Alta (ejemplo: arroz, granos, harinas y con proteina)').replace('al_limite','Media (ejemplo: arroz, granos, harinas y sin proteina)').replace('pobre','Baja (ejemplo: café, pan, paquetes de tiendas…)').replace('ns','No sabe').replace('nose','No sabe').replace('no_sabe','No sabe').replace('nosabe','No sabe').replace('','No Responde')
df_final['Consumo de alimentos NNA en la comunidad'] = df['consumo alimentario NNA']

# ¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?

df['nutric_1/cond_alim'] = df['nutric_1/cond_alim'].replace(np.nan, '')
df['nutric_/cond_alim'] = df['nutric_/cond_alim'].replace(np.nan, '')
df['desnutrición'] = df[['nutric_1/cond_alim','nutric_/cond_alim']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
df['desnutrición'] = df['desnutrición'].replace('si', 'Si').replace('no','No').replace('ns','No sabe').replace('nose','No sabe').replace('no_sabe','No sabe').replace('nosabe','No sabe').replace('','No Responde').replace('bajopes','Si').replace('sobp','No').replace('pessal','No')
df_final['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'] = df['desnutrición']

########################################
## Depuración base

##################
## datos aprobados
df_aprobados = df_final[df_final['_validation_status'] == {}]
df_aprobados.drop(['_validation_status'], axis=1, inplace = True)

##################
## Departamentos

departamentos = list(df_aprobados['4. Departamento'])
departamentos.append('Nacional') 
departamentos = list(dict.fromkeys(departamentos))

##################
## Datos por departamento

Arauca = df_aprobados[df_aprobados['4. Departamento'] == 'Arauca']
Atlantico = df_aprobados[df_aprobados['4. Departamento'] == 'Atlantico']
Choco = df_aprobados[df_aprobados['4. Departamento'] == 'Choco']
Guajira = df_aprobados[df_aprobados['4. Departamento'] == 'La Guajira']
Nariño = df_aprobados[df_aprobados['4. Departamento'] == 'Nariño']
NorteSantander = df_aprobados[df_aprobados['4. Departamento'] == 'Norte de Santander']

##################
## agrupación por departamento (contar)
agrupacion_dep_count = df_aprobados.drop_duplicates(subset=['8. Barrio, asentamiento, comunidad'])
agrupacion_dep_count =  agrupacion_dep_count.groupby(['4. Departamento'],as_index=False).count()

##################
## agrupación por departamento (suma)
agrupacion_dep_sum =  df_aprobados.groupby(['4. Departamento'],as_index=False).sum()

##################
## Caracteristicas

Caracteristicas = df_aprobados.loc[:,['11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto veredal',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto comunal',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto campesino',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Agua potable',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Alcantarillado',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Energía eléctrica',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Instituciones educativas',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Gas natural',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Hospitales y/o puestos de salud',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Internet',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Presencia de policía y/o ejército',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Saneamiento',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Vías pavimentadas',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Viviendas en ladrillos, concreto, cemento',
                                      '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Ninguna']]

Caracteristicas.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
Caracteristicas.rename({'o puestos de salud':'Hospitales y/o puestos de salud','o ejército':'Presencia de policía y/o ejército'},
                       axis = 'columns', inplace=True)
Caracteristicas = Caracteristicas.T
Caracteristicas.insert(0, 'Caracteristicas', Caracteristicas.index)
Caracteristicas.reset_index()
Caracteristicas['Total por caracteristicas'] = Caracteristicas.sum(axis = 1)
Caracteristicas = Caracteristicas.filter(['Caracteristicas','Total por caracteristicas'], axis = 1)


# arauca
CaracArauca = Arauca.loc[:,['4. Departamento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto veredal',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto comunal',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto campesino',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Agua potable',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Alcantarillado',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Energía eléctrica',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Instituciones educativas',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Gas natural',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Hospitales y/o puestos de salud',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Internet',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Presencia de policía y/o ejército',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Saneamiento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Vías pavimentadas',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Viviendas en ladrillos, concreto, cemento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Ninguna']]

CaracArauca.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
CaracArauca.rename({'o puestos de salud':'Hospitales y/o puestos de salud','o ejército':'Presencia de policía y/o ejército'},
                       axis = 'columns', inplace=True)
CaracArauca = CaracArauca.melt(id_vars=['4. Departamento'],var_name='Caracteristica', value_name='Total')
CaracArauca = CaracArauca.groupby(['4. Departamento','Caracteristica'],as_index=False).sum()

# Chcoco
CaracChoco = Choco.loc[:,['4. Departamento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto veredal',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto comunal',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto campesino',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Agua potable',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Alcantarillado',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Energía eléctrica',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Instituciones educativas',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Gas natural',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Hospitales y/o puestos de salud',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Internet',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Presencia de policía y/o ejército',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Saneamiento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Vías pavimentadas',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Viviendas en ladrillos, concreto, cemento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Ninguna']]

CaracChoco.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)

CaracChoco.rename({'o puestos de salud':'Hospitales y/o puestos de salud','o ejército':'Presencia de policía y/o ejército'},
                       axis = 'columns', inplace=True)
CaracChoco = CaracChoco.melt(id_vars=['4. Departamento'],var_name='Caracteristica', value_name='Total')
CaracChoco = CaracChoco.groupby(['4. Departamento','Caracteristica'],as_index=False).sum()

# Guajira
CaracGuajira = Guajira.loc[:,['4. Departamento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto veredal',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto comunal',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto campesino',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Agua potable',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Alcantarillado',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Energía eléctrica',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Instituciones educativas',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Gas natural',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Hospitales y/o puestos de salud',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Internet',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Presencia de policía y/o ejército',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Saneamiento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Vías pavimentadas',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Viviendas en ladrillos, concreto, cemento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Ninguna']]

CaracGuajira.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
CaracGuajira.rename({'o puestos de salud':'Hospitales y/o puestos de salud','o ejército':'Presencia de policía y/o ejército'},
                       axis = 'columns', inplace=True)
CaracGuajira = CaracGuajira.melt(id_vars=['4. Departamento'],var_name='Caracteristica', value_name='Total')
CaracGuajira = CaracGuajira.groupby(['4. Departamento','Caracteristica'],as_index=False).sum()

# Norte de santander
CaracNorteSantander = NorteSantander.loc[:,['4. Departamento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto veredal',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto comunal',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Acueducto campesino',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Agua potable',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Alcantarillado',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Energía eléctrica',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Instituciones educativas',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Gas natural',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Hospitales y/o puestos de salud',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Internet',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Presencia de policía y/o ejército',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Saneamiento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Vías pavimentadas',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Viviendas en ladrillos, concreto, cemento',
                            '11. Indique con qué características cuenta el barrio, asentamiento o comunidad/Ninguna']]

CaracNorteSantander.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
CaracNorteSantander.rename({'o puestos de salud':'Hospitales y/o puestos de salud','o ejército':'Presencia de policía y/o ejército'},
                       axis = 'columns', inplace=True)
CaracNorteSantander = CaracNorteSantander.melt(id_vars=['4. Departamento'],var_name='Caracteristica', value_name='Total')
CaracNorteSantander = CaracNorteSantander.groupby(['4. Departamento','Caracteristica'],as_index=False).sum()

##################
## asentamiento humano informal

#Nacional
asentamiento_informal = df_aprobados.groupby(['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'],as_index=False).count()
asentamiento_informal = asentamiento_informal.filter(['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?','1. ¿Quién responde la encuesta?/lider'])
asentamiento_informal.rename(columns ={'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
asentamiento_informal_dep = df_aprobados.filter(['4. Departamento','5. Municipio','8. Barrio, asentamiento, comunidad','19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'])

#Arauca
asentamiento_informalArauca = Arauca.groupby(['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'],as_index=False).count()
asentamiento_informalArauca = asentamiento_informalArauca.filter(['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?','1. ¿Quién responde la encuesta?/lider'])
asentamiento_informalArauca.rename(columns ={'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

#Choco
asentamiento_informalChoco = Choco.groupby(['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'],as_index=False).count()
asentamiento_informalChoco = asentamiento_informalChoco.filter(['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?','1. ¿Quién responde la encuesta?/lider'])
asentamiento_informalChoco.rename(columns ={'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# La Guajira
asentamiento_informalGuajira = Guajira.groupby(['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'],as_index=False).count()
asentamiento_informalGuajira = asentamiento_informalGuajira.filter(['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?','1. ¿Quién responde la encuesta?/lider'])
asentamiento_informalGuajira.rename(columns ={'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# Norte Santander
asentamiento_informalNorteSantander = NorteSantander.groupby(['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'],as_index=False).count()
asentamiento_informalNorteSantander = asentamiento_informalNorteSantander.filter(['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?','1. ¿Quién responde la encuesta?/lider'])
asentamiento_informalNorteSantander.rename(columns ={'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

##################
## terreno
# Nacional
Terrenos = df_aprobados.loc[:,['4. Departamento',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Bosque',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a bahia, estuario, lagunas',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a los cauces de ríos, quebradas, arroyos',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca de volcanes',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte alta de una montaña',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte baja de una montaña',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Humedales',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Isla',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Paramo',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Terreno desértico',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Zona costera',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Ninguna de las anteriores',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Otro']]

Terrenos.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
Terrenos = Terrenos.melt(id_vars=['4. Departamento'],var_name='Terreno', value_name='Total')
#Terrenos = Terrenos.groupby(['4. Departamento','Terreno'],as_index=False).sum()
Terrenos = Terrenos.groupby(['Terreno'],as_index=False).sum()

# Arauca
TerrenosArauca = Arauca.loc[:,['4. Departamento',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Bosque',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a bahia, estuario, lagunas',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a los cauces de ríos, quebradas, arroyos',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca de volcanes',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte alta de una montaña',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte baja de una montaña',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Humedales',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Isla',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Paramo',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Terreno desértico',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Zona costera',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Ninguna de las anteriores',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Otro']]

TerrenosArauca.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
TerrenosArauca = TerrenosArauca.melt(id_vars=['4. Departamento'],var_name='Terreno', value_name='Total')
TerrenosArauca = TerrenosArauca.groupby(['Terreno'],as_index=False).sum()

# Choco
TerrenosChoco = Choco.loc[:,['4. Departamento',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Bosque',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a bahia, estuario, lagunas',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a los cauces de ríos, quebradas, arroyos',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca de volcanes',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte alta de una montaña',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte baja de una montaña',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Humedales',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Isla',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Paramo',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Terreno desértico',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Zona costera',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Ninguna de las anteriores',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Otro']]

TerrenosChoco.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
TerrenosChoco = TerrenosChoco.melt(id_vars=['4. Departamento'],var_name='Terreno', value_name='Total')
TerrenosChoco = TerrenosChoco.groupby(['Terreno'],as_index=False).sum()

# Guajira
TerrenosGuajira = Guajira.loc[:,['4. Departamento',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Bosque',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a bahia, estuario, lagunas',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a los cauces de ríos, quebradas, arroyos',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca de volcanes',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte alta de una montaña',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte baja de una montaña',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Humedales',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Isla',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Paramo',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Terreno desértico',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Zona costera',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Ninguna de las anteriores',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Otro']]

TerrenosGuajira.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
TerrenosGuajira = TerrenosGuajira.melt(id_vars=['4. Departamento'],var_name='Terreno', value_name='Total')
TerrenosGuajira = TerrenosGuajira.groupby(['Terreno'],as_index=False).sum()

# Norte 
TerrenosNorteSantander = NorteSantander.loc[:,['4. Departamento',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Bosque',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a bahia, estuario, lagunas',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca a los cauces de ríos, quebradas, arroyos',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Cerca de volcanes',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte alta de una montaña',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/En la parte baja de una montaña',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Humedales',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Isla',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Paramo',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Terreno desértico',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Zona costera',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Ninguna de las anteriores',
                               '23. ¿Cómo es el terreno donde está asentada la comunidad?/Otro']]

TerrenosNorteSantander.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
TerrenosNorteSantander = TerrenosNorteSantander.melt(id_vars=['4. Departamento'],var_name='Terreno', value_name='Total')
TerrenosNorteSantander = TerrenosNorteSantander.groupby(['Terreno'],as_index=False).sum()

##################
## Necesidades de los niños, niñas y adolescentes de la comunidad

## Nacional
Necesidades = df_aprobados.loc[:,['4. Departamento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a agua potable',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a alimentación básica',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a asistencia en salud',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a educación',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a instalaciones sanitarias',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Alojamiento deficitario',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Asistencia a primera infancia',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia física',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia sexual',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Deserción escolar',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Embarazo adolescente',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Escasez de elementos de higiene y desinfección',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Espacios de recreación y esparcimiento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Falta de oportunidades laborales de los cuidadores',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Hacinamiento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Incremento de enfermedades o epidemias',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Saneamiento básico (Acueducto, alcantarillado y recolección de basuras)',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Situación de migración',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Trabajo infantil',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Otra',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/No sabe (Está en fase de investigación)']]

Necesidades.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
Necesidades.rename({'as y adolescentes por grupos armados.':'Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.'},
                       axis = 'columns', inplace=True)
Necesidades = Necesidades.melt(id_vars=['4. Departamento'],var_name='Necesidades NNA', value_name='Total')
Necesidades = Necesidades.groupby(['Necesidades NNA'],as_index=False).sum()

## Arauca
NecesidadesArauca = Arauca.loc[:,['4. Departamento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a agua potable',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a alimentación básica',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a asistencia en salud',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a educación',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a instalaciones sanitarias',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Alojamiento deficitario',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Asistencia a primera infancia',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia física',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia sexual',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Deserción escolar',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Embarazo adolescente',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Escasez de elementos de higiene y desinfección',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Espacios de recreación y esparcimiento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Falta de oportunidades laborales de los cuidadores',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Hacinamiento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Incremento de enfermedades o epidemias',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Saneamiento básico (Acueducto, alcantarillado y recolección de basuras)',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Situación de migración',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Trabajo infantil',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Otra',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/No sabe (Está en fase de investigación)']]

NecesidadesArauca.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
NecesidadesArauca.rename({'as y adolescentes por grupos armados.':'Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.'},
                       axis = 'columns', inplace=True)
NecesidadesArauca = NecesidadesArauca.melt(id_vars=['4. Departamento'],var_name='Necesidades NNA', value_name='Total')
NecesidadesArauca = NecesidadesArauca.groupby(['Necesidades NNA'],as_index=False).sum()

## Choco
NecesidadesChoco = Choco.loc[:,['4. Departamento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a agua potable',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a alimentación básica',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a asistencia en salud',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a educación',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a instalaciones sanitarias',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Alojamiento deficitario',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Asistencia a primera infancia',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia física',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia sexual',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Deserción escolar',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Embarazo adolescente',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Escasez de elementos de higiene y desinfección',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Espacios de recreación y esparcimiento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Falta de oportunidades laborales de los cuidadores',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Hacinamiento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Incremento de enfermedades o epidemias',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Saneamiento básico (Acueducto, alcantarillado y recolección de basuras)',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Situación de migración',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Trabajo infantil',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Otra',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/No sabe (Está en fase de investigación)']]

NecesidadesChoco.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
NecesidadesChoco.rename({'as y adolescentes por grupos armados.':'Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.'},
                       axis = 'columns', inplace=True)
NecesidadesChoco = NecesidadesChoco.melt(id_vars=['4. Departamento'],var_name='Necesidades NNA', value_name='Total')
NecesidadesChoco = NecesidadesChoco.groupby(['Necesidades NNA'],as_index=False).sum()
NecesidadesChoco

## Guajira
NecesidadesGuajira = Guajira.loc[:,['4. Departamento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a agua potable',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a alimentación básica',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a asistencia en salud',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a educación',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a instalaciones sanitarias',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Alojamiento deficitario',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Asistencia a primera infancia',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia física',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia sexual',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Deserción escolar',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Embarazo adolescente',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Escasez de elementos de higiene y desinfección',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Espacios de recreación y esparcimiento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Falta de oportunidades laborales de los cuidadores',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Hacinamiento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Incremento de enfermedades o epidemias',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Saneamiento básico (Acueducto, alcantarillado y recolección de basuras)',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Situación de migración',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Trabajo infantil',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Otra',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/No sabe (Está en fase de investigación)']]

NecesidadesGuajira.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
NecesidadesGuajira.rename({'as y adolescentes por grupos armados.':'Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.'},
                       axis = 'columns', inplace=True)
NecesidadesGuajira = NecesidadesGuajira.melt(id_vars=['4. Departamento'],var_name='Necesidades NNA', value_name='Total')
NecesidadesGuajira = NecesidadesGuajira.groupby(['Necesidades NNA'],as_index=False).sum()

## Norte de Santander
NecesidadesNortSantander = NorteSantander.loc[:,['4. Departamento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a agua potable',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a alimentación básica',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a asistencia en salud',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a educación',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Acceso a instalaciones sanitarias',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Alojamiento deficitario',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Asistencia a primera infancia',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia física',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Casos de Violencia sexual',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Deserción escolar',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Embarazo adolescente',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Escasez de elementos de higiene y desinfección',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Espacios de recreación y esparcimiento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Falta de oportunidades laborales de los cuidadores',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Hacinamiento',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Incremento de enfermedades o epidemias',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Saneamiento básico (Acueducto, alcantarillado y recolección de basuras)',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Situación de migración',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Trabajo infantil',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/Otra',
                                  '18. ¿Seleccione las tres principales necesidades de los niños, niñas y adolescentes de la comunidad?/No sabe (Está en fase de investigación)']]

NecesidadesNortSantander.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
NecesidadesNortSantander.rename({'as y adolescentes por grupos armados.':'Reclutamiento forzado/ Utilización de niños/as y adolescentes por grupos armados.'},
                       axis = 'columns', inplace=True)
NecesidadesNortSantander = NecesidadesNortSantander.melt(id_vars=['4. Departamento'],var_name='Necesidades NNA', value_name='Total')
NecesidadesNortSantander = NecesidadesNortSantander.groupby(['Necesidades NNA'],as_index=False).sum()


##################
## migrantes

### Tiene migrantes

# Nacional
Tiene_migrantes_sum =  df_aprobados.groupby(['¿En la comunidad viven personas migrantes?'],as_index=False).count()
Tiene_migrantes_sum = Tiene_migrantes_sum.filter(['¿En la comunidad viven personas migrantes?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiene_migrantes_sum.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

 # Arauca
Tiene_migrantes_sumArauca =  Arauca.groupby(['¿En la comunidad viven personas migrantes?'],as_index=False).count()
Tiene_migrantes_sumArauca = Tiene_migrantes_sumArauca.filter(['¿En la comunidad viven personas migrantes?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiene_migrantes_sumArauca.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

 # Choco
Tiene_migrantes_sumChoco =  Choco.groupby(['¿En la comunidad viven personas migrantes?'],as_index=False).count()
Tiene_migrantes_sumChoco = Tiene_migrantes_sumChoco.filter(['¿En la comunidad viven personas migrantes?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiene_migrantes_sumChoco.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

 # Guajira
Tiene_migrantes_sumGuajira =  Guajira.groupby(['¿En la comunidad viven personas migrantes?'],as_index=False).count()
Tiene_migrantes_sumGuajira = Tiene_migrantes_sumGuajira.filter(['¿En la comunidad viven personas migrantes?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiene_migrantes_sumGuajira.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

 # NorteSantander
Tiene_migrantes_sumNorteSantander =  NorteSantander.groupby(['¿En la comunidad viven personas migrantes?'],as_index=False).count()
Tiene_migrantes_sumNorteSantander = Tiene_migrantes_sumNorteSantander.filter(['¿En la comunidad viven personas migrantes?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiene_migrantes_sumNorteSantander.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)


### Participación-  Porcentajes
## Nacional
agrupacion_migrantes_sum =  df_aprobados.groupby(['¿Qué porcentaje de la población que vive en la comunidad es migrante?'],as_index=False).count()
agrupacion_migrantes_sum = agrupacion_migrantes_sum.filter(['¿Qué porcentaje de la población que vive en la comunidad es migrante?','1. ¿Quién responde la encuesta?/lider'], axis=1)
agrupacion_migrantes_sum.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

## Arauca
agrupacion_migrantes_sum_arauca =  Arauca.groupby(['¿Qué porcentaje de la población que vive en la comunidad es migrante?'],as_index=False).count()
agrupacion_migrantes_sum_arauca = agrupacion_migrantes_sum_arauca.filter(['¿Qué porcentaje de la población que vive en la comunidad es migrante?','1. ¿Quién responde la encuesta?/lider'], axis=1)
agrupacion_migrantes_sum_arauca.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# Choco
agrupacion_migrantes_sum_choco =  Choco.groupby(['¿Qué porcentaje de la población que vive en la comunidad es migrante?'],as_index=False).count()
agrupacion_migrantes_sum_choco = agrupacion_migrantes_sum_choco.filter(['¿Qué porcentaje de la población que vive en la comunidad es migrante?','1. ¿Quién responde la encuesta?/lider'], axis=1)
agrupacion_migrantes_sum_choco.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# La Guajira
agrupacion_migrantes_sum_guajira=  Guajira.groupby(['¿Qué porcentaje de la población que vive en la comunidad es migrante?'],as_index=False).count()
agrupacion_migrantes_sum_guajira = agrupacion_migrantes_sum_guajira.filter(['¿Qué porcentaje de la población que vive en la comunidad es migrante?','1. ¿Quién responde la encuesta?/lider'], axis=1)
agrupacion_migrantes_sum_guajira.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# norte de santander
agrupacion_migrantes_sum_NorteSantander = NorteSantander.groupby(['¿Qué porcentaje de la población que vive en la comunidad es migrante?'],as_index=False).count()
agrupacion_migrantes_sum_NorteSantander = agrupacion_migrantes_sum_NorteSantander.filter(['¿Qué porcentaje de la población que vive en la comunidad es migrante?','1. ¿Quién responde la encuesta?/lider'], axis=1)
agrupacion_migrantes_sum_NorteSantander.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)


##################
## Salud

### Tiene afectaciones de salud

# Nacional
Tiene_afectaciones_sum =  df_aprobados.groupby(['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'],as_index=False).count()
Tiene_afectaciones_sum = Tiene_afectaciones_sum.filter(['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiene_afectaciones_sum.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# Arauca
Tiene_afectaciones_sumArauca =  Arauca.groupby(['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'],as_index=False).count()
Tiene_afectaciones_sumArauca = Tiene_afectaciones_sumArauca.filter(['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiene_afectaciones_sumArauca.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# Choco
Tiene_afectaciones_sumChoco =  Choco.groupby(['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'],as_index=False).count()
Tiene_afectaciones_sumChoco = Tiene_afectaciones_sumChoco.filter(['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiene_afectaciones_sumChoco.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# Guajira
Tiene_afectaciones_sumGuajira =  Guajira.groupby(['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'],as_index=False).count()
Tiene_afectaciones_sumGuajira = Tiene_afectaciones_sumGuajira.filter(['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiene_afectaciones_sumGuajira.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# Norte Santander
Tiene_afectaciones_sumNorteSantander =  NorteSantander.groupby(['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'],as_index=False).count()
Tiene_afectaciones_sumNorteSantander = Tiene_afectaciones_sumNorteSantander.filter(['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiene_afectaciones_sumNorteSantander.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

### Enfermedades

# Nacional
Enfermedades = df_aprobados.loc[:,['Casos afectaciones salud/Anemia',
                                  'Casos afectaciones salud/Afecciones en la piel',
                                  'Casos afectaciones salud/Chikunguna',
                                  'Casos afectaciones salud/COVID19',
                                  'Casos afectaciones salud/Dengue',
                                  'Casos afectaciones salud/Deshidratación',
                                  'Casos afectaciones salud/Desnutrición',
                                  'Casos afectaciones salud/Enfermedad Diarreíca Aguda - EDA',
                                  'Casos afectaciones salud/Infección Respiratoria Aguda - IRA',
                                  'Casos afectaciones salud/Malaria',
                                  'Casos afectaciones salud/Meningitis',
                                  'Casos afectaciones salud/Rubeola',
                                  'Casos afectaciones salud/Sarampión',
                                  'Casos afectaciones salud/Vómito',
                                  'Casos afectaciones salud/Zika',
                                  'Casos afectaciones salud/Otro']]

Enfermedades.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
Enfermedades = Enfermedades.melt(var_name='Enfermedades', value_name='Total')
Enfermedades = Enfermedades.groupby(['Enfermedades'],as_index=False).sum()

# Arauca
EnfermedadesArauca = Arauca.loc[:,['Casos afectaciones salud/Anemia',
                                  'Casos afectaciones salud/Afecciones en la piel',
                                  'Casos afectaciones salud/Chikunguna',
                                  'Casos afectaciones salud/COVID19',
                                  'Casos afectaciones salud/Dengue',
                                  'Casos afectaciones salud/Deshidratación',
                                  'Casos afectaciones salud/Desnutrición',
                                  'Casos afectaciones salud/Enfermedad Diarreíca Aguda - EDA',
                                  'Casos afectaciones salud/Infección Respiratoria Aguda - IRA',
                                  'Casos afectaciones salud/Malaria',
                                  'Casos afectaciones salud/Meningitis',
                                  'Casos afectaciones salud/Rubeola',
                                  'Casos afectaciones salud/Sarampión',
                                  'Casos afectaciones salud/Vómito',
                                  'Casos afectaciones salud/Zika',
                                  'Casos afectaciones salud/Otro']]

EnfermedadesArauca.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
EnfermedadesArauca = EnfermedadesArauca.melt(var_name='Enfermedades', value_name='Total')
EnfermedadesArauca = EnfermedadesArauca.groupby(['Enfermedades'],as_index=False).sum()

# Choco
EnfermedadesChoco = Choco.loc[:,['Casos afectaciones salud/Anemia',
                                  'Casos afectaciones salud/Afecciones en la piel',
                                  'Casos afectaciones salud/Chikunguna',
                                  'Casos afectaciones salud/COVID19',
                                  'Casos afectaciones salud/Dengue',
                                  'Casos afectaciones salud/Deshidratación',
                                  'Casos afectaciones salud/Desnutrición',
                                  'Casos afectaciones salud/Enfermedad Diarreíca Aguda - EDA',
                                  'Casos afectaciones salud/Infección Respiratoria Aguda - IRA',
                                  'Casos afectaciones salud/Malaria',
                                  'Casos afectaciones salud/Meningitis',
                                  'Casos afectaciones salud/Rubeola',
                                  'Casos afectaciones salud/Sarampión',
                                  'Casos afectaciones salud/Vómito',
                                  'Casos afectaciones salud/Zika',
                                  'Casos afectaciones salud/Otro']]

EnfermedadesChoco.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
EnfermedadesChoco = EnfermedadesChoco.melt(var_name='Enfermedades', value_name='Total')
EnfermedadesChoco = EnfermedadesChoco.groupby(['Enfermedades'],as_index=False).sum()

# Guajira
EnfermedadesGuajira = Guajira.loc[:,['Casos afectaciones salud/Anemia',
                                  'Casos afectaciones salud/Afecciones en la piel',
                                  'Casos afectaciones salud/Chikunguna',
                                  'Casos afectaciones salud/COVID19',
                                  'Casos afectaciones salud/Dengue',
                                  'Casos afectaciones salud/Deshidratación',
                                  'Casos afectaciones salud/Desnutrición',
                                  'Casos afectaciones salud/Enfermedad Diarreíca Aguda - EDA',
                                  'Casos afectaciones salud/Infección Respiratoria Aguda - IRA',
                                  'Casos afectaciones salud/Malaria',
                                  'Casos afectaciones salud/Meningitis',
                                  'Casos afectaciones salud/Rubeola',
                                  'Casos afectaciones salud/Sarampión',
                                  'Casos afectaciones salud/Vómito',
                                  'Casos afectaciones salud/Zika',
                                  'Casos afectaciones salud/Otro']]

EnfermedadesGuajira.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
EnfermedadesGuajira = EnfermedadesGuajira.melt(var_name='Enfermedades', value_name='Total')
EnfermedadesGuajira = EnfermedadesGuajira.groupby(['Enfermedades'],as_index=False).sum()

# Norte de santander
EnfermedadesNorteSantander = NorteSantander.loc[:,['Casos afectaciones salud/Anemia',
                                  'Casos afectaciones salud/Afecciones en la piel',
                                  'Casos afectaciones salud/Chikunguna',
                                  'Casos afectaciones salud/COVID19',
                                  'Casos afectaciones salud/Dengue',
                                  'Casos afectaciones salud/Deshidratación',
                                  'Casos afectaciones salud/Desnutrición',
                                  'Casos afectaciones salud/Enfermedad Diarreíca Aguda - EDA',
                                  'Casos afectaciones salud/Infección Respiratoria Aguda - IRA',
                                  'Casos afectaciones salud/Malaria',
                                  'Casos afectaciones salud/Meningitis',
                                  'Casos afectaciones salud/Rubeola',
                                  'Casos afectaciones salud/Sarampión',
                                  'Casos afectaciones salud/Vómito',
                                  'Casos afectaciones salud/Zika',
                                  'Casos afectaciones salud/Otro']]

EnfermedadesNorteSantander.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
EnfermedadesNorteSantander = EnfermedadesNorteSantander.melt(var_name='Enfermedades', value_name='Total')
EnfermedadesNorteSantander = EnfermedadesNorteSantander.groupby(['Enfermedades'],as_index=False).sum()


### Acceso a salud
# Nacional
AccesoSalud = df_aprobados.loc[:,['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con recursos para el pago de tratamientos médicos',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay centro de salud funcional cerca',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay suficiente capacidad médica para la atención',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con documentos de identidad',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud  (EPS)',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud por condición irregular de migración',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Tiempo de espera para la atención',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Transporte',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Otro']]
AccesoSalud.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
AccesoSalud = AccesoSalud.melt(var_name='Acceso Salud', value_name='Total')
AccesoSalud = AccesoSalud.groupby(['Acceso Salud'],as_index=False).sum()

# Arauca
AccesoSaludArauca = Arauca.loc[:,['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con recursos para el pago de tratamientos médicos',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay centro de salud funcional cerca',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay suficiente capacidad médica para la atención',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con documentos de identidad',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud  (EPS)',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud por condición irregular de migración',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Tiempo de espera para la atención',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Transporte',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Otro']]
AccesoSaludArauca.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
AccesoSaludArauca = AccesoSaludArauca.melt(var_name='Acceso Salud', value_name='Total')
AccesoSaludArauca = AccesoSaludArauca.groupby(['Acceso Salud'],as_index=False).sum()

# Choco
AccesoSaludChoco = Choco.loc[:,['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con recursos para el pago de tratamientos médicos',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay centro de salud funcional cerca',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay suficiente capacidad médica para la atención',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con documentos de identidad',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud  (EPS)',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud por condición irregular de migración',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Tiempo de espera para la atención',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Transporte',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Otro']]
AccesoSaludChoco.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
AccesoSaludChoco = AccesoSaludChoco.melt(var_name='Acceso Salud', value_name='Total')
AccesoSaludChoco = AccesoSaludChoco.groupby(['Acceso Salud'],as_index=False).sum()

# Guajira
AccesoSaludGuajira = Guajira.loc[:,['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con recursos para el pago de tratamientos médicos',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay centro de salud funcional cerca',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay suficiente capacidad médica para la atención',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con documentos de identidad',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud  (EPS)',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud por condición irregular de migración',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Tiempo de espera para la atención',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Transporte',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Otro']]
AccesoSaludGuajira.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
AccesoSaludGuajira = AccesoSaludGuajira.melt(var_name='Acceso Salud', value_name='Total')
AccesoSaludGuajira = AccesoSaludGuajira.groupby(['Acceso Salud'],as_index=False).sum()

# Norte de Santander
AccesoSaludNSan = NorteSantander.loc[:,['¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con recursos para el pago de tratamientos médicos',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay centro de salud funcional cerca',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No hay suficiente capacidad médica para la atención',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No cuentan con documentos de identidad',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud  (EPS)',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/No tiene acceso a servicios de salud por condición irregular de migración',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Tiempo de espera para la atención',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Transporte',
                                  '¿Cuál es la principal barrera que se puede presentar para el acceso a salud?/Otro']]
AccesoSaludNSan.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
AccesoSaludNSan = AccesoSaludNSan.melt(var_name='Acceso Salud', value_name='Total')
AccesoSaludNSan = AccesoSaludNSan.groupby(['Acceso Salud'],as_index=False).sum()


##################
## educación

## tiempo eduación
# Nacional
Tiempo_educacion =  df_aprobados.groupby(['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'],as_index=False).count()
Tiempo_educacion = Tiempo_educacion.filter(['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiempo_educacion.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Arauca
Tiempo_educacionArauca =  Arauca.groupby(['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'],as_index=False).count()
Tiempo_educacionArauca = Tiempo_educacionArauca.filter(['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiempo_educacionArauca.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Choco
Tiempo_educacionChoco =  Choco.groupby(['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'],as_index=False).count()
Tiempo_educacionChoco = Tiempo_educacionChoco.filter(['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiempo_educacionChoco.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Guajira
Tiempo_educacionGuajira =  Guajira.groupby(['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'],as_index=False).count()
Tiempo_educacionGuajira = Tiempo_educacionGuajira.filter(['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiempo_educacionGuajira.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Norte santander
Tiempo_educacionNSan =  NorteSantander.groupby(['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'],as_index=False).count()
Tiempo_educacionNSan = Tiempo_educacionNSan.filter(['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Tiempo_educacionNSan.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)


## Casos sin estudiar
# Nacional
sin_educacion =  df_aprobados.groupby(['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'],as_index=False).count()
sin_educacion = sin_educacion.filter(['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?','1. ¿Quién responde la encuesta?/lider'], axis=1)
sin_educacion.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Arauca
sin_educacionArauca =  Arauca.groupby(['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'],as_index=False).count()
sin_educacionArauca = sin_educacionArauca.filter(['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?','1. ¿Quién responde la encuesta?/lider'], axis=1)
sin_educacionArauca.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Choco
sin_educacionChoco =  Choco.groupby(['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'],as_index=False).count()
sin_educacionChoco = sin_educacionChoco.filter(['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?','1. ¿Quién responde la encuesta?/lider'], axis=1)
sin_educacionChoco.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Guajira
sin_educacionGuajira =  Guajira.groupby(['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'],as_index=False).count()
sin_educacionGuajira = sin_educacionGuajira.filter(['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?','1. ¿Quién responde la encuesta?/lider'], axis=1)
sin_educacionGuajira.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Norte Santander
sin_educacionNSan =  NorteSantander.groupby(['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'],as_index=False).count()
sin_educacionNSan = sin_educacionNSan.filter(['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?','1. ¿Quién responde la encuesta?/lider'], axis=1)
sin_educacionNSan.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# Razones

# Nacional
RazonesSinEducacion = df_aprobados.loc[:,['Razón no estudio/Afectación en la comunidad por conflicto',
                                         'Razón no estudio/Afectación en la infraestructura de las instituciones',
                                         'Razón no estudio/Climas extremos (Temporadas de lluvias)',
                                         'Razón no estudio/Desastres naturales',
                                         'Razón no estudio/Falta de Cupos',
                                         'Razón no estudio/Hacinamiento en las aulas',
                                         'Razón no estudio/Los entornos no son seguros',
                                         'Razón no estudio/No hay docentes',
                                         'Razón no estudio/No hay dotación suficiente (tableros, pupitres, etc)',
                                         'Razón no estudio/No los pueden llevar o recoger del colegio',
                                         'Razón no estudio/Por falta de recursos económicos',
                                         'Razón no estudio/Por largas distancias entre el colegio y la vivienda',
                                         'Razón no estudio/Por su estatus migratorio',
                                         'Razón no estudio/Trabajo infantil (dentro o fuera del hogar)',
                                         'Razón no estudio/Otro']]

RazonesSinEducacion.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
RazonesSinEducacion = RazonesSinEducacion.melt(var_name='Razones sin educacion', value_name='Total')
RazonesSinEducacion = RazonesSinEducacion.groupby(['Razones sin educacion'],as_index=False).sum()

# Arauca
RazonesSinEducacionArauca = Arauca.loc[:,['Razón no estudio/Afectación en la comunidad por conflicto',
                                         'Razón no estudio/Afectación en la infraestructura de las instituciones',
                                         'Razón no estudio/Climas extremos (Temporadas de lluvias)',
                                         'Razón no estudio/Desastres naturales',
                                         'Razón no estudio/Falta de Cupos',
                                         'Razón no estudio/Hacinamiento en las aulas',
                                         'Razón no estudio/Los entornos no son seguros',
                                         'Razón no estudio/No hay docentes',
                                         'Razón no estudio/No hay dotación suficiente (tableros, pupitres, etc)',
                                         'Razón no estudio/No los pueden llevar o recoger del colegio',
                                         'Razón no estudio/Por falta de recursos económicos',
                                         'Razón no estudio/Por largas distancias entre el colegio y la vivienda',
                                         'Razón no estudio/Por su estatus migratorio',
                                         'Razón no estudio/Trabajo infantil (dentro o fuera del hogar)',
                                         'Razón no estudio/Otro']]

RazonesSinEducacionArauca.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
RazonesSinEducacionArauca = RazonesSinEducacionArauca.melt(var_name='Razones sin educacion', value_name='Total')
RazonesSinEducacionArauca = RazonesSinEducacionArauca.groupby(['Razones sin educacion'],as_index=False).sum()

#Choco
RazonesSinEducacionChoco = Choco.loc[:,['Razón no estudio/Afectación en la comunidad por conflicto',
                                         'Razón no estudio/Afectación en la infraestructura de las instituciones',
                                         'Razón no estudio/Climas extremos (Temporadas de lluvias)',
                                         'Razón no estudio/Desastres naturales',
                                         'Razón no estudio/Falta de Cupos',
                                         'Razón no estudio/Hacinamiento en las aulas',
                                         'Razón no estudio/Los entornos no son seguros',
                                         'Razón no estudio/No hay docentes',
                                         'Razón no estudio/No hay dotación suficiente (tableros, pupitres, etc)',
                                         'Razón no estudio/No los pueden llevar o recoger del colegio',
                                         'Razón no estudio/Por falta de recursos económicos',
                                         'Razón no estudio/Por largas distancias entre el colegio y la vivienda',
                                         'Razón no estudio/Por su estatus migratorio',
                                         'Razón no estudio/Trabajo infantil (dentro o fuera del hogar)',
                                         'Razón no estudio/Otro']]

RazonesSinEducacionChoco.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
RazonesSinEducacionChoco = RazonesSinEducacionChoco.melt(var_name='Razones sin educacion', value_name='Total')
RazonesSinEducacionChoco = RazonesSinEducacionChoco.groupby(['Razones sin educacion'],as_index=False).sum()

# Guajira
RazonesSinEducacionGuajira = Guajira.loc[:,['Razón no estudio/Afectación en la comunidad por conflicto',
                                         'Razón no estudio/Afectación en la infraestructura de las instituciones',
                                         'Razón no estudio/Climas extremos (Temporadas de lluvias)',
                                         'Razón no estudio/Desastres naturales',
                                         'Razón no estudio/Falta de Cupos',
                                         'Razón no estudio/Hacinamiento en las aulas',
                                         'Razón no estudio/Los entornos no son seguros',
                                         'Razón no estudio/No hay docentes',
                                         'Razón no estudio/No hay dotación suficiente (tableros, pupitres, etc)',
                                         'Razón no estudio/No los pueden llevar o recoger del colegio',
                                         'Razón no estudio/Por falta de recursos económicos',
                                         'Razón no estudio/Por largas distancias entre el colegio y la vivienda',
                                         'Razón no estudio/Por su estatus migratorio',
                                         'Razón no estudio/Trabajo infantil (dentro o fuera del hogar)',
                                         'Razón no estudio/Otro']]

RazonesSinEducacionGuajira.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
RazonesSinEducacionGuajira = RazonesSinEducacionGuajira.melt(var_name='Razones sin educacion', value_name='Total')
RazonesSinEducacionGuajira = RazonesSinEducacionGuajira.groupby(['Razones sin educacion'],as_index=False).sum()

# Norte Santander
RazonesSinEducacionNSan = NorteSantander.loc[:,['Razón no estudio/Afectación en la comunidad por conflicto',
                                         'Razón no estudio/Afectación en la infraestructura de las instituciones',
                                         'Razón no estudio/Climas extremos (Temporadas de lluvias)',
                                         'Razón no estudio/Desastres naturales',
                                         'Razón no estudio/Falta de Cupos',
                                         'Razón no estudio/Hacinamiento en las aulas',
                                         'Razón no estudio/Los entornos no son seguros',
                                         'Razón no estudio/No hay docentes',
                                         'Razón no estudio/No hay dotación suficiente (tableros, pupitres, etc)',
                                         'Razón no estudio/No los pueden llevar o recoger del colegio',
                                         'Razón no estudio/Por falta de recursos económicos',
                                         'Razón no estudio/Por largas distancias entre el colegio y la vivienda',
                                         'Razón no estudio/Por su estatus migratorio',
                                         'Razón no estudio/Trabajo infantil (dentro o fuera del hogar)',
                                         'Razón no estudio/Otro']]

RazonesSinEducacionNSan.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
RazonesSinEducacionNSan = RazonesSinEducacionNSan.melt(var_name='Razones sin educacion', value_name='Total')
RazonesSinEducacionNSan = RazonesSinEducacionNSan.groupby(['Razones sin educacion'],as_index=False).sum()

##################
## WASH

## Principal fuente de agua
# Nacional
FuenteAguaPrincipal = df_aprobados.loc[:,['Principal fuente de agua/Acueducto por tubería',
                                          'Principal fuente de agua/Agua embotellada o en bolsa',
                                          'Principal fuente de agua/Aguas lluvias',
                                          'Principal fuente de agua/Aguatero',
                                          'Principal fuente de agua/Carro tanque o agua en camión cisterna',
                                          'Principal fuente de agua/No hay servicio',
                                          'Principal fuente de agua/Otra fuente por tubería',
                                          'Principal fuente de agua/Pila pública o de suministro comunitario',
                                          'Principal fuente de agua/Pozo con bomba',
                                          'Principal fuente de agua/Pozo sin bomba, aljibe, jagüey o barreno',
                                          'Principal fuente de agua/Río, quebrada, nacimiento o manantial',
                                          'Principal fuente de agua/Tanque de agua',
                                          'Principal fuente de agua/Tecnologías alternativas (puntos de suministro o de abasto)',
                                          'Principal fuente de agua/Otra',
                                          'Principal fuente de agua/No sabe']]

FuenteAguaPrincipal.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
FuenteAguaPrincipal = FuenteAguaPrincipal.melt(var_name='Fuente de agua', value_name='Total')
FuenteAguaPrincipal = FuenteAguaPrincipal.groupby(['Fuente de agua'],as_index=False).sum()

# Arauca
FuenteAguaPrincipalArauca = Arauca.loc[:,['Principal fuente de agua/Acueducto por tubería',
                                          'Principal fuente de agua/Agua embotellada o en bolsa',
                                          'Principal fuente de agua/Aguas lluvias',
                                          'Principal fuente de agua/Aguatero',
                                          'Principal fuente de agua/Carro tanque o agua en camión cisterna',
                                          'Principal fuente de agua/No hay servicio',
                                          'Principal fuente de agua/Otra fuente por tubería',
                                          'Principal fuente de agua/Pila pública o de suministro comunitario',
                                          'Principal fuente de agua/Pozo con bomba',
                                          'Principal fuente de agua/Pozo sin bomba, aljibe, jagüey o barreno',
                                          'Principal fuente de agua/Río, quebrada, nacimiento o manantial',
                                          'Principal fuente de agua/Tanque de agua',
                                          'Principal fuente de agua/Tecnologías alternativas (puntos de suministro o de abasto)',
                                          'Principal fuente de agua/Otra',
                                          'Principal fuente de agua/No sabe']]

FuenteAguaPrincipalArauca.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
FuenteAguaPrincipalArauca = FuenteAguaPrincipalArauca.melt(var_name='Fuente de agua', value_name='Total')
FuenteAguaPrincipalArauca = FuenteAguaPrincipalArauca.groupby(['Fuente de agua'],as_index=False).sum()

# Choco
FuenteAguaPrincipalChoco = Choco.loc[:,['Principal fuente de agua/Acueducto por tubería',
                                          'Principal fuente de agua/Agua embotellada o en bolsa',
                                          'Principal fuente de agua/Aguas lluvias',
                                          'Principal fuente de agua/Aguatero',
                                          'Principal fuente de agua/Carro tanque o agua en camión cisterna',
                                          'Principal fuente de agua/No hay servicio',
                                          'Principal fuente de agua/Otra fuente por tubería',
                                          'Principal fuente de agua/Pila pública o de suministro comunitario',
                                          'Principal fuente de agua/Pozo con bomba',
                                          'Principal fuente de agua/Pozo sin bomba, aljibe, jagüey o barreno',
                                          'Principal fuente de agua/Río, quebrada, nacimiento o manantial',
                                          'Principal fuente de agua/Tanque de agua',
                                          'Principal fuente de agua/Tecnologías alternativas (puntos de suministro o de abasto)',
                                          'Principal fuente de agua/Otra',
                                          'Principal fuente de agua/No sabe']]

FuenteAguaPrincipalChoco.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
FuenteAguaPrincipalChoco = FuenteAguaPrincipalChoco.melt(var_name='Fuente de agua', value_name='Total')
FuenteAguaPrincipalChoco = FuenteAguaPrincipalChoco.groupby(['Fuente de agua'],as_index=False).sum()

# Guajira
FuenteAguaPrincipalGuajira = Guajira.loc[:,['Principal fuente de agua/Acueducto por tubería',
                                          'Principal fuente de agua/Agua embotellada o en bolsa',
                                          'Principal fuente de agua/Aguas lluvias',
                                          'Principal fuente de agua/Aguatero',
                                          'Principal fuente de agua/Carro tanque o agua en camión cisterna',
                                          'Principal fuente de agua/No hay servicio',
                                          'Principal fuente de agua/Otra fuente por tubería',
                                          'Principal fuente de agua/Pila pública o de suministro comunitario',
                                          'Principal fuente de agua/Pozo con bomba',
                                          'Principal fuente de agua/Pozo sin bomba, aljibe, jagüey o barreno',
                                          'Principal fuente de agua/Río, quebrada, nacimiento o manantial',
                                          'Principal fuente de agua/Tanque de agua',
                                          'Principal fuente de agua/Tecnologías alternativas (puntos de suministro o de abasto)',
                                          'Principal fuente de agua/Otra',
                                          'Principal fuente de agua/No sabe']]

FuenteAguaPrincipalGuajira.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
FuenteAguaPrincipalGuajira = FuenteAguaPrincipalGuajira.melt(var_name='Fuente de agua', value_name='Total')
FuenteAguaPrincipalGuajira = FuenteAguaPrincipalGuajira.groupby(['Fuente de agua'],as_index=False).sum()

# Norte de Santander
FuenteAguaPrincipalNSan = NorteSantander.loc[:,['Principal fuente de agua/Acueducto por tubería',
                                          'Principal fuente de agua/Agua embotellada o en bolsa',
                                          'Principal fuente de agua/Aguas lluvias',
                                          'Principal fuente de agua/Aguatero',
                                          'Principal fuente de agua/Carro tanque o agua en camión cisterna',
                                          'Principal fuente de agua/No hay servicio',
                                          'Principal fuente de agua/Otra fuente por tubería',
                                          'Principal fuente de agua/Pila pública o de suministro comunitario',
                                          'Principal fuente de agua/Pozo con bomba',
                                          'Principal fuente de agua/Pozo sin bomba, aljibe, jagüey o barreno',
                                          'Principal fuente de agua/Río, quebrada, nacimiento o manantial',
                                          'Principal fuente de agua/Tanque de agua',
                                          'Principal fuente de agua/Tecnologías alternativas (puntos de suministro o de abasto)',
                                          'Principal fuente de agua/Otra',
                                          'Principal fuente de agua/No sabe']]

FuenteAguaPrincipalNSan.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
FuenteAguaPrincipalNSan = FuenteAguaPrincipalNSan.melt(var_name='Fuente de agua', value_name='Total')
FuenteAguaPrincipalNSan = FuenteAguaPrincipalNSan.groupby(['Fuente de agua'],as_index=False).sum()

## Recolección basura
# Nacional
RecoleccionBasuras = df_aprobados.loc[:,['Modalidad de recolección de basuras en la comunidad/Por recolección pública, privada o comunitaria',
                                         'Modalidad de recolección de basuras en la comunidad/Se arroja a un río, quebrada, cano o laguna',
                                         'Modalidad de recolección de basuras en la comunidad/Se arroja a un patio, lote, zanja o baldío',
                                         'Modalidad de recolección de basuras en la comunidad/Se quema o se entierra',
                                         'Modalidad de recolección de basuras en la comunidad/Se elimina de otra forma',
                                         'Modalidad de recolección de basuras en la comunidad/Se clasifica la basura entre orgánicos y reciclaje, aprovechando todos los residuos',
                                         'Modalidad de recolección de basuras en la comunidad/Otro',
                                         'Modalidad de recolección de basuras en la comunidad/No sabe']]

RecoleccionBasuras.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
RecoleccionBasuras = RecoleccionBasuras.melt(var_name='Recoleccion basuras', value_name='Total')
RecoleccionBasuras = RecoleccionBasuras.groupby(['Recoleccion basuras'],as_index=False).sum()

# Arauca
RecoleccionBasurasArauca = Arauca.loc[:,['Modalidad de recolección de basuras en la comunidad/Por recolección pública, privada o comunitaria',
                                         'Modalidad de recolección de basuras en la comunidad/Se arroja a un río, quebrada, cano o laguna',
                                         'Modalidad de recolección de basuras en la comunidad/Se arroja a un patio, lote, zanja o baldío',
                                         'Modalidad de recolección de basuras en la comunidad/Se quema o se entierra',
                                         'Modalidad de recolección de basuras en la comunidad/Se elimina de otra forma',
                                         'Modalidad de recolección de basuras en la comunidad/Se clasifica la basura entre orgánicos y reciclaje, aprovechando todos los residuos',
                                         'Modalidad de recolección de basuras en la comunidad/Otro',
                                         'Modalidad de recolección de basuras en la comunidad/No sabe']]

RecoleccionBasurasArauca.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
RecoleccionBasurasArauca = RecoleccionBasurasArauca.melt(var_name='Recoleccion basuras', value_name='Total')
RecoleccionBasurasArauca = RecoleccionBasurasArauca.groupby(['Recoleccion basuras'],as_index=False).sum()

# Choco
RecoleccionBasurasChoco = Choco.loc[:,['Modalidad de recolección de basuras en la comunidad/Por recolección pública, privada o comunitaria',
                                         'Modalidad de recolección de basuras en la comunidad/Se arroja a un río, quebrada, cano o laguna',
                                         'Modalidad de recolección de basuras en la comunidad/Se arroja a un patio, lote, zanja o baldío',
                                         'Modalidad de recolección de basuras en la comunidad/Se quema o se entierra',
                                         'Modalidad de recolección de basuras en la comunidad/Se elimina de otra forma',
                                         'Modalidad de recolección de basuras en la comunidad/Se clasifica la basura entre orgánicos y reciclaje, aprovechando todos los residuos',
                                         'Modalidad de recolección de basuras en la comunidad/Otro',
                                         'Modalidad de recolección de basuras en la comunidad/No sabe']]

RecoleccionBasurasChoco.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
RecoleccionBasurasChoco = RecoleccionBasurasChoco.melt(var_name='Recoleccion basuras', value_name='Total')
RecoleccionBasurasChoco = RecoleccionBasurasChoco.groupby(['Recoleccion basuras'],as_index=False).sum()

# Guajira
RecoleccionBasurasGuajira = Guajira.loc[:,['Modalidad de recolección de basuras en la comunidad/Por recolección pública, privada o comunitaria',
                                         'Modalidad de recolección de basuras en la comunidad/Se arroja a un río, quebrada, cano o laguna',
                                         'Modalidad de recolección de basuras en la comunidad/Se arroja a un patio, lote, zanja o baldío',
                                         'Modalidad de recolección de basuras en la comunidad/Se quema o se entierra',
                                         'Modalidad de recolección de basuras en la comunidad/Se elimina de otra forma',
                                         'Modalidad de recolección de basuras en la comunidad/Se clasifica la basura entre orgánicos y reciclaje, aprovechando todos los residuos',
                                         'Modalidad de recolección de basuras en la comunidad/Otro',
                                         'Modalidad de recolección de basuras en la comunidad/No sabe']]

RecoleccionBasurasGuajira.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
RecoleccionBasurasGuajira = RecoleccionBasurasGuajira.melt(var_name='Recoleccion basuras', value_name='Total')
RecoleccionBasurasGuajira = RecoleccionBasurasGuajira.groupby(['Recoleccion basuras'],as_index=False).sum()

# Norte Sand
RecoleccionBasurasNSan = NorteSantander.loc[:,['Modalidad de recolección de basuras en la comunidad/Por recolección pública, privada o comunitaria',
                                         'Modalidad de recolección de basuras en la comunidad/Se arroja a un río, quebrada, cano o laguna',
                                         'Modalidad de recolección de basuras en la comunidad/Se arroja a un patio, lote, zanja o baldío',
                                         'Modalidad de recolección de basuras en la comunidad/Se quema o se entierra',
                                         'Modalidad de recolección de basuras en la comunidad/Se elimina de otra forma',
                                         'Modalidad de recolección de basuras en la comunidad/Se clasifica la basura entre orgánicos y reciclaje, aprovechando todos los residuos',
                                         'Modalidad de recolección de basuras en la comunidad/Otro',
                                         'Modalidad de recolección de basuras en la comunidad/No sabe']]

RecoleccionBasurasNSan.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
RecoleccionBasurasNSan = RecoleccionBasurasNSan.melt(var_name='Recoleccion basuras', value_name='Total')
RecoleccionBasurasNSan = RecoleccionBasurasNSan.groupby(['Recoleccion basuras'],as_index=False).sum()

## modalidad de recolección de basuras en la comunidad
# Nacional
FocosContaminacion = df_aprobados.loc[:,['Focos de contaminación/Agua estancada',
                                         'Focos de contaminación/Animales muertos',
                                         'Focos de contaminación/Basureros clandestinos',
                                         'Focos de contaminación/Corrientes de aguas negras',
                                         'Focos de contaminación/Defecación al aire libre',
                                         'Focos de contaminación/Desechos químicos',
                                         'Focos de contaminación/Disposición de basura al aire libre',
                                         'Focos de contaminación/Disposición de excretas inadecuada',
                                         'Focos de contaminación/Ninguno',
                                         'Focos de contaminación/Plantas de tratamiento de aguas residuales',
                                         'Focos de contaminación/Roedores',
                                         'Focos de contaminación/Transmisión de enfermedades por vectores',
                                         'Focos de contaminación/Zonas de basuras permanentes',
                                         'Focos de contaminación/Otro',
                                         'Focos de contaminación/No sabe']]

FocosContaminacion.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
FocosContaminacion = FocosContaminacion.melt(var_name='Focos contaminacion', value_name='Total')
FocosContaminacion = FocosContaminacion.groupby(['Focos contaminacion'],as_index=False).sum()

# Arauca
FocosContaminacionArauca = Arauca.loc[:,['Focos de contaminación/Agua estancada',
                                         'Focos de contaminación/Animales muertos',
                                         'Focos de contaminación/Basureros clandestinos',
                                         'Focos de contaminación/Corrientes de aguas negras',
                                         'Focos de contaminación/Defecación al aire libre',
                                         'Focos de contaminación/Desechos químicos',
                                         'Focos de contaminación/Disposición de basura al aire libre',
                                         'Focos de contaminación/Disposición de excretas inadecuada',
                                         'Focos de contaminación/Ninguno',
                                         'Focos de contaminación/Plantas de tratamiento de aguas residuales',
                                         'Focos de contaminación/Roedores',
                                         'Focos de contaminación/Transmisión de enfermedades por vectores',
                                         'Focos de contaminación/Zonas de basuras permanentes',
                                         'Focos de contaminación/Otro',
                                         'Focos de contaminación/No sabe']]

FocosContaminacionArauca.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
FocosContaminacionArauca = FocosContaminacionArauca.melt(var_name='Focos contaminacion', value_name='Total')
FocosContaminacionArauca = FocosContaminacionArauca.groupby(['Focos contaminacion'],as_index=False).sum()

#Choco
FocosContaminacionChoco = Choco.loc[:,['Focos de contaminación/Agua estancada',
                                         'Focos de contaminación/Animales muertos',
                                         'Focos de contaminación/Basureros clandestinos',
                                         'Focos de contaminación/Corrientes de aguas negras',
                                         'Focos de contaminación/Defecación al aire libre',
                                         'Focos de contaminación/Desechos químicos',
                                         'Focos de contaminación/Disposición de basura al aire libre',
                                         'Focos de contaminación/Disposición de excretas inadecuada',
                                         'Focos de contaminación/Ninguno',
                                         'Focos de contaminación/Plantas de tratamiento de aguas residuales',
                                         'Focos de contaminación/Roedores',
                                         'Focos de contaminación/Transmisión de enfermedades por vectores',
                                         'Focos de contaminación/Zonas de basuras permanentes',
                                         'Focos de contaminación/Otro',
                                         'Focos de contaminación/No sabe']]

FocosContaminacionChoco.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
FocosContaminacionChoco = FocosContaminacionChoco.melt(var_name='Focos contaminacion', value_name='Total')
FocosContaminacionChoco = FocosContaminacionChoco.groupby(['Focos contaminacion'],as_index=False).sum()

# Guajira
FocosContaminacionGuajira = Guajira.loc[:,['Focos de contaminación/Agua estancada',
                                         'Focos de contaminación/Animales muertos',
                                         'Focos de contaminación/Basureros clandestinos',
                                         'Focos de contaminación/Corrientes de aguas negras',
                                         'Focos de contaminación/Defecación al aire libre',
                                         'Focos de contaminación/Desechos químicos',
                                         'Focos de contaminación/Disposición de basura al aire libre',
                                         'Focos de contaminación/Disposición de excretas inadecuada',
                                         'Focos de contaminación/Ninguno',
                                         'Focos de contaminación/Plantas de tratamiento de aguas residuales',
                                         'Focos de contaminación/Roedores',
                                         'Focos de contaminación/Transmisión de enfermedades por vectores',
                                         'Focos de contaminación/Zonas de basuras permanentes',
                                         'Focos de contaminación/Otro',
                                         'Focos de contaminación/No sabe']]

FocosContaminacionGuajira.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
FocosContaminacionGuajira = FocosContaminacionGuajira.melt(var_name='Focos contaminacion', value_name='Total')
FocosContaminacionGuajira = FocosContaminacionGuajira.groupby(['Focos contaminacion'],as_index=False).sum()

# Norte Santander
FocosContaminacionNSan = NorteSantander.loc[:,['Focos de contaminación/Agua estancada',
                                         'Focos de contaminación/Animales muertos',
                                         'Focos de contaminación/Basureros clandestinos',
                                         'Focos de contaminación/Corrientes de aguas negras',
                                         'Focos de contaminación/Defecación al aire libre',
                                         'Focos de contaminación/Desechos químicos',
                                         'Focos de contaminación/Disposición de basura al aire libre',
                                         'Focos de contaminación/Disposición de excretas inadecuada',
                                         'Focos de contaminación/Ninguno',
                                         'Focos de contaminación/Plantas de tratamiento de aguas residuales',
                                         'Focos de contaminación/Roedores',
                                         'Focos de contaminación/Transmisión de enfermedades por vectores',
                                         'Focos de contaminación/Zonas de basuras permanentes',
                                         'Focos de contaminación/Otro',
                                         'Focos de contaminación/No sabe']]

FocosContaminacionNSan.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
FocosContaminacionNSan = FocosContaminacionNSan.melt(var_name='Focos contaminacion', value_name='Total')
FocosContaminacionNSan = FocosContaminacionNSan.groupby(['Focos contaminacion'],as_index=False).sum()

##################
## Protección

# Trabajo infantil
# Nacional
trabajo_infantil =  df_aprobados.groupby(['¿Existen casos de trabajo infantil en la comunidad?'],as_index=False).count()
trabajo_infantil = trabajo_infantil.filter(['¿Existen casos de trabajo infantil en la comunidad?','1. ¿Quién responde la encuesta?/lider'], axis=1)
trabajo_infantil.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Arauca
trabajo_infantilArauca =  Arauca.groupby(['¿Existen casos de trabajo infantil en la comunidad?'],as_index=False).count()
trabajo_infantilArauca = trabajo_infantilArauca.filter(['¿Existen casos de trabajo infantil en la comunidad?','1. ¿Quién responde la encuesta?/lider'], axis=1)
trabajo_infantilArauca.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Choco
trabajo_infantilChoco =  Choco.groupby(['¿Existen casos de trabajo infantil en la comunidad?'],as_index=False).count()
trabajo_infantilChoco = trabajo_infantilChoco.filter(['¿Existen casos de trabajo infantil en la comunidad?','1. ¿Quién responde la encuesta?/lider'], axis=1)
trabajo_infantilChoco.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Guajira
trabajo_infantilGuajira =  Guajira.groupby(['¿Existen casos de trabajo infantil en la comunidad?'],as_index=False).count()
trabajo_infantilGuajira = trabajo_infantilGuajira.filter(['¿Existen casos de trabajo infantil en la comunidad?','1. ¿Quién responde la encuesta?/lider'], axis=1)
trabajo_infantilGuajira.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# N Santander
trabajo_infantilNSan =  NorteSantander.groupby(['¿Existen casos de trabajo infantil en la comunidad?'],as_index=False).count()
trabajo_infantilNSan = trabajo_infantilNSan.filter(['¿Existen casos de trabajo infantil en la comunidad?','1. ¿Quién responde la encuesta?/lider'], axis=1)
trabajo_infantilNSan.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

## NNA Mendicidad

# Nacional
mendicidad =  df_aprobados.groupby(['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'],as_index=False).count()
mendicidad = mendicidad.filter(['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?','1. ¿Quién responde la encuesta?/lider'], axis=1)
mendicidad.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Arauca
mendicidadArauca =  Arauca.groupby(['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'],as_index=False).count()
mendicidadArauca = mendicidadArauca.filter(['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?','1. ¿Quién responde la encuesta?/lider'], axis=1)
mendicidadArauca.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Choco
mendicidadChoco =  Choco.groupby(['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'],as_index=False).count()
mendicidadChoco = mendicidadChoco.filter(['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?','1. ¿Quién responde la encuesta?/lider'], axis=1)
mendicidadChoco.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Guajira
mendicidadGuajira =  Guajira.groupby(['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'],as_index=False).count()
mendicidadGuajira = mendicidadGuajira.filter(['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?','1. ¿Quién responde la encuesta?/lider'], axis=1)
mendicidadGuajira.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# N Santander
mendicidadNSan =  NorteSantander.groupby(['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'],as_index=False).count()
mendicidadNSan = mendicidadNSan.filter(['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?','1. ¿Quién responde la encuesta?/lider'], axis=1)
mendicidadNSan.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

## Apoyos economicos

# Nacional
ApoyosEconomicos =  df_aprobados.groupby(['¿Se han presentado apoyo o ayudas económicas a las familias?'],as_index=False).count()
ApoyosEconomicos = ApoyosEconomicos.filter(['¿Se han presentado apoyo o ayudas económicas a las familias?','1. ¿Quién responde la encuesta?/lider'], axis=1)
ApoyosEconomicos.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Arauca
ApoyosEconomicosArauca =  Arauca.groupby(['¿Se han presentado apoyo o ayudas económicas a las familias?'],as_index=False).count()
ApoyosEconomicosArauca = ApoyosEconomicosArauca.filter(['¿Se han presentado apoyo o ayudas económicas a las familias?','1. ¿Quién responde la encuesta?/lider'], axis=1)
ApoyosEconomicosArauca.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Choco
ApoyosEconomicosChoco =  Choco.groupby(['¿Se han presentado apoyo o ayudas económicas a las familias?'],as_index=False).count()
ApoyosEconomicosChoco = ApoyosEconomicosChoco.filter(['¿Se han presentado apoyo o ayudas económicas a las familias?','1. ¿Quién responde la encuesta?/lider'], axis=1)
ApoyosEconomicosChoco.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Guajira
ApoyosEconomicosGuajira =  Guajira.groupby(['¿Se han presentado apoyo o ayudas económicas a las familias?'],as_index=False).count()
ApoyosEconomicosGuajira = ApoyosEconomicosGuajira.filter(['¿Se han presentado apoyo o ayudas económicas a las familias?','1. ¿Quién responde la encuesta?/lider'], axis=1)
ApoyosEconomicosGuajira.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# N Santander
ApoyosEconomicosNSan =  NorteSantander.groupby(['¿Se han presentado apoyo o ayudas económicas a las familias?'],as_index=False).count()
ApoyosEconomicosNSan = ApoyosEconomicosNSan.filter(['¿Se han presentado apoyo o ayudas económicas a las familias?','1. ¿Quién responde la encuesta?/lider'], axis=1)
ApoyosEconomicosNSan.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)


##################
## SAN

##¿En la comunidad, los niños, niñas y adolescentes reciben algún apoyo alimentario?

# Nacional
ApoyoAlimentario = df_aprobados.loc[:,['Apoyo alimentario/Subsidio económico',
                                      'Apoyo alimentario/Comedores comunitarios',
                                      'Apoyo alimentario/Kits o bonos alimentarios',
                                      'Apoyo alimentario/Ninguno',
                                      'Apoyo alimentario/No sabe',
                                      'Apoyo alimentario/Otra']]

ApoyoAlimentario.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
ApoyoAlimentario = ApoyoAlimentario.melt(var_name='Apoyo Alimentario', value_name='Total')
ApoyoAlimentario = ApoyoAlimentario.groupby(['Apoyo Alimentario'],as_index=False).sum()
# Arauca
ApoyoAlimentarioArauca = Arauca.loc[:,['Apoyo alimentario/Subsidio económico',
                                      'Apoyo alimentario/Comedores comunitarios',
                                      'Apoyo alimentario/Kits o bonos alimentarios',
                                      'Apoyo alimentario/Ninguno',
                                      'Apoyo alimentario/No sabe',
                                      'Apoyo alimentario/Otra']]

ApoyoAlimentarioArauca.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
ApoyoAlimentarioArauca = ApoyoAlimentarioArauca.melt(var_name='Apoyo Alimentario', value_name='Total')
ApoyoAlimentarioArauca = ApoyoAlimentarioArauca.groupby(['Apoyo Alimentario'],as_index=False).sum()
# Choco
ApoyoAlimentarioChoco = Choco.loc[:,['Apoyo alimentario/Subsidio económico',
                                      'Apoyo alimentario/Comedores comunitarios',
                                      'Apoyo alimentario/Kits o bonos alimentarios',
                                      'Apoyo alimentario/Ninguno',
                                      'Apoyo alimentario/No sabe',
                                      'Apoyo alimentario/Otra']]

ApoyoAlimentarioChoco.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
ApoyoAlimentarioChoco = ApoyoAlimentarioChoco.melt(var_name='Apoyo Alimentario', value_name='Total')
ApoyoAlimentarioChoco = ApoyoAlimentarioChoco.groupby(['Apoyo Alimentario'],as_index=False).sum()
# Guajira
ApoyoAlimentarioGuajira = Guajira.loc[:,['Apoyo alimentario/Subsidio económico',
                                      'Apoyo alimentario/Comedores comunitarios',
                                      'Apoyo alimentario/Kits o bonos alimentarios',
                                      'Apoyo alimentario/Ninguno',
                                      'Apoyo alimentario/No sabe',
                                      'Apoyo alimentario/Otra']]

ApoyoAlimentarioGuajira.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
ApoyoAlimentarioGuajira = ApoyoAlimentarioGuajira.melt(var_name='Apoyo Alimentario', value_name='Total')
ApoyoAlimentarioGuajira = ApoyoAlimentarioGuajira.groupby(['Apoyo Alimentario'],as_index=False).sum()
# Norte de Santander
ApoyoAlimentarioNSan = NorteSantander.loc[:,['Apoyo alimentario/Subsidio económico',
                                      'Apoyo alimentario/Comedores comunitarios',
                                      'Apoyo alimentario/Kits o bonos alimentarios',
                                      'Apoyo alimentario/Ninguno',
                                      'Apoyo alimentario/No sabe',
                                      'Apoyo alimentario/Otra']]

ApoyoAlimentarioNSan.rename(lambda x: x.split('/')[-1], axis = 'columns', inplace=True)
ApoyoAlimentarioNSan = ApoyoAlimentarioNSan.melt(var_name='Apoyo Alimentario', value_name='Total')
ApoyoAlimentarioNSan = ApoyoAlimentarioNSan.groupby(['Apoyo Alimentario'],as_index=False).sum()

## Indique el nivel aproximado de consumo de alimentos por parte de los niños, niñas y adolescentes de la comunidadeconomicos
# Nacional
ConsumoAlimentos =  df_aprobados.groupby(['Consumo de alimentos NNA en la comunidad'],as_index=False).count()
ConsumoAlimentos = ConsumoAlimentos.filter(['Consumo de alimentos NNA en la comunidad','1. ¿Quién responde la encuesta?/lider'], axis=1)
ConsumoAlimentos.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Arauca
ConsumoAlimentosArauca =  Arauca.groupby(['Consumo de alimentos NNA en la comunidad'],as_index=False).count()
ConsumoAlimentosArauca = ConsumoAlimentosArauca.filter(['Consumo de alimentos NNA en la comunidad','1. ¿Quién responde la encuesta?/lider'], axis=1)
ConsumoAlimentosArauca.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Choco
ConsumoAlimentosChoco =  Choco.groupby(['Consumo de alimentos NNA en la comunidad'],as_index=False).count()
ConsumoAlimentosChoco = ConsumoAlimentosChoco.filter(['Consumo de alimentos NNA en la comunidad','1. ¿Quién responde la encuesta?/lider'], axis=1)
ConsumoAlimentosChoco.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Guajira
ConsumoAlimentosGuajira =  Guajira.groupby(['Consumo de alimentos NNA en la comunidad'],as_index=False).count()
ConsumoAlimentosGuajira = ConsumoAlimentosGuajira.filter(['Consumo de alimentos NNA en la comunidad','1. ¿Quién responde la encuesta?/lider'], axis=1)
ConsumoAlimentosGuajira.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# N San
ConsumoAlimentosNSan =  NorteSantander.groupby(['Consumo de alimentos NNA en la comunidad'],as_index=False).count()
ConsumoAlimentosNSan = ConsumoAlimentosNSan.filter(['Consumo de alimentos NNA en la comunidad','1. ¿Quién responde la encuesta?/lider'], axis=1)
ConsumoAlimentosNSan.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

# ¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?
# Nacional
Desnutricion =  df_aprobados.groupby(['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'],as_index=False).count()
Desnutricion = Desnutricion.filter(['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?','1. ¿Quién responde la encuesta?/lider'], axis=1)
Desnutricion.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Arauca
DesnutricionArauca =  Arauca.groupby(['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'],as_index=False).count()
DesnutricionArauca = DesnutricionArauca.filter(['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?','1. ¿Quién responde la encuesta?/lider'], axis=1)
DesnutricionArauca.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Choco
DesnutricionChoco =  Choco.groupby(['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'],as_index=False).count()
DesnutricionChoco = DesnutricionChoco.filter(['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?','1. ¿Quién responde la encuesta?/lider'], axis=1)
DesnutricionChoco.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# Guajira
DesnutricionGuajira =  Guajira.groupby(['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'],as_index=False).count()
DesnutricionGuajira = DesnutricionGuajira.filter(['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?','1. ¿Quién responde la encuesta?/lider'], axis=1)
DesnutricionGuajira.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)
# NSan
DesnutricionNSan =  NorteSantander.groupby(['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'],as_index=False).count()
DesnutricionNSan = DesnutricionNSan.filter(['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?','1. ¿Quién responde la encuesta?/lider'], axis=1)
DesnutricionNSan.rename(columns = {'1. ¿Quién responde la encuesta?/lider':'Total'}, inplace = True)

########################################
## para graficas

##################
## mapa

## Nacional

asentamientos = df_aprobados['8. Barrio, asentamiento, comunidad'].tolist()
longitud = df_aprobados['Longitud'].tolist()
latitud = df_aprobados['Latitud'].tolist()


##################
## Evaluaciones realizadas

## evaluaciones realizadas

EveReaDepar = agrupacion_dep_count['4. Departamento'].tolist()
EveReaCuantas = agrupacion_dep_count['1. ¿Quién responde la encuesta?/lider'].tolist()

##################
## Necesidades

## Necesidades Nacionales
NecesidadesNom = Necesidades['Necesidades NNA'].tolist()
NecesidadesNum = Necesidades['Total'].tolist()

## Necesidades Arauca
NecesidadesNomAra = NecesidadesArauca['Necesidades NNA'].tolist()
NecesidadesNumAra = NecesidadesArauca['Total'].tolist()

## Necesidades Choco
NecesidadesNomChoco = NecesidadesChoco['Necesidades NNA'].tolist()
NecesidadesNumChoco = NecesidadesChoco['Total'].tolist()

## Necesidades Guajira
NecesidadesNomGuajira = NecesidadesGuajira['Necesidades NNA'].tolist()
NecesidadesNumGuajira = NecesidadesGuajira['Total'].tolist()

## Necesidades Norte de Santander
NecesidadesNomNSant = NecesidadesNortSantander['Necesidades NNA'].tolist()
NecesidadesNumNSant = NecesidadesNortSantander['Total'].tolist()

##################
## tres maximos

# Nacional
OrderNecesidades = Necesidades.sort_values(by=['Total'],ascending=[False])
MaxNecesidades = OrderNecesidades.iloc[:1]
MaxNecesidadesNom = MaxNecesidades['Necesidades NNA'].values[0]
MaxNecesidadesNum = MaxNecesidades['Total'].values[0]

MaxSecNecesidades = OrderNecesidades.iloc[1:2]
MaxSecNecesidadesNom = MaxSecNecesidades['Necesidades NNA'].values[0]
MaxSecNecesidadesNum = MaxSecNecesidades['Total'].values[0]

MaxThrNecesidades = OrderNecesidades.iloc[2:3]
MaxThrNecesidadesNom = MaxThrNecesidades['Necesidades NNA'].values[0]
MaxThrNecesidadesNum = MaxThrNecesidades['Total'].values[0]

# Arauca
OrderNecesidadesAra = NecesidadesArauca.sort_values(by=['Total'],ascending=[False])
MaxNecesidadesAra = OrderNecesidadesAra.iloc[:1]
MaxNecesidadesNomAra = MaxNecesidadesAra['Necesidades NNA'].values[0]
MaxNecesidadesNumAra = MaxNecesidadesAra['Total'].values[0]

MaxSecNecesidadesAra = OrderNecesidadesAra.iloc[1:2]
MaxSecNecesidadesNomAra = MaxSecNecesidadesAra['Necesidades NNA'].values[0]
MaxSecNecesidadesNumAra = MaxSecNecesidadesAra['Total'].values[0]

MaxThrNecesidadesAra = OrderNecesidadesAra.iloc[2:3]
MaxThrNecesidadesNomAra = MaxThrNecesidadesAra['Necesidades NNA'].values[0]
MaxThrNecesidadesNumAra = MaxThrNecesidadesAra['Total'].values[0]

# Chocó
OrderNecesidadesChoco = NecesidadesChoco.sort_values(by=['Total'],ascending=[False])
MaxNecesidadesChoco = OrderNecesidadesChoco.iloc[:1]
MaxNecesidadesNomChoco = MaxNecesidadesChoco['Necesidades NNA'].values[0]
MaxNecesidadesNumChoco = MaxNecesidadesChoco['Total'].values[0]

MaxSecNecesidadesChoco = OrderNecesidadesChoco.iloc[1:2]
MaxSecNecesidadesNomChoco = MaxSecNecesidadesChoco['Necesidades NNA'].values[0]
MaxSecNecesidadesNumChoco = MaxSecNecesidadesChoco['Total'].values[0]

MaxThrNecesidadesChoco = OrderNecesidadesChoco.iloc[2:3]
MaxThrNecesidadesNomChoco = MaxThrNecesidadesChoco['Necesidades NNA'].values[0]
MaxThrNecesidadesNumChoco = MaxThrNecesidadesChoco['Total'].values[0]

# Guajira
OrderNecesidadesGuajira = NecesidadesGuajira.sort_values(by=['Total'],ascending=[False])
MaxNecesidadesGuajira = OrderNecesidadesGuajira.iloc[:1]
MaxNecesidadesNomGuajira = MaxNecesidadesGuajira['Necesidades NNA'].values[0]
MaxNecesidadesNumGuajira = MaxNecesidadesGuajira['Total'].values[0]

MaxSecNecesidadesGuajira = OrderNecesidadesGuajira.iloc[1:2]
MaxSecNecesidadesNomGuajira = MaxSecNecesidadesGuajira['Necesidades NNA'].values[0]
MaxSecNecesidadesNumGuajira = MaxSecNecesidadesGuajira['Total'].values[0]

MaxThrNecesidadesGuajira = OrderNecesidadesGuajira.iloc[2:3]
MaxThrNecesidadesNomGuajira = MaxThrNecesidadesGuajira['Necesidades NNA'].values[0]
MaxThrNecesidadesNumGuajira = MaxThrNecesidadesGuajira['Total'].values[0]

# Norte de Santander
OrderNecesidadesNSan = NecesidadesNortSantander.sort_values(by=['Total'],ascending=[False])
MaxNecesidadesNSan = OrderNecesidadesNSan.iloc[:1]
MaxNecesidadesNomNSan = MaxNecesidadesNSan['Necesidades NNA'].values[0]
MaxNecesidadesNumNSan = MaxNecesidadesNSan['Total'].values[0]

MaxSecNecesidadesNSan = OrderNecesidadesNSan.iloc[1:2]
MaxSecNecesidadesNomNSan = MaxSecNecesidadesNSan['Necesidades NNA'].values[0]
MaxSecNecesidadesNumNSan = MaxSecNecesidadesNSan['Total'].values[0]

MaxThrNecesidadesNSan = OrderNecesidadesNSan.iloc[2:3]
MaxThrNecesidadesNomNSan = MaxThrNecesidadesNSan['Necesidades NNA'].values[0]
MaxThrNecesidadesNumNSan = MaxThrNecesidadesNSan['Total'].values[0]


##################
## Caracteristicas

####
## Caracteristicas Nacionales
CaracteristicasNom = Caracteristicas['Caracteristicas'].tolist()
CaracteristicasNum = Caracteristicas['Total por caracteristicas'].tolist()

####
## Caracteristicas Arauca
CaracteristicasNomArauca = CaracArauca['Caracteristica'].tolist()
CaracteristicasNumArauca = CaracArauca['Total'].tolist()

####
## Caracteristicas Choco
CaracteristicasNomChoco = CaracChoco['Caracteristica'].tolist()
CaracteristicasNumChoco = CaracChoco['Total'].tolist()

####
## Caracteristicas Guajira
CaracteristicasNomGuajira = CaracGuajira['Caracteristica'].tolist()
CaracteristicasNumGuajira = CaracGuajira['Total'].tolist()

####
## Caracteristicas Norte de Santander
CaracteristicasNomNorSan = CaracNorteSantander['Caracteristica'].tolist()
CaracteristicasNumNorSan = CaracNorteSantander['Total'].tolist()

## Informal

# Nacional
asentamiento_informalNom = asentamiento_informal['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'].tolist()
asentamiento_informalNum = asentamiento_informal['Total'].tolist()

# Arauca
asentamiento_informalNomAra = asentamiento_informalArauca['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'].tolist()
asentamiento_informalNumAra = asentamiento_informalArauca['Total'].tolist()

# Choco
asentamiento_informalNomChoco = asentamiento_informalChoco['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'].tolist()
asentamiento_informalNumChoco = asentamiento_informalChoco['Total'].tolist()

# Guajira
asentamiento_informalNomGuajira = asentamiento_informalGuajira['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'].tolist()
asentamiento_informalNumGuajira = asentamiento_informalGuajira['Total'].tolist()

# Norte
asentamiento_informalNomNSan = asentamiento_informalNorteSantander['19. ¿La comunidad donde se realiza la evaluación es un asentamiento humano informal?'].tolist()
asentamiento_informalNumNSan = asentamiento_informalNorteSantander['Total'].tolist()


## Terrenos

#Nacional
TerrenoNom = Terrenos['Terreno'].tolist()
TerrenolNum = Terrenos['Total'].tolist()

#Arauca
TerrenoNomAra = TerrenosArauca['Terreno'].tolist()
TerrenolNumAra = TerrenosArauca['Total'].tolist()

#Choco
TerrenoNomChoco = TerrenosChoco['Terreno'].tolist()
TerrenolNumChoco = TerrenosChoco['Total'].tolist()

#Guajira
TerrenoNomGuajira = TerrenosGuajira['Terreno'].tolist()
TerrenolNumGuajira = TerrenosGuajira['Total'].tolist()

#N Santander
TerrenoNomNSan = TerrenosNorteSantander['Terreno'].tolist()
TerrenolNumNSan = TerrenosNorteSantander['Total'].tolist()


##################
## Migración

# tiene migrantes
#Nacional
Tiene_migrantes_Nom = Tiene_migrantes_sum['¿En la comunidad viven personas migrantes?'].tolist()
Tiene_migrantes_Num = Tiene_migrantes_sum['Total'].tolist()

# Arauca
Tiene_migrantes_NomAra = Tiene_migrantes_sumArauca['¿En la comunidad viven personas migrantes?'].tolist()
Tiene_migrantes_NumAra = Tiene_migrantes_sumArauca['Total'].tolist()

#Choco
Tiene_migrantes_NomChoco = Tiene_migrantes_sumChoco['¿En la comunidad viven personas migrantes?'].tolist()
Tiene_migrantes_NumChoco = Tiene_migrantes_sumChoco['Total'].tolist()

#La Guajira
Tiene_migrantes_NomGua = Tiene_migrantes_sumGuajira['¿En la comunidad viven personas migrantes?'].tolist()
Tiene_migrantes_NumGua = Tiene_migrantes_sumGuajira['Total'].tolist()

# Norte de Santander
Tiene_migrantes_NomNSan = Tiene_migrantes_sumNorteSantander['¿En la comunidad viven personas migrantes?'].tolist()
Tiene_migrantes_NumNSan = Tiene_migrantes_sumNorteSantander['Total'].tolist()


# Porcentaje de migrantes en el asentamiento
# Nacional
MigrantesNom = agrupacion_migrantes_sum['¿Qué porcentaje de la población que vive en la comunidad es migrante?'].tolist()
MigrantesNum = agrupacion_migrantes_sum['Total'].tolist()

# Arauca
MigrantesNomAra = agrupacion_migrantes_sum_arauca['¿Qué porcentaje de la población que vive en la comunidad es migrante?'].tolist()
MigrantesNumAra = agrupacion_migrantes_sum_arauca['Total'].tolist()

# Choco
MigrantesNomCho = agrupacion_migrantes_sum_choco['¿Qué porcentaje de la población que vive en la comunidad es migrante?'].tolist()
MigrantesNumCho = agrupacion_migrantes_sum_choco['Total'].tolist()

# La Guajira
MigrantesNomGua = agrupacion_migrantes_sum_guajira['¿Qué porcentaje de la población que vive en la comunidad es migrante?'].tolist()
MigrantesNumGua = agrupacion_migrantes_sum_guajira['Total'].tolist()

# Norte de Santander
MigrantesNomNSan = agrupacion_migrantes_sum_NorteSantander['¿Qué porcentaje de la población que vive en la comunidad es migrante?'].tolist()
MigrantesNumNSan = agrupacion_migrantes_sum_NorteSantander['Total'].tolist()


##################
## Salud

## Tiene afectaciones

# Nacional
Tiene_afectaciones_salud_Nom = Tiene_afectaciones_sum['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'].tolist()
Tiene_afectaciones_salud_Num = Tiene_afectaciones_sum['Total'].tolist()

# Arauca
Tiene_afectaciones_salud_NomArauca = Tiene_afectaciones_sumArauca['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'].tolist()
Tiene_afectaciones_salud_NumArauca = Tiene_afectaciones_sumArauca['Total'].tolist()

# Choco
Tiene_afectaciones_salud_NomChoco = Tiene_afectaciones_sumChoco['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'].tolist()
Tiene_afectaciones_salud_NumChoco = Tiene_afectaciones_sumChoco['Total'].tolist()

# Guajira
Tiene_afectaciones_salud_NomGuajira = Tiene_afectaciones_sumGuajira['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'].tolist()
Tiene_afectaciones_salud_NumGuajira = Tiene_afectaciones_sumGuajira['Total'].tolist()

# Norte de Sanatnder
Tiene_afectaciones_salud_NomNSant = Tiene_afectaciones_sumNorteSantander['¿Existen casos de afectaciones en la salud principalmente a niños, niñas y adolescentes?'].tolist()
Tiene_afectaciones_salud_NumNSant = Tiene_afectaciones_sumNorteSantander['Total'].tolist()

## enfermedades

# Nacionales
EnfermedadesNom = Enfermedades['Enfermedades'].tolist()
EnfermedadesNum = Enfermedades['Total'].tolist()

# Arauca
EnfermedadesNomArauca = EnfermedadesArauca['Enfermedades'].tolist()
EnfermedadesNumArauca = EnfermedadesArauca['Total'].tolist()

# Choco
EnfermedadesNomChoco = EnfermedadesChoco['Enfermedades'].tolist()
EnfermedadesNumChoco = EnfermedadesChoco['Total'].tolist()

# Guajira
EnfermedadesNomGuajira = EnfermedadesGuajira['Enfermedades'].tolist()
EnfermedadesNumGuajira = EnfermedadesGuajira['Total'].tolist()

# Norte Santander 
EnfermedadesNomNSan = EnfermedadesNorteSantander['Enfermedades'].tolist()
EnfermedadesNumNSan = EnfermedadesNorteSantander['Total'].tolist()

## acceso a salud

# Nacionales
AccesoSaludNom = AccesoSalud['Acceso Salud'].tolist()
AccesoSaludNum = AccesoSalud['Total'].tolist()

# Arauca
AccesoSaludNomArauca = AccesoSaludArauca['Acceso Salud'].tolist()
AccesoSaludNumArauca = AccesoSaludArauca['Total'].tolist()

# Choco
AccesoSaludNomChoco = AccesoSaludChoco['Acceso Salud'].tolist()
AccesoSaludNumChoco = AccesoSaludChoco['Total'].tolist()

# Guajira
AccesoSaludNomGuajira = AccesoSaludGuajira['Acceso Salud'].tolist()
AccesoSaludNumGuajira = AccesoSaludGuajira['Total'].tolist()

# Norte Santander
AccesoSaludNomNSan = AccesoSaludNSan['Acceso Salud'].tolist()
AccesoSaludNumNsan = AccesoSaludNSan['Total'].tolist()


##################
## Educación

## Tiempo escuela
# Nacionales
TiempoEscdNom = Tiempo_educacion['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'].tolist()
TiempoEscNum = Tiempo_educacion['Total'].tolist()
# Arauca
TiempoEscdNomArauca = Tiempo_educacionArauca['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'].tolist()
TiempoEscNumArauca = Tiempo_educacionArauca['Total'].tolist()
# Choco
TiempoEscdNomChoco = Tiempo_educacionChoco['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'].tolist()
TiempoEscNumChoco = Tiempo_educacionChoco['Total'].tolist()
# Guajira
TiempoEscdNomGuajira = Tiempo_educacionGuajira['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'].tolist()
TiempoEscNumGuajira = Tiempo_educacionGuajira['Total'].tolist()
# Norte de Santander
TiempoEscdNomNSan = Tiempo_educacionNSan['¿A cuántos minutos caminando de la comunidad se encuentra la Institución Educativa más cercana?'].tolist()
TiempoEscNumNSan = Tiempo_educacionNSan['Total'].tolist()

## sin educacion 
#Nacional
SinEducacionNom = sin_educacion['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'].tolist()
SinEducacionNum = sin_educacion['Total'].tolist()
#Arauca
SinEducacionNomArauca = sin_educacionArauca['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'].tolist()
SinEducacionNumArauca = sin_educacionArauca['Total'].tolist()
#Choco
SinEducacionNomChoco = sin_educacionChoco['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'].tolist()
SinEducacionNumChoco = sin_educacionChoco['Total'].tolist()
#Guajira
SinEducacionNomGuajira = sin_educacionGuajira['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'].tolist()
SinEducacionNumGuajira = sin_educacionGuajira['Total'].tolist()
#NSantadner
SinEducacionNomNSan = sin_educacionNSan['¿Existen casos de niños, niñas o adolescentes que no asisten a instituciones educativas ya sea de forma presencial o virtual?'].tolist()
SinEducacionNumNSan = sin_educacionNSan['Total'].tolist()

## Razones sin educacion
#Nacional
RazonesSinEducacionNom = RazonesSinEducacion['Razones sin educacion'].tolist()
RazonesSinEducacionNum = RazonesSinEducacion['Total'].tolist()
#Arauca
RazonesSinEducacionNomArauca = RazonesSinEducacionArauca['Razones sin educacion'].tolist()
RazonesSinEducacionNumArauca = RazonesSinEducacionArauca['Total'].tolist()
#Choco
RazonesSinEducacionNomChoco = RazonesSinEducacionChoco['Razones sin educacion'].tolist()
RazonesSinEducacionNumChoco = RazonesSinEducacionChoco['Total'].tolist()
#Guajira
RazonesSinEducacionNomGuajira = RazonesSinEducacionGuajira['Razones sin educacion'].tolist()
RazonesSinEducacionNumGuajira = RazonesSinEducacionGuajira['Total'].tolist()
#Norte de Santander
RazonesSinEducacionNomNSan = RazonesSinEducacionNSan['Razones sin educacion'].tolist()
RazonesSinEducacionNumNSan = RazonesSinEducacionNSan['Total'].tolist()

##################
## WASH

## Principal fuente de agua
#Nacional
FuenteAguaPrincipalNom = FuenteAguaPrincipal['Fuente de agua'].tolist()
FuenteAguaPrincipalNum = FuenteAguaPrincipal['Total'].tolist()
#Arauca
FuenteAguaPrincipalNomArauca = FuenteAguaPrincipalArauca['Fuente de agua'].tolist()
FuenteAguaPrincipalNumArauca = FuenteAguaPrincipalArauca['Total'].tolist()
#Choco
FuenteAguaPrincipalNomChoco = FuenteAguaPrincipalChoco['Fuente de agua'].tolist()
FuenteAguaPrincipalNumChoco = FuenteAguaPrincipalChoco['Total'].tolist()
#Guajira
FuenteAguaPrincipalNomGuajira = FuenteAguaPrincipalGuajira['Fuente de agua'].tolist()
FuenteAguaPrincipalNumGuajira = FuenteAguaPrincipalGuajira['Total'].tolist()
#Norte de Santander
FuenteAguaPrincipalNomNSan = FuenteAguaPrincipalNSan['Fuente de agua'].tolist()
FuenteAguaPrincipalNumNSan = FuenteAguaPrincipalNSan['Total'].tolist()

## Recolecion de basura
#Nacional
RecoleccionBasuraslNom = RecoleccionBasuras['Recoleccion basuras'].tolist()
RecoleccionBasuraslNum = RecoleccionBasuras['Total'].tolist()
#Arauca
RecoleccionBasuraslNomArauca = RecoleccionBasurasArauca['Recoleccion basuras'].tolist()
RecoleccionBasuraslNumArauca = RecoleccionBasurasArauca['Total'].tolist()
#Choco
RecoleccionBasuraslNomChoco = RecoleccionBasurasChoco['Recoleccion basuras'].tolist()
RecoleccionBasuraslNumChoco = RecoleccionBasurasChoco['Total'].tolist()
#Guajira
RecoleccionBasuraslNomGuajira = RecoleccionBasurasGuajira['Recoleccion basuras'].tolist()
RecoleccionBasuraslNumGuajira = RecoleccionBasurasGuajira['Total'].tolist()
#Norte de Santander
RecoleccionBasuraslNomNSan = RecoleccionBasurasNSan['Recoleccion basuras'].tolist()
RecoleccionBasuraslNumNSan = RecoleccionBasurasNSan['Total'].tolist()

## Focos contaminacion
#Nacional
FocosContaminacionlNom = FocosContaminacion['Focos contaminacion'].tolist()
FocosContaminacionlNum = FocosContaminacion['Total'].tolist()
#Arauca
FocosContaminacionlNomArauca = FocosContaminacionArauca['Focos contaminacion'].tolist()
FocosContaminacionlNumArauca = FocosContaminacionArauca['Total'].tolist()
#Choco
FocosContaminacionlNomChoco = FocosContaminacionChoco['Focos contaminacion'].tolist()
FocosContaminacionlNumChoco = FocosContaminacionChoco['Total'].tolist()
#Guajira
FocosContaminacionlNomGuajira = FocosContaminacionGuajira['Focos contaminacion'].tolist()
FocosContaminacionlNumGuajira = FocosContaminacionGuajira['Total'].tolist()
#Norte de Santander
FocosContaminacionlNomNSan = FocosContaminacionNSan['Focos contaminacion'].tolist()
FocosContaminacionlNumNSan = FocosContaminacionNSan['Total'].tolist()

##################
## Protección

## Trabajo infantil
#Nacional
TrabajoInfantillNom = trabajo_infantil['¿Existen casos de trabajo infantil en la comunidad?'].tolist()
TrabajoInfantillNum = trabajo_infantil['Total'].tolist()
#Arauca
TrabajoInfantillNomArauca = trabajo_infantilArauca['¿Existen casos de trabajo infantil en la comunidad?'].tolist()
TrabajoInfantillNumArauca = trabajo_infantilArauca['Total'].tolist()
#Choco
TrabajoInfantillNomChoco = trabajo_infantilChoco['¿Existen casos de trabajo infantil en la comunidad?'].tolist()
TrabajoInfantillNumChoco = trabajo_infantilChoco['Total'].tolist()
#Guajira
TrabajoInfantillNomGuajira = trabajo_infantilGuajira['¿Existen casos de trabajo infantil en la comunidad?'].tolist()
TrabajoInfantillNumGuajira = trabajo_infantilGuajira['Total'].tolist()
#Norte de Santander
TrabajoInfantillNomNSan = trabajo_infantilNSan['¿Existen casos de trabajo infantil en la comunidad?'].tolist()
TrabajoInfantillNumNsan = trabajo_infantilNSan['Total'].tolist()

## Mendicidad
MendicidadlNom = mendicidad['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'].tolist()
MendicidadlNum = mendicidad['Total'].tolist()
#Arauca
MendicidadlNomArauca = mendicidadArauca['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'].tolist()
MendicidadlNumArauca = mendicidadArauca['Total'].tolist()
#Choco
MendicidadlNomChoco = mendicidadChoco['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'].tolist()
MendicidadlNumChoco = mendicidadChoco['Total'].tolist()
#Guajira
MendicidadlNomGuajira = mendicidadGuajira['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'].tolist()
MendicidadlNumGuajira = mendicidadGuajira['Total'].tolist()
#Norte de Santander
MendicidadlNomNSan = mendicidadNSan['¿Existen casos de niños, niñas y adolescentes que ejercen la mendicidad?'].tolist()
MendicidadlNumNSan = mendicidadNSan['Total'].tolist()

## Apoyo
#Nacional
ApoyoEconomicoNom = ApoyosEconomicos['¿Se han presentado apoyo o ayudas económicas a las familias?'].tolist()
ApoyoEconomicoNum = ApoyosEconomicos['Total'].tolist()
#Arauca
ApoyoEconomicoNomArauca = ApoyosEconomicosArauca['¿Se han presentado apoyo o ayudas económicas a las familias?'].tolist()
ApoyoEconomicoNumArauca = ApoyosEconomicosArauca['Total'].tolist()
#Choco
ApoyoEconomicoNomChoco = ApoyosEconomicosChoco['¿Se han presentado apoyo o ayudas económicas a las familias?'].tolist()
ApoyoEconomicoNumChoco = ApoyosEconomicosChoco['Total'].tolist()
#Guajira
ApoyoEconomicoNomGuajira = ApoyosEconomicosGuajira['¿Se han presentado apoyo o ayudas económicas a las familias?'].tolist()
ApoyoEconomicoNumGaujira = ApoyosEconomicosGuajira['Total'].tolist()
#Norte de Santander
ApoyoEconomicoNomNSan = ApoyosEconomicosNSan['¿Se han presentado apoyo o ayudas económicas a las familias?'].tolist()
ApoyoEconomicoNumNSan = ApoyosEconomicosNSan['Total'].tolist()



##################
## SAN

## Apoyo alimentario
#Nacional
ApoyoAlimentarioNom = ApoyoAlimentario['Apoyo Alimentario'].tolist()
ApoyoAlimentarioNum = ApoyoAlimentario['Total'].tolist()
#Arauca
ApoyoAlimentarioNomArauca = ApoyoAlimentarioArauca['Apoyo Alimentario'].tolist()
ApoyoAlimentarioNumArauca = ApoyoAlimentarioArauca['Total'].tolist()
#Choco
ApoyoAlimentarioNomChoco = ApoyoAlimentarioChoco['Apoyo Alimentario'].tolist()
ApoyoAlimentarioNumChoco = ApoyoAlimentarioChoco['Total'].tolist()
#Guajira
ApoyoAlimentarioNomGuajira = ApoyoAlimentarioGuajira['Apoyo Alimentario'].tolist()
ApoyoAlimentarioNumGuajira = ApoyoAlimentarioGuajira['Total'].tolist()
#Norte de Santander
ApoyoAlimentarioNomNSan = ApoyoAlimentarioNSan['Apoyo Alimentario'].tolist()
ApoyoAlimentarioNumNSan = ApoyoAlimentarioNSan['Total'].tolist()

## Consumo de alimentos
#Nacional
ConsumoAlimentosNom = ConsumoAlimentos['Consumo de alimentos NNA en la comunidad'].tolist()
ConsumoAlimentosNum = ConsumoAlimentos['Total'].tolist()
#Arauca
ConsumoAlimentosNomArauca = ConsumoAlimentosArauca['Consumo de alimentos NNA en la comunidad'].tolist()
ConsumoAlimentosArauca = ConsumoAlimentosArauca['Total'].tolist()
#Choco
ConsumoAlimentosNomChoco = ConsumoAlimentosChoco['Consumo de alimentos NNA en la comunidad'].tolist()
ConsumoAlimentosChoco = ConsumoAlimentosChoco['Total'].tolist()
#Guajira
ConsumoAlimentosNomGuajira = ConsumoAlimentosGuajira['Consumo de alimentos NNA en la comunidad'].tolist()
ConsumoAlimentosGuajira = ConsumoAlimentosGuajira['Total'].tolist()
#Norte de Santander
ConsumoAlimentosNomNSan = ConsumoAlimentosNSan['Consumo de alimentos NNA en la comunidad'].tolist()
ConsumoAlimentosNSan = ConsumoAlimentosNSan['Total'].tolist()

## Desnutrición
#Nacional
DesnutricionNom = Desnutricion['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'].tolist()
DesnutricionNum = Desnutricion['Total'].tolist()
#Arauca
DesnutricionNomArauca = DesnutricionArauca['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'].tolist()
DesnutricionArauca = DesnutricionArauca['Total'].tolist()
#Choco
DesnutricionNomChoco = DesnutricionChoco['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'].tolist()
DesnutricionChoco = DesnutricionChoco['Total'].tolist()
#Guajira
DesnutricionNomGuajira = DesnutricionGuajira['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'].tolist()
DesnutricionGuajira = DesnutricionGuajira['Total'].tolist()
#Norte de Santander
DesnutricionNomNSan = DesnutricionNSan['¿Existen casos de niños, niñas o adolescentes que se encuentren en estado de desnutrición?'].tolist()
DesnutricionNSan = DesnutricionNSan['Total'].tolist()
