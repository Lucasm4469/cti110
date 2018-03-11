# CTI-110
# P3HW2 - Software Sales
# Mary Ann Lucas
# 11 March 2018

bulkdiscount = int(input('Enter the number of packages bought: '))
packagecost = 99

if bulkdiscount < 10:
    discountrate = 0;
elif bulkdiscount < 20:
    discountrate = 0.10
elif bulkdiscount < 50:
    discountrate = 0.20
elif bulkdiscount < 100:
    discountrate = 0.30
else:
    discountrate = 0.40

subtotal = bulkdiscount * packagecost
discountrate = discountrate * subtotal
total = subtotal - discountrate

print('\namount of discount: $' + format(discountrate, ',.2f' )+ '\ntotal amount: \
$' + format(total, ',.2f' ))
