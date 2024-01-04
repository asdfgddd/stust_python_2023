# 建立一個名為 Friedchicken 的類別
class Friedchicken:
   
    def __init__(self, flavor, parts, sauces, spiciness, bones):
        self.flavor = flavor  # 炸雞的口味
        self.parts = parts  # 炸雞的部位
        self.sauces = sauces  # 配醬
        self.spiciness = spiciness  # 辣度
        self.bones = bones  # 是否去骨

    # 建立一個副函數印出訂單時間
    def print_order_time(self):
        print("訂餐時間下午12:30")

    # 建立一個副函數印出價格
    def print_price(self):
        print("價格10美元")

    # 建立一個副函數印出內用或外帶
    def print_dine_in_or_takeout(self):
        print("內用" if self.dine_in else "外帶")

# 建立四個炸雞物件，每個物件都有自己的口味、部位、配醬、辣度和是否去骨
Ordernumber1 = Friedchicken('原味', '雞腿', '白醬', 'spiciness2', '去骨')
Ordernumber2 = Friedchicken('韓式', '雞腿', '紅醬', 'spiciness1', '去骨')
Ordernumber3 = Friedchicken('美式', '雞翅', '芥末', 'spiciness4', '有骨')
Ordernumber4 = Friedchicken('炭燒', '雞翅', '不加', 'spiciness3', '有骨')

# 將兩個訂單變更為外帶並更改時間為9點
Ordernumber1.dine_in = False
Ordernumber2.dine_in = False
Ordernumber1.print_order_time = lambda: print("訂餐時間上午9點")
Ordernumber2.print_order_time = lambda: print("訂餐時間上午9點")

# 為每個炸雞物件呼叫用三個子函數
for chicken in [Ordernumber1, Ordernumber2, Ordernumber3, Ordernumber4]:
    print("炸雞口味:", chicken.flavor)
    print("炸雞部位:", chicken.parts)
    print("炸雞配醬:", chicken.sauces)
    print("炸雞辣度:", chicken.spiciness)
    print("是否去骨:", chicken.bones)
    chicken.print_order_time()
    chicken.print_price()
    chicken.print_dine_in_or_takeout()
    print()  # 在每個炸雞物件空一行
