# IIC Specific Impulse Calculator (ISIC)
<h3>Overview</h3>
Solid rocket motors are a very effective and relatively simple method of propulsion. They are used in amateur model rocketry. The solid rocket engine is a device in which the propellants are burned and the resulting high-pressure gases are expanded through a specially shaped nozzle to produce thrust. However, several tests for evaluating the rocket engine performance must be done to verify the stability and safety of the solid propellant rocket motor. Before launching a rocket, the performance of a rocket motor is generally verified in a test bench in ground, which is called the <b>Static Test</b>. Ground tests are normally performed in test bench to verify if the desirable characteristics and integrity of the develop rocket engine could be maintained prior to any rocket flight. The importance of conducting ground static tests is that they help to ascertain that motor characteristics are in line with design parameters. 

<h3>Dependencies</h3>
<ol>
<li> Pandas (pip install pandas) </li>
<li> Matplotlib (pip install matplotlib) </li>
<li> Numpy (pip install numpy) </li>
</ol>

<h3>Usage</h3>
<ol>
<li>After the static test is done, save the values in a text file according the format specified in the file 'data.txt'. The file should be named as 'data.txt' and should be in the directory as the script.</li>
<li>Run the Python Script. The script plots the graph and gives the area under the curve which is the Impulse of the Motor.</li>
<li>It then asks the user for the amount of fuel taken. After the input is given, the script displays the Specific Impulse.</li>
</ol>

<h3>Output</h3>

![Thrust vs Time Graph](https://github.com/rajdas2001/ISIC/blob/master/Thrust-vs-Time.png)

<p align="center">
Thrust Vs Time Graph
</p>

<p>
 </p>

![Command Line Output](https://github.com/rajdas2001/ISIC/blob/master/Output-cmd.jpg)
 
 <p align="center">
Script Output displaying Impulse and Specific Impulse
</p>
