EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Screw_Terminal_01x02 uC_Propulsion1
U 1 1 5E7CEAB7
P 1500 1700
F 0 "uC_Propulsion1" H 1400 1500 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 1418 1466 50  0001 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 1500 1700 50  0001 C CNN
F 3 "~" H 1500 1700 50  0001 C CNN
	1    1500 1700
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 Bateria1
U 1 1 5E7FBF26
P 6550 3750
F 0 "Bateria1" H 6550 3550 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 6468 3516 50  0001 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 6550 3750 50  0001 C CNN
F 3 "~" H 6550 3750 50  0001 C CNN
	1    6550 3750
	1    0    0    -1  
$EndComp
$Comp
L Device:Fuse F1
U 1 1 5E8E5D3E
P 6100 3750
F 0 "F1" V 5903 3750 50  0000 C CNN
F 1 "Fuse" V 5994 3750 50  0000 C CNN
F 2 "Fuse:Fuse_Blade_Mini_directSolder" V 6030 3750 50  0001 C CNN
F 3 "~" H 6100 3750 50  0001 C CNN
	1    6100 3750
	0    1    1    0   
$EndComp
Wire Wire Line
	6250 3750 6350 3750
$Comp
L Transistor_FET:IRF9540N Q1
U 1 1 5E9D0354
P 3250 1150
F 0 "Q1" H 3454 1104 50  0000 L CNN
F 1 "IRF9540N" H 3454 1195 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 3450 1075 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf9540n.pdf" H 3250 1150 50  0001 L CNN
	1    3250 1150
	1    0    0    1   
$EndComp
$Comp
L Transistor_FET:IRF540N Q2
U 1 1 5E9D2967
P 3250 2150
F 0 "Q2" H 3454 2196 50  0000 L CNN
F 1 "IRF540N" H 3454 2105 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 3500 2075 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 3250 2150 50  0001 L CNN
	1    3250 2150
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 Motor_Propulsion1
U 1 1 5E9D5504
P 3900 1850
F 0 "Motor_Propulsion1" V 3650 1800 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 3818 1616 50  0001 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 3900 1850 50  0001 C CNN
F 3 "~" H 3900 1850 50  0001 C CNN
	1    3900 1850
	0    1    1    0   
$EndComp
Wire Wire Line
	2900 1150 3050 1150
Wire Wire Line
	3350 1350 3350 1650
Wire Wire Line
	3050 2150 2900 2150
$Comp
L Device:R R3
U 1 1 5E9DEC23
P 2900 950
F 0 "R3" H 2970 996 50  0000 L CNN
F 1 "10k" H 2970 905 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 2830 950 50  0001 C CNN
F 3 "~" H 2900 950 50  0001 C CNN
	1    2900 950 
	1    0    0    -1  
$EndComp
Wire Wire Line
	2900 1100 2900 1150
$Comp
L Device:R R4
U 1 1 5E9DFAB9
P 2900 2350
F 0 "R4" H 2970 2396 50  0000 L CNN
F 1 "10k" H 2970 2305 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 2830 2350 50  0001 C CNN
F 3 "~" H 2900 2350 50  0001 C CNN
	1    2900 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2900 2150 2900 2200
$Comp
L power:Earth #PWR0101
U 1 1 5E9DC5BA
P 2550 1650
F 0 "#PWR0101" H 2550 1400 50  0001 C CNN
F 1 "Earth" H 2550 1500 50  0001 C CNN
F 2 "" H 2550 1650 50  0001 C CNN
F 3 "~" H 2550 1650 50  0001 C CNN
	1    2550 1650
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:IRF9540N Q3
U 1 1 5E9EE782
P 4400 1150
F 0 "Q3" H 4605 1104 50  0000 L CNN
F 1 "IRF9540N" H 4605 1195 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 4600 1075 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf9540n.pdf" H 4400 1150 50  0001 L CNN
	1    4400 1150
	-1   0    0    1   
