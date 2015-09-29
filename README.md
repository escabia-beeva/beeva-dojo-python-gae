# Kata
---

Estamos en el año 3000 y eres un cazarecompensas de élite. Un magnate contrata tus servicios para que des caza a unos  
maleantes de una banda peligrosa. Tu cliente te da una semana exacta para que acabes con todos o con la mayoría que  
puedas.  

Cuanto más secuaces atrapes más serán tus ingresos, pero no conoces el número total que hay de malotes ni su paradero,  
así que necesitas de chivatos para conocer dónde se encuentran.  

Tu cliente te ha mencionado que los maleantes que tienes que dar caza son bastante astutos y rápidos  
(unos más que otros) con lo que solamente puedes dañar un punto de su vida por cada hora del día.  
No te preocupes, tu cliente te pagará las horas extras.  

Con todo esto, necesitas organizarte y crear un horario de una semana con los nombres de los criminales que vas  
a dar caza. El nombre y su paradero los puedes obtener de tus chivatos y teniendo en cuenta que por cada hora que pasa  
logras hacer daño a un criminal en un punto de vida. También es posible que un chivato sea uno de esos criminales,  
en ese caso no puedes darle caza porque te puede dar información valiosa.  

Se pide hacer una aplicación que muestre el horario antes mencionado.  
Teniendo en cuenta las reglas mencionadas anteriormente y otras nuevas:

* No puedes dar caza a un chivato

* Cuando des caza a un villano, por cada hora que pase atrapándole, se resta un punto de su vida hasta llegar a 0  

* Como quieres ser eficiente en tu trabajo, vas a ir a capturar los villanos que se encuentran más cerca de tu posición,  
de esa manera conseguirás más ingresos  

* Cada desplazamiento para capturar a un villano conlleva un coste, debes tenerlo en cuenta  

* El programa debe mostrar el horario que vas a tener con los nombres de los villanos que vas a dar caza y los gastos  
e ingresos finales


## Notas y pistas

* No tengas en cuenta la velocidad de los villanos, pero sí del valor de la distancia que tengan

* Utiliza listas para almacenar los objetos, de esa manera luego podrás ordenarlos más facilmente

* La distancia es un valor positivo, por ejemplo 5 metros

* El número de villanos y de chivatos puede ser aleatorio, también sus valores para cada propiedad


## El resultado final podría ser lo siguiente:

Voy a dar caza a los siguientes villanos:  

Nombre - puntos de vida - recompensa  
Alberto - 40 puntos de vida - 1200 euros  
Juan - 60 puntos de vida - 2000 euros  
Penelope - 80 puntos de vida - 2400 euros  
Clara - 50 puntos de vida - 2400 euros  

Lunes  
  
0 H - Alberto 40 pv  
1 H - Alberto 39 pv  
2 H - Alberto 38 pv  
...  
23 H - Alberto 16 pv  
  
Martes  
  
0 H - Alberto 15 pv  
1 H - Alberto 14 pv  
...  
15 H - Alberto 0 pv  
16 H - Juan 60 pv  
...  
23 H - Juan 53 pv  
  
Miércoles  
  
0 H - Juan 52 pv  
...  
  
Recompensa total ...