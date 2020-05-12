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
P 1000 1650
F 0 "uC_Propulsion1" H 1100 1450 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 918 1416 50  0001 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 1000 1650 50  0001 C CNN
F 3 "~" H 1000 1650 50  0001 C CNN
	1    1000 1650
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 Bateria1
U 1 1 5E7FBF26
P 5700 3700
F 0 "Bateria1" H 5700 3500 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 5618 3466 50  0001 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 5700 3700 50  0001 C CNN
F 3 "~" H 5700 3700 50  0001 C CNN
	1    5700 3700
	1    0    0    -1  
$EndComp
$Comp
L Device:Fuse F1
U 1 1 5E8E5D3E
P 5250 3700
F 0 "F1" V 5053 3700 50  0000 C CNN
F 1 "Fuse" V 5144 3700 50  0000 C CNN
F 2 "Fuse:Fuse_Blade_Mini_directSolder" V 5180 3700 50  0001 C CNN
F 3 "~" H 5250 3700 50  0001 C CNN
	1    5250 3700
	0    1    1    0   
$EndComp
Wire Wire Line
	5400 3700 5500 3700
$Comp
L Transistor_FET:IRF9540N Q1
U 1 1 5E9D0354
P 2400 1100
F 0 "Q1" H 2604 1054 50  0000 L CNN
F 1 "IRF9540N" H 2604 1145 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 2600 1025 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf9540n.pdf" H 2400 1100 50  0001 L CNN
	1    2400 1100
	1    0    0    1   
$EndComp
$Comp
L Transistor_FET:IRF540N Q2
U 1 1 5E9D2967
P 2400 2100
F 0 "Q2" H 2604 2146 50  0000 L CNN
F 1 "IRF540N" H 2604 2055 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 2650 2025 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 2400 2100 50  0001 L CNN
	1    2400 2100
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 Motor_Propulsion1
U 1 1 5E9D5504
P 3050 1800
F 0 "Motor_Propulsion1" V 2800 1750 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2968 1566 50  0001 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 3050 1800 50  0001 C CNN
F 3 "~" H 3050 1800 50  0001 C CNN
	1    3050 1800
	0    1    1    0   
$EndComp
$Comp
L Transistor_BJT:2N2219 Q1A1
U 1 1 5E9D9A09
P 1950 1300
F 0 "Q1A1" H 2140 1346 50  0000 L CNN
F 1 "2N2219" H 2140 1255 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline_Wide" H 2150 1225 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF" H 1950 1300 50  0001 L CNN
	1    1950 1300
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 1100 2200 1100
$Comp
L Transistor_BJT:2N2219 Q2A1
U 1 1 5E9DCBA8
P 1950 1900
F 0 "Q2A1" H 2140 1946 50  0000 L CNN
F 1 "2N2219" H 2140 1855 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline_Wide" H 2150 1825 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF" H 1950 1900 50  0001 L CNN
	1    1950 1900
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 1300 2500 1600
Wire Wire Line
	2200 2100 2050 2100
$Comp
L Device:R R3
U 1 1 5E9DEC23
P 2050 900
F 0 "R3" H 2120 946 50  0000 L CNN
F 1 "R" H 2120 855 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1980 900 50  0001 C CNN
F 3 "~" H 2050 900 50  0001 C CNN
	1    2050 900 
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 1050 2050 1100
Connection ~ 2050 1100
$Comp
L Device:R R4
U 1 1 5E9DFAB9
P 2050 2300
F 0 "R4" H 2120 2346 50  0000 L CNN
F 1 "R" H 2120 2255 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1980 2300 50  0001 C CNN
F 3 "~" H 2050 2300 50  0001 C CNN
	1    2050 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 2100 2050 2150
Connection ~ 2050 2100
Wire Wire Line
	2050 1500 2050 1550
$Comp
L power:Earth #PWR0101
U 1 1 5E9DC5BA
P 2050 1550
F 0 "#PWR0101" H 2050 1300 50  0001 C CNN
F 1 "Earth" H 2050 1400 50  0001 C CNN
F 2 "" H 2050 1550 50  0001 C CNN
F 3 "~" H 2050 1550 50  0001 C CNN
	1    2050 1550
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:IRF9540N Q3
U 1 1 5E9EE782
P 3550 1100
F 0 "Q3" H 3755 1054 50  0000 L CNN
F 1 "IRF9540N" H 3755 1145 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 3750 1025 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf9540n.pdf" H 3550 1100 50  0001 L CNN
	1    3550 1100
	-1   0    0    1   
