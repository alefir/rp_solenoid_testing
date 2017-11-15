#import piplates.RELAYplate as RELAY

## Initialize an array to represent the current states of the five relays
## False = Closed; True = Open
states = [ False, False, False, False, False ]

## Initialize the REPLAYplate
#id_str = RELAY.getID(0)
#if id_str != '':
#    print('RELAYplate failed to initialize at address 0')
#    sys.exit(-1)

def toggle_relay(num):
#    RELAY.relayTOGGLE(0,num-1)
    states[num] = not states[num]

def get_status(num):
    if states[num] == False:
        return 'CLOSED'
    else:
        return 'OPEN'

def run_commands(command):
    relays = command.split(',')
    for relay in relays:
        try:
            num = int(float(relay))
        except ValueError:
            print('{} is not an integer'.format(relay))
            return
        if num > 5 or num < 1:
            print('{} is out of range'.format(num))
            return
        toggle_relay( num - 1 )

def show_status():
    statustext = "\n\n\n" \
            "RELAY STATUS\n" \
            "--------------------------\n" \
            "Relay 1:       {}\n" \
            "Relay 2:       {}\n" \
            "Relay 3:       {}\n" \
            "Relay 4:       {}\n" \
            "Relay 5:       {}\n" \
            "\n" \
            "Enter relay number(s) to toggle (comma separated) or 'quit'".format(
                    get_status(0),
                    get_status(1),
                    get_status(2),
                    get_status(3),
                    get_status(4))
    print(statustext)

show_status()
command = input(" > ")
while command != 'quit':
    run_commands(command)
    show_status()
    command = input(" > ")
