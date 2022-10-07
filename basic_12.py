'''
Exercise 12: Calculate income tax for the given income by adhering to the below rules
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.
'''
salary=float(input('enter your net salary'))
if salary==10000:
    incom_tax=0
elif salary>10000 and salary<20000:
    incom_tax=0+((salary-10000)*.1)
elif salary>20000:
    incom_tax=0+(10000*.1)+((salary-20000)*.2)
else:
    print('enter an integer')
print(f'the net incom tax to be paid is {incom_tax}$')