$EndComp
$Comp
L Transistor_FET:IRF540N Q4
U 1 1 5E9EE788
P 3550 2100
F 0 "Q4" H 3755 2146 50  0000 L CNN
F 1 "IRF540N" H 3755 2055 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 3800 2025 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 3550 2100 50  0001 L CNN
	1    3550 2100
	-1   0    0    -1  
$EndComp
$Comp
L Transistor_BJT:2N2219 Q3A1
U 1 1 5E9EE78E
P 4000 1300
F 0 "Q3A1" H 4191 1346 50  0000 L CNN
F 1 "2N2219" H 4191 1255 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline_Wide" H 4200 1225 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF" H 4000 1300 50  0001 L CNN
	1    4000 1300
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3900 1100 3750 1100
$Comp
L Transistor_BJT:2N2219 Q4A1
U 1 1 5E9EE795
P 4000 1900
F 0 "Q4A1" H 4191 1946 50  0000 L CNN
F 1 "2N2219" H 4191 1855 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline_Wide" H 4200 1825 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF" H 4000 1900 50  0001 L CNN
	1    4000 1900
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3450 1300 3450 1600
Wire Wire Line
	3750 2100 3900 2100
$Comp
L Device:R R5
U 1 1 5E9EE79D
P 3900 900
F 0 "R5" H 3830 946 50  0000 R CNN
F 1 "R" H 3830 855 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 3830 900 50  0001 C CNN
F 3 "~" H 3900 900 50  0001 C CNN
	1    3900 900 
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3900 1050 3900 1100
Connection ~ 3900 1100
$Comp
L Device:R R6
U 1 1 5E9EE7A5
P 3900 2300
F 0 "R6" H 3830 2346 50  0000 R CNN
F 1 "R" H 3830 2255 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 3830 2300 50  0001 C CNN
F 3 "~" H 3900 2300 50  0001 C CNN
	1    3900 2300
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3900 2100 3900 2150
Connection ~ 3900 2100
Wire Wire Line
	3900 1500 3900 1550
$Comp
L power:Earth #PWR0102
U 1 1 5E9EE7AE
P 3900 1550
F 0 "#PWR0102" H 3900 1300 50  0001 C CNN
F 1 "Earth" H 3900 1400 50  0001 C CNN
F 2 "" H 3900 1550 50  0001 C CNN
F 3 "~" H 3900 1550 50  0001 C CNN
	1    3900 1550
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2500 1600 2950 1600
Connection ~ 2500 1600
Wire Wire Line
	2500 1600 2500 1900
Wire Wire Line
	3050 1600 3450 1600
Connection ~ 3450 1600
Wire Wire Line
	3450 1600 3450 1900
Wire Wire Line
	3450 2300 2950 2300
Wire Wire Line
	2500 900  2950 900 
$Comp
L power:Earth #PWR0103
U 1 1 5E9EFCCD
P 2950 2450
F 0 "#PWR0103" H 2950 2200 50  0001 C CNN
F 1 "Earth" H 2950 2300 50  0001 C CNN
F 2 "" H 2950 2450 50  0001 C CNN
F 3 "~" H 2950 2450 50  0001 C CNN
	1    2950 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2950 2300 2950 2450
Connection ~ 2950 2300
Wire Wire Line
	2950 2300 2500 2300
Wire Wire Line
	3900 2450 2950 2450
Connection ~ 2950 2450
Wire Wire Line
	2050 2450 2950 2450
Wire Wire Line
	2950 750  2950 900 
Connection ~ 2950 900 
Wire Wire Line
	2950 900  3450 900 
Wire Wire Line
	3900 750  2950 750 
Connection ~ 2950 750 
Wire Wire Line
	2050 1700 1700 1700
Wire Wire Line
	1700 1700 1700 750 
Wire Wire Line
	1700 750  2050 750 
Wire Wire Line
	2050 750  2950 750 
Connection ~ 2050 750 
Wire Wire Line
	3900 1700 4300 1700
