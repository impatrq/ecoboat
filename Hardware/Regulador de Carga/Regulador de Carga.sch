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
L Connector:Screw_Terminal_01x04 BATout1
U 1 1 5E9E2845
P 4400 1900
F 0 "BATout1" V 4364 1612 50  0000 R CNN
F 1 "Screw_Terminal_01x04" V 4273 1612 50  0001 R CNN
F 2 "TerminalBlock:TerminalBlock_bornier-4_P5.08mm" H 4400 1900 50  0001 C CNN
F 3 "~" H 4400 1900 50  0001 C CNN
	1    4400 1900
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4400 2100 4500 2100
$Comp
L power:Earth #PWR0101
U 1 1 5E9E4EF0
P 4300 2150
F 0 "#PWR0101" H 4300 1900 50  0001 C CNN
F 1 "Earth" H 4300 2000 50  0001 C CNN
F 2 "" H 4300 2150 50  0001 C CNN
F 3 "~" H 4300 2150 50  0001 C CNN
	1    4300 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 2100 4300 2150
Wire Wire Line
	4600 2100 4700 2100
Wire Wire Line
	4700 2100 4700 1800
Wire Wire Line
	4700 1800 4200 1800
Wire Wire Line
	4200 1800 4200 2150
Wire Wire Line
	4200 2150 4300 2150
Connection ~ 4300 2150
$Comp
L Connector:Screw_Terminal_01x02 BATin1
U 1 1 5E9E5C1C
P 4400 2350
F 0 "BATin1" V 4364 2162 50  0000 R CNN
F 1 "Screw_Terminal_01x02" V 4350 3300 50  0001 R CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 4400 2350 50  0001 C CNN
F 3 "~" H 4400 2350 50  0001 C CNN
	1    4400 2350
	0    -1   -1   0   
$EndComp
$Comp
L power:Earth #PWR0102
U 1 1 5E9E6D05
P 4400 2600
F 0 "#PWR0102" H 4400 2350 50  0001 C CNN
F 1 "Earth" H 4400 2450 50  0001 C CNN
F 2 "" H 4400 2600 50  0001 C CNN
F 3 "~" H 4400 2600 50  0001 C CNN
	1    4400 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	4400 2550 4400 2600
$Comp
L Regulator_Linear:LM7805_TO220 LM7805
U 1 1 5E9E75E9
P 4800 2750
F 0 "LM7805" H 4800 2992 50  0000 C CNN
F 1 "LM7805_TO220" H 4800 2901 50  0000 C CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 4800 2975 50  0001 C CIN
F 3 "http://www.fairchildsemi.com/ds/LM/LM7805.pdf" H 4800 2700 50  0001 C CNN
	1    4800 2750
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5E9E8FE4
P 5250 2950
F 0 "R1" H 5320 2996 50  0000 L CNN
F 1 "270K" H 5300 3100 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 5180 2950 50  0001 C CNN
F 3 "~" H 5250 2950 50  0001 C CNN
	1    5250 2950
	1    0    0    -1  
$EndComp
$Comp
L Device:C C1
U 1 1 5E9E9735
P 4650 3150
F 0 "C1" H 4765 3196 50  0000 L CNN
F 1 "330nF" H 4765 3105 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 4688 3000 50  0001 C CNN
F 3 "~" H 4650 3150 50  0001 C CNN
	1    4650 3150
	0    1    1    0   
$EndComp
$Comp
L Amplifier_Operational:OP07 op1
U 1 1 5E9EA082
P 7800 2850
F 0 "op1" H 7950 3100 50  0000 L CNN
F 1 "OP07" H 7950 3000 50  0000 L CNN
F 2 "Package_DIP:DIP-8_W7.62mm" H 7850 2900 50  0001 C CNN
F 3 "https://www.analog.com/media/en/technical-documentation/data-sheets/OP07.pdf" H 7850 3000 50  0001 C CNN
	1    7800 2850
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT RV1
U 1 1 5E9EA848
P 5450 4100
F 0 "RV1" H 5381 4146 50  0000 R CNN
F 1 "R_POT" H 5381 4055 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_ACP_CA14-H5_Horizontal" H 5450 4100 50  0001 C CNN
F 3 "~" H 5450 4100 50  0001 C CNN
	1    5450 4100
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED LED1
U 1 1 5E9EAEE0
P 7450 3600
F 0 "LED1" H 7450 3500 50  0000 C CNN
F 1 "LED" H 7450 3400 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm" H 7450 3600 50  0001 C CNN
F 3 "~" H 7450 3600 50  0001 C CNN
	1    7450 3600
	0    -1   -1   0   