$EndComp
$Comp
L Transistor_FET:IRF540N Q4
U 1 1 5E9EE788
P 4400 2150
F 0 "Q4" H 4605 2196 50  0000 L CNN
F 1 "IRF540N" H 4605 2105 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 4650 2075 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 4400 2150 50  0001 L CNN
	1    4400 2150
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4750 1150 4600 1150
Wire Wire Line
	4300 1350 4300 1650
Wire Wire Line
	4600 2150 4750 2150
$Comp
L Device:R R5
U 1 1 5E9EE79D
P 4750 950
F 0 "R5" H 4680 996 50  0000 R CNN
F 1 "10k" H 4680 905 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4680 950 50  0001 C CNN
F 3 "~" H 4750 950 50  0001 C CNN
	1    4750 950 
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4750 1100 4750 1150
$Comp
L Device:R R6
U 1 1 5E9EE7A5
P 4750 2350
F 0 "R6" H 4680 2396 50  0000 R CNN
F 1 "10k" H 4680 2305 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4680 2350 50  0001 C CNN
F 3 "~" H 4750 2350 50  0001 C CNN
	1    4750 2350
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4750 2150 4750 2200
$Comp
L power:Earth #PWR0102
U 1 1 5E9EE7AE
P 5100 1650
F 0 "#PWR0102" H 5100 1400 50  0001 C CNN
F 1 "Earth" H 5100 1500 50  0001 C CNN
F 2 "" H 5100 1650 50  0001 C CNN
F 3 "~" H 5100 1650 50  0001 C CNN
	1    5100 1650
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3350 1650 3800 1650
Connection ~ 3350 1650
Wire Wire Line
	3350 1650 3350 1950
Wire Wire Line
	3900 1650 4300 1650
Connection ~ 4300 1650
Wire Wire Line
	4300 1650 4300 1950
Wire Wire Line
	4300 2350 3800 2350
Wire Wire Line
	3350 950  3800 950 
$Comp
L power:Earth #PWR0103
U 1 1 5E9EFCCD
P 3800 2500
F 0 "#PWR0103" H 3800 2250 50  0001 C CNN
F 1 "Earth" H 3800 2350 50  0001 C CNN
F 2 "" H 3800 2500 50  0001 C CNN
F 3 "~" H 3800 2500 50  0001 C CNN
	1    3800 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 2350 3800 2500
Connection ~ 3800 2350
Wire Wire Line
	3800 2350 3350 2350
Wire Wire Line
	4750 2500 3800 2500
Connection ~ 3800 2500
Wire Wire Line
	2900 2500 3800 2500
Wire Wire Line
	3800 800  3800 950 
Connection ~ 3800 950 
Wire Wire Line
	3800 950  4300 950 
Wire Wire Line
	4750 800  4500 800 
Connection ~ 3800 800 
Wire Wire Line
	2900 800  3150 800 
$Comp
L Device:R R1
U 1 1 5E9F4322
P 2000 1350
F 0 "R1" V 1793 1350 50  0000 C CNN
F 1 "220" V 1884 1350 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1930 1350 50  0001 C CNN
F 3 "~" H 2000 1350 50  0001 C CNN
	1    2000 1350
	0    1    1    0   
$EndComp
Wire Wire Line
	2250 1350 2150 1350
Wire Wire Line
	1850 1600 1850 1350
$Comp
L Connector:Screw_Terminal_01x02 uC_Cangilon1
U 1 1 5EA1814D
P 1500 3850
F 0 "uC_Cangilon1" H 1400 3650 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 1418 3616 50  0001 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 1500 3850 50  0001 C CNN
F 3 "~" H 1500 3850 50  0001 C CNN
	1    1500 3850
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 Motor_Cangilon1
U 1 1 5EA1815F
P 3900 4000
F 0 "Motor_Cangilon1" V 3650 3950 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 3818 3766 50  0001 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 3900 4000 50  0001 C CNN
F 3 "~" H 3900 4000 50  0001 C CNN
	1    3900 4000
	0    1    1    0   
$EndComp
Wire Wire Line
	2900 3300 3050 3300
Wire Wire Line
	3350 3500 3350 3800
Wire Wire Line
	3050 4300 2900 4300
Wire Wire Line
	2900 3250 2900 3300
