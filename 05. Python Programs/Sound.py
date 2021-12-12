import winsound

# Sa,  re,  Re,  ga,  Ga,  ma,  Ma,    Pa,  dh,  Dha, ni,  Ni,  Sa
# 240, 256, 270, 288, 300, 320, 337.5, 360, 384, 400, 432, 450, 480

# C    C#   D    D#   E     F    F#   G    G#   A    A#   B     C
# 1.000     1.122     1.260 1.335     1.498     1.682     1.888 2.000
#      1.059     1.189           1.414     1.587     1.782

note_frequency = {
    'Sa': 240,
    're': 256,
    'Re': 270,
    'ga': 288,
    'Ga': 300,
    'Ma': 320,
    'MA': 338,
    'Pa': 360,
    'dha': 384,
    'Dha': 400,
    'ni': 432,
    'Ni': 450,
    'SA': 480,
}

song = ['Sa', 'Re', 'Ga', 'Ma', 'Pa', 'Dha', 'Ni', 'SA']
# song = ['Sa', 'Re', 'Ga', 'Ga', 'Ga', 'Ga', 'Ga', 'Ga', 'Ga', 'Ga', 'Ga', 'Ga', 'Re', 'Ga', 'Ma', 'Ma']

for note in song:
    winsound.Beep(note_frequency[note], 1000)
