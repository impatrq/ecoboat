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
L Analog_ADC:MCP3008 U1
U 1 1 5EF4E0FD
P 5500 3050
F 0 "U1" H 5500 3731 50  0000 C CNN
F 1 "MCP3008" H 5500 3640 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W7.62mm" H 5600 3150 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/21295d.pdf" H 5600 3150 50  0001 C CNN
	1    5500 3050
	1    0    0    -1  
$EndComp
Text Label 3900 2800 0    50   ~ 0
ACS712_N°1
Text Label 3900 2900 0    50   ~ 0
ACS712_N°2
Wire Wire Line
	5400 2550 5400 2500
$Comp
L Connector:Screw_Terminal_01x07 J2
U 1 1 5EF54988
P 6450 3050
F 0 "J2" H 6400 3550 50  0000 L CNN
F 1 "Screw_Terminal_01x07" H 6300 3450 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-07A_1x07_P2.54mm_Vertical" H 6450 3050 50  0001 C CNN
F 3 "~" H 6450 3050 50  0001 C CNN
	1    6450 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	6100 3250 6250 3250
Wire Wire Line
	6100 3150 6250 3150
Wire Wire Line
	6100 3050 6250 3050
Wire Wire Line
	6100 2950 6250 2950
Wire Wire Line
	5700 2550 6250 2550
Wire Wire Line
	6250 2550 6250 2750
Wire Wire Line
	5400 2500 6200 2500
Wire Wire Line
	6200 2500 6200 2850
Wire Wire Line
	6200 2850 6250 2850
Text Label 6500 2800 0    50   ~ 0
3,3V
Text Label 6500 2900 0    50   ~ 0
5V
Text Label 6500 3000 0    50   ~ 0
sclk
Text Label 6500 3100 0    50   ~ 0
MISO
Text Label 6500 3200 0    50   ~ 0
MOSI
Text Label 6500 3300 0    50   ~ 0
CEO
Text Label 6500 3400 0    50   ~ 0
GND
$Comp
L Connector:Screw_Terminal_01x05 J1
U 1 1 5EF696C7
P 4450 2950
F 0 "J1" H 4400 2550 50  0000 C CNN
F 1 "Entradas X5" H 4600 2650 50  0000 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical" H 4450 2950 50  0001 C CNN
F 3 "~" H 4450 2950 50  0001 C CNN
	1    4450 2950
	-1   0    0    1   
$EndComp
$Comp
L Device:R_POT RV1
U 1 1 5EF6BB3C
P 4850 2450
F 0 "RV1" V 4643 2450 50  0000 C CNN
F 1 "500k" V 4734 2450 50  0000 C CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3006P_Horizontal" H 4850 2450 50  0001 C CNN
F 3 "~" H 4850 2450 50  0001 C CNN
	1    4850 2450
	0    1    1    0   
$EndComp
Wire Wire Line
	4650 2950 4700 2950
Wire Wire Line
	4700 2950 4700 2450
Wire Wire Line
	4650 2850 4900 2850
Wire Wire Line
	4650 2750 4900 2750
Wire Wire Line
	4850 2600 4850 2950
Wire Wire Line
	4850 2950 4900 2950
Text Label 4100 3000 0    50   ~ 0
Batería
$Comp
L power:Earth #PWR0101
U 1 1 5EF723B2
P 5000 2500
F 0 "#PWR0101" H 5000 2250 50  0001 C CNN
F 1 "Earth" H 5000 2350 50  0001 C CNN
F 2 "" H 5000 2500 50  0001 C CNN
F 3 "~" H 5000 2500 50  0001 C CNN
	1    5000 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 2450 5000 2500
$Comp
L power:Earth #PWR0102
U 1 1 5EF72D32
P 5550 3650
F 0 "#PWR0102" H 5550 3400 50  0001 C CNN
F 1 "Earth" H 5550 3500 50  0001 C CNN
F 2 "" H 5550 3650 50  0001 C CNN
F 3 "~" H 5550 3650 50  0001 C CNN
	1    5550 3650
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR0103
U 1 1 5EF73268
P 6250 3400
F 0 "#PWR0103" H 6250 3150 50  0001 C CNN
F 1 "Earth" H 6250 3250 50  0001 C CNN
F 2 "" H 6250 3400 50  0001 C CNN
F 3 "~" H 6250 3400 50  0001 C CNN
	1    6250 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	6250 3350 6250 3400
Wire Wire Line
	5700 3650 5550 3650
Wire Wire Line
	5400 3650 5550 3650
Connection ~ 5550 3650
$EndSCHEMATC