Wire Wire Line
	4300 1700 4300 750 
Wire Wire Line
	4300 750  3900 750 
Connection ~ 3900 750 
$Comp
L Device:R R1
U 1 1 5E9F4322
P 1500 1300
F 0 "R1" V 1293 1300 50  0000 C CNN
F 1 "R" V 1384 1300 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1430 1300 50  0001 C CNN
F 3 "~" H 1500 1300 50  0001 C CNN
	1    1500 1300
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 5E9F4861
P 1500 1900
F 0 "R2" V 1293 1900 50  0000 C CNN
F 1 "R" V 1384 1900 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1430 1900 50  0001 C CNN
F 3 "~" H 1500 1900 50  0001 C CNN
	1    1500 1900
	0    1    1    0   
$EndComp
$Comp
L Device:R R7
U 1 1 5E9F4CEB
P 4500 1300
F 0 "R7" V 4293 1300 50  0000 C CNN
F 1 "R" V 4384 1300 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4430 1300 50  0001 C CNN
F 3 "~" H 4500 1300 50  0001 C CNN
	1    4500 1300
	0    1    1    0   
$EndComp
$Comp
L Device:R R8
U 1 1 5E9F50A4
P 4500 1900
F 0 "R8" V 4293 1900 50  0000 C CNN
F 1 "R" V 4384 1900 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4430 1900 50  0001 C CNN
F 3 "~" H 4500 1900 50  0001 C CNN
	1    4500 1900
	0    1    1    0   
$EndComp
Wire Wire Line
	4200 1900 4350 1900
Wire Wire Line
	4200 1300 4350 1300
Wire Wire Line
	1750 1300 1650 1300
Wire Wire Line
	1750 1900 1650 1900
Wire Wire Line
	1200 1550 1250 1550
Wire Wire Line
	1350 1550 1350 1300
Connection ~ 1250 1550
Wire Wire Line
	1250 1550 1350 1550
Wire Wire Line
	1200 1650 1350 1650
Wire Wire Line
	1350 1650 1350 1900
Wire Wire Line
	1250 2700 4650 2700
Wire Wire Line
	1250 1550 1250 2700
Wire Wire Line
	4650 1900 4650 2700
Wire Wire Line
	1350 1900 1350 2600
Wire Wire Line
	1350 2600 4700 2600
Wire Wire Line
	4700 2600 4700 1300
Wire Wire Line
	4700 1300 4650 1300
Connection ~ 1350 1900
$Comp
L Connector:Screw_Terminal_01x02 uC_Cangilon1
U 1 1 5EA1814D
P 1000 3800
F 0 "uC_Cangilon1" H 1100 3600 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 918 3566 50  0001 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 1000 3800 50  0001 C CNN
F 3 "~" H 1000 3800 50  0001 C CNN
	1    1000 3800
	-1   0    0    1   
$EndComp
$Comp
L Transistor_FET:IRF9540N Q5
U 1 1 5EA18153
P 2400 3250
F 0 "Q5" H 2604 3204 50  0000 L CNN
F 1 "IRF9540N" H 2604 3295 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 2600 3175 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf9540n.pdf" H 2400 3250 50  0001 L CNN
	1    2400 3250
	1    0    0    1   
$EndComp
$Comp
L Transistor_FET:IRF540N Q6
U 1 1 5EA18159
P 2400 4250
F 0 "Q6" H 2604 4296 50  0000 L CNN
F 1 "IRF540N" H 2604 4205 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 2650 4175 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 2400 4250 50  0001 L CNN
	1    2400 4250
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 Motor_Cangilon1
U 1 1 5EA1815F
P 3050 3950
F 0 "Motor_Cangilon1" V 2800 3900 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2968 3716 50  0001 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 3050 3950 50  0001 C CNN
F 3 "~" H 3050 3950 50  0001 C CNN
	1    3050 3950
	0    1    1    0   
$EndComp
$Comp
L Transistor_BJT:2N2219 Q5A1
U 1 1 5EA18165
P 1950 3450
F 0 "Q5A1" H 2140 3496 50  0000 L CNN
F 1 "2N2219" H 2140 3405 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline_Wide" H 2150 3375 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF" H 1950 3450 50  0001 L CNN
	1    1950 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 3250 2200 3250
