# Practica Aqueductes
Aquesta pràctica ha estat realitzada per Antonio Lobateras i correspont a la pràctica 1.
### Costos iteratiu
Respecte als costos del algorisme iteratiu, ha sortit un cost de O(n)
### Costos recursiu
Respecte als costos del algorisme recursiu, ha sortit un cost de O(n)
### Costos empírics dels algoritmes
Basant-me en els costos dels dos algorimes, i en les gràfiques de temps, encara que el cost sigui el mateix, en les gràfiques del algorisme recursiu, tardava una mica més.
## Disseny
A l'hora de realizar la pràctica, la idea principal era calcular els costos de la construcció de aqueductes i ponts, amb els seus respectius pilars amb unes coordenades en concret. Per tan, sabia de saber si era possible fer aquesta construcció i quin era el preu optim entre contruir pilars en tots els punts o només en el primer i l'últim (pilars claus). També s'havia de tenir en compte, en el cas que fos més òptim construir els pilars del primer i l'últim punt, si el aqueducte es trobava per sota de la terra o per sobre, ja que si es trobava per sota o xocava significava que no es podia construir. Per saber si era possible vaig pensar en calcular la distància de cada punt respecte al centre de la semicercle del aqueducte i si la distàncìa era major que el radi i el punt es trobava per sobre de centre, en l'eix de coordenades y, significava que aquest aqueducte. Un altre punt important era comprobar que els pilars es puguessin contruir, i per combrobar-ho, s'havia de saber la altura del pilar dels dos punts en els que s'anava a contruir l'aqueducte i la distància. Llavors si la distància partida entre dos era més gran que la altura de algun dels dos pilars significava que aquell aqueducte no es podia contruir. 
En l'ámbit d'extreure les dades del fitxer amb les dades de la contrucció, com eren strings, ho vaig haver de passar a integers. 

## Enllaç Github

https://github.com/alobateras/prac1_recu_algo
