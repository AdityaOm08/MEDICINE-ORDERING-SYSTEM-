Project Statement: Medicine Ordering System

## Problem Statement

Hospitals need a clear way to select medicines, specify quantities, choose a delivery option, and review the order cost. This project demonstrates a command-line workflow for creating a hospital medicine order, checking that the delivery location is supported, applying basic quantity and date rules, and generating an itemized invoice.

## Scope of the Project

The project is a standalone Python console application. Its implemented hospital workflow lets a user enter a hospital name, select a supported region (Bhopal, Indore, Ashta, or Ujjain), choose normal or urgent delivery, browse a predefined medicine catalog, add quantities to a cart, and view an invoice with the calculated total.

For normal delivery, the program asks for an order date and requires the requested delivery date to be at least three days later. Normal orders are limited to 100 boxes per medicine. The Antidotes category is available only for urgent delivery.

The project uses an in-memory catalog and does not save orders after the program ends. It does not include individual-user ordering, inventory updates, user accounts, payments, database storage, or connections to pharmacies and delivery services. The individual-user menu option is currently a placeholder.

## Target Users

- Hospital staff who need to prepare a medicine order through the console.
- Students and evaluators reviewing a basic ordering workflow, input validation, date handling, and invoice calculation in Python.

## High-Level Features

- Main menu for hospital users, individual users, and exiting the program.
- Hospital name entry and service-region validation.
- Normal and urgent delivery selection.
- Predefined medicine catalog organized by category.
- Urgent-delivery-only access to Antidotes.
- Cart creation and review with quantity-based line totals.
- Positive whole-number quantity validation and a 100-box normal-delivery limit per medicine.
- Date-format validation and a three-day minimum lead time for normal delivery.
- Final invoice showing the order details and total amount.