$Comp
L Transistor_BJT:2N2219 Q6A1
U 1 1 5EA1816C
P 1950 4050
F 0 "Q6A1" H 2140 4096 50  0000 L CNN
F 1 "2N2219" H 2140 4005 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline_Wide" H 2150 3975 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF" H 1950 4050 50  0001 L CNN
	1    1950 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 3450 2500 3750
Wire Wire Line
	2200 4250 2050 4250
$Comp
L Device:R R11
U 1 1 5EA18174
P 2050 3050
F 0 "R11" H 2120 3096 50  0000 L CNN
F 1 "R" H 2120 3005 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1980 3050 50  0001 C CNN
F 3 "~" H 2050 3050 50  0001 C CNN
	1    2050 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 3200 2050 3250
Connection ~ 2050 3250
$Comp
L Device:R R12
U 1 1 5EA1817C
P 2050 4450
F 0 "R12" H 2120 4496 50  0000 L CNN
F 1 "R" H 2120 4405 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1980 4450 50  0001 C CNN
F 3 "~" H 2050 4450 50  0001 C CNN
	1    2050 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 4250 2050 4300
Connection ~ 2050 4250
Wire Wire Line
	2050 3650 2050 3700
$Comp
L power:Earth #PWR0104
U 1 1 5EA18185
P 2050 3700
F 0 "#PWR0104" H 2050 3450 50  0001 C CNN
F 1 "Earth" H 2050 3550 50  0001 C CNN
F 2 "" H 2050 3700 50  0001 C CNN
F 3 "~" H 2050 3700 50  0001 C CNN
	1    2050 3700
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:IRF9540N Q7
U 1 1 5EA1818B
P 3550 3250
F 0 "Q7" H 3755 3204 50  0000 L CNN
F 1 "IRF9540N" H 3755 3295 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 3750 3175 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf9540n.pdf" H 3550 3250 50  0001 L CNN
	1    3550 3250
	-1   0    0    1   
$EndComp
$Comp
L Transistor_FET:IRF540N Q8
U 1 1 5EA18191
P 3550 4250
F 0 "Q8" H 3755 4296 50  0000 L CNN
F 1 "IRF540N" H 3755 4205 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 3800 4175 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 3550 4250 50  0001 L CNN
	1    3550 4250
	-1   0    0    -1  
$EndComp
$Comp
L Transistor_BJT:2N2219 Q7A1
U 1 1 5EA18197
P 4000 3450
F 0 "Q7A1" H 4191 3496 50  0000 L CNN
F 1 "2N2219" H 4191 3405 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline_Wide" H 4200 3375 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF" H 4000 3450 50  0001 L CNN
	1    4000 3450
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3900 3250 3750 3250
$Comp
L Transistor_BJT:2N2219 Q8A1
U 1 1 5EA1819E
P 4000 4050
F 0 "Q8A1" H 4191 4096 50  0000 L CNN
F 1 "2N2219" H 4191 4005 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline_Wide" H 4200 3975 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF" H 4000 4050 50  0001 L CNN
	1    4000 4050
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3450 3450 3450 3750
Wire Wire Line
	3750 4250 3900 4250
$Comp
L Device:R R13
U 1 1 5EA181A6
P 3900 3050
F 0 "R13" H 3830 3096 50  0000 R CNN
F 1 "R" H 3830 3005 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 3830 3050 50  0001 C CNN
F 3 "~" H 3900 3050 50  0001 C CNN
	1    3900 3050
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3900 3200 3900 3250
Connection ~ 3900 3250
$Comp
L Device:R R14
U 1 1 5EA181AE
P 3900 4450
F 0 "R14" H 3830 4496 50  0000 R CNN
F 1 "R" H 3830 4405 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 3830 4450 50  0001 C CNN
F 3 "~" H 3900 4450 50  0001 C CNN
	1    3900 4450
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3900 4250 3900 4300
Connection ~ 3900 4250
Wire Wire Line
	3900 3650 3900 3700
$Comp
L power:Earth #PWR0105
U 1 1 5EA181B7
P 3900 3700
F 0 "#PWR0105" H 3900 3450 50  0001 C CNN
F 1 "Earth" H 3900 3550 50  0001 C CNN
F 2 "" H 3900 3700 50  0001 C CNN
F 3 "~" H 3900 3700 50  0001 C CNN
	1    3900 3700
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2500 3750 2950 3750
Connection ~ 2500 3750
Wire Wire Line
	2500 3750 2500 4050