Wire Wire Line
	2900 4300 2900 4350
Wire Wire Line
	4750 3300 4600 3300
Wire Wire Line
	4300 3500 4300 3800
Wire Wire Line
	4600 4300 4750 4300
Wire Wire Line
	4750 3250 4750 3300
Wire Wire Line
	4750 4300 4750 4350
Wire Wire Line
	3350 3800 3800 3800
Connection ~ 3350 3800
Wire Wire Line
	3350 3800 3350 4100
Wire Wire Line
	3900 3800 4300 3800
Connection ~ 4300 3800
Wire Wire Line
	4300 3800 4300 4100
Wire Wire Line
	4300 4500 3800 4500
Wire Wire Line
	3350 3100 3800 3100
$Comp
L power:Earth #PWR0106
U 1 1 5EA181C5
P 3800 4650
F 0 "#PWR0106" H 3800 4400 50  0001 C CNN
F 1 "Earth" H 3800 4500 50  0001 C CNN
F 2 "" H 3800 4650 50  0001 C CNN
F 3 "~" H 3800 4650 50  0001 C CNN
	1    3800 4650
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 4500 3800 4650
Connection ~ 3800 4500
Wire Wire Line
	3800 4500 3350 4500
Connection ~ 3800 4650
Wire Wire Line
	3800 2950 3800 3100
Connection ~ 3800 3100
Wire Wire Line
	3800 3100 4300 3100
Wire Wire Line
	4750 2950 4500 2950
Connection ~ 3800 2950
Wire Wire Line
	2900 2950 3150 2950
Wire Wire Line
	1850 3750 1850 3500
Wire Wire Line
	1700 3850 1850 3850
Wire Wire Line
	1850 3850 1850 4100
$Comp
L Transistor_Array:ULN2003 U1
U 1 1 5E9A62F3
P 3800 5500
F 0 "U1" H 3350 6000 50  0000 C CNN
F 1 "ULN2003" H 3300 5900 50  0000 C CNN
F 2 "Package_DIP:DIP-14_W10.16mm" H 3850 4950 50  0001 L CNN
F 3 "http://www.ti.com/lit/ds/symlink/uln2003a.pdf" H 3900 5300 50  0001 C CNN
	1    3800 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5950 3750 5900 3750
Wire Wire Line
	5900 3750 5900 750 
Wire Wire Line
	5900 750  3800 750 
Wire Wire Line
	3800 750  3800 800 
Wire Wire Line
	3800 2850 3800 2950
Connection ~ 5900 3750
$Comp
L power:Earth #PWR0107
U 1 1 5E9A9A4B
P 3800 6150
F 0 "#PWR0107" H 3800 5900 50  0001 C CNN
F 1 "Earth" H 3800 6000 50  0001 C CNN
F 2 "" H 3800 6150 50  0001 C CNN
F 3 "~" H 3800 6150 50  0001 C CNN
	1    3800 6150
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 6100 3800 6150
Wire Wire Line
	5900 3750 5900 5100
Wire Wire Line
	5900 5100 4200 5100
$Comp
L Connector:Screw_Terminal_01x04 Motor_Direccion1
U 1 1 5E9B4600
P 5500 5400
F 0 "Motor_Direccion1" H 5150 5600 50  0000 L CNN
F 1 "Screw_Terminal_01x04" H 5580 5301 50  0001 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-04A_1x04_P2.54mm_Vertical" H 5500 5400 50  0001 C CNN
F 3 "~" H 5500 5400 50  0001 C CNN
	1    5500 5400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2100 5300 3400 5300
Wire Wire Line
	2100 5400 3400 5400
Wire Wire Line
	2100 5500 3400 5500
Wire Wire Line
	2100 5600 3400 5600
Wire Wire Line
	4200 5300 5300 5300
Wire Wire Line
	4200 5400 5300 5400
Wire Wire Line
	4200 5500 5300 5500
Wire Wire Line
	4200 5600 5300 5600
