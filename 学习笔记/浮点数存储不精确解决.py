#解决前print(1.1+2.2)=3.3000000000000003
#解决后
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
