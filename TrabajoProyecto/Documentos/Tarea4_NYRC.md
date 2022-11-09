## Tarea No.4

___

# Pricing Planes MedPlus, actualización

![](https://iso.cat/wp-content/uploads/2019/05/RSC.png)

> Presupuesto general:\
Todas las acciones que se desarrollan en este importante proceso de actuación de los actuarios debe estar regido por valores que permitan velar por el desarrollo activo y de equidad en las comunidades y las economías.

Actualización según norma de tarifa de los planes de MedPlus Medicina Prepagada, segmento delegado.

### Reporte No. 1

Según la norma de la Superintendencia Nacional de Salud, cada año las compañías que proveen planes voluntarios de salud deben actualizar sus tarifas con el fin de dar a conocer las tarifas a aplicar en el año siguiente.

**Asesor principal:**

Profesor Álvaro Montenegro

**Autor@s**

- Nidia Yomaira Rodríguez Castro
- Álvaro Mauricio Montenegro Diaz
- Daniel Montenegro (eventualmente, según lo mencionado)

### ***Introducción***

Las compañías de medicina prepagada y otras entidades supervisados por la Superintendencia Nacional de Salud deben cumplir la normativa en donde se estipula que, a corte de cada noviembre se deben consignar las notas técnicas con la respectiva actualización de tarifas. &nbsp;</p>
En esta se debe analizar, la población expuesta en los diferentes productos o planes que comercialice la compañía, y su proyección que según norma se debe hacer para los próximos cinco años, pero que para efectos de la aplicación de la tarifa y eficiencia de la misma solo bastará con tener conocimiento sobre las proyecciones de la línea de negocio y esta en consenso con la proyección de la gestión de la parte comercial. &nbsp;</p>
Para el caso de la tarifa se deberá estimar la frecuencia y la severidad, esto es, cual de la población expuesta hará uso de las atenciones de servicios de salud y por otro lado al materializarse una de estas utilizaciones o atenciones se deberá estimar su impacto económico. &nbsp;</p>

### ***Descripción del problema***

Cumplir con la normativa de la Superintendencia Nacional de Salud (CIRCULAR EXTERNA [2022151000000051-5](https://docs.supersalud.gov.co/PortalWeb/Juridica/CircularesExterna/Circular%20Externa%20No.%202022151000000051-5%20de%202022.pdf) DE 2022 – 03-08-2022 –.

Realizar la actualización de las tarifas, a partir de la estimación posible de predicciones para el año 2023, estas estimaciones deberán ser obtenidas a partir del desarrollo de herramientas y metodologías técnicamente aceptadas y en el caso actual de la estadística y de la ciencia de datos.

En el año anterior, se realizó esta gestión a partir de las herramientas del software R y a partir del conocimiento que se tiene de los procesos de definición de tarifa, encontrando muchos aspectos que provee la herramienta en el software R y las experiencias anteriores con la herramienta Emblem.

Para esta oportunidad se desea aprender sobre las herramientas que ofrece la ciencia de datos y el software Python y hacer uso de ellas para la tarea mencionada según norma.

### ***Fuentes de datos***

Principalmente será usada la información propia de la compañía MedPlus
El período de estudio comprenderá desde 01/01/2017 hasta el 30/09/2022 

***Información de Expuestos***

Se toma la información de cada uno de los cierres contables, en estas oportunidades se obtiene un archivo con la información de los usuarios que estuvieron expuestos (pudieron requerir atención de los servicios de salud) por lo menos un día durante cada uno de los meses del período de estudio.

Con el fin de complementar la información de los usuarios se toma la información del área Técnica de MedPlus, dado que esta contiene la información de fecha inicio y fecha fin de vigencia de los contratos vigentes en cada mes, en este archivo solo se consideran los usuarios que llegan al último día del mes vigente.

Con estos dos archivos se obtiene la información de:

##### Archivo_Exp

Variable      | Descripción
------------- | -------------
Periodo  | : el año y el mes de cada uno de los meses del período de estudio
FecIni_Per  | : el mismo período de arriba, pero puesto como fecha inicio del período y esto con el fin del cálculo de la frecuencia
FecFin_Per  | : el mismo período de arriba, pero puesto como fecha fin del período y esto con el fin del cálculo de la frecuencia
numerocontrato  | : número con el que se identifica el contrato del usuario (es un campo que hace parte de la identificación única de cada individuo en la población)
CarnetUsuario  | : número con el que se identifica el a cada uno de los usuarios (cada individuo en la población)
Parentesco  | : el vínculo consanguíneo o de afinidad que de cada usuario con el asegurado principal (madre, cónyuge, hijo, entre otros)
Edad  | : la edad de cada uno de los individuos en la población en cada uno de los meses
Sexo  | : el género de cada uno de los individuos en la población
TipoContrato  | : si el contrato es A, alianza (tipo de agrupadores, modalidad que se usa para poder otorgar descuentos comerciales), C, colectivos (empresas, fondos de empleados, asociaciones, entre otros) y F, familiares, esto es contratos cuyos miembros tiene relación de consanguinidad o civil
nombreplan  | :  identificación del producto o del plan de cobertura que tiene el individuo
CodMatriz  | : identificación para las alianzas y colectivos, esto con el fin de realizar seguimientos a estos grupos de usuarios
ciudad  | : ciudad donde se celebra el contrato de plan voluntario de salud, se usa como variable de localización de los individuos en cada mes
Premium  | : monto de la prima devengada, solo se registra lo correspondiente a cada uno de los meses
P_GrossPtoPag  | : monto de prima remanente después de hacer las deducciones del caso – comisiones, descuento por IPS aliada, entre otros, sin incluir descuento por pronto pago
P_NetPtoPag  | : monto de prima remanente después de hacer las deducciones del caso y por último descuento por pronto pago
Conteo  | : variable usada para temas de contar individuos
TypePaid  | : estado apriori, según cálculos, puede ser, “Inforce”, vigente, “Cancel”, cancelado y “Movew/oPrem”, movimientos normales en el contrato y que se realizan sin tener que hacer un pago en específico
Periodo_1  | : otra variable que se usa para el cruce entre los dos archivos mencionados
AñoMes_Per  | : el año y el mes de cada uno de los meses del período de estudio (variable de cruce)
NUMERO CONTRATO  | : número con el que se identifica el contrato del usuario (es un campo que hace parte de la identificación única de cada individuo en la población) (variable de cruce)
Carnet  | : número con el que se identifica el a cada uno de los usuarios (cada individuo en la población)
FECHA INI VIGENCIA  | : fecha en que el usuario puede hacer uso de servicios de salud, fecha de inicio del contrato
FECHA FIN VIGENCIA  | : fecha hasta o límite que el usuario puede hacer uso de servicios de salud, fecha de finalización del contrato
Conteo1  | : variable usada para temas de contar individuos
Range_0  | : clasificación de los contratos para el cálculo de la exposición
Exposure  | : resultado preliminar de la exposición se obtiene como meses_riesgo, aspecto que se puede cambiar con el fin de hacer el proceso más eficiente??, se cambiaría a años_riesgo
Mult  | : una columna que indica si en realidad es un expuesto, dado que en algunos registros se tiene prima cero o prima negativa, se debe realizar análisis en estos casos
Exp_F  | : exposición final, se obtiene de hacer la operación “Exposure” * “Mult”

>Se tiene el siguiente [link]() a la información, pero esta deberá ser modificada nuevamente, así, quitar las columnas redundantes como, “número contrato”, “carnet”, “conteo_1” y dejar solo los registros relevantes para la aplicación de los modelos. Y además se incluirá una columna con el año de suscripción.

>Además de la modificación posible entre meses_riesgo y años_riesgo

***Información de atenciones de salud (reclamaciones)***

Se trabajan dos archivos principalmente, el record del costo médico radicado a MedPlus por parte de los prestadores de servicios de salud o proveedores de tecnologías y el archivo de las autorizaciones pendientes por servicios de salud en donde los usuarios manifiestan su querer de hacer uso de algunos servicios y por tanto se crea una autorización en firme con parámetros de usuario, servicios y prestador.

Para el caso actual y para el año 2017, se debe considerar una información adicional, debido a que, durante algún tiempo de ese año, se vieron en la necesidad de guardar información en archivos de Excel.

De estos archivos se obtiene la siguiente información:

##### Archivo_Claims

Variable      | Descripción
------------- | -------------
AnioMes_Acc  | : el año y el mes de la prestación de la atención en salud
CarnetUsuario  | : número con el que se identifica el a cada uno de los usuarios (cada individuo en la población)
Edad  | : la edad de cada uno de los individuos en la población en cada uno de los meses
Sexo  | : el género de cada uno de los individuos en la población 
NAP  | : número de autorización de la prestación es un código único que se crea a partir de la información de usuario, servicio y prestador
TSA  | : tipo de servicio agrupado, 
NombrePlanCosto  | :  identificación del producto o del plan de cobertura que tiene el individuo
SucursalContrato  | : ciudad donde se celebra el contrato de plan voluntario de salud, se usa como variable de localización de los individuos en cada mes
TipoContrato  | : si el contrato es A, alianza (tipo de agrupadores, modalidad que se usa para poder otorgar descuentos comerciales), C, colectivos (empresas, fondos de empleados, asociaciones, entre otros) y F, familiares, esto es contratos cuyos miembros tiene relación de consanguinidad o civil
CM  | : costo médico radicado o pendiente que corresponde a la proporción del costo a cargo de la compañía MedPlus y que es radicado por los prestadores, o para el caso de las autorizaciones pendientes un valor de referencia de acuerdo con el histórico por servicio y prestador, según prescripción del servicio (cantidad)
Deb  | : deducible (bono), participación del usuario en el costo de las atenciones de salud, es una de las medidas de control que se usa para la frecuencia
Conteo  | : variable que se usa solo para contar

>En este momento la base compartida tiene la base central, pero lo valores se deberán modificar en el sentido de incrementar su valor global en un 2.61% aproximadamente, pero al tomar solo el 2017 o 2022 respectivamente los valores a complementar son mucho más significativos.

>Por último, se deberá usar la información de inflación, tanto total como del grupo de servicios de salud, esto con el fin de usar la información con pesos en un solo período.

##### Procesamiento ETL

ETL: *Extracción, Transformación y Carga de datos*. 

La extracción se realiza mes a mes por parte del área de IT de la organización, de los sistemas core usando código SQL, esto es, Panacea para el caso de primas y usuarios y Medicafe para el caso del costo médico, estas son entregadas en formato Excel y en el área de Actuaría históricamente se ha procedido a unir estas “bases mensuales” hasta el punto de copar el número de registros permitidos por Excel y dejando solo meses completos. Esto se continúa realizando actualmente.

Para el caso de primas y usuarios y la consolidación del archivo central se usa 22 archivos tipo .csv, esto es, 11 archivos con la información central y otros 11 archivos para obtener las fechas de inicio y fin de vigencia. Para el caso de costo médico y la consolidación del archivo central se usa 12 archivos tipo .csv, esto es, 10 archivos con el costo médico radicado, uno con la parte adicional de 2017 y otro con la parte de la reserva de autorizaciones.

Para “mejorar” el desempeño de cargue de la información en Python se que se decidió que los archivos fueran trabajados en formato csv. Para lo anterior también se muestra el link de los códigos usados para su consolidación por parte del área de Actuaría.

##### Exploración de los datos

Técnicas que se usarán inicialmente para describir y entender sus datos:

Estadísticas y gráficas univariadas
Tablas y gráficas de resumen por variables de interés y que serán usadas en la definición de la tarifa, esto se edad, sexo, plan y una exploración por año de suscripción, y cada una de ellas según el volumen y la frecuencia y el costro medio a priori, según datos.

En el análisis gráfico mencionada, se usa para determinar las agrupaciones plausibles de las categorías en cada una de las variables, se debe mencionar que para el caso de la edad se realizan agrupaciones afines a como ya están definidos en las notas técnicas de los mismos.

Menor a 1 Año  
1 - 4 Años  
5 - 14 Años  
15 - 18 Años  
19 - 44 Años  
45 - 49 Años  
50 - 54 Años  
55 - 59 Años  
60 - 64 Años  
65 - 69Años  
70 - 74 Años  
75 años o más  

Para el caso de los montos por fecha de radicado se deberá hacer una actualización de los montos por algún indicador, para este fin se trabajará con la inflación, de esta manera se pretende eliminar de alguna manera este efecto y así poder identificar una real tendencia de los valores que se vienen indemnizando desde hace seis años, comportamientos propios de los prestadores o de los individuos de la población.

Para el caso de los planes este análisis servirá para establecer grupos internos de seguimiento de planes.

Si el tiempo lo permite se podría hacer una interacción entre las variables edad y sexo, y así poder constatar la hipótesis de mayor costo en las mujeres en las edades gestacionales.

De ser posible la estimación y definición de parámetros de interés de técnicas como ACP, serían de utilidad para acompañar el análisis, presentando estos parámetros como conductores del costo (aumento y abrir la discusión de estrategia para mitigar estos aumentos).

##### Técnicas de modelación propuestas

Para el proyecto actual de manera inicial se había propuesto la aplicación de modelos predictivos GLM independientes para la frecuencia y para el costo medio.  En la sesión inicial se mencionó la posibilidad de modelos de predicción a partir de procesamiento de lenguaje natural (concatenar las variables categóricas que en si mayoría son las variables para trabajar), en la segunda sesión el profesor Álvaro sugirió realizar la tarea 4 y así empezar a trabajar.

##### Conocimientos requeridos para el desarrollo del proyecto

De forma lamentable no se ha discutido previamente con el Profesor asesor

>- Bases de datos relacionales
>- Python: nivel actual es de manejo y consolidación de bases de datos
>- Modelos supervisados: explicativos y predictivos
>- Modelos de lenguaje natural

##### Resultados esperados

La actualización de la tarifa, valores posibles de prima a cobrar a los usuarios según sus características para hacer que los productos sean viables, esto es, para cubrir los valores predichos para la siguiente vigencia de aplicación, valores de predicción para la frecuencia y su impacto económico (costos medio).

##### Tiempo de desarrollo esperado

Seis semanas

### Indicadores claves

$$
Exposicion = \frac{Numero de dias expuesto}{Total dias de calendario (365 o 366)} \\
Prima devengada = Anual Premium*Exposicion \\
Frecuencia = \frac{Numero de atenciones}{Exposicion} \\
Costo Medio = \frac{Costo Incurrido de atenciones}{Numero de atenciones} \\
Prima Pura de Riesgo = Frecuencia*CostoMedio \\
Indice de siniestralidad = \frac{Costo Incurrido}{Prima Devengada} \\
$$

### Acciones complementarias

$$
PCOC = RP*(1+IBNR)*(1+ci)*(1+cf)*(1+extS) \\
$$
Donde
>***PCOC***: Projected cost of claims  
>***IBNR***: Factor de ajuste por IBNR  
>***ci***  : Factor de ajuste por la inflación para el período o períodos de aplicación  
>***cf***  : Factor de ajuste por alguna tendencia identificada en la frecuencia  
>***extS***: Factor de ajuste por cualquier otro fenómeno externo que deba ser tenido en cuenta (cambios en la política de gobierno)  

$$
Prima Comercial = \frac{PCOC}{1-(com+exp+u)} \\ \\
$$
Donde
>***com***: porcentaje de comisiones que se da a los intermediarios y fuerza de ventas  
>***exp***: porcentaje de gastos, deben estar todos incluidos, administrativos y otros  
>***u***  : porcentaje esperado de utilidad
___
###### 07/11/2022
###### Nidia Rodríguez