$EndComp
$Comp
L pspice:DIODE D1
U 1 1 5E9E51EC
P 8400 2850
F 0 "D1" V 8354 2978 50  0000 L CNN
F 1 "DIODE" V 8445 2978 50  0000 L CNN
F 2 "Diode_THT:D_A-405_P12.70mm_Horizontal" H 8400 2850 50  0001 C CNN
F 3 "~" H 8400 2850 50  0001 C CNN
	1    8400 2850
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 2550 4500 2750
Wire Wire Line
	4500 2750 4500 3150
Connection ~ 4500 2750
Wire Wire Line
	4800 3150 4800 3050
$Comp
L Device:C C2
U 1 1 5E9EAF6F
P 4950 3150
F 0 "C2" H 5065 3196 50  0000 L CNN
F 1 "100nF" H 5065 3105 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 4988 3000 50  0001 C CNN
F 3 "~" H 4950 3150 50  0001 C CNN
	1    4950 3150
	0    1    1    0   
$EndComp
Connection ~ 4800 3150
$Comp
L power:Earth #PWR0103
U 1 1 5E9EB611
P 4800 3200
F 0 "#PWR0103" H 4800 2950 50  0001 C CNN
F 1 "Earth" H 4800 3050 50  0001 C CNN
F 2 "" H 4800 3200 50  0001 C CNN
F 3 "~" H 4800 3200 50  0001 C CNN
	1    4800 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4800 3150 4800 3200
Wire Wire Line
	5100 2750 5100 3150
Wire Wire Line
	5100 2750 5250 2750
Wire Wire Line
	5250 2750 5250 2800
Connection ~ 5100 2750
$Comp
L power:Earth #PWR0104
U 1 1 5E9ECB81
P 5250 3200
F 0 "#PWR0104" H 5250 2950 50  0001 C CNN
F 1 "Earth" H 5250 3050 50  0001 C CNN
F 2 "" H 5250 3200 50  0001 C CNN
F 3 "~" H 5250 3200 50  0001 C CNN
	1    5250 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5250 3100 5250 3200
$Comp
L Device:C C3
U 1 1 5E9EDB4A
P 7200 3800
F 0 "C3" H 7315 3846 50  0000 L CNN
F 1 "100nF" H 7250 3700 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 7238 3650 50  0001 C CNN
F 3 "~" H 7200 3800 50  0001 C CNN
	1    7200 3800
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 5E9F03A1
P 4800 4100
F 0 "R2" H 4870 4146 50  0000 L CNN
F 1 "82K" H 4870 4055 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4730 4100 50  0001 C CNN
F 3 "~" H 4800 4100 50  0001 C CNN
	1    4800 4100
	0    1    1    0   
$EndComp
Connection ~ 4500 3150
$Comp
L power:Earth #PWR0105
U 1 1 5E9F166F
P 6350 4100
F 0 "#PWR0105" H 6350 3850 50  0001 C CNN
F 1 "Earth" H 6350 3950 50  0001 C CNN
F 2 "" H 6350 4100 50  0001 C CNN
F 3 "~" H 6350 4100 50  0001 C CNN
	1    6350 4100
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 PANEL1
U 1 1 5E9F9816
P 7600 2250
F 0 "PANEL1" V 7564 2062 50  0000 R CNN
F 1 "Screw_Terminal_01x02" V 7550 3200 50  0001 R CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 7600 2250 50  0001 C CNN
F 3 "~" H 7600 2250 50  0001 C CNN
	1    7600 2250
	0    -1   -1   0   
$EndComp
$Comp
L power:Earth #PWR0107
U 1 1 5E9FBB4D
P 7550 2450
F 0 "#PWR0107" H 7550 2200 50  0001 C CNN
F 1 "Earth" H 7550 2300 50  0001 C CNN
F 2 "" H 7550 2450 50  0001 C CNN
F 3 "~" H 7550 2450 50  0001 C CNN
	1    7550 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	7600 2450 7550 2450
Wire Wire Line
	4500 2100 4500 2200
Wire Wire Line
	4500 2200 4600 2200
Wire Wire Line
	4600 2200 4600 2550
Wire Wire Line
	4600 2550 4500 2550
Connection ~ 4500 2100
Connection ~ 4500 2550
Wire Wire Line
	8100 2850 8200 2850
Wire Wire Line
	8600 2850 8600 2150
Wire Wire Line
	4600 2150 4600 2200
