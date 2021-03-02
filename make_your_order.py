"""
This module contains program, which helps to make purchases in the virtual market.
"""


class Item:
    """
    This class creates objects (items), which you buy.

    >>> my_oitem = Item("salt", 12)
    >>> my_oitem.name
    'salt'
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """
        Ths method returns your item`s name and price.

        >>> my_oitem = Item("salt", 12)
        >>> my_oitem.__str__()
        'salt, price - 12'
        """
        return self.name + ", price - " + str(self.price)


class Vehicle:
    """
    This class creates objectes (vehicles).

    >>> my_vehicle = Vehicle(1, True)
    >>> my_vehicle.vehicleNo
    1
    """

    def __init__(self, vehicleNo, isAvailable):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Location:
    """
    This class creates object - location.

    >>> my_loc = Location("Kiev", 42)
    >>> my_loc.city
    'Kiev'
    """

    def __init__(self, city, postoffice):
        self.city = city
        self.postoffice = postoffice


class Order():
    """
    This class creates your order, according to the data you entered.

    >>> my_order = Order(user_name='Oleg', orderId=165488695, city='Lviv',\
        postoffice=53, items=my_items)
    >>> my_order.orderId
    165488695
    """

    def __init__(self, orderId, user_name, city, postoffice, items, vechile=None):
        self.orderId = orderId
        self.location = Location(city, postoffice)
        self.user_name = user_name
        self.items = items
        self.vechile = vechile

    def __str__(self):
        """
        This method returns your order number.

        >>> my_order = Order(user_name='Oleg', orderId=165488695, city='Lviv',\
            postoffice=53, items=my_items)
        >>> my_order.__str__()
        'Your order number is 165488695.'
        """
        return "Your order number is " + str(self.orderId) + "."

    def calculateAmount(self):
        """
        This method calculates the whole price of your products.

        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order(user_name='Oleg', orderId=165488695, city='Lviv',\
            postoffice=53, items=my_items)
        >>> my_order.calculateAmount()
        154
        """
        result = 0
        for i in self.items:
            result += i.price
        return result

    def assignVechile(self, vechile: Vehicle):
        """
        This method assigns a vehicle to the order, and returns nothing.
        """
        self.vechile = vechile
        counter = 0
        for i in vechile:
            if i.isAvailable:
                i.isAvailable = False
                counter += 1
                break
        if counter == 0:
            print("There is no available vehicle to deliver an order.")


class LogisticSystem():
    """
    This clas creates objects which helps with navigating in your order.

    >>> vehicles = [Vehicle(1, True), Vehicle(2, True)]
    >>> my_items = [Item('book', 110), Item('chupachups', 44)]
    >>> my_order = Order(user_name='Oleg', orderId=165488695, city='Lviv',\
postoffice=53, items=my_items)
    >>> logSystem = LogisticSystem([my_order], vehicles)
    >>> print(logSystem.orders[0])
    Your order number is 165488695.
    """

    def __init__(self, orders, vehicles):
        self.orders = orders
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        """
        This method submits your order, and assigns to it a vehicle.

        >>> vehicles = []
        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order(user_name='Oleg', orderId=165488695, city='Lviv',\
postoffice=53, items=my_items)
        >>> logSystem = LogisticSystem([my_order], vehicles)
        >>> logSystem.placeOrder(my_order)
        There is no available vehicle to deliver an order.
        """
        self.order = order
        order.assignVechile(self.vehicles)

    def trackOrder(self, orderId):
        """
        This method helps to track status of your order.

        >>> vehicles = [Vehicle(1, True), Vehicle(2, True)]
        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order(user_name='Oleg', orderId=165488695, city='Lviv',\
postoffice=53, items=my_items)
        >>> logSystem = LogisticSystem([my_order], vehicles)
        >>> logSystem.trackOrder(165488695)
        Your order #165488695 is sent to Lviv. Total price: 154 UAH.
        """
        counter = 0
        for i in self.orders:
            if i.orderId == orderId:
                print("Your order #" + str(orderId) + " is sent to " + i.location.city +
                      ". Total price: " + str(i.calculateAmount()) + " UAH.")
                counter += 1
                break
        if counter == 0:
            print("No such order.")


if __name__ == "__main__":
    loc = Location("Lviv", 12)
    my_vehicles = [Vehicle(1, True), Vehicle(2, True)]
    my_items = [Item('book', 110), Item('chupachups', 44)]
    my_order = Order(user_name='Oleg', orderId=165488695, city='Lviv',
                     postoffice=53, items=my_items)
    my_items2 = [Item('flowers', 11), Item(
        'shoes', 153), Item('helicopter', 0.33)]
    my_order2 = Order(186541566, 'Andrii', 'Odessa', 3, my_items2)
    my_items3 = [Item('coat', 61.8), Item(
        'shower', 5070), Item('rollers', 700)]
    my_order3 = Order(186541546, "Olesya", 'Kharkiv', 17, my_items3)
    print(my_order)
    logSystem = LogisticSystem([my_order, my_order2, my_order3], my_vehicles)
