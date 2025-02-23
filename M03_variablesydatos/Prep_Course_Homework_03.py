#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
numero = 10
print(numero)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
numeroDecimal = 8.5
type(numeroDecimal)




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
type(numero)




# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre = "Gerardo Gr"



# 5) Crear una variable que contenga un número complejo

# In[3]:
numeroComplejo = 5 + 2j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
type(numeroComplejo)




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
text = 'True'
booleano = True
# Son diferentes por que una es de tipo texto y la otra de tipo bool
print(type(text))
print(type(booleano))




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print("El tipo de dato de la primer variable ", type(text), "Y de la segunda variable " , type(booleano))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
resultado = 6 + 3.2
print(resultado)





# 11) Realizar una operación de suma de números complejos

# In[2]:
numeroComplejo1 = 23 + 4j
numeroComplejo2 = 21 + 2j
resultado1 = numeroComplejo1 + numeroComplejo2
print(resultado1)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
numeroEntero = 23
numeroComplejo3 = 2 + 4j
resultado2 = numeroComplejo3 + numeroEntero
print(resultado2)



# 13) Realizar una operación de multiplicación

# In[5]:
resultado3 = 4 * 5
print(resultado3)




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
resultado4 = 2 ** 8
print(resultado4)




# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
print(27/4)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
print(27//4)





# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
print(27%4)





# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
print(((27//44) * 4 ) + (27%3))




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
texto1 = "hola"
texto2 = "como estas"
print(texto1 + " " + texto2)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
print('2' == 2) #Uno es cadena de texto y el otro es entero




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
print(int('2') == 2) # se cambio la cadena de texto a entero




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
# a = float('3,8') # manda error por la , se debe usar el .
a = float('3.8') 




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
numero2 = 3 
numero2 -= 1
print(numero2 )




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
print (1 << 2) 




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
print( 2 + int('2')) # son de distinto tipo de dato



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
print( str(2) + '2') # se concatenan los datos 


