# Minion - Oficina de Chão CPBR8
At the CPBR8 (Campus Party Brazil 2015) I attended the Oficina de Chão Minions, ministered by Alexandre Casemonstro every night at 11pm. The purpose of the workshop was to build a robot using recyclable material and personalizing it as a Minion.

## Components
* Intel Galileo Gen2 board
* DC Motor with gearbox (x2)
* H Bridge motor drive   
* Micro Servo motor (x3)
* Bluetooth Module HC-05
* Power source (AA or 9V batteries)

## Characterization
My group's Minion was characterized as Martin McFly from Back to the Future because it was 2015, the year they travel to in the movie. Along with the Minion, we also made an Hoverboard for it to be on top of.

![Minion Picture](http://julianaklulo.github.io/images/minion.jpg)

## Structure
The structure of the Minion was made using a cleaning product package and the head was an isopor ball. Inside it there was three Micro Servos 9g SG90 TowerPro to move its head and arms. The Hoverboard was made with cardboard and there were two DC motors and wheels so it could move forward, backward and sideways.
![Minion structure](http://julianaklulo.github.io/images/minion2.jpg)
![Hoverboard structure](http://julianaklulo.github.io/images/minion3.jpg)

## Source Code
The workshop was sponsored by Intel, so each group received an Intel Galileo Gen2 board to use in the project. Since it supports Python, we wrote a [script](https://github.com/julianaklulo/minion/blob/master/minion.py) that receives commands via Bluetooth module and controls both the Minion and the Hoverboard. To send the commands we developed an app with MIT AppInventor2.
![App](https://i.imgur.com/xxWBmu6.png)