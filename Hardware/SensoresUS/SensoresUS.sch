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
L Connector:Conn_01x08_Female SalidasEcho1
U 1 1 5EDF2DE8
P 4700 4700
F 0 "SalidasEcho1" H 4728 4630 50  0000 L CNN
F 1 "Conn_01x08_Female" H 4728 4585 50  0001 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-08A_1x08_P2.54mm_Vertical" H 4700 4700 50  0001 C CNN
F 3 "~" H 4700 4700 50  0001 C CNN
	1    4700 4700
	-1   0    0    -1  
$EndComp
Wire Wire Line
	5250 4400 4900 4400
Wire Wire Line
	5250 4500 4900 4500
Wire Wire Line
	5250 4600 4900 4600
Wire Wire Line
	5250 4700 4900 4700
Wire Wire Line
	5250 4800 4900 4800
Wire Wire Line
	5250 4900 4900 4900
Wire Wire Line
	5250 5000 4900 5000
Wire Wire Line
	5250 5100 4900 5100
$Comp
L Connector:Conn_01x03_Female Seleccion1
U 1 1 5EDFA4FC
P 4400 4000
F 0 "Seleccion1" H 4292 4193 50  0000 C CNN
F 1 "Conn_01x03_Female" H 4292 4194 50  0001 C CNN
F 2 "" H 4400 4000 50  0001 C CNN
F 3 "~" H 4400 4000 50  0001 C CNN
	1    4400 4000
	-1   0    0    -1  
$EndComp
Text GLabel 4750 3900 2    50   Input ~ 0
Select1
Text GLabel 4750 4000 2    50   Input ~ 0
Select2
Text GLabel 4750 4100 2    50   Input ~ 0
Select3
Wire Wire Line
	4600 3900 4750 3900
Wire Wire Line
	4600 4000 4750 4000
Wire Wire Line
	4600 4100 4750 4100
Text GLabel 5000 5300 0    50   Input ~ 0
Select1
Text GLabel 5000 5400 0    50   Input ~ 0
Select2
Text GLabel 5000 5500 0    50   Input ~ 0
Select3
Wire Wire Line
	5000 5300 5250 5300
Wire Wire Line
	5000 5400 5250 5400
Wire Wire Line
	5000 5500 5250 5500
$Comp
L Connector:Conn_01x08_Female EntradasTrig1
U 1 1 5EE0315F
P 6650 3250
F 0 "EntradasTrig1" H 6678 3180 50  0000 L CNN
F 1 "Conn_01x08_Female" H 6542 3644 50  0001 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-08A_1x08_P2.54mm_Vertical" H 6650 3250 50  0001 C CNN
F 3 "~" H 6650 3250 50  0001 C CNN
	1    6650 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	6100 2950 6450 2950
Wire Wire Line
	6100 3050 6450 3050
Wire Wire Line
	6100 3150 6450 3150
Wire Wire Line
	6100 3250 6450 3250
Wire Wire Line
	6100 3350 6450 3350
Wire Wire Line
	6100 3450 6450 3450
Wire Wire Line
	6100 3550 6450 3550
Wire Wire Line
	6100 3650 6450 3650
Text GLabel 5050 2950 0    50   Input ~ 0
Select1
Text GLabel 5050 3050 0    50   Input ~ 0
Select2
Text GLabel 5050 3150 0    50   Input ~ 0
Select3
$Comp
L Connector:Conn_01x01_Female Trig1
U 1 1 5EE0702A
P 4850 3650
F 0 "Trig1" H 4742 3743 50  0000 C CNN
F 1 "Conn_01x01_Female" H 4742 3744 50  0001 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 4850 3650 50  0001 C CNN
F 3 "~" H 4850 3650 50  0001 C CNN
	1    4850 3650
	-1   0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x01_Female Echo1
U 1 1 5EE08B55
P 6700 4400
F 0 "Echo1" H 6592 4493 50  0000 C CNN
F 1 "Conn_01x01_Female" H 6592 4494 50  0001 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-06A_1x06_P2.54mm_Vertical" H 6700 4400 50  0001 C CNN
F 3 "~" H 6700 4400 50  0001 C CNN
	1    6700 4400
	1    0    0    -1  
