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
L Analog_ADC:MCP3008 U?
U 1 1 5EF4E0FD
P 5500 3050
F 0 "U?" H 5500 3731 50  0000 C CNN
F 1 "MCP3008" H 5500 3640 50  0000 C CNN
F 2 "" H 5600 3150 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/21295d.pdf" H 5600 3150 50  0001 C CNN
	1    5500 3050
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 5EF50EC2
P 4550 2850
F 0 "J?" H 4468 2525 50  0000 C CNN
F 1 "Sensores de Corriente" H 4468 2616 50  0000 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 4550 2850 50  0001 C CNN
F 3 "~" H 4550 2850 50  0001 C CNN
	1    4550 2850
	-1   0    0    1   
$EndComp
Wire Wire Line
	4750 2750 4900 2750
Wire Wire Line
	4750 2850 4900 2850
Text Label 4000 2800 0    50   ~ 0
ACS712_N°1
Text Label 4000 2900 0    50   ~ 0
ACS712_N°2
Wire Wire Line
	5400 3650 5700 3650
Wire Wire Line
	5400 2550 5400 2500
$Comp
L Connector:Screw_Terminal_01x07 J?
U 1 1 5EF54988
P 6450 3050
F 0 "J?" H 6400 3550 50  0000 L CNN
F 1 "Screw_Terminal_01x07" H 6300 3450 50  0000 L CNN
F 2 "" H 6450 3050 50  0001 C CNN
F 3 "~" H 6450 3050 50  0001 C CNN
	1    6450 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 3650 6250 3650
Wire Wire Line
	6250 3650 6250 3350
Connection ~ 5700 3650
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
$EndSCHEMATC
