<div>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Presidential_Seal_of_Colombia.svg/200px-Presidential_Seal_of_Colombia.svg.png" width="80"/>
</div>

<div>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Logotipo_de_la_Universidad_Nacional_de_Colombia.svg/1024px-Logotipo_de_la_Universidad_Nacional_de_Colombia.svg.png" width="100"/>
</div>

# Universidad Nacional de Colombia
## Facultad de Ciencias
## Departamento de Matemáticas
## Diplomado en Ciencias de Datos</p>
___

# ***Actualización anual, tarifa de planes de Medicina Prepagada***
# ***haciendo uso de modelos GLM supervisados (python)***</p>

___

### Nidia Yomaira Rodríguez Castro
### Profesor: Álvaro Mauricio Montenegro Diaz</p>

___

#### Bogotá D.C., 17 de diciembre de 2022
___

## Actualización anual, tarifa de planes de Medicina Prepagada haciendo uso de modelos GLM (python)</p>

![](http://chris35wills.github.io/courses/pydata_stack.png)</p>

> #### Objetivo:
>Cumplir con el compromiso de actualización de los planes de medicina prepagada que en la actualidad comercializa la compañía MedPlus, esto no solo permite el cumplimiento de la normativa que corresponde sino que además se presenta como una práctica sana de seguimiento y monitoreo de los productos.</p>
>Se aprovecha la oportunidad para aplicar el conocimiento obtenido en el desarrollo del presente Diplomado y aplicar modelos GLM para las medidas de Frecuencia y Severidad (vista como el costo medio).</p>
>Aprovechar la oportunidad para dar a conocer a la organización sobre las nuevas tendencias de análisis de este tipo de análisis.

Además python se utiliza para la limpieza y manejo de las bases de datos trabajadas.</p>

### ***Introducción***

El precio comercial de los productos de seguros esta dado por la expresión:

$$
Prima Comercial = \frac{PCOC}{1-(com+exp+u)} \\ \\
$$

Donde
>***com***: porcentaje de comisiones que se da a los intermediarios y fuerza de ventas  
>***exp***: porcentaje de gastos, deben estar todos incluidos, administrativos y otros  
>***u***: porcentaje esperado de utilidad

La expresión muestra como los ingresos recibidos por el pago de los productos debe cubrir la siniestralidad, para el caso del ramo de salud es el monto agregado (***PCOC***) esperado de las utilizaciones de servicios de salud requeridos por los usuarios o asegurados, el monto de comisiones pagadas a la fuerza de ventas, todos los gastos en los que incurren las compañías para garantizar la continuidad del negocio y además la utilidad esperada del mismo producto

Ahora bien el ***PCOC*** (projected cost of claims) esta dada por la siguiente expresión:

$$
PCOC = RP*(1+IBNR)*(1+ci)*(1+cf)*(1+extS) \\
$$

Donde
>***IBNR***: Factor de ajuste por IBNR  
>***ci***  : Factor de ajuste por la inflación para el período o períodos de aplicación  
>***cf***  : Factor de ajuste por alguna tendencia identificada en la frecuencia  
>***extS***: Factor de ajuste por cualquier otro fenómeno externo que deba ser tenido en cuenta (cambios en la política de gobierno)  

Esta expresión contiene el concepto que da origen a este trabajo, la prima de riesgo (***RP***), el cual se obtiene como el producto de la estimación de la frecuencia y la estimación del costo medio, el cual serán obtenidos a partir de la aplicación de los modelos GLM.

$$
Prima Pura de Riesgo (RP) = Freq * CM \\
$$

En otras palabras, cuantas atenciones de servicios de salud son requeridas por "unidad de tiempo - usuario" y cuál es el impacto económico (costo medio) de estas atenciones. 

### ***Fuentes de datos***

Se usara la información propia de la compañía y el indicador del IPC Salud
El período de estudio comprenderá desde 01/01/2017 hasta el 30/09/2022

***Información de Expuestos***

Se toma la información de cada uno de los cierres contables, un archivo con la información de los usuarios que estuvieron expuestos (pudieron requerir atención de los servicios de salud) por lo menos un día durante cada uno de los meses del período de estudio. Con esta información se calculan los años riesgo, esto es, que proporción de año estuvo expuesto cada uno de los usuarios en un año determinado de los usados en el período de estudio.

#### Archivo_Exp

Variable      | Descripción
------------- | -------------
Anio_Per  | : el año de suscripción según el período de estudio
Carnet  | : número con el que se identifica cada uno de los usuarios (cada individuo en la población)
Rango_E  | : la edad (dispuesta por rangos etareos) de cada uno de los individuos en la población en cada uno de los años
Sexo  | : el género de cada uno de los individuos en la población
nombreplan  | :  identificación del producto o del plan de medicina prepagada que contrata el individuo
P_NetPtoPag  | : monto de prima después de hacer las descuentos del caso (comisiones, gastos, etc.)
Exp_F  | : exposición final, porción de año en riesgo o con cobertura


***Información de atenciones de salud (reclamaciones) efectuados***

Se trabajan dos archivos principalmente, el record del costo médico radicado por parte de los prestadores de servicios de salud (IPS) o proveedores de tecnologías (imágenes) y el archivo de las autorizaciones pendientes por servicios de salud en donde los usuarios manifiestan su querer de hacer uso de algunos servicios de salud y por tanto se crea una autorización en firme con parámetros de usuario, servicios y prestador.

Los valores que se consideran en el estudio o análisis del archivo de costo médico radicado, se indexan a partir del indicador IPC Salud publicado por el DANE, esto se realiza con el fin de disminuir o eliminar posibles tendencias en los valores año tras año.

De estos archivos se obtiene la siguiente información:

#### Archivo_Claims

Variable      | Descripción
------------- | -------------
Anio_Acc  | : el año de la prestación de la atención en salud
Carnet  | : número con el que se identifica cada uno de los usuarios (cada individuo en la población) que recibe la atención de salud
Edad  | : la edad de cada uno de los individuos en la población en cada uno de los años
Sexo  | : el género de cada uno de los individuos en la población 
NAP  | : número única de autorización de la prestación es un código alfanumérica que se crea a partir de la información de usuario, servicio y prestador (se usa para el conteo de las atenciones)
TSA  | : tipo de servicio agrupado, 
nombreplan  | :  identificación del producto o del plan de cobertura que tiene el individuo
CM_Update  | : costo médico radicado indexado + el valor de autorizaciones pendientes
Conteo  | : variable que se usa solo para contar (por NAP - usuario - tipo servicio)

#### Descipción de la información

Se realiza el trabajo ETL tanto para la base de expuestos / riesgos, como para la base de reclamaciones / atenciones de servicios de salud de manera independiente, al final a partir de variables comunes se realiza el cruce de las dos bases para obtener la base de trabajo, tal como se muestra en la tabla de abajo: 

![](https://nbviewer.org/github/Yomacas/MyProject_220909/blob/main/Imagenes/Info.png)

#### Estimación de la Frecuencia

Como es un problema de conteo, se selecciona la distribución Poisson en la familia exponencial de los modelos GLM.

$$
f(y_{i}; {\theta}) = \frac{{\theta}^{y_{i}} * e^{-t}}{y_{i}!}, y_{i} = 0, 1, 2, ... \\ \\
$$

Se usó el siguiente código:

```python
exog = sm.add_constant(X1)
poission_model = sm.GLM(y, exog, family = sm.families.Poisson(), freq_weights = Price_Prod.Exp_F)
result = poission_model.fit()
result.summary()
```
Donde se llama la atención en la parte:</p> "freq_weights = Price_Prod.Exp_F", dado que los datos usados son tabulares

#### Resultados Frecuencia

![](https://nbviewer.org/github/Yomacas/MyProject_220909/blob/main/Imagenes/Poisson_Results.png)

![](https://nbviewer.org/github/Yomacas/MyProject_220909/blob/main/Imagenes/plot0_Freq.png)


#### Estimación de la Severidad (costo medio)

Para el caso de modelar valores de dinero, se selecciona la distribución Gamma en la familia exponencial de los modelos GLM.

$$
f(y; {\theta}) = \frac{y^{{\phi}-1} * {\theta}^{\phi} * e^{-y{\theta}}}{{\Gamma}({\phi})} \\ \\
$$

Se usó el siguiente código:

```python
exog = sm.add_constant(X1)
gamma_model = sm.GLM(y_1, exog, family = sm.families.Gamma(link=sm.families.links.log()), freq_weights = Price_Prod.Num_Claims, missing = 'raise')
result_1 = gamma_model.fit()
result_1.summary()
```
Donde se llama la atención en las partes:<p>"family = sm.families.Gamma(link=sm.families.links.log())", en donde se cambia la función de enlace que viene por defecto<p>"freq_weights = Price_Prod.Num_Claims", dado que los datos usados son tabulares<p>"missing = 'raise", debido a que la función gamma solo trabaja con valores positivos y se debe hacer tratamiento para los ceros

#### Resultados Severidad (costo medio)

![](https://nbviewer.org/github/Yomacas/MyProject_220909/blob/main/Imagenes/Gamma_Results.png)

![](https://nbviewer.org/github/Yomacas/MyProject_220909/blob/main/Imagenes/plot0_Sev.png)

#### Ejemplo de aplicación
    
Anio 2022<p>
Hombre<p>
Edad 45 años<p>
Plan 6

$$
Freq = e^{Const + Coef_{Anio2022} + Coef_{SexoM} + Coef_{RangoE 45-49} + Coef_{nombreplan 6}} \\ \\

$$
Freq = e^{2.9735 + 0.6115 - 0.2880 - 0.3102 + 0.4900} = 12.1436 \\ \\
$$
    
$$
Sev = e^{Const + Coef_{Anio2022} + Coef_{SexoM} + Coef_{RangoE 45-49} + Coef_{nombreplan 6}} \\ \\
    
$$
Sev = e^{-2.0857 - 0.4430 + 0.1876 - 0.0148 + 0.2406} = 0.120597 \\ \\
$$

$$    
RP = Freq * Sev = 12.1436 * 0.120597 = 1.464.480 \\ \\
$$

#### Otras Gráficas
    
Caso Frecuencia

![](https://nbviewer.org/github/Yomacas/MyProject_220909/blob/main/Imagenes/plot1_numabs.png)

![](https://nbviewer.org/github/Yomacas/MyProject_220909/blob/main/Imagenes/plot2_numweighted.png)

![](https://nbviewer.org/github/Yomacas/MyProject_220909/blob/main/Imagenes/plot3_numpred.png)


# Gracias