from django.shortcuts import render

# Create your views here.

# New import
from django.http import HttpResponse

##
from app.data import *


class Beginning():

    def index(request):
        uno = 1

        context = {

            #Mapa
            'asentamientos':asentamientos,
            'longitud':longitud,
            'latitud':latitud,

            #asentamientos evaluados

            'EveReaDepar':EveReaDepar,
            'EveReaCuantas':EveReaCuantas,

            ###### Necesidades

            # nacional
            'NecesidadesNom':NecesidadesNom,
            'NecesidadesNum':NecesidadesNum,

            # Arauca
            'NecesidadesNomAra':NecesidadesNomAra,
            'NecesidadesNumAra':NecesidadesNumAra,

            # Choco
            'NecesidadesNomChoco':NecesidadesNomChoco,
            'NecesidadesNumChoco':NecesidadesNumChoco,

            # Guajira
            'NecesidadesNomGuajira':NecesidadesNomGuajira,
            'NecesidadesNumGuajira':NecesidadesNumGuajira,

            # Norte de Santander
            'NecesidadesNomNSant':NecesidadesNomNSant,
            'NecesidadesNumNSant':NecesidadesNumNSant,

            ###### 3 primeras necesidades

            # Nacional
            # Primera
            'MaxNecesidadesNom':MaxNecesidadesNom,
            'MaxNecesidadesNum':MaxNecesidadesNum,
            # Secunda
            'MaxSecNecesidadesNom':MaxSecNecesidadesNom,
            'MaxSecNecesidadesNum':MaxSecNecesidadesNum,
            #Tercera
            'MaxThrNecesidadesNom':MaxThrNecesidadesNom,
            'MaxThrNecesidadesNum':MaxThrNecesidadesNum,

            # Arauca
            # Primera
            'MaxNecesidadesNomAra':MaxNecesidadesNomAra,
            'MaxNecesidadesNumAra':MaxNecesidadesNumAra,
            # Secunda
            'MaxSecNecesidadesNomAra':MaxSecNecesidadesNomAra,
            'MaxSecNecesidadesNumAra':MaxSecNecesidadesNumAra,
            #Tercera
            'MaxThrNecesidadesNomAra':MaxThrNecesidadesNomAra,
            'MaxThrNecesidadesNumAra':MaxThrNecesidadesNumAra,


            # Choco
            # Primera
            'MaxNecesidadesNomChoco':MaxNecesidadesNomChoco,
            'MaxNecesidadesNumChoco':MaxNecesidadesNumChoco,
            # Secunda
            'MaxSecNecesidadesNomChoco':MaxSecNecesidadesNomChoco,
            'MaxSecNecesidadesNumChoco':MaxSecNecesidadesNumChoco,
            #Tercera
            'MaxThrNecesidadesNomChoco':MaxThrNecesidadesNomChoco,
            'MaxThrNecesidadesNumChoco':MaxThrNecesidadesNumChoco,


            # Guajira
            # Primera
            'MaxNecesidadesNomGuajira':MaxNecesidadesNomGuajira,
            'MaxNecesidadesNumGuajira':MaxNecesidadesNumGuajira,
            # Secunda
            'MaxSecNecesidadesNomGuajira':MaxSecNecesidadesNomGuajira,
            'MaxSecNecesidadesNumGuajira':MaxSecNecesidadesNumGuajira,
            #Tercera
            'MaxThrNecesidadesNomGuajira':MaxThrNecesidadesNomGuajira,
            'MaxThrNecesidadesNumGuajira':MaxThrNecesidadesNumGuajira,  


            # Norte de Santander
            # Primera
            'MaxNecesidadesNom':MaxNecesidadesNom,
            'MaxNecesidadesNum':MaxNecesidadesNum,
            # Secunda
            'MaxSecNecesidadesNom':MaxSecNecesidadesNom,
            'MaxSecNecesidadesNum':MaxSecNecesidadesNum,
            #Tercera
            'MaxThrNecesidadesNom':MaxThrNecesidadesNom,
            'MaxThrNecesidadesNum':MaxThrNecesidadesNum,

            ############ Departamentos
            'departamentos':departamentos,

            ##### caracteristicas
            # nacional
            'CaracteristicasNom':CaracteristicasNom,
            'CaracteristicasNum':CaracteristicasNum,

            # Arauca
            'CaracteristicasNomArauca':CaracteristicasNomArauca,
            'CaracteristicasNumArauca':CaracteristicasNumArauca,

            # Choco
            'CaracteristicasNomChoco':CaracteristicasNomChoco,
            'CaracteristicasNumChoco':CaracteristicasNumChoco,

            # Guajira
            'CaracteristicasNomGuajira':CaracteristicasNomGuajira,
            'CaracteristicasNumGuajira':CaracteristicasNumGuajira,

            # Norte de Santander
            'CaracteristicasNomNorSan':CaracteristicasNomNorSan,
            'CaracteristicasNumNorSan':CaracteristicasNumNorSan,

            ## informal
            # Nacional
            'asentamiento_informalNom':asentamiento_informalNom,
            'asentamiento_informalNum':asentamiento_informalNum,

            # Arauca
            'asentamiento_informalNomAra':asentamiento_informalNomAra,
            'asentamiento_informalNumAra':asentamiento_informalNumAra,

            # Choco
            'asentamiento_informalNomChoco':asentamiento_informalNomChoco,
            'asentamiento_informalNumChoco':asentamiento_informalNumChoco,

            #Guajira
            'asentamiento_informalNomGuajira':asentamiento_informalNomGuajira,
            'asentamiento_informalNumGuajira':asentamiento_informalNumGuajira,

            # N Sant
            'asentamiento_informalNomNSan':asentamiento_informalNomNSan,
            'asentamiento_informalNumNSan':asentamiento_informalNumNSan,

            ## Terreno
            # Nacional
            'TerrenoNom':TerrenoNom,
            'TerrenolNum':TerrenolNum,

            #Arauca
            'TerrenoNomAra':TerrenoNomAra,
            'TerrenolNumAra':TerrenolNumAra,

            #Choco
            'TerrenoNomChoco':TerrenoNomChoco,
            'TerrenolNumChoco':TerrenolNumChoco,

            #Guajira
            'TerrenoNomGuajira':TerrenoNomGuajira,
            'TerrenolNumGuajira':TerrenolNumGuajira,

            # N Santander
            'TerrenoNomNSan':TerrenoNomNSan,
            'TerrenolNumNSan':TerrenolNumNSan,


            ##### Migrantes

            ## Tiene migrantes
            # Nacional
            'Tiene_migrantes_Nom':Tiene_migrantes_Nom,
            'Tiene_migrantes_Num':Tiene_migrantes_Num,

            # Arauca
            'Tiene_migrantes_NomAra':Tiene_migrantes_NomAra,
            'Tiene_migrantes_NumAra':Tiene_migrantes_NumAra,

            # Choco
            'Tiene_migrantes_NomChoco':Tiene_migrantes_NomChoco,
            'Tiene_migrantes_NumChoco':Tiene_migrantes_NumChoco,

            # Guajira
            'Tiene_migrantes_NomGua':Tiene_migrantes_NomGua,
            'Tiene_migrantes_NumGua':Tiene_migrantes_NumGua,

            # Norte Santander
            'Tiene_migrantes_NomNSan':Tiene_migrantes_NomNSan,
            'Tiene_migrantes_NumNSan':Tiene_migrantes_NumNSan,

            ## Porcetnaje
            # nacional
            'MigrantesNom':MigrantesNom,
            'MigrantesNum':MigrantesNum,

            # Arauca
            'MigrantesNomAra':MigrantesNomAra,
            'MigrantesNumAra':MigrantesNumAra,

            # Choco
            'MigrantesNomCho':MigrantesNomCho,
            'MigrantesNumCho':MigrantesNumCho,

            # La Guajira
            'MigrantesNomGua':MigrantesNomGua,
            'MigrantesNumGua':MigrantesNumGua,

            # Norte de Santander
            'MigrantesNomNSan':MigrantesNomNSan,
            'MigrantesNumNSan':MigrantesNumNSan,

            ##### Salud

            ##Tiene afectaciones de salid
            # Nacional
            'Tiene_afectaciones_salud_Nom':Tiene_afectaciones_salud_Nom,
            'Tiene_afectaciones_salud_Num':Tiene_afectaciones_salud_Num,

            # Arauca
            'Tiene_afectaciones_salud_NomArauca':Tiene_afectaciones_salud_NomArauca,
            'Tiene_afectaciones_salud_NumArauca':Tiene_afectaciones_salud_NumArauca,

            #Choco
            'Tiene_afectaciones_salud_NomChoco':Tiene_afectaciones_salud_NomChoco,
            'Tiene_afectaciones_salud_NumChoco':Tiene_afectaciones_salud_NumChoco,

            #Guajira
            'Tiene_afectaciones_salud_NomGuajira':Tiene_afectaciones_salud_NomGuajira,
            'Tiene_afectaciones_salud_NumGuajira':Tiene_afectaciones_salud_NumGuajira,

            #Norte de santander
            'Tiene_afectaciones_salud_NomNSant':Tiene_afectaciones_salud_NomNSant,
            'Tiene_afectaciones_salud_NumNSant':Tiene_afectaciones_salud_NumNSant,

            ##enfermedades
            #nacional
            'EnfermedadesNom':EnfermedadesNom,
            'EnfermedadesNum':EnfermedadesNum,

            #Arauca
            'EnfermedadesNomArauca':EnfermedadesNomArauca,
            'EnfermedadesNumArauca':EnfermedadesNumArauca,

            #Choco
            'EnfermedadesNomChoco':EnfermedadesNomChoco,
            'EnfermedadesNumChoco':EnfermedadesNumChoco,

            #Guajira
            'EnfermedadesNomGuajira':EnfermedadesNomGuajira,
            'EnfermedadesNumGuajira':EnfermedadesNumGuajira,

            #Norte Santander
            'EnfermedadesNomNSan':EnfermedadesNomNSan,
            'EnfermedadesNumNSan':EnfermedadesNumNSan,

            ##Acceso salud
            #nacional
            'AccesoSaludNom':AccesoSaludNom,
            'AccesoSaludNum':AccesoSaludNum,

            #Arauca
            'AccesoSaludNomArauca':AccesoSaludNomArauca,
            'AccesoSaludNumArauca':AccesoSaludNumArauca,

            #Choco
            'AccesoSaludNomChoco':AccesoSaludNomChoco,
            'AccesoSaludNumChoco':AccesoSaludNumChoco,

            #Guajira
            'AccesoSaludNomGuajira':AccesoSaludNomGuajira,
            'AccesoSaludNumGuajira':AccesoSaludNumGuajira,

            #Norte Santander
            'AccesoSaludNomNSan':AccesoSaludNomNSan,
            'AccesoSaludNumNsan':AccesoSaludNumNsan,

            ##### Eduacion

            ## Escuelas
            # Nacional
            'TiempoEscdNom':TiempoEscdNom,
            'TiempoEscNum':TiempoEscNum,
            #Arauca
            'TiempoEscdNomArauca':TiempoEscdNomArauca,
            'TiempoEscNumArauca':TiempoEscNumArauca,
            #Choco
            'TiempoEscdNomChoco':TiempoEscdNomChoco,
            'TiempoEscNumChoco':TiempoEscNumChoco,
            #Guajira
            'TiempoEscdNomGuajira':TiempoEscdNomGuajira,
            'TiempoEscNumGuajira':TiempoEscNumGuajira,
            #Norte de Santander
            'TiempoEscdNomNSan':TiempoEscdNomNSan,
            'TiempoEscNumNSan':TiempoEscNumNSan,

            ##Sin eduación
            # nacional
            'SinEducacionNom':SinEducacionNom,
            'SinEducacionNum':SinEducacionNum,
            #Arauca
            'SinEducacionNomArauca':SinEducacionNomArauca,
            'SinEducacionNumArauca':SinEducacionNumArauca,
            #Choco
            'SinEducacionNomChoco':SinEducacionNomChoco,
            'SinEducacionNumChoco':SinEducacionNumChoco,
            # Guajira
            'SinEducacionNomGuajira':SinEducacionNomGuajira,
            'SinEducacionNumGuajira':SinEducacionNumGuajira,
            # Norte de Santander
            'SinEducacionNomNSan':SinEducacionNomNSan,
            'SinEducacionNumNSan':SinEducacionNumNSan,

            ## Razones sin edu
            #nacional
            'RazonesSinEducacionNom':RazonesSinEducacionNom,
            'RazonesSinEducacionNum':RazonesSinEducacionNum,
            #Arauca
            'RazonesSinEducacionNomArauca':RazonesSinEducacionNomArauca,
            'RazonesSinEducacionNumArauca':RazonesSinEducacionNumArauca,
            #Choco
            'RazonesSinEducacionNomChoco':RazonesSinEducacionNomChoco,
            'RazonesSinEducacionNumChoco':RazonesSinEducacionNumChoco,
            # Guajira
            'RazonesSinEducacionNomGuajira':RazonesSinEducacionNomGuajira,
            'RazonesSinEducacionNumGuajira':RazonesSinEducacionNumGuajira,
            # Norte de Santander
            'RazonesSinEducacionNomNSan':RazonesSinEducacionNomNSan,
            'RazonesSinEducacionNumNSan':RazonesSinEducacionNumNSan,

            ##### WASH
            ## Fuente de agua
            #nacional
            'FuenteAguaPrincipalNom':FuenteAguaPrincipalNom,
            'FuenteAguaPrincipalNum':FuenteAguaPrincipalNum,
            #Arauca
            'FuenteAguaPrincipalNomArauca':FuenteAguaPrincipalNomArauca,
            'FuenteAguaPrincipalNumArauca':FuenteAguaPrincipalNumArauca,
            #Choco
            'FuenteAguaPrincipalNomChoco':FuenteAguaPrincipalNomChoco,
            'FuenteAguaPrincipalNumChoco':FuenteAguaPrincipalNumChoco,
            # Guajira
            'FuenteAguaPrincipalNomGuajira':FuenteAguaPrincipalNomGuajira,
            'FuenteAguaPrincipalNumGuajira':FuenteAguaPrincipalNumGuajira,
            # Norte de Santander
            'FuenteAguaPrincipalNomNSan':FuenteAguaPrincipalNomNSan,
            'FuenteAguaPrincipalNumNSan':FuenteAguaPrincipalNumNSan,

            ## Recoleccion basuras
            #nacional
            'RecoleccionBasuraslNom':RecoleccionBasuraslNom,
            'RecoleccionBasuraslNum':RecoleccionBasuraslNum,
            #Arauca
            'RecoleccionBasuraslNomArauca':RecoleccionBasuraslNomArauca,
            'RecoleccionBasuraslNumArauca':RecoleccionBasuraslNumArauca,
            #Choco
            'RecoleccionBasuraslNomChoco':RecoleccionBasuraslNomChoco,
            'RecoleccionBasuraslNumChoco':RecoleccionBasuraslNumChoco,
            # Guajira
            'RecoleccionBasuraslNomGuajira':RecoleccionBasuraslNomGuajira,
            'RecoleccionBasuraslNumGuajira':RecoleccionBasuraslNumGuajira,
            # Norte de Santander
            'RecoleccionBasuraslNomNSan':RecoleccionBasuraslNomNSan,
            'RecoleccionBasuraslNumNSan':RecoleccionBasuraslNumNSan,

            ## Focos contaminacion
            #nacional
            'FocosContaminacionlNom':FocosContaminacionlNom,
            'FocosContaminacionlNum':FocosContaminacionlNum,
            #Arauca
            'FocosContaminacionlNomArauca':FocosContaminacionlNomArauca,
            'FocosContaminacionlNumArauca':FocosContaminacionlNumArauca,
            #Choco
            'FocosContaminacionlNomChoco':FocosContaminacionlNomChoco,
            'FocosContaminacionlNumChoco':FocosContaminacionlNumChoco,
            # Guajira
            'FocosContaminacionlNomGuajira':FocosContaminacionlNomGuajira,
            'FocosContaminacionlNumGuajira':FocosContaminacionlNumGuajira,
            # Norte de Santander
            'FocosContaminacionlNomNSan':FocosContaminacionlNomNSan,
            'FocosContaminacionlNumNSan':FocosContaminacionlNumNSan,

            ##### Protección
            ## Trabjo infantil
            #nacional
            'TrabajoInfantillNom':TrabajoInfantillNom,
            'TrabajoInfantillNum':TrabajoInfantillNum,
            #Arauca
            'TrabajoInfantillNomArauca':TrabajoInfantillNomArauca,
            'TrabajoInfantillNumArauca':TrabajoInfantillNumArauca,
            #Choco
            'TrabajoInfantillNomChoco':TrabajoInfantillNomChoco,
            'TrabajoInfantillNumChoco':TrabajoInfantillNumChoco,
            # Guajira
            'TrabajoInfantillNomGuajira':TrabajoInfantillNomGuajira,
            'TrabajoInfantillNumGuajira':TrabajoInfantillNumGuajira,
            # Norte de Santander
            'TrabajoInfantillNomNSan':TrabajoInfantillNomNSan,
            'TrabajoInfantillNumNsan':TrabajoInfantillNumNsan,

            ## Mendicidad
            #nacional
            'MendicidadlNom':MendicidadlNom,
            'MendicidadlNum':MendicidadlNum,
            #Arauca
            'MendicidadlNomArauca':MendicidadlNomArauca,
            'MendicidadlNumArauca':MendicidadlNumArauca,
            #Choco
            'MendicidadlNomChoco':MendicidadlNomChoco,
            'MendicidadlNumChoco':MendicidadlNumChoco,
            # Guajira
            'MendicidadlNomGuajira':MendicidadlNomGuajira,
            'MendicidadlNumGuajira':MendicidadlNumGuajira,
            # Norte de Santander
            'MendicidadlNomNSan':MendicidadlNomNSan,
            'MendicidadlNumNSan':MendicidadlNumNSan,

            ## Apoyo economico
            #nacional
            'ApoyoEconomicoNom':ApoyoEconomicoNom,
            'ApoyoEconomicoNum':ApoyoEconomicoNum,
            #Arauca
            'ApoyoEconomicoNomArauca':ApoyoEconomicoNomArauca,
            'ApoyoEconomicoNumArauca':ApoyoEconomicoNumArauca,
            #Choco
            'ApoyoEconomicoNomChoco':ApoyoEconomicoNomChoco,
            'ApoyoEconomicoNumChoco':ApoyoEconomicoNumChoco,
            # Guajira
            'ApoyoEconomicoNomGuajira':ApoyoEconomicoNomGuajira,
            'ApoyoEconomicoNumGaujira':ApoyoEconomicoNumGaujira,
            # Norte de Santander
            'ApoyoEconomicoNomNSan':ApoyoEconomicoNomNSan,
            'ApoyoEconomicoNumNSan':ApoyoEconomicoNumNSan,

            ##### SAN
            # Apoyo alimentario
            #nacional
            'ApoyoAlimentarioNom':ApoyoAlimentarioNom,
            'ApoyoAlimentarioNum':ApoyoAlimentarioNum,
            #Arauca
            'ApoyoAlimentarioNomArauca':ApoyoAlimentarioNomArauca,
            'ApoyoAlimentarioNumArauca':ApoyoAlimentarioNumArauca,
            #Choco
            'ApoyoAlimentarioNomChoco':ApoyoAlimentarioNomChoco,
            'ApoyoAlimentarioNumChoco':ApoyoAlimentarioNumChoco,
            # Guajira
            'ApoyoAlimentarioNomGuajira':ApoyoAlimentarioNomGuajira,
            'ApoyoAlimentarioNumGuajira':ApoyoAlimentarioNumGuajira,
            # Norte de Santander
            'ApoyoAlimentarioNomNSan':ApoyoAlimentarioNomNSan,
            'ApoyoAlimentarioNumNSan':ApoyoAlimentarioNumNSan,   

            # Consumo alimentos
            #nacional
            'ConsumoAlimentosNom':ConsumoAlimentosNom,
            'ConsumoAlimentosNum':ConsumoAlimentosNum,
            #Arauca
            'ConsumoAlimentosNomArauca':ConsumoAlimentosNomArauca,
            'ConsumoAlimentosArauca':ConsumoAlimentosArauca,
            #Choco
            'ConsumoAlimentosNomChoco':ConsumoAlimentosNomChoco,
            'ConsumoAlimentosChoco':ConsumoAlimentosChoco,
            # Guajira
            'ConsumoAlimentosNomGuajira':ConsumoAlimentosNomGuajira,
            'ConsumoAlimentosGuajira':ConsumoAlimentosGuajira,
            # Norte de Santander
            'ConsumoAlimentosNomNSan':ConsumoAlimentosNomNSan,
            'ConsumoAlimentosNSan':ConsumoAlimentosNSan,  

            # Desnutrición
            #nacional
            'DesnutricionNom':DesnutricionNom,
            'DesnutricionNum':DesnutricionNum,
            #Arauca
            'DesnutricionNomArauca':DesnutricionNomArauca,
            'DesnutricionArauca':DesnutricionArauca,
            #Choco
            'DesnutricionNomChoco':DesnutricionNomChoco,
            'DesnutricionChoco':DesnutricionChoco,
            # Guajira
            'DesnutricionNomGuajira':DesnutricionNomGuajira,
            'DesnutricionGuajira':DesnutricionGuajira,
            # Norte de Santander
            'DesnutricionNomNSan':DesnutricionNomNSan,
            'DesnutricionNSan':DesnutricionNSan,  
            }

        return render(request, 'index.html', context)