Connection ~ 3800 6100
$Comp
L power:Earth #PWR0108
U 1 1 5EA83A93
P 6350 3900
F 0 "#PWR0108" H 6350 3650 50  0001 C CNN
F 1 "Earth" H 6350 3750 50  0001 C CNN
F 2 "" H 6350 3900 50  0001 C CNN
F 3 "~" H 6350 3900 50  0001 C CNN
	1    6350 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	6350 3850 6350 3900
$Comp
L Device:C C1
U 1 1 5E9ED93B
P 5900 5500
F 0 "C1" H 6015 5546 50  0000 L CNN
F 1 "C" H 6015 5455 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 6015 5409 50  0001 L CNN
F 3 "~" H 5900 5500 50  0001 C CNN
	1    5900 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 5100 5900 5350
Connection ~ 5900 5100
Wire Wire Line
	5900 5650 5900 6100
Wire Wire Line
	5900 6100 3800 6100
$Comp
L Connector:Screw_Terminal_01x04 uCDireccion1
U 1 1 5EFAC944
P 1900 5500
F 0 "uCDireccion1" H 1818 5075 50  0000 C CNN
F 1 "Screw_Terminal_01x04" H 1818 5166 50  0000 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-04A_1x04_P2.54mm_Vertical" H 1900 5500 50  0001 C CNN
F 3 "~" H 1900 5500 50  0001 C CNN
	1    1900 5500
	-1   0    0    1   
$EndComp
$Comp
L Isolator:4N25 U2
U 1 1 5F002069
P 2550 1450
F 0 "U2" H 2550 1775 50  0000 C CNN
F 1 "4N25" H 2550 1684 50  0000 C CNN
F 2 "Package_DIP:DIP-6_W7.62mm" H 2350 1250 50  0001 L CIN
F 3 "https://www.vishay.com/docs/83725/4n25.pdf" H 2550 1450 50  0001 L CNN
	1    2550 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	1700 1600 1800 1600
Wire Wire Line
	1700 1700 1850 1700
Wire Wire Line
	2900 1150 2900 1450
Wire Wire Line
	2900 1450 2850 1450
Connection ~ 2900 1150
Wire Wire Line
	2250 1650 2550 1650
Wire Wire Line
	2250 1550 2250 1650
Wire Wire Line
	2550 1650 2850 1650
Wire Wire Line
	2850 1650 2850 1550
Connection ~ 2550 1650
$Comp
L Isolator:4N25 U4
U 1 1 5F020A68
P 2600 2050
F 0 "U4" H 2600 2375 50  0000 C CNN
F 1 "4N25" H 2600 2284 50  0000 C CNN
F 2 "Package_DIP:DIP-6_W7.62mm" H 2400 1850 50  0001 L CIN
F 3 "https://www.vishay.com/docs/83725/4n25.pdf" H 2600 2050 50  0001 L CNN
	1    2600 2050
	1    0    0    -1  
$EndComp
Connection ~ 2900 2150
Wire Wire Line
	2150 1950 2300 1950
Wire Wire Line
	2900 2050 3150 2050
Wire Wire Line
	3150 2050 3150 800 
Connection ~ 3150 800 
Wire Wire Line
	3150 800  3800 800 
Wire Wire Line
	2300 2150 2300 2500
Wire Wire Line
	2300 2500 2900 2500
Connection ~ 2900 2500
$Comp
L Isolator:4N25 U6
U 1 1 5F02FF87
P 5050 2050
F 0 "U6" H 5050 2375 50  0000 C CNN
F 1 "4N25" H 5050 2284 50  0000 C CNN
F 2 "Package_DIP:DIP-6_W7.62mm" H 4850 1850 50  0001 L CIN
F 3 "https://www.vishay.com/docs/83725/4n25.pdf" H 5050 2050 50  0001 L CNN
	1    5050 2050
	-1   0    0    -1  
$EndComp
Connection ~ 4750 2150
$Comp
L Isolator:4N25 U8
U 1 1 5F033177
P 5100 1450
F 0 "U8" H 5100 1775 50  0000 C CNN
F 1 "4N25" H 5100 1684 50  0000 C CNN
F 2 "Package_DIP:DIP-6_W7.62mm" H 4900 1250 50  0001 L CIN
F 3 "https://www.vishay.com/docs/83725/4n25.pdf" H 5100 1450 50  0001 L CNN
	1    5100 1450
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4750 1150 4750 1450
Wire Wire Line
	4750 1450 4800 1450