Wire Wire Line
	3050 3750 3450 3750
Connection ~ 3450 3750
Wire Wire Line
	3450 3750 3450 4050
Wire Wire Line
	3450 4450 2950 4450
Wire Wire Line
	2500 3050 2950 3050
$Comp
L power:Earth #PWR0106
U 1 1 5EA181C5
P 2950 4600
F 0 "#PWR0106" H 2950 4350 50  0001 C CNN
F 1 "Earth" H 2950 4450 50  0001 C CNN
F 2 "" H 2950 4600 50  0001 C CNN
F 3 "~" H 2950 4600 50  0001 C CNN
	1    2950 4600
	1    0    0    -1  
$EndComp
Wire Wire Line
	2950 4450 2950 4600
Connection ~ 2950 4450
Wire Wire Line
	2950 4450 2500 4450
Wire Wire Line
	3900 4600 2950 4600
Connection ~ 2950 4600
Wire Wire Line
	2050 4600 2950 4600
Wire Wire Line
	2950 2900 2950 3050
Connection ~ 2950 3050
Wire Wire Line
	2950 3050 3450 3050
Wire Wire Line
	3900 2900 2950 2900
Connection ~ 2950 2900
Wire Wire Line
	2050 3850 1700 3850
Wire Wire Line
	1700 3850 1700 2900
Wire Wire Line
	1700 2900 2050 2900
Wire Wire Line
	2050 2900 2950 2900
Connection ~ 2050 2900
Wire Wire Line
	3900 3850 4300 3850
Wire Wire Line
	4300 3850 4300 2900
Wire Wire Line
	4300 2900 3900 2900
Connection ~ 3900 2900
$Comp
L Device:R R9
U 1 1 5EA181DF
P 1500 3450
F 0 "R9" V 1293 3450 50  0000 C CNN
F 1 "R" V 1384 3450 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1430 3450 50  0001 C CNN
F 3 "~" H 1500 3450 50  0001 C CNN
	1    1500 3450
	0    1    1    0   
$EndComp
$Comp
L Device:R R10
U 1 1 5EA181E5
P 1500 4050
F 0 "R10" V 1293 4050 50  0000 C CNN
F 1 "R" V 1384 4050 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1430 4050 50  0001 C CNN
F 3 "~" H 1500 4050 50  0001 C CNN
	1    1500 4050
	0    1    1    0   
$EndComp
$Comp
L Device:R R15
U 1 1 5EA181EB
P 4500 3450
F 0 "R15" V 4293 3450 50  0000 C CNN
F 1 "R" V 4384 3450 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4430 3450 50  0001 C CNN
F 3 "~" H 4500 3450 50  0001 C CNN
	1    4500 3450
	0    1    1    0   
$EndComp
$Comp
L Device:R R16
U 1 1 5EA181F1
P 4500 4050
F 0 "R16" V 4293 4050 50  0000 C CNN
F 1 "R" V 4384 4050 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4430 4050 50  0001 C CNN
F 3 "~" H 4500 4050 50  0001 C CNN
	1    4500 4050
	0    1    1    0   
$EndComp
Wire Wire Line
	4200 4050 4350 4050
Wire Wire Line
	4200 3450 4350 3450
Wire Wire Line
	1750 3450 1650 3450
Wire Wire Line
	1750 4050 1650 4050
Wire Wire Line
	1200 3700 1250 3700
Wire Wire Line
	1350 3700 1350 3450
Connection ~ 1250 3700
Wire Wire Line
	1250 3700 1350 3700
Wire Wire Line
	1200 3800 1350 3800
Wire Wire Line
	1350 3800 1350 4050
Wire Wire Line
	1250 4850 4650 4850
Wire Wire Line
	1250 3700 1250 4850
Wire Wire Line
	4650 4050 4650 4850
Wire Wire Line
	1350 4050 1350 4750
Wire Wire Line
	1350 4750 4700 4750
Wire Wire Line
	4700 4750 4700 3450
Wire Wire Line
	4700 3450 4650 3450
