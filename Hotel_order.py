{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNgxU+O44Y1yJq/YM3E7NzH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Imdad990/hotel-order/blob/main/Hotel_order.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yctw2Hi3pfl_"
      },
      "outputs": [],
      "source": [
        "def display_menu():\n",
        "    print(\"\\nWelcome to the Hotel!\")\n",
        "    print(\"Here is our menu:\")\n",
        "    print(\"1. Burger - $5\")\n",
        "    print(\"2. Pizza - $8\")\n",
        "    print(\"3. Sandwich - $4\")\n",
        "    print(\"4. Coffee - $3\")\n",
        "    print(\"5. Exit\")\n",
        "\n",
        "def take_order():\n",
        "    menu = {\n",
        "        1: (\"Burger\", 5),\n",
        "        2: (\"Pizza\", 8),\n",
        "        3: (\"Sandwich\", 4),\n",
        "        4: (\"Coffee\", 3)\n",
        "    }\n",
        "    order = []  # List to store ordered items\n",
        "    while True:\n",
        "        display_menu()\n",
        "        try:\n",
        "            choice = int(input(\"Enter your choice (1-5): \"))\n",
        "            if choice == 5:\n",
        "                print(\"Exiting...\")\n",
        "                break\n",
        "            elif choice in menu:\n",
        "                try:\n",
        "                    quantity = int(input(f\"How many {menu[choice][0]}(s) would you like to order? \"))\n",
        "                    if quantity <= 0:\n",
        "                        print(\"Quantity must be greater than zero.\")\n",
        "                        continue\n",
        "                    order.append((menu[choice][0], menu[choice][1], quantity))\n",
        "                    print(f\"{quantity} {menu[choice][0]}(s) added to your order.\")\n",
        "                except ValueError:\n",
        "                    print(\"Invalid quantity. Please enter a number.\")\n",
        "            else:\n",
        "                print(\"Invalid choice. Please try again.\")\n",
        "        except ValueError:\n",
        "            print(\"Invalid input. Please enter a number.\")\n",
        "    return order\n",
        "\n",
        "def calculate_total(order):\n",
        "    if not order:  # If the order list is empty\n",
        "        print(\"No items in the order.\")\n",
        "        return 0\n",
        "\n",
        "    total = 0\n",
        "    print(\"\\nYour Order Summary:\")\n",
        "    print(f\"{'Item':<15}{'Price ($)':<10}{'Quantity':<10}{'Subtotal ($)':<10}\")\n",
        "    print(\"-\" * 50)\n",
        "\n",
        "    for item, price, quantity in order:\n",
        "        subtotal = price * quantity\n",
        "        total += subtotal\n",
        "        print(f\"{item:<15}{price:<10}{quantity:<10}{subtotal:<10}\")\n",
        "\n",
        "    print(\"-\" * 50)\n",
        "    print(f\"Total Bill: ${total}\")\n",
        "    return total"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "    order = take_order()  # Take the order from the user\n",
        "    if order:  # Check if the order is not empty\n",
        "        total_bill = calculate_total(order)  # Call calculate_total to get the total bill\n",
        "        if total_bill > 0:  # Only show the bill if it's greater than zero\n",
        "            print(f\"\\nThank you for ordering! Your total bill is: ${total_bill}\")\n",
        "        else:\n",
        "            print(\"No valid items in your order.\")\n",
        "    else:\n",
        "        print(\"No items ordered. Thank you for visiting!\")  # If no items were ordered\n",
        "\n",
        "if __name__==\"__main__\":\n",
        "     main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0GGn-8eGrvdq",
        "outputId": "429079ec-08aa-4391-acb7-58ecbff2d7f6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Welcome to the Hotel!\n",
            "Here is our menu:\n",
            "1. Burger - $5\n",
            "2. Pizza - $8\n",
            "3. Sandwich - $4\n",
            "4. Coffee - $3\n",
            "5. Exit\n",
            "Enter your choice (1-5): 4\n",
            "How many Coffee(s) would you like to order? 66\n",
            "66 Coffee(s) added to your order.\n",
            "\n",
            "Welcome to the Hotel!\n",
            "Here is our menu:\n",
            "1. Burger - $5\n",
            "2. Pizza - $8\n",
            "3. Sandwich - $4\n",
            "4. Coffee - $3\n",
            "5. Exit\n",
            "Enter your choice (1-5): 5\n",
            "Exiting...\n",
            "\n",
            "Your Order Summary:\n",
            "Item           Price ($) Quantity  Subtotal ($)\n",
            "--------------------------------------------------\n",
            "Coffee         3         66        198       \n",
            "--------------------------------------------------\n",
            "Total Bill: $198\n",
            "\n",
            "Thank you for ordering! Your total bill is: $198\n"
          ]
        }
      ]
    }
  ]
}