Connection ~ 4750 1150
Wire Wire Line
	5400 1350 5450 1350
Wire Wire Line
	4800 1550 4800 1650
Wire Wire Line
	4800 1650 5100 1650
Wire Wire Line
	5100 1650 5400 1650
Wire Wire Line
	5400 1650 5400 1550
Connection ~ 5100 1650
Wire Wire Line
	5450 1950 5350 1950
Wire Wire Line
	5350 2150 5350 2500
Wire Wire Line
	5350 2500 4750 2500
Connection ~ 4750 2500
Wire Wire Line
	1800 1600 1800 2650
Wire Wire Line
	1800 2650 5750 2650
Wire Wire Line
	5750 2650 5750 1950
Connection ~ 1800 1600
Wire Wire Line
	1800 1600 1850 1600
Wire Wire Line
	5750 1350 5800 1350
Wire Wire Line
	5800 1350 5800 2700
Wire Wire Line
	5800 2700 1850 2700
$Comp
L Transistor_FET:IRF9540N Q5
U 1 1 5F05B32E
P 3250 3300
F 0 "Q5" H 3454 3254 50  0000 L CNN
F 1 "IRF9540N" H 3454 3345 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 3450 3225 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf9540n.pdf" H 3250 3300 50  0001 L CNN
	1    3250 3300
	1    0    0    1   
$EndComp
$Comp
L Transistor_FET:IRF9540N Q7
U 1 1 5F05BBDD
P 4400 3300
F 0 "Q7" H 4605 3254 50  0000 L CNN
F 1 "IRF9540N" H 4605 3345 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 4600 3225 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf9540n.pdf" H 4400 3300 50  0001 L CNN
	1    4400 3300
	-1   0    0    1   
$EndComp
$Comp
L Transistor_FET:IRF540N Q6
U 1 1 5F05C27A
P 3250 4300
F 0 "Q6" H 3454 4346 50  0000 L CNN
F 1 "IRF540N" H 3454 4255 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 3500 4225 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 3250 4300 50  0001 L CNN
	1    3250 4300
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:IRF540N Q8
U 1 1 5F05CF57
P 4400 4300
F 0 "Q8" H 4605 4346 50  0000 L CNN
F 1 "IRF540N" H 4605 4255 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 4650 4225 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 4400 4300 50  0001 L CNN
	1    4400 4300
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4750 2050 4500 2050
Wire Wire Line
	4500 2050 4500 800 
Connection ~ 4500 800 
Wire Wire Line
	4500 800  3800 800 
Wire Wire Line
	1850 1700 1850 1950
$Comp
L Device:R R2
U 1 1 5F063F20
P 2000 1950
F 0 "R2" V 1793 1950 50  0000 C CNN
F 1 "220" V 1884 1950 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1930 1950 50  0001 C CNN
F 3 "~" H 2000 1950 50  0001 C CNN
	1    2000 1950
	0    1    1    0   
$EndComp
Connection ~ 1850 1950
Wire Wire Line
	1850 1950 1850 2700
$Comp
L Device:R R14
U 1 1 5F0641E7
P 5600 1950
F 0 "R14" V 5393 1950 50  0000 C CNN
F 1 "220" V 5484 1950 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 5530 1950 50  0001 C CNN
F 3 "~" H 5600 1950 50  0001 C CNN
	1    5600 1950
	0    1    1    0   
$EndComp
$Comp
L Device:R R13
U 1 1 5F0646E3
P 5600 1350
F 0 "R13" V 5393 1350 50  0000 C CNN
F 1 "220" V 5484 1350 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 5530 1350 50  0001 C CNN
F 3 "~" H 5600 1350 50  0001 C CNN
	1    5600 1350
	0    1    1    0   
$EndComp
Wire Wire Line
	1700 3750 1800 3750
