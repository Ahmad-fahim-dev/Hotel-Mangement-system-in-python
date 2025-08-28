print("*********************************************************")
print("********** Welcome to Hostel management system **********")
print("*********************************************************")
def input_int(prompt, min_val=None, max_val=None):
    while True:
        v = input(prompt).strip()
        try:
            n = int(v)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if min_val is not None and n < min_val:
            print(f"Enter a number >= {min_val}.")
            continue
        if max_val is not None and n > max_val:
            print(f"Enter a number <= {max_val}.")
            continue
        return n

def room_booking():
    print("\n--- ROOM BOOKING ---")
    rooms = {
        1: ("AC Single", 75),   # $75 per day
        2: ("AC Double", 120),  # $120 per day
        3: ("Non-AC Single", 50),
        4: ("Non-AC Double", 80),
        5: ("VIP", 200)
    }
    for k, (name, price) in rooms.items():
        print(f"{k}. {name} - ${price}/day")
    print("6. Back to Main Menu")
    choice = input_int("Choose room type (1-6): ", 1, 6)
    if choice == 6:
        return
    room_name, price = rooms[choice]
    days = input_int(f"How many days for {room_name}? ", 1)
    total = price * days
    print(f"\nBooking Summary: {room_name} for {days} day(s) -> ${total}")
    confirm = input("Confirm booking? (Y/N): ").strip().lower()
    if confirm == 'y':
        print("Room booking complete. Returning to main menu.\n")
    else:
        print("Booking cancelled. Returning to main menu.\n")

def food_ordering():
    food_menu = {
        1: ("Veg Burger", 5),
        2: ("Veg Pizza (Slice)", 6),
        3: ("Paneer Wrap", 4),
        4: ("Chicken Burger", 6),
        5: ("Chicken Wrap", 7),
        6: ("Grilled Sandwich", 5),
        7: ("French Fries", 3),
        8: ("Cold Drink (500ml)", 2),
        9: ("Tea/Coffee", 1)
    }
    food_orders = []
    next_food_id = 1

    while True:
        print("\n--- FOOD ORDERING ---")
        print("1. New Order")
        print("2. View Orders")
        print("3. Remove Order")
        print("4. Checkout Order")
        print("5. Back to Main Menu")
        choice = input_int("Enter your choice (1-5): ", 1, 5)

        if choice == 1:
            customer = input("Customer name: ").strip()
            if not customer:
                print("Name cannot be empty.")
                continue
            items = []
            while True:
                print("\nMenu:")
                for k in sorted(food_menu):
                    n, p = food_menu[k]
                    print(f"{k}. {n} - ${p}")
                print("0. Done adding items")
                sel = input_int("Enter item number to add (0 to finish): ", 0, max(food_menu.keys()))
                if sel == 0:
                    break
                if sel not in food_menu:
                    print("Invalid item number.")
                    continue
                qty = input_int("Enter quantity: ", 1)
                name, price = food_menu[sel]
                items.append((name, qty, price))
                print(f"Added {qty} x {name} - ${price} each")
            if not items:
                print("No items added. Order cancelled.")
                continue
            total = sum(q * pr for _, q, pr in items)
            order = {'id': next_food_id, 'customer': customer, 'items': items, 'total': total, 'status': 'pending'}
            food_orders.append(order)
            print(f"Order placed: ID {next_food_id} | {customer} | Total: ${total}")
            next_food_id += 1

        elif choice == 2:
            if not food_orders:
                print("No food orders yet.")
            else:
                print("\nCurrent Food Orders:")
                for o in food_orders:
                    print(f"ID {o['id']}: {o['customer']} | ${o['total']} | {o['status']}")
                    for name, qty, price in o['items']:
                        print(f"   - {qty} x {name} @ ${price} each")
                    print()

        elif choice == 3:
            if not food_orders:
                print("No orders to remove.")
                continue
            oid = input_int("Enter Order ID to remove: ", 1)
            matched = next((o for o in food_orders if o['id'] == oid), None)
            if not matched:
                print("Order ID not found.")
                continue
            food_orders = [o for o in food_orders if o['id'] != oid]
            print(f"Order {oid} removed.")

        elif choice == 4:
            if not food_orders:
                print("No orders to checkout.")
                continue
            oid = input_int("Enter Order ID to checkout: ", 1)
            order = next((o for o in food_orders if o['id'] == oid), None)
            if not order:
                print("Order ID not found.")
                continue
            if order['status'] == 'completed':
                print("Order already completed.")
                continue
            print("\n--- RECEIPT ---")
            print(f"Order ID: {order['id']}")
            print(f"Customer: {order['customer']}")
            for name, qty, price in order['items']:
                print(f"{qty} x {name} @ ${price} = ${qty*price}")
            print(f"TOTAL: ${order['total']}")
            pay = input("Mark as paid & completed? (Y/N): ").strip().lower()
            if pay == 'y':
                order['status'] = 'completed'
                print("Food order completed. Returning to main menu.\n")
                break  # return to main hotel services after completion
            else:
                print("Checkout cancelled.")

        elif choice == 5:
            print("Returning to main menu.\n")
            break

