import datetime

# Medicine Inventory

inventory = {
    "Antidotes": [
        {"name": "Antivenom", "price": 435},
        {"name": "N-acetylcysteine", "price": 549},
        {"name": "Atropine", "price": 520},
        {"name": "Activated charcoal", "price": 490},
        {"name": "Naloxone", "price": 870},
        {"name": "Flumazenil", "price": 503},
        {"name": "Fomepizole", "price": 1500},
        {"name": "Deferoxamine", "price": 800},
        {"name": "Methylene blue", "price": 530},
        {"name": "Protamine sulfate", "price": 600},
        {"name": "Sodium bicarbonate", "price": 500}
    ],
    "Heart": [
        {"name": "Aspirin", "price": 1530},
        {"name": "Atorvastatin", "price": 1450},
        {"name": "Metoprolol", "price": 980},
        {"name": "Lisinopril", "price": 505},
        {"name": "Furosemide", "price": 534}
    ],
    "Kidney": [
        {"name": "Lisinopril", "price": 430},
        {"name": "Losartan", "price": 340},
        {"name": "Dapagliflozin", "price": 540},
        {"name": "Empagliflozin", "price": 500},
        {"name": "Furosemide", "price": 870}
    ],
    "Brain": [
        {"name": "Donepezil", "price": 1520},
        {"name": "Levetiracetam", "price": 1400},
        {"name": "Memantine", "price": 340},
        {"name": "Gabapentin", "price": 880},
        {"name": "Carbidopa-Levodopa", "price": 500}
    ],
    "Lungs": [
        {"name": "Albuterol", "price": 870},
        {"name": "Fluticasone", "price": 750},
        {"name": "Tiotropium", "price": 630},
        {"name": "Montelukast", "price": 890},
        {"name": "Budesonide", "price": 456}
    ],


    "Liver": [
        {"name": "Ursodeoxycholic Acid", "price": 430},
        {"name": "Silymarin", "price": 640},
        {"name": "L-Ornithine L-Aspartate", "price": 780},
        {"name": "Ademetionine", "price": 600},
        {"name": "Metadoxine", "price": 500}
    ],


    "Eyes": [
        {"name": "Latanoprost", "price": 507},
        {"name": "Moxifloxacin", "price": 850},
        {"name": "Olopatadine", "price": 172},
        {"name": "Carbomer", "price": 640},
        {"name": "Prednisolone", "price": 740}
    ]
}

SERVICEABLE_REGIONS = {
    "1": "BHOPAL",
    "2": "INDORE",
    "3": "ASHTA",
    "4": "UJJAIN"
}



