class Order():
    def __init__(self, id, customer_name, product_name, unit_price, quantity, shipping_fee, voucher):
        self.id = id
        self.customer_name = customer_name
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.shipping_fee = shipping_fee
        self.voucher = voucher
        self.total_amount = 0
        self.order_type = ""
        self.calculate_total_amount()
        self.classify_order()

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
        id_input = validate("Nhập mã đơn hàng: ")
        customer_name = validate("Nhập tên khách hàng: ")
        product_name = validate("Nhập tên sản phẩm: ")
        unit_price = validate("Nhập giá sản phẩm: ", "int")
        quantity = validate("Nhập số lượng: ", "quantity")
        shipping_fee = validate("Nhập phí vận chuyển: ", "int")
        voucher = validate("Nhập số tiền giảm giá: ", "int")

        order = Order(id_input, customer_name, product_name, unit_price, quantity, shipping_fee, voucher)
        self.orders.append(order)
        print("Thêm đơn hàng thành công!")

    def show_all(self):
        if not self.orders:
            print("Danh sách rỗng!")
            return
        print(f"{'Mã đơn hàng':<11} | {'Tên khách hàng':<20} | {'Tên sản phẩm':<20} | {'Đơn giá':<10} | {'Số lượng':<10} | {'Phí vận chuyển':<15} | {'Voucher':<10} | {'Tổng tiền':<20} | {'Phân loại':<10}")
        for order in self.orders:
            print(f"{order.id:<11} | {order.customer_name:<20} | {order.product_name:<20} | {order.unit_price:<10} | {order.quantity:<10} | {order.shipping_fee:<15} | {order.voucher:<10} | {order.total_amount:<20} | {order.order_type:<10}")

    def update_order(self):
        if not self.orders:
            print("Danh sách rỗng!")
            return
        id_input = validate("Nhập id đơn hàng cần cập nhật: ")
        for order in self.orders:
            if order.id == id_input:
                order.customer_name = validate("Nhập tên khách hàng mới: ")
                order.product_name = validate("Nhập tên sản phẩm mới: ")
                order.unit_price = validate("Nhập giá sản phẩm mới: ", "int")
                order.quantity = validate("Nhập số lượng mới: ", "quantity")
                order.shipping_fee = validate("Nhập phí vận chuyển mới: ", "int")
                order.voucher = validate("Nhập số tiền giảm giá mới: ", "int")
                order.calculate_total_amount()
                order.classify_order()
                print("Cập nhật thành công!")
                return
        print("Không tìm thấy đơn hàng với ID này!")

    def delete_order(self):
        if not self.orders:
            print("Danh sách rỗng!")
            return
        id_input = validate("Nhập id đơn hàng cần xóa: ")
        for order in self.orders:
            if order.id == id_input:
                self.orders.remove(order)
                print("Xóa thành công!")
                return
        print("Không tìm thấy đơn hàng!")

    def search_order(self):
        if not self.orders:
            print("Danh sách rỗng!")
            return
        keyword = validate("Nhập từ khóa tìm kiếm (theo tên khách hàng hoặc sản phẩm): ")
        found = [order for order in self.orders if keyword.lower() in order.customer_name.lower() or keyword.lower() in order.product_name.lower()]
        if not found:
            print("Không tìm thấy đơn hàng nào!")
        else:
            self.show_all(found)


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
            except ValueError:
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
    order_manager = OrderManager()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                order_manager.show_all()
            case "2":
                order_manager.add_order()
            case "3":
                order_manager.update_order()
            case "4":
                order_manager.delete_order()
            case "5":
                order_manager.search_order()
            case "6":
                print("Đã thoát !!")
                break
            case _:
                print("Lựa chọn không hợp lệ !!")


main()