def laundry_service():
    prices = {'wash_pair': 2.0, 'wash_iron_pair': 3.5, 'iron_item': 1.0}  # dollars
    laundry_orders = []
    next_id = 1

    while True:
        print("\n--- LAUNDRY SERVICE ---")
        print("1. New Order - Wash (per pair) - ${}/pair".format(prices['wash_pair']))
        print("2. New Order - Wash & Iron (per pair) - ${}/pair".format(prices['wash_iron_pair']))
        print("3. New Order - Iron Only (per item) - ${}/item".format(prices['iron_item']))
        print("4. View Orders")
        print("5. Complete / Remove Order")
        print("6. Back to Main Menu")
        choice = input_int("Enter your choice (1-6): ", 1, 6)

        if choice in (1, 2, 3):
            name = input("Customer name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            if choice == 1:
                service = 'wash_pair'
                qty = input_int("Enter number of pairs: ", 1)
            elif choice == 2:
                service = 'wash_iron_pair'
                qty = input_int("Enter number of pairs: ", 1)
            else:
                service = 'iron_item'
                qty = input_int("Enter number of items: ", 1)
            cost = prices[service] * qty
            order = {'id': next_id, 'name': name, 'service': service, 'qty': qty, 'cost': cost, 'status': 'pending'}
            laundry_orders.append(order)
            print(f"Order added: ID {next_id} | {name} | {service} | qty: {qty} | Cost: ${cost}")
            next_id += 1

        elif choice == 4:
            if not laundry_orders:
                print("No laundry orders yet.")
            else:
                print("\nCurrent Laundry Orders:")
                for o in laundry_orders:
                    print(f"ID {o['id']}: {o['name']} | {o['service']} | qty: {o['qty']} | ${o['cost']} | {o['status']}")

        elif choice == 5:
            if not laundry_orders:
                print("No orders to complete/remove.")
                continue
            oid = input_int("Enter Order ID to complete/remove: ", 1)
            matched = next((o for o in laundry_orders if o['id'] == oid), None)
            if not matched:
                print("Order ID not found.")
                continue
            print(f"Found: ID {matched['id']} | {matched['name']} | ${matched['cost']} | {matched['status']}")
            sub = input("Mark as completed (C) or Remove (R)? (C/R): ").strip().lower()
            if sub == 'c':
                matched['status'] = 'completed'
                print(f"Laundry order {oid} marked completed. Returning to main menu.\n")
                break  # return to main hotel services after completion
            elif sub == 'r':
                laundry_orders = [o for o in laundry_orders if o['id'] != oid]
                print(f"Order {oid} removed.")
            else:
                print("Invalid choice. Enter C or R.")

        elif choice == 6:
            print("Returning to main menu.\n")
            break

def main():
    while True:
        print("What is your Service")
        print("1. Room Booking")
        print("2. Food Ordering")
        print("3. Laundry Service")
        print("4. Exit")
        ser = input_int("Enter your Service (1-4): ", 1, 4)
        print()
        if ser == 1:
            room_booking()
        elif ser == 2:
            food_ordering()
        elif ser == 3:
            laundry_service()
        elif ser == 4:
            print("Exiting. Goodbye.")
            break

if __name__ == "__main__":
    main()
 