import string, operator, random
lists = open('./chords.txt', 'r');

all_chords = dict()

recent = ["", "", ""]
start_count = 0

def clean(chord):
    return string.replace(chord, "\n", "").strip(" ")


#Create tree
for song in lists:
    chords = song.split(" ")
    start_count = 0
    for chord in chords:
        if(start_count < 3):
            recent[start_count] = clean(chord)
            start_count += 1
        else:
            if recent[0] not in all_chords:
                all_chords[recent[0]] = dict()
            if recent[1] not in all_chords[recent[0]]:
                all_chords[recent[0]][recent[1]] = dict()
            if recent[2] not in all_chords[recent[0]][recent[1]]:
                all_chords[recent[0]][recent[1]][recent[2]] = 0
            all_chords[recent[0]][recent[1]][recent[2]] += 1
            recent[0] = recent[1]
            recent[1] = recent[2]
            recent[2] = clean(chord)

for chord_0 in all_chords:
    for chord_1 in all_chords[chord_0]:
        all_chords[chord_0][chord_1] = sorted(all_chords[chord_0][chord_1].iteritems(), key=operator.itemgetter(1))

# Create chart
# input is a 2-length array of chord strings
def get_by_maximum(my_chords, length = 16):
    for i in range(length):
        choice_node = all_chords[my_chords[0]][my_chords[1]]
        choice_chord = choice_node[len(choice_node) - 1][0]
        print(my_chords[0])
        my_chords[0] = my_chords[1]
        my_chords[1] = choice_chord

def get_by_probability(my_chords, wierdness = 1, length = 16):
    for i in range(length):
        choice_node = all_chords[my_chords[0]][my_chords[1]]
        total = 0
        for choice in choice_node:
            total += choice[1]
        rand = int(random.randint(0, total) * wierdness)
        chosen_chord = ""
        for choice in choice_node:
            rand -= choice[1]
            if(rand <= 0):
                chosen_chord = choice[0]
                break
        print(my_chords[0])
        my_chords[0] = my_chords[1]
        my_chords[1] = chosen_chord

get_by_probability(["C:maj", "G:maj"], .5)