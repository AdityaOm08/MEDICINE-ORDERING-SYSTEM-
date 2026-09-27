# CSE1021
python | projects | problem solving 
MEDICINE ORDERING SYSTEM Ordering System

## Overview

MEDICINE ORDERING SYSTEM Ordering System is a menu-driven Python command-line application for placing MEDICINE ORDERING SYSTEM orders on behalf of hospitals. Hospital users can select a serviceable delivery region, choose normal or urgent delivery, build a MEDICINE ORDERING SYSTEM cart from available categories, and receive an itemized invoice with the total cost. The MEDICINE ORDERING SYSTEM catalog and prices are stored in the program as in-memory data.

The individual-user menu option is present, but its ordering flow is not implemented yet; choosing it currently displays a placeholder message and returns to the main menu.

## Features

- Hospital ordering workflow with hospital name and service-region selection.
- Service coverage for Bhopal, Indore, Ashta, and Ujjain.
- Normal and urgent delivery options.
- MEDICINE ORDERING SYSTEM catalog grouped into Antidotes, Heart, Kidney, Brain, Lungs, Liver, and Eyes.
- Antidotes are available only when urgent delivery is selected.
- Cart review with medicine, quantity, and line amount.
- Quantity validation; normal delivery is limited to 100 boxes per medicine.
- Date validation for normal delivery, which must be at least three days after the order date.
- Final invoice showing delivery details, ordered medicines, and total amount.
- Main menu loop with an option to exit.

## Technologies and Tools

- Python 3 . 14 . 7
- Python standard library: `datetime`
- Command-line interface (console input and output)

No third-party packages are required.

## Installation and Run

1. Install Python 3 . 14 . 7 if it is not already available. Confirm it is on your PATH:

   ```bash
python --version  ```

   On some systems, use 'python3.14.7' instead of 'python'.

2. Download or clone this project and open a terminal in the folder containing `MEDICINE ORDERING SYSTEM .py`.

3. Start the program:

   ```bash
   python "MEDICINE ORDERING SYSTEM .py"
   ```

   Or, where needed:

   ```bash
   python3 "MEDICINE ORDERING SYSTEM .py"
   ```

4. Choose **1. Hospital User** to place a hospital order, **2. Individual User** to view the current placeholder behavior, or **3. Exit System** to quit.

## Testing Instructions

There is currently no automated test suite. Test the program interactively from the terminal using the following checks:

1. **Exit:** Choose '3' and confirm the program exits.
2. **Invalid main-menu input:** Enter a value outside '1'-'3' and confirm an error is shown and the menu is repeated.
3. **Serviceable region:** Start a hospital order and select each of the four supported regions; confirm each is accepted.
4. **Unsupported region:** Select '5' (Other City) and confirm the order returns to the main menu with an availability message.
5. **Delivery and catalog:** Choose normal delivery and confirm Antidotes is not listed. Choose urgent delivery and confirm it is listed.
6. **Quantity validation:** Try a non-numeric or zero quantity and confirm it is rejected. For normal delivery, try more than 100 boxes and confirm it is not added; try a valid quantity of 100 or fewer and confirm it is added.
7. **Normal-delivery dates:** Enter an invalid date format and confirm it is rejected. Enter a preferred delivery date fewer than three days after the order date and confirm it is rejected; then enter a date at least three days later and confirm it is accepted.
8. **Cart and invoice:** Add multiple medicines, proceed to checkout, and verify line amounts and the final total equal each medicine's price multiplied by its quantity.
9. **Empty cart:** Proceed without selecting medicines and confirm no invoice is produced.
10. **Individual user:** Choose '2' and confirm the placeholder message appears; no individual order is placed.

## Notes

- Prices are entered as numeric values in the source code; no currency symbol or currency unit is specified by the application.
- Orders are not saved between runs, and the application does not connect to a pharmacy, payment service, or delivery service.
- This program is an ordering workflow demonstration, not medical advice. The catalog is not a substitute for guidance from a qualified healthcare professional.