$EndComp
Wire Wire Line
	6500 4400 6250 4400
Wire Wire Line
	5050 3650 5300 3650
Wire Wire Line
	5050 3150 5300 3150
Wire Wire Line
	5050 3050 5300 3050
Wire Wire Line
	5050 2950 5300 2950
$Comp
L power:+5V #PWR0101
U 1 1 5EE0D3E3
P 5000 2450
F 0 "#PWR0101" H 5000 2300 50  0001 C CNN
F 1 "+5V" H 5015 2623 50  0000 C CNN
F 2 "" H 5000 2450 50  0001 C CNN
F 3 "" H 5000 2450 50  0001 C CNN
	1    5000 2450
	1    0    0    -1  
$EndComp
Text GLabel 4900 2500 0    50   BiDi ~ 0
5V
Text GLabel 5500 2750 0    50   BiDi ~ 0
5V
Wire Wire Line
	5500 2750 5700 2750
Wire Wire Line
	4900 2500 5000 2500
Wire Wire Line
	5000 2500 5000 2450
$Comp
L power:GND #PWR0102
U 1 1 5EE138C4
P 5750 6100
F 0 "#PWR0102" H 5750 5850 50  0001 C CNN
F 1 "GND" H 5755 5927 50  0000 C CNN
F 2 "" H 5750 6100 50  0001 C CNN
F 3 "" H 5750 6100 50  0001 C CNN
	1    5750 6100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0103
U 1 1 5EE141AD
P 6000 3850
F 0 "#PWR0103" H 6000 3600 50  0001 C CNN
F 1 "GND" H 6005 3677 50  0000 C CNN
F 2 "" H 6000 3850 50  0001 C CNN
F 3 "" H 6000 3850 50  0001 C CNN
	1    6000 3850
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 3850 6000 3850
Wire Wire Line
	5750 6000 5750 6100
Text GLabel 5600 4100 0    50   BiDi ~ 0
5V
Wire Wire Line
	5600 4100 5750 4100
$Comp
L 74xx:74HC237 Trig3
U 1 1 5EDE9FF8
P 5700 3350
F 0 "Trig3" H 5700 4131 50  0000 C CNN
F 1 "74HC237" H 5700 4040 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W7.62mm_LongPads" H 5700 3350 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/cd74hc237.pdf" H 5700 3350 50  0001 C CNN
	1    5700 3350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 5EDEB9F0
P 4700 3350
F 0 "#PWR0104" H 4700 3100 50  0001 C CNN
F 1 "GND" H 4705 3177 50  0000 C CNN
F 2 "" H 4700 3350 50  0001 C CNN
F 3 "" H 4700 3350 50  0001 C CNN
	1    4700 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	5300 3350 4700 3350
$Comp
L Connector:Conn_01x01_Female Trig2
U 1 1 5EDED08B
P 4850 3500
F 0 "Trig2" H 4742 3593 50  0000 C CNN
F 1 "Conn_01x01_Female" H 4742 3594 50  0001 C CNN
F 2 "" H 4850 3500 50  0001 C CNN
F 3 "~" H 4850 3500 50  0001 C CNN
	1    4850 3500
	-1   0    0    -1  
$EndComp
Wire Wire Line
	5050 3500 5300 3500
Wire Wire Line
	5300 3500 5300 3550
$Comp
L 74xx:74LS151 Echo2
U 1 1 5EDEF353
P 5750 5000
F 0 "Echo2" H 5750 6081 50  0000 C CNN
F 1 "74LS151" H 5750 5990 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W7.62mm_LongPads" H 5750 5000 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS151" H 5750 5000 50  0001 C CNN
	1    5750 5000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 5EE064BB
P 5250 5700
F 0 "#PWR0105" H 5250 5450 50  0001 C CNN
F 1 "GND" H 5255 5527 50  0000 C CNN
F 2 "" H 5250 5700 50  0001 C CNN
F 3 "" H 5250 5700 50  0001 C CNN
	1    5250 5700
	1    0    0    -1  
$EndComp
$EndSCHEMATC