Connection ~ 1350 4050
$Comp
L Transistor_Array:ULN2003 U1
U 1 1 5E9A62F3
P 2950 5450
F 0 "U1" H 2500 5950 50  0000 C CNN
F 1 "ULN2003" H 2450 5850 50  0000 C CNN
F 2 "Package_DIP:DIP-14_W10.16mm" H 3000 4900 50  0001 L CNN
F 3 "http://www.ti.com/lit/ds/symlink/uln2003a.pdf" H 3050 5250 50  0001 C CNN
	1    2950 5450
	1    0    0    -1  
$EndComp
Wire Wire Line
	5100 3700 5050 3700
Wire Wire Line
	5050 3700 5050 700 
Wire Wire Line
	5050 700  2950 700 
Wire Wire Line
	2950 700  2950 750 
Wire Wire Line
	5050 3700 4900 3700
Wire Wire Line
	4900 3700 4900 2800
Wire Wire Line
	4900 2800 2950 2800
Wire Wire Line
	2950 2800 2950 2900
Connection ~ 5050 3700
$Comp
L power:Earth #PWR0107
U 1 1 5E9A9A4B
P 2950 6100
F 0 "#PWR0107" H 2950 5850 50  0001 C CNN
F 1 "Earth" H 2950 5950 50  0001 C CNN
F 2 "" H 2950 6100 50  0001 C CNN
F 3 "~" H 2950 6100 50  0001 C CNN
	1    2950 6100
	1    0    0    -1  
$EndComp
Wire Wire Line
	2950 6050 2950 6100
Wire Wire Line
	5050 3700 5050 5050
Wire Wire Line
	5050 5050 3350 5050
$Comp
L Connector:Screw_Terminal_01x04 Motor_Direccion1
U 1 1 5E9B4600
P 4650 5350
F 0 "Motor_Direccion1" H 4300 5550 50  0000 L CNN
F 1 "Screw_Terminal_01x04" H 4730 5251 50  0001 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-04A_1x04_P2.54mm_Vertical" H 4650 5350 50  0001 C CNN
F 3 "~" H 4650 5350 50  0001 C CNN
	1    4650 5350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1250 5250 2550 5250
Wire Wire Line
	1250 5350 2550 5350
Wire Wire Line
	1250 5450 2550 5450
Wire Wire Line
	1250 5550 2550 5550
Wire Wire Line
	3350 5250 4450 5250
Wire Wire Line
	3350 5350 4450 5350
Wire Wire Line
	3350 5450 4450 5450
Wire Wire Line
	3350 5550 4450 5550
$Comp
L Connector:Screw_Terminal_01x05 uC_Direccion1
U 1 1 5E9D6D91
P 1050 5450
F 0 "uC_Direccion1" H 968 5775 50  0000 C CNN
F 1 "Screw_Terminal_01x05" H 968 5776 50  0001 C CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical" H 1050 5450 50  0001 C CNN
F 3 "~" H 1050 5450 50  0001 C CNN
	1    1050 5450
	-1   0    0    -1  
$EndComp
Wire Wire Line
	1250 5650 1450 5650
Wire Wire Line
	1450 5650 1450 6050
Wire Wire Line
	1450 6050 2950 6050
Connection ~ 2950 6050
$Comp
L power:Earth #PWR0108
U 1 1 5EA83A93
P 5500 3850
F 0 "#PWR0108" H 5500 3600 50  0001 C CNN
F 1 "Earth" H 5500 3700 50  0001 C CNN
F 2 "" H 5500 3850 50  0001 C CNN
F 3 "~" H 5500 3850 50  0001 C CNN
	1    5500 3850
	1    0    0    -1  
$EndComp
Wire Wire Line
	5500 3800 5500 3850
$Comp
L Device:C C1
U 1 1 5E9ED93B
P 5050 5450
F 0 "C1" H 5165 5496 50  0000 L CNN
F 1 "C" H 5165 5405 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 5165 5359 50  0001 L CNN
F 3 "~" H 5050 5450 50  0001 C CNN
	1    5050 5450
	1    0    0    -1  
$EndComp
Wire Wire Line
	5050 5050 5050 5300
Connection ~ 5050 5050
Wire Wire Line
	5050 5600 5050 6050
Wire Wire Line
	5050 6050 2950 6050
$EndSCHEMATC
