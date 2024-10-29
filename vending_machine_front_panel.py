"""vending_machine_graphical.py - simulate a coin operated vending machine
TPRG 2131 Fall 2022 Project 1
Louis Bertrand <louis.bertrand@durhamcollege.ca>

This is a demonstration of a simple GUI for a vending machine.
The buttons simply cause their key values to be printed.
Close the window with the X in the top right corner.
"""

import PySimpleGUI as sg


COIN_LIST = [ ("$2", 200),  # Example of using an integer as the key
              ("$1", "Loonie"),  # The other buttons use string keys
              ("25\u00A2", "Quarter"),
              ("10\u00A2", "Dime"),
              ("5\u00A2", "Nickel"),
              ("RETURN", "Return")
            ]
SELECTION_LIST = [ ("CHIPS", "A"),  # Example of using single letter keys
                   ("CHOCOLATE", "B"),
                   ("HEINEKEN", "C"),
                   ("SUGAR DRINK", "D"),
                   ("SURPRISE", "E")
                 ]

if __name__ == "__main__":
    # Define the coins column
    coin_col = []
    coin_col.append([sg.Text("ENTER COINS")])
    for item in COIN_LIST:
        button = sg.Button(item[0], key=item[1])  # Name and key are different
        row = [button]
        coin_col.append(row)

    # Define the selections column
    select_col = []
    select_col.append([sg.Text("SELECT ITEM")])
    for item in SELECTION_LIST:
        button = sg.Button(item[0])  # Use the name of the button as the key
        row = [button]
        select_col.append(row)

    # Define the layout as two columns separated by a vertical line
    layout = [ [sg.Column(coin_col, vertical_alignment="TOP"),
                     sg.VSeparator(),
                     sg.Column(select_col, vertical_alignment="TOP")
                ]
            ]

    # Create the window
    window = sg.Window("Vending Machine", layout)

    ## Main loop ##
    while True:
        # It's important to have a timeout to window.read() in case there are
        # periodic tasks to be done by the state machine; a timeout event
        # would let the machine update itself
        event, values = window.read(timeout = 100, timeout_key = "__TIMEOUT__")
        # Here you would feed the event to machine.update()
        # But instead we will just print it out.
        if event == "__TIMEOUT__":
            pass  # no user interaction event occurred
        elif event == sg.WIN_CLOSED:
            print("Event sg.WIN_CLOSED")
            break
        else:
            print("Event", event)

    window.close()
    print("Exiting...")