while True:
    print("\n=========================================")
    print("   MAIN MENU - WELCOME TO MEDIC BUDDY")
    print("=========================================")
    print("1. Hospital User")
    print("2. Individual User")
    print("3. Exit System")

    user_choice = input("Select (1-3): ").strip()

    if user_choice == "3":
        print("Exiting the system. Thank you!")
        break

    # Both Hospital (1) and Individual (2) use the same ordering flow
    elif user_choice in ("1", "2"):

        user_type = "Hospital" if user_choice == "1" else "Individual"
        customer_name = input(f"Enter {user_type.upper()} name: ").strip()

        print(f"\nSelect {user_type} Region:")
        print("1. BHOPAL")
        print("2. INDORE")
        print("3. ASHTA")
        print("4. UJJAIN")
        print("5. Other City")
        area_choice = input("Select region (1-5): ").strip()

        if area_choice in SERVICEABLE_REGIONS:
            city_name = SERVICEABLE_REGIONS[area_choice]
            print(f"Location verified: Service is available in {city_name}.")
        else:
            print("Sorry, services are currently only available in BHOPAL, INDORE, ASHTA, or UJJAIN. Returning to main menu.")
            continue

        print("\n--- Delivery Options ---")
        print("1. Normal Delivery")
        print("2. Urgent Delivery")
        del_choice = input("Select delivery type (1-2): ").strip()

        order_date_obj = None
        order_date_str = "N/A"
        delivery_option = ""

        if del_choice == "1":
            delivery_option = "normal"
            while True:
                date_input = input("Enter the date of order (DD-MM-YYYY): ").strip()
                try:
                    order_date_obj = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()
                    order_date_str = order_date_obj.strftime('%d-%m-%Y')
                    break
                except ValueError:
                    print("Wrong format. Please use DD-MM-YYYY.")
        elif del_choice == "2":
            delivery_option = "urgent"
        else:
            print("Invalid delivery option. Defaulting to 'urgent' delivery.")
            delivery_option = "urgent"

        cart = []

        while True:
            print("\n--- Medicine Categories ---")
            # Antidotes are only available for urgent delivery
            categories = [cat for cat in inventory if cat != "Antidotes" or delivery_option == "urgent"]
            for i, cat in enumerate(categories, start=1):
                print(f"{i}. {cat}")
            print("0. Done selecting medicines")

            cat_choice = input("Select a category number (or 0 to proceed to checkout): ").strip()

            if cat_choice == '0':
                break

            if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
                selected_category = categories[int(cat_choice) - 1]

                while True:
                    print(f"\n--- {selected_category} Medicines ---")
                    medicines = inventory[selected_category]
                    for i, med in enumerate(medicines, start=1):
                        print(f"{i}. {med['name']} - {med['price']} per box")
                    print("0. Return to categories")

                    med_choice = input(f"Select a medicine number from {selected_category} to add (or 0 to go back): ").strip()

                    if med_choice == '0':
                        break

                    if med_choice.isdigit() and 1 <= int(med_choice) <= len(medicines):
                        selected_med = medicines[int(med_choice) - 1]

                        qty_input = input(f"Enter the quantity of boxes for {selected_med['name']}: ").strip()
                        if qty_input.isdigit() and int(qty_input) > 0:
                            qty = int(qty_input)

                            # Limit check for normal delivery
                            if delivery_option == "normal" and qty > 100:
                                print("\n[!] Limit Exceeded: For normal delivery, you cannot order more than 100 boxes per medicine.")
                                print("Medicine not added. Please try again with a quantity of 100 or less.\n")
                            else:
                                cart.append({
                                    "category": selected_category,
                                    "name": selected_med['name'],
                                    "price": selected_med['price'],
                                    "quantity": qty
                                })
                                print(f"--> Added {qty} box(es) of {selected_med['name']} to your order.")
                        else:
                            print("Invalid quantity.")
                    else:
                        print("Invalid medicine selection.")
            else:
                print("Invalid category selection.")

        if not cart:
            print("\nNo medicines selected. Returning to main screen...")
            continue
        print("moving to CART PLEASE WAIT...")
        print("\n==============================")
        print("        CART REVIEW           ")
        print("==============================")
        for item in cart:
            item_total = item['price'] * item['quantity']
            print(f"- {item['name']} | {item['quantity']} box(es) | Amount: {item_total}")
        print("==============================\n")

        delivery_date_str = "within few hours, as soon as possible"

        if delivery_option == "normal":
            while True:
                date_input = input("Enter preferred delivery date (DD-MM-YYYY): ").strip()
                try:
                    pref_date_obj = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()

                    if (pref_date_obj - order_date_obj).days < 3:
                        min_date = order_date_obj + datetime.timedelta(days=3)
                        print(f"\n[!] ERROR: Delivery date must be at least 3 days after the order date ({order_date_str}).")
                        print(f"The earliest available delivery date is {min_date.strftime('%d-%m-%Y')}.\n")
                    else:
                        delivery_date_str = pref_date_obj.strftime('%d-%m-%Y')
                        break
                except ValueError:
                    print("Invalid date format. use format same as DD-MM-YYYY.")
        print("INVOICE IS LOADING...")
        print("\n========================================")
        print("            FINAL INVOICE               ")
        print("========================================")
        print(f"{user_type} Name: {customer_name}")
        print(f"City: {city_name}")
        print(f"Delivery Type: {delivery_option.capitalize()}")
        if delivery_option == "normal":
            print(f"Date of Order: {order_date_str}")
        print(f"Date of delivery: {delivery_date_str}")

        print("\nMedicines Ordered:")
        final_amount = 0
        for item in cart:
            item_total = item['price'] * item['quantity']
            final_amount += item_total
            print(f" * {item['name']} ({item['category']}) x{item['quantity']} = {item_total}")

        print("-" * 40)
        print(f"FINAL TOTAL AMOUNT: {final_amount}")
        print("========================================")

        print("\nThank you for TRUSTING us , always ready to help ! Redirecting to main screen...\n")

    else:
        print("unfounded selection. Please enter 1, 2, or 3.\n")