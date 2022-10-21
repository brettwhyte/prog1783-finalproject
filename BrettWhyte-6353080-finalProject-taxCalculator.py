# "Canadian Income Tax Calculator" for IT Support Programming Fundamentals
# Name:             Brett-Whyte-6353080-finalProject-taxCalculator.py
# Author:           Brett Whyte
# Date Created:     Oct. 21, 2022
# Last Modified:    Oct. 21, 2022


'''
Pseudocode (rough copy)
-----------------------
1) Get user's province
2) Get user's salary
3) Check whether salary is annual, monthly, bi-weekly, weekly, hourly
4) Convert salary to annual
5) Calculate federal tax
6) Calculate provincial tax
7) Calculate EI contribution
8) Convert salary back to original entry
9) Show all taxes, and the difference (take home salary)
-----------------------
'''

# Purpose:
#
# Tax Calculator app that calculates the basic tax rate in your region.
# would like to add in functionality at some point to enter deductable items


print("------------------------------------------------")
print("-------------- Pick Your Province --------------")
print("------------------------------------------------")
print("")
print("              1. Ontario")
print("              2. Quebec")
print("              3. Nova Scotia")
print("              4. New Brunswick")
print("              5. Manitoba")
print("              6. British Columbia")
print("              7. P.E.I.")
print("              8. Saskatchewan")
print("              9. Alberta")
print("             10. Newfoundland & Labrador")
print("             11. Northwest Territories")
print("             12. Yukon")
print("             13. Nunavut")
print("")
print("------------------------------------------------")
print("")

prov = int(input())


print("------------------------------------------------")
print("----------- Please Enter Your Salary -----------")
print("------------------------------------------------")
print("")

salary = float(input("$"))

print("")
print("------------------------------------------------")
print("")

print("------------------------------------------------")
print("------- How Often do you make this much? -------")
print("------------------------------------------------")
print("")
print("              1. Annually")
print("              2. Monthly")
print("              3. Bi-Weekly")
print("              4. Weekly")
print("              5. Hourly")
print("")
print("------------------------------------------------")
print("")

frequency = int(input())


# Calculating the annual salary

if frequency == 1:
    annualSal = salary
elif frequency == 2:
    annualSal = salary * 12
elif frequency == 3:
    annualSal = salary * 26
elif frequency == 4:
    annualSal = salary * 52
elif frequency == 5:
    annualSal = salary * 37.5 * 52

print("")
print("Salary before tax:      $", annualSal)
print("")


# Figures out the federal tax bracket
if annualSal <= 49020:
    fedBracket = 1
elif annualSal > 49020 and annualSal <= 98040:
    fedBracket = 2
elif annualSal > 98040 and annualSal <= 151978:
    fedBracket = 3
elif annualSal > 151978 and annualSal <= 216511:
    fedBracket = 4
elif annualSal > 216511:
    fedBracket = 5


# Figures out the federal tax payable
if annualSal <= 49020:
    fedTax = annualSal * 0.15
elif annualSal > 49020 and annualSal <= 98040:
    fedTax = annualSal * 0.205
elif annualSal > 98040 and annualSal <= 151978:
    fedTax = annualSal * 0.26
elif annualSal > 151978 and annualSal <= 216511:
    fedTax = annualSal * 0.29
elif annualSal > 216511:
    fedTax = annualSal * 0.33


# Functions for tax calculation based on province

# Calculate the Ontario tax payable
def onTax(annualSal):
    
    if annualSal < 45142:
        provTax = annualSal * 0.0505
        return provTax

    elif annualSal > 45142 and annualSal <= 90287:
        provTax = (((annualSal - 45142) * 0.0915) + (45142 * 0.0505))
        return provTax

    elif annualSal > 90287 and annualSal <= 150000:
        provTax = (((annualSal - 90287) * 0.1116) + (45145 * 0.0915) + (45142 * 0.0505))
        return provTax

    elif annualSal > 150000 and annualSal <= 220000:
        provTax = (((annualSal - 150000) * 0.1216) + (59713 * 0.1116) + (45145 * 0.0915) + (45142 * 0.0505))
        return provTax

    elif annualSal > 220000:
        provTax = (((annualSal - 220000) * 0.1316) + (70000 * 0.1216) + (59713 * 0.1116) + (45145 * 0.0915) + (45142 * 0.0505))
        return provTax