Connection ~ 4600 2200
$Comp
L Transistor_BJT:2N3904 Q1
U 1 1 5EBEE765
P 7350 3200
F 0 "Q1" H 7540 3246 50  0000 L CNN
F 1 "2N3904" H 7540 3155 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 7550 3125 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/2N/2N3904.pdf" H 7350 3200 50  0001 L CNN
	1    7350 3200
	1    0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 5EBF2660
P 7450 2550
F 0 "R3" H 7520 2596 50  0000 L CNN
F 1 "220" H 7520 2505 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 7380 2550 50  0001 C CNN
F 3 "~" H 7450 2550 50  0001 C CNN
	1    7450 2550
	-1   0    0    1   
$EndComp
Wire Wire Line
	7700 2450 7700 2500
Wire Wire Line
	7700 2500 7800 2500
Wire Wire Line
	7800 2500 7800 2100
Wire Wire Line
	7800 2100 7450 2100
Wire Wire Line
	7450 2100 7450 2400
Connection ~ 7700 2500
Wire Wire Line
	7700 2500 7700 2550
Wire Wire Line
	7450 2700 7450 3000
Wire Wire Line
	7450 3400 7450 3450
Wire Wire Line
	4500 4100 4650 4100
Wire Wire Line
	4500 3150 4500 4100
Wire Wire Line
	4950 4100 5300 4100
Wire Wire Line
	5600 4100 6350 4100
Wire Wire Line
	5450 3800 5450 3950
Wire Wire Line
	7350 3800 7450 3800
Wire Wire Line
	7450 3800 7450 3750
Wire Wire Line
	7700 3150 7700 3800
Wire Wire Line
	7450 3800 7700 3800
Connection ~ 7450 3800
Connection ~ 7700 3800
Wire Wire Line
	7700 3800 7700 4100
$Comp
L Device:R R4
U 1 1 5EBEB6D4
P 6950 3200
F 0 "R4" H 7000 3200 50  0000 L CNN
F 1 "220" H 7000 3100 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 6880 3200 50  0001 C CNN
F 3 "~" H 6950 3200 50  0001 C CNN
	1    6950 3200
	0    1    1    0   
$EndComp
$Comp
L pspice:DIODE D5
U 1 1 5ECF23A4
P 6550 3200
F 0 "D5" V 6504 3328 50  0000 L CNN
F 1 "DIODE" V 6595 3328 50  0000 L CNN
F 2 "Diode_THT:D_A-405_P12.70mm_Horizontal" H 6550 3200 50  0001 C CNN
F 3 "~" H 6550 3200 50  0001 C CNN
	1    6550 3200
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D4
U 1 1 5ECFBDFE
P 6100 3200
F 0 "D4" V 6054 3328 50  0000 L CNN
F 1 "DIODE" V 6145 3328 50  0000 L CNN
F 2 "Diode_THT:D_A-405_P12.70mm_Horizontal" H 6100 3200 50  0001 C CNN
F 3 "~" H 6100 3200 50  0001 C CNN
	1    6100 3200
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D3
U 1 1 5ECFC15C
P 5650 3200
F 0 "D3" V 5604 3328 50  0000 L CNN
F 1 "DIODE" V 5695 3328 50  0000 L CNN
F 2 "Diode_THT:D_A-405_P12.70mm_Horizontal" H 5650 3200 50  0001 C CNN
F 3 "~" H 5650 3200 50  0001 C CNN
	1    5650 3200
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D2
U 1 1 5ECFE728
P 5450 3500
F 0 "D2" V 5404 3628 50  0000 L CNN
F 1 "DIODE" V 5495 3628 50  0000 L CNN
F 2 "Diode_THT:D_A-405_P12.70mm_Horizontal" H 5450 3500 50  0001 C CNN
F 3 "~" H 5450 3500 50  0001 C CNN
	1    5450 3500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5450 3800 7050 3800
Wire Wire Line
	5450 3800 5450 3700
Connection ~ 5450 3800
Wire Wire Line
	5450 3300 5450 3200
Wire Wire Line
	5250 2750 7500 2750
Connection ~ 5250 2750
Wire Wire Line
	4600 2150 8600 2150
Wire Wire Line
	7700 4100 6350 4100
Connection ~ 6350 4100
Wire Wire Line
	5850 3200 5900 3200
Wire Wire Line
	6300 3200 6350 3200
Wire Wire Line
	6750 3200 6800 3200
Wire Wire Line
	7100 3200 7150 3200
$EndSCHEMATC
