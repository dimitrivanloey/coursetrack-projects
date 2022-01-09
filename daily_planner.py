meetings = int(input('How many meetings today?\n'))
meetings_list = []
line_list = []
ordered_list = []


for _ in range(meetings):
    meeting = {}
    races_list = []
    meeting_name = input('What is the name of the meeting?\n')
    number_races = int(input('How many races?\n'))
    race_type = input('Flat or Jumps?\n')
    operator = input('What is the name of the operator?\n')
    runners = ''
    for _ in range(number_races):
        races = {}
        hour = input('Enter hour\n')
        runners = input('How many runners?\n')
        races['hour'] = hour
        races['runners'] = runners
        races_list.append(races)
    meeting['name'] = meeting_name
    meeting['type'] = race_type
    meeting['operator'] = operator
    meeting['races'] = races_list
    meetings_list.append(meeting)

# print(meetings_list)

for meeting in meetings_list:
    teller = 1
    for race in meeting['races']:
        line = ''
        line1 = f"{race['hour']} {meeting['name']} R{teller}: {race['runners']} runners - {meeting['type']}" \
               f" - {meeting['operator']}\n"

        num_line = ''
        for num in range(1, int(race['runners']) + 1):
            num_line += str(num) + 'A     '
        num_line2 = f'\n'
        for num in range(1, int(race['runners']) + 1):
            num_line2 += str(num) + 'B     '
        teller += 1

        if meeting['type'] == 'Flat':
            info_line = f'\n\nUnofficial:\t\t\t\tOfficial:\t\t\t\tU/O:'
        else:
            info_line = f'\n\nManual Starts for Jumps!'

        line = line1 + num_line + num_line2 + info_line
        line_list.append(line)


runners = 0
num_races = 0
for meeting in meetings_list:
    print(f"{meeting['name']} - {meeting['type']} - {meeting['operator']}")
    for race in meeting['races']:
        runners += int(race['runners'])
        num_races += 1
print(f"{runners} runners in {num_races} races!")
print('')
for line in sorted(line_list):
    print(f"{line}")
    print('')