$Comp
L Isolator:4N25 U5
U 1 1 5F06CB3C
P 2600 4200
F 0 "U5" H 2600 4525 50  0000 C CNN
F 1 "4N25" H 2600 4434 50  0000 C CNN
F 2 "Package_DIP:DIP-6_W7.62mm" H 2400 4000 50  0001 L CIN
F 3 "https://www.vishay.com/docs/83725/4n25.pdf" H 2600 4200 50  0001 L CNN
	1    2600 4200
	1    0    0    -1  
$EndComp
Connection ~ 2900 4300
$Comp
L Isolator:4N25 U3
U 1 1 5F0726D9
P 2550 3600
F 0 "U3" H 2550 3925 50  0000 C CNN
F 1 "4N25" H 2550 3834 50  0000 C CNN
F 2 "Package_DIP:DIP-6_W7.62mm" H 2350 3400 50  0001 L CIN
F 3 "https://www.vishay.com/docs/83725/4n25.pdf" H 2550 3600 50  0001 L CNN
	1    2550 3600
	1    0    0    -1  
$EndComp
$Comp
L Isolator:4N25 U7
U 1 1 5F0735D6
P 5050 4200
F 0 "U7" H 5050 4525 50  0000 C CNN
F 1 "4N25" H 5050 4434 50  0000 C CNN
F 2 "Package_DIP:DIP-6_W7.62mm" H 4850 4000 50  0001 L CIN
F 3 "https://www.vishay.com/docs/83725/4n25.pdf" H 5050 4200 50  0001 L CNN
	1    5050 4200
	-1   0    0    -1  
$EndComp
Connection ~ 4750 4300
$Comp
L Isolator:4N25 U9
U 1 1 5F07448D
P 5100 3600
F 0 "U9" H 5100 3925 50  0000 C CNN
F 1 "4N25" H 5100 3834 50  0000 C CNN
F 2 "Package_DIP:DIP-6_W7.62mm" H 4900 3400 50  0001 L CIN
F 3 "https://www.vishay.com/docs/83725/4n25.pdf" H 5100 3600 50  0001 L CNN
	1    5100 3600
	-1   0    0    -1  
$EndComp
$Comp
L power:Earth #PWR0105
U 1 1 5F075575
P 5100 3800
F 0 "#PWR0105" H 5100 3550 50  0001 C CNN
F 1 "Earth" H 5100 3650 50  0001 C CNN
F 2 "" H 5100 3800 50  0001 C CNN
F 3 "~" H 5100 3800 50  0001 C CNN
	1    5100 3800
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R16
U 1 1 5F07592F
P 5600 4100
F 0 "R16" V 5393 4100 50  0000 C CNN
F 1 "220" V 5484 4100 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 5530 4100 50  0001 C CNN
F 3 "~" H 5600 4100 50  0001 C CNN
	1    5600 4100
	0    1    1    0   
$EndComp
$Comp
L Device:R R15
U 1 1 5F075D82
P 5600 3500
F 0 "R15" V 5393 3500 50  0000 C CNN
F 1 "220" V 5484 3500 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 5530 3500 50  0001 C CNN
F 3 "~" H 5600 3500 50  0001 C CNN
	1    5600 3500
	0    1    1    0   
$EndComp
Wire Wire Line
	5900 3750 5850 3750
Wire Wire Line
	5850 3750 5850 2850
Wire Wire Line
	3800 2850 5850 2850
$Comp
L Device:R R7
U 1 1 5F07AAF0
P 2000 3500
F 0 "R7" V 1793 3500 50  0000 C CNN
F 1 "220" V 1884 3500 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1930 3500 50  0001 C CNN
F 3 "~" H 2000 3500 50  0001 C CNN
	1    2000 3500
	0    1    1    0   
$EndComp
$Comp
L Device:R R8
U 1 1 5F07B007
P 2000 4100
F 0 "R8" V 1793 4100 50  0000 C CNN
F 1 "220" V 1884 4100 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1930 4100 50  0001 C CNN
F 3 "~" H 2000 4100 50  0001 C CNN
	1    2000 4100
	0    1    1    0   