# Calculate the Quebec tax payable (I think this needs to be changed because of some weird Quebec tax expemtions or something?
#                                   Because this just seems like way too much tax...)
def qcTax(annualSal):
    
    if annualSal < 45142:
        provTax = annualSal * 0.0505
        return provTax

    elif annualSal > 45142 and annualSal <= 90287:
        provTax = (((annualSal - 45142) * 0.0915) + (45142 * 0.0505))
        return provTax

    elif annualSal > 90287 and annualSal <= 150000:
        provTax = (((annualSal - 90287) * 0.1116) + (45145 * 0.0915) + (45142 * 0.0505))
        return provTax

    elif annualSal > 150000 and annualSal <= 220000:
        provTax = (((annualSal - 150000) * 0.1216) + (59713 * 0.1116) + (45145 * 0.0915) + (45142 * 0.0505))
        return provTax

    elif annualSal > 220000:
        provTax = (((annualSal - 220000) * 0.1316) + (70000 * 0.1216) + (59713 * 0.1116) + (45145 * 0.0915) + (45142 * 0.0505))
        return provTax


# Calculate the Nova Scotia tax payable
def nsTax(annualSal):
    
    if annualSal < 29590:
        provTax = annualSal * 0.0879
        return provTax

    elif annualSal > 29590 and annualSal <= 59180:
        provTax = (((annualSal - 29590) * 0.1495) + (29590 * 0.0879))
        return provTax

    elif annualSal > 59180 and annualSal <= 93000:
        provTax = (((annualSal - 59180) * 0.1667) + (29590 * 0.1495) + (29590 * 0.0879))
        return provTax

    elif annualSal > 93000 and annualSal <= 150000:
        provTax = (((annualSal - 93000) * 0.175) + (33820 * 0.1667) + (29590 * 0.1495) + (29590 * 0.0879))
        return provTax

    elif annualSal > 150000:
        provTax = (((annualSal - 150000) * 0.21) + (57000 * 0.175) + (33820 * 0.1667) + (29590 * 0.1495) + (29590 * 0.0879))
        return provTax


# Calculate the New Brunswick tax payable
def nbTax(annualSal):
    
    if annualSal < 43835:
        provTax = annualSal * 0.0968
        return provTax

    elif annualSal > 43835 and annualSal <= 87671:
        provTax = (((annualSal - 43835) * 0.1482) + (43835 * 0.0968))
        return provTax

    elif annualSal > 87671 and annualSal <= 142534:
        provTax = (((annualSal - 87671) * 0.1652) + (43836 * 0.1482) + (43835 * 0.0968))
        return provTax

    elif annualSal > 142534 and annualSal <= 162383:
        provTax = (((annualSal - 142534) * 0.1784) + (54863 * 0.1652) + (43836 * 0.1482) + (43835 * 0.0968))
        return provTax

    elif annualSal > 162383:
        provTax = (((annualSal - 162383) * 0.203) + (19849 * 0.1784) + (54863 * 0.1652) + (43836 * 0.1482) + (43835 * 0.0968))
        return provTax


# Calculate the Manitoba tax payable
def mbTax(annualSal):
    
    if annualSal < 33723:
        provTax = annualSal * 0.108
        return provTax

    elif annualSal > 33723 and annualSal <= 72885:
        provTax = (((annualSal - 33723) * 0.1275) + (33723 * 0.108))
        return provTax

    elif annualSal > 72885:
        provTax = (((annualSal - 72885) * 0.174) + (39162 * 0.1275) + (33723 * 0.108))
        return provTax


