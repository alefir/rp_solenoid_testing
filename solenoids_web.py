import urllib.request

## Initialize an array to represent the current states of the five relays
## False = Closed; True = Open
states = [ False, False, False, False, False, False ]

def relay_on(num):
    url = urllib.request.urlopen("http://192.168.1.132/{}on".format(str(num)))
    states[num-1] = not states[num-1]

def relay_off(num):
    url = urllib.request.urlopen("http://192.168.1.132/{}off".format(str(num)))
    states[num-1] = not states[num-1]

def toggle_relay(num):
    if states[num-1]:
        relay_off(num)
    else:
        relay_on(num)

def get_status(num):
    if states[num] == False:
        return 'CLOSED'
    else:
        return 'OPEN'

def run_commands(command):
    relays = command.split(',')
    for relay in relays:
        if relay.lower() == 'all':
            for i in range(1,7):
                toggle_relay(i)
            return
        try:
            num = int(float(relay))
        except ValueError:
            print('{} is not an integer'.format(relay))
            return
        if num > 6 or num < 1:
            print('{} is out of range'.format(num))
            return
        toggle_relay(num)

def show_status():
    statustext = "\n\n\n" \
            "RELAY STATUS\n" \
            "--------------------------\n" \
            "Relay 1:       {}\n" \
            "Relay 2:       {}\n" \
            "Relay 3:       {}\n" \
            "Relay 4:       {}\n" \
            "Relay 5:       {}\n" \
            "Relay 6:       {}\n" \
            "\n" \
            "Enter relay number(s) to toggle (comma separated) or 'quit'".format(
                    get_status(0),
                    get_status(1),
                    get_status(2),
                    get_status(3),
                    get_status(4),
                    get_status(5))
    print(statustext)

show_status()
command = input(" > ")
while command != 'quit':
    run_commands(command)
    show_status()
    command = input(" > ")
