# requirements
# quarter notes
# fill in gaps with chromatic and diatonic steps
# root on beat 1
# fifth as leading tone
# chromatic approach tones for forward motion
# precede a note with neighbour tones above then below the target
import random
import unittest

chord_qualities = {'min': [0, 3, 7, 10], 'maj': [0, 4, 7, 11],
                   'dom': [0, 4, 7, 10], 'dim': [0, 3, 6, 9],
                   'half_dim': [0, 3, 6, 10]}

notes = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
keys = {}  # generated when program is run


def generate_keys():
    for note in notes:
        idx = notes.index(note)
        new_key = []
        for i in range(12):
            new_key.append(notes[(idx + i) % len(notes)])  # treats the notes list as a circular array
        keys[note] = new_key


def get_major_scale(key):
    scale = []
    scale.append(key[0])
    scale.append(key[2])
    scale.append(key[4])
    scale.append(key[5])
    scale.append(key[7])
    scale.append(key[9])
    scale.append(key[11])
    return scale


def get_dorian_scale(key):
    scale = []
    scale.append(key[0])
    scale.append(key[2])
    scale.append(key[3])
    scale.append(key[5])
    scale.append(key[7])
    scale.append(key[9])
    scale.append(key[10])
    return scale


def get_mixolydian_scale(key):
    scale = []
    scale.append(key[0])
    scale.append(key[2])
    scale.append(key[4])
    scale.append(key[5])
    scale.append(key[7])
    scale.append(key[9])
    scale.append(key[10])
    return scale


def get_wh_diminished_scale(key):
    scale = []
    scale.append(key[0])
    scale.append(key[2])
    scale.append(key[3])
    scale.append(key[5])
    scale.append(key[6])
    scale.append(key[8])
    scale.append(key[9])
    scale.append(key[11])
    return scale


def get_locrian_scale(key):
    scale = []
    scale.append(key[0])
    scale.append(key[1])
    scale.append(key[3])
    scale.append(key[5])
    scale.append(key[6])
    scale.append(key[8])
    scale.append(key[10])
    return scale


def create_bassline(chords):
    bassline = []
    for i, chord in enumerate(chords):
        tonality_and_quality = chord.split()
        tonality = tonality_and_quality[0]

        if tonality not in notes:
            raise Exception('{} is not a valid note. please use b`s over #`s'.format(tonality))

        quality = tonality_and_quality[1]
        key = keys[tonality]

        major_scale = get_major_scale(key)
        dorian_scale = get_dorian_scale(key)
        mixolydian_scale = get_mixolydian_scale(key)
        locrian_scale = get_locrian_scale(key)
        wh_diminished_scale = get_wh_diminished_scale(key)

        if quality not in chord_qualities.keys():
            raise Exception('{} is not a valid chord quality'.format(quality))

        quality_degrees = chord_qualities[quality]
        chord_tones = []
        for d in quality_degrees:
            chord_tones.append(key[d])

        if i + 1 >= len(chords):  # if its the final note in the bassline we use the root of that chord
            leading_tone = tonality
        else:
            chromatic_leading_tone = keys[chords[i + 1].split()[0]][-1]
            dominant_leading_tone = keys[chords[i + 1].split()[0]][7]
            leading_tone = random.choice(
                [chromatic_leading_tone, dominant_leading_tone])  # randomly decide which leading tone to use

        passing_tones = random.choice(['steps', 'chord_tones'])  # randomly decide to use scale or chord tones

        bassline.append(tonality)  # start each measure with the root tone

        if passing_tones == 'steps':
            if quality == 'maj':
                bassline.append(major_scale[1])
                bassline.append(major_scale[2])
            elif quality == 'min':
                bassline.append(dorian_scale[1])
                bassline.append(dorian_scale[2])
            elif quality == 'dom':
                bassline.append(mixolydian_scale[1])
                bassline.append(mixolydian_scale[2])
            elif quality == 'dim':
                bassline.append(wh_diminished_scale[1])
                bassline.append(wh_diminished_scale[2])
            elif quality == 'half_dim':
                bassline.append(locrian_scale[1])
                bassline.append(locrian_scale[2])
        else:
            bassline.append(chord_tones[1])
            bassline.append(chord_tones[2])

        bassline.append(leading_tone)
    return bassline


class InvalidInputTestCase(unittest.TestCase):
    def test_invalid_chords(self):
        with self.assertRaises(Exception):
            create_bassline(['C mmm'])

    def test_invalid_note(self):
        with self.assertRaises(Exception):
            create_bassline(['v maj'])


if __name__ == '__main__':
    take_input = True
    input_chords = []
    while take_input:
        chord = raw_input("enter chords one at a time. ex. 'A maj'. or enter nothing to return: ")
        if chord == '':
            take_input = False
        else:
            input_chords.append(chord)

    generate_keys()
    output = create_bassline(input_chords)
    print(output)

# Future nice to haves
# OCR for input
# machine learning to find other patterns/rules given a chord series
# midi sound output
# specific notes (ascending, descending)
# 8th notes
# dynamics
# rhythmic variety
# handle sharps
# take command line args
# write more tests for corner cases