# Calculate the BC tax payable
def bcTax(annualSal):
    
    if annualSal < 42184:
        provTax = annualSal * 0.0506
        return provTax

    elif annualSal > 42184 and annualSal <= 84369:
        provTax = (((annualSal - 42184) * 0.0707) + (42184 * 0.0506))
        return provTax

    elif annualSal > 84369 and annualSal <= 96866:
        provTax = (((annualSal - 84369) * 0.105) + (42185 * 0.0707) + (42184 * 0.0506))
        return provTax

    elif annualSal > 96866 and annualSal <= 117623:
        provTax = (((annualSal - 96866) * 0.1229) + (12497 * 0.105) + (42185 * 0.0707) + (42184 * 0.0506))
        return provTax

    elif annualSal > 117623 and annualSal <= 159483:
        provTax = (((annualSal - 117623) * 0.147) + (20757 * 0.1229) + (12497 * 0.105) + (42185 * 0.0707) + (42184 * 0.0506))
        return provTax

    elif annualSal > 159483 and annualSal <= 222420:
        provTax = (((annualSal - 159483) * 0.168) + (41860 * 0.147) + (20757 * 0.1229) + (12497 * 0.105) + (42185 * 0.0707) + (42184 * 0.0506))
        return provTax

    elif annualSal > 222420:
        provTax = (((annualSal - 222420) * 0.205) + (62937 * 0.168) + (41860 * 0.147) + (20757 * 0.1229) + (12497 * 0.105) + (42185 * 0.0707) + (42184 * 0.0506))
        return provTax


# Calculate the PEI tax payable
def peiTax(annualSal):
    
    if annualSal < 31984:
        provTax = annualSal * 0.098
        return provTax

    elif annualSal > 31984 and annualSal <= 63969:
        provTax = (((annualSal - 31984) * 0.138) + (31984 * 0.098))
        return provTax

    elif annualSal > 63969:
        provTax = (((annualSal - 63969) * 0.167) + (31985 * 0.138) + (31984 * 0.098))
        return provTax


# Calculate the Saskatchewan tax payable
def skTax(annualSal):
    
    if annualSal < 45677:
        provTax = annualSal * 0.105
        return provTax

    elif annualSal > 45677 and annualSal <= 130506:
        provTax = (((annualSal - 45677) * 0.125) + (45677 * 0.105))
        return provTax

    elif annualSal > 130506:
        provTax = (((annualSal - 130506) * 0.145) + (84829 * 0.125) + (45677 * 0.105))
        return provTax


# Calculate the Alberta tax payable
def abTax(annualSal):
    
    if annualSal < 131220:
        provTax = annualSal * 0.1
        return provTax

    elif annualSal > 131220 and annualSal <= 157464:
        provTax = (((annualSal - 45142) * 0.12) + (45142 * 0.1))
        return provTax

    elif annualSal > 157464 and annualSal <= 209952:
        provTax = (((annualSal - 90287) * 0.13) + (45145 * 0.12) + (45142 * 0.1))
        return provTax

    elif annualSal > 209952 and annualSal <= 314928:
        provTax = (((annualSal - 150000) * 0.14) + (59713 * 0.13) + (45145 * 0.12) + (45142 * 0.1))
        return provTax

    elif annualSal > 314928:
        provTax = (((annualSal - 314928) * 0.15) + (104976 * 0.14) + (52488 * 0.13) + (26244 * 0.12) + (131220 * 0.1))
        return provTax


# Calculate the Newfoundland tax payable
def nlTax(annualSal):
    
    if annualSal < 38081:
        provTax = annualSal * 0.087
        return provTax

    elif annualSal > 38081 and annualSal <= 76161:
        provTax = (((annualSal - 38081) * 0.145) + (38081 * 0.087))
        return provTax

    elif annualSal > 76161 and annualSal <= 135973:
        provTax = (((annualSal - 76161) * 0.158) + (38080 * 0.145) + (38081 * 0.087))
        return provTax

    elif annualSal > 135973 and annualSal <= 190363:
        provTax = (((annualSal - 135973) * 0.173) + (59713 * 0.158) + (38080 * 0.145) + (38081 * 0.087))
        return provTax

    elif annualSal > 190363:
        provTax = (((annualSal - 190363) * 0.183) + (54390 * 0.173) + (59812 * 0.158) + (38080 * 0.145) + (38081 * 0.087))
        return provTax