$EndComp
Wire Wire Line
	2150 3500 2250 3500
Wire Wire Line
	2150 4100 2300 4100
$Comp
L power:Earth #PWR0109
U 1 1 5F083A08
P 2550 3800
F 0 "#PWR0109" H 2550 3550 50  0001 C CNN
F 1 "Earth" H 2550 3650 50  0001 C CNN
F 2 "" H 2550 3800 50  0001 C CNN
F 3 "~" H 2550 3800 50  0001 C CNN
	1    2550 3800
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2250 3700 2250 3800
Wire Wire Line
	2250 3800 2550 3800
Wire Wire Line
	2550 3800 2850 3800
Wire Wire Line
	2850 3800 2850 3700
Connection ~ 2550 3800
Wire Wire Line
	2850 3600 2900 3600
Wire Wire Line
	2900 3600 2900 3300
Connection ~ 2900 3300
Wire Wire Line
	3150 4200 3150 2950
Connection ~ 3150 2950
Wire Wire Line
	3150 2950 3800 2950
Wire Wire Line
	2300 4300 2300 4650
Wire Wire Line
	5450 4100 5350 4100
Wire Wire Line
	5350 4300 5350 4650
Wire Wire Line
	4750 4200 4500 4200
Wire Wire Line
	4500 4200 4500 2950
Connection ~ 4500 2950
Wire Wire Line
	4500 2950 3800 2950
Wire Wire Line
	4750 3300 4750 3600
Wire Wire Line
	4750 3600 4800 3600
Connection ~ 4750 3300
Wire Wire Line
	4800 3700 4800 3800
Wire Wire Line
	4800 3800 5100 3800
Wire Wire Line
	5400 3700 5100 3700
Wire Wire Line
	5100 3700 5100 3800
Connection ~ 5100 3800
Wire Wire Line
	1800 3750 1800 4800
Wire Wire Line
	1800 4800 5750 4800
Wire Wire Line
	5750 4800 5750 4100
Connection ~ 1800 3750
Wire Wire Line
	1800 3750 1850 3750
Wire Wire Line
	1850 4100 1850 4850
Wire Wire Line
	1850 4850 5800 4850
Wire Wire Line
	5800 4850 5800 3500
Wire Wire Line
	5800 3500 5750 3500
Connection ~ 1850 4100
Wire Wire Line
	2300 4650 2900 4650
Wire Wire Line
	3800 4650 4750 4650
$Comp
L Device:R R9
U 1 1 5F0CA0D4
P 2900 3100
F 0 "R9" H 2970 3146 50  0000 L CNN
F 1 "10k" H 2970 3055 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 2830 3100 50  0001 C CNN
F 3 "~" H 2900 3100 50  0001 C CNN
	1    2900 3100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R10
U 1 1 5F0CA4D1
P 2900 4500
F 0 "R10" H 2970 4546 50  0000 L CNN
F 1 "10k" H 2970 4455 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 2830 4500 50  0001 C CNN
F 3 "~" H 2900 4500 50  0001 C CNN
	1    2900 4500
	1    0    0    -1  
$EndComp
Connection ~ 2900 4650
Wire Wire Line
	2900 4650 3800 4650
$Comp
L Device:R R11
U 1 1 5F0CAFB0
P 4750 3100
F 0 "R11" H 4820 3146 50  0000 L CNN
F 1 "10k" H 4820 3055 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4680 3100 50  0001 C CNN
F 3 "~" H 4750 3100 50  0001 C CNN
	1    4750 3100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R12
U 1 1 5F0CB34B
P 4750 4500
F 0 "R12" H 4820 4546 50  0000 L CNN
F 1 "10k" H 4820 4455 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4680 4500 50  0001 C CNN
F 3 "~" H 4750 4500 50  0001 C CNN
	1    4750 4500
	1    0    0    -1  
$EndComp
Connection ~ 4750 4650
Wire Wire Line
	4750 4650 5350 4650
Wire Wire Line
	2900 4200 3150 4200
Wire Wire Line
	5450 3500 5400 3500
$EndSCHEMATC
