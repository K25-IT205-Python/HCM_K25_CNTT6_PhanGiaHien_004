class Order():
    def __init__(self, id, customer_name, product_name, unit_price, quantity, shipping_fee, voucher,total_amount, order_type):
        self.id = id
        self.customer_name = customer_name
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.shipping_fee = shipping_fee
        self.voucher = voucher
        self.total_amount = 0
        self.order_type = ""

    
    def calculate_total_amount(self):
        self.total_amount = self.unit_price * self.quantity + self.shipping_fee - self.voucher

    def classify_order(self):
        if self.total_amount < 500000:
            self.order_type = "Nhỏ"
        elif 500000 <= self.total_amount < 2000000:
            self.order_type = "Trung bình"
        elif 2000000 <= self.total_amount < 10000000:
            self.order_type = "Lớn"
        else: 
            self.order_type = "VIP"


class OrderManager():
    def __init__(self):
        self.orders = []

    
    def add_order(self):
       while True:
           id_input = validate("Nhập id: ")
           for order in Order:
                if order.lower() == Order.id.lower():
                    print("ID trùng! Nhập lại")
                    break
                else:
                    input_customer_name = validate("Nhập vào tên khách hàng:")
                    input_product_name = validate("Nhập vào tên sản phẩm: ")
                    input_unit_price = validate("Nhập vào giá sản phẩm: ")
                    input_quantity = validate("Nhập vào số lượng: ")
                    input_shipping_fee = validate("Nhập vào phí vận chuyển: ")
                    input_voucher = validate("Nhập vào số tiền giảm giá:")

                Order.customer_name = input_customer_name
                Order.product_name = input_product_name
                Order.unit_price = input_unit_price
                Order.quantity = input_quantity
                Order.shipping_fee = input_shipping_fee
                Order.voucher = input_voucher   

                print("Cập nhật thành công !")

    def show_all(self):
        print(f"{'Mã đơn hàng':<11} | {'Tên khách hàng':<20} | {'Tên sản phẩm':<20} | {'Đơn giá':<10} | {'Phí vận chuyển':<15} | {'Voucher':<10} | {'Tổng tiền':<20} | {'Phân loại':<10}")
        for self.order in Order:
            print(f"{Order.id:<11} | {Order.customer_name:<20} | {Order.product_name:<20} | {Order.unit_price:<10} | {Order.shipping_fee:<15} | {Order.voucher:<10} | {Order.total_amount:<20} | {Order.order_type:<10}")
    def update_order():
        print()
    def delete_order():
        print()
    def search_order():
        print()
    

        

def menu():
    print('''
    =========== MENU ==============
        1. Hiển thị danh sách đơn hàng
        2. Thêm đơn hàng mới
        3. Cập nhật đơn hàng
        4. Xóa đơn hàng
        5. Tìm kiếm đơn hàng
        6. Thoát
          ''')
    
    
def validate(promt: str, type: str = "str"):
    while True:
        order_input = input(promt)
        if not order_input:
            print("Không được để trống !!!")
            continue
        if type == 'int':
            try:
                value = int(order_input)
                if value < 0:
                    print("Không được âm !!!")
                    continue
                return value
            except ValueError :
                print("Dữ liệu không hợp lệ !!")
                continue
        if type == 'quantity':
            try:
                value = int(order_input)
                if value < 0 or value > 1000:
                    print("Nhập trong khoảng từ 0 - 1000")
                    continue
                return value
            except ValueError:
                print('Dữ liệu không hợp lệ')
                continue
        return order_input

    
def main():
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn:")
        match choice:
            case "1":
                OrderManager.show_all()
            case "2":
                OrderManager.add_order()
            case "6":
                print("Đã thoát !!")
                break
            case _:
                print("Lựa chọn không hợp lệ !!")

main()