# Calculate the Northwest Territories tax payable
def ntTax(annualSal):
    
    if annualSal < 44396:
        provTax = annualSal * 0.059
        return provTax

    elif annualSal > 44396 and annualSal <= 88796:
        provTax = (((annualSal - 44396) * 0.086) + (44396 * 0.059))
        return provTax

    elif annualSal > 88796 and annualSal <= 144362:
        provTax = (((annualSal - 88796) * 0.122) + (44400 * 0.086) + (44396 * 0.059))
        return provTax

    elif annualSal > 144362:
        provTax = (((annualSal - 144362) * 0.1405) + (55566 * 0.122) + (44400 * 0.086) + (44396 * 0.059))
        return provTax


# Calculate the Yukon tax payable
def ytTax(annualSal):
    
    if annualSal < 49020:
        provTax = annualSal * 0.064
        return provTax

    elif annualSal > 49020 and annualSal <= 98040:
        provTax = (((annualSal - 49020) * 0.09) + (49020 * 0.064))
        return provTax

    elif annualSal > 98040 and annualSal <= 151978:
        provTax = (((annualSal - 98040) * 0.109) + (49020 * 0.09) + (49020 * 0.064))
        return provTax

    elif annualSal > 151978 and annualSal <= 500000:
        provTax = (((annualSal - 151978) * 0.128) + (53938 * 0.109) + (49020 * 0.09) + (49020 * 0.064))
        return provTax

    elif annualSal > 500000:
        provTax = (((annualSal - 500000) * 0.15) + (348022 * 0.128) + (59713 * 0.109) + (49020 * 0.09) + (49020 * 0.064))
        return provTax


# Calculate the Nunavut tax payable
def nuTax(annualSal):
    
    if annualSal < 46740:
        provTax = annualSal * 0.04
        return provTax

    elif annualSal > 46740 and annualSal <= 93480:
        provTax = (((annualSal - 46740) * 0.07) + (46740 * 0.04))
        return provTax

    elif annualSal > 93480 and annualSal <= 151978:
        provTax = (((annualSal - 93480) * 0.09) + (46740 * 0.07) + (46740 * 0.04))
        return provTax

    elif annualSal > 151978:
        provTax = (((annualSal - 151978) * 0.115) + (58498 * 0.09) + (46740 * 0.07) + (46740 * 0.04))
        return provTax





print("Federal Tax Payable:    $", fedTax)

if prov == 1:
    provTaxTotal = onTax(annualSal)
    print("Provincial Tax Payable: $", onTax(annualSal))

elif prov == 2:
    provTaxTotal = qcTax(annualSal)
    print("Provincial Tax Payable: $", qcTax(annualSal))

elif prov == 3:
    provTaxTotal = nsTax(annualSal)
    print("Provincial Tax Payable: $", nsTax(annualSal))

elif prov == 4:
    provTaxTotal = nbTax(annualSal)
    print("Provincial Tax Payable: $", nbTax(annualSal))

elif prov == 5:
    provTaxTotal = mbTax(annualSal)
    print("Provincial Tax Payable: $", mbTax(annualSal))

elif prov == 6:
    provTaxTotal = bcTax(annualSal)
    print("Provincial Tax Payable: $", bcTax(annualSal))

elif prov == 7:
    provTaxTotal = peiTax(annualSal)
    print("Provincial Tax Payable: $", peiTax(annualSal))

elif prov == 8:
    provTaxTotal = skTax(annualSal)
    print("Provincial Tax Payable: $", skTax(annualSal))

elif prov == 9:
    provTaxTotal = abTax(annualSal)
    print("Provincial Tax Payable: $", abTax(annualSal))

elif prov == 10:
    provTaxTotal = nlTax(annualSal)
    print("Provincial Tax Payable: $", nlTax(annualSal))

elif prov == 11:
    provTaxTotal = ntTax(annualSal)
    print("Provincial Tax Payable: $", ntTax(annualSal))

elif prov == 12:
    provTaxTotal = ytTax(annualSal)
    print("Provincial Tax Payable: $", ytTax(annualSal))

elif prov == 13:
    provTaxTotal = nuTax(annualSal)
    print("Provincial Tax Payable: $", nuTax(annualSal))


print("                        -----------------")
print("Total income after tax: $", (annualSal - provTaxTotal - fedTax))
print("")