# Midi note chart
NOTE_TO_MIDI = {
# octave -2
'C-2' : 0, 'C#-2': 1, 'Db-2':  1, 'D-2' :  2, 'D#-2':  3,
'Eb-2': 3, 'E-2' : 4, 'F-2' :  5, 'F#-2':  6,
'Gb-2': 6, 'G-2' : 7, 'G#-2':  8,
'Ab-2': 8, 'A-2' : 9, 'A#-2': 10, 'Bb-2': 10, 'B-2' : 11,

# octave -1
'C-1' : 12, 'C#-1': 13, 'Db-1': 13, 'D-1' : 14, 'D#-1': 15,
'Eb-1': 15, 'E-1' : 16, 'F-1' : 17, 'F#-1': 18,
'Gb-1': 18, 'G-1' : 19, 'G#-1': 20,
'Ab-1': 20, 'A#-1': 22, 'A-1' : 21, 'Bb-1': 22, 'B-1' : 23,
# octave 0
'C0' : 24, 'C#0': 25, 'Db0': 25, 'D0' : 26, 'D#0': 27,
'Eb0': 27, 'E0' : 28, 'F0' : 29, 'F#0': 30,
'Gb0': 30, 'G0' : 31, 'G#0': 32,
'Ab0': 32, 'A0' : 33, 'A#0': 34, 'Bb0': 34, 'B0' : 35,
# octave 1
'C1' : 36, 'C#1': 37, 'Db1': 37, 'D1' : 38, 'D#1': 39,
'Eb1': 39, 'E1' : 40, 'F1' : 41, 'F#1': 42,
'Gb1': 42, 'G1' : 43, 'G#1': 44,
'Ab1': 44, 'A1' : 45, 'A#1': 46, 'Bb1': 46, 'B1' : 47,
# octave 2
'C2' : 48, 'C#2': 49, 'Db2': 49, 'D2' : 50, 'D#2': 51,
'Eb2': 51, 'E2' : 52, 'F2' : 53, 'F#2': 54,
'Gb2': 54, 'G2' : 55, 'G#2': 56,
'Ab2': 56, 'A2' : 57, 'A#2': 58, 'Bb2': 58, 'B2' : 59,
# octave 3
'C3' : 60, 'C#3': 61, 'Db3': 61, 'D3' : 62, 'D#3': 63,
'Eb3': 63, 'E3' : 64, 'F3' : 65, 'F#3': 66,
'Gb3': 66, 'G3' : 67, 'G#3': 68,
'Ab3': 68, 'A3' : 69, 'A#3': 70, 'Bb3': 70, 'B3' : 71,
# octave 4
'C4' : 72, 'C#4': 73, 'Db4': 73, 'D4' : 74, 'D#4': 75,
'Eb4': 75, 'E4' : 76, 'F4' : 77, 'F#4': 78,
'Gb4': 78, 'G4' : 79, 'G#4': 80,
'Ab4': 80, 'A4' : 81, 'A#4': 82, 'Bb4': 82, 'B4' : 83,
# ocatve 5
'C5' : 84, 'C#5': 85, 'Db5': 85, 'D5' : 86, 'D#5': 87,
'Eb5': 87, 'E5' : 88, 'F5' : 89, 'F#5': 90,
'Gb5': 90, 'G5' : 91, 'G#5': 92,
'Ab5': 92, 'A5' : 93, 'A#5': 94, 'Bb5': 94, 'B5' : 95,
# octave 6
'C6' :  96, 'C#6':  97, 'Db6':  97, 'D6' :  98, 'D#6':  99,
'Eb6':  99, 'E6' : 100, 'F6' : 101, 'F#6': 102,
'Gb6': 102, 'G6' : 103, 'G#6': 104,
'Ab6': 104, 'A6' : 105, 'A#6': 106, 'Bb6': 106, 'B6' : 107,
#octave 7
'C7' : 108, 'C#7': 109, 'Db7': 109, 'D7' : 110, 'D#7': 111,
'Eb7': 111, 'E7' : 112, 'F7' : 113, 'F#7': 114,
'Gb7': 114, 'G7' : 115, 'G#7': 116,
'Ab7': 116, 'A7' : 117, 'A#7': 118, 'Bb7': 118, 'B7':  119,
#octave 8
'C8' : 120, 'C#8': 121, 'Db8': 121, 'D8' : 122, 'D#8': 123,
'Eb8': 123, 'E8' : 124, 'F8' : 125, 'F#8': 126,
'Gb8': 126, 'G8' : 127, 'G#8': 128,
'Ab8': 128, 'A8' : 129, 'A#8': 130, 'Bb8': 130, 'B8' : 131,

}


NOTE_TIMINGS = {
    'hqu' : (0.01625 , "hemidemisemiquaver"),
    'dhq' : ((0.01625 * 1.5), "dotted hemidemisemiquaver"),
    'dqu' : (0.03125 , "demisemiquaver"),
    'ddq' : ((0.03125 * 1.5), "dotted demisemiquaver"),
    'squ' : (0.0625 , "semiquaver"),
    'dsq' : ((0.0625 * 1.5), "dotted semiquaver"),
    'qua' : (0.125 , "quaver"),
    'dqu' : ((0.125 * 1.5), "dotted quaver"),
    'cro' : (0.25 , "crotchet"),
    'dcr' : ((0.25 *1.5), "dotted crotchet"),
    'min' : (0.5 , "minim"),
    'dmi' : ((0.5 * 1.5), "dotted minim"),
    'sbr' : (1 , "semibreve"),
    'dsb' : ((1 * 1.5), "dotted semibreve"),
    'bre' : (2 , "breve"),
    'dbr' : ((2 * 1.5), "dotted breve"),
    'lon' : (4 , "longa"),
    'dlo' : ((4 * 1.5), "dotted longa"),
    'max' : (8 , "maxima"),
    'dma' : ((8 * 1.5), "dotted maxima"),

}

if __name__ == '__main__':

    errorsOccurred = False
    #test and correction for the octave notes in case are incorrect
    for notePos, letter in enumerate(['C', 'C#', 'Db', 'D','D#', 'Eb' ,'E', 'F', 'F#', 'Gb','G', 'G#', 'Ab', 'A', 'A#', 'Bb','B']):
        for octave in range(-2, 8):
            #print(letter + str(octave))
            lowerNote  = letter+ str(octave)
            higherNote = letter+ str(octave+1)
            #print("Notes")
            #print(lowerNote , " comp to " , higherNote)
            #print("Values")
            #print(NOTE_TO_MIDI[lowerNote], " comp to " , NOTE_TO_MIDI[higherNote])
            if lowerNote not in NOTE_TO_MIDI:
                errorsOccurred = True
                print "Missing Note " + lowerNote
                offset = (octave + 2) * 12
                NOTE_TO_MIDI[lowerNote] = offset + notePos
            elif higherNote not in NOTE_TO_MIDI:
                errorsOccurred = True
                print "Missing Note " + higherNote
                NOTE_TO_MIDI[higherNote] = NOTE_TO_MIDI[lowerNote]+12
            else:
                if((NOTE_TO_MIDI[lowerNote]+12) != NOTE_TO_MIDI[higherNote]):
                    errorsOccurred = True
                    print("Need to change note value from ", NOTE_TO_MIDI[higherNote], " to ", NOTE_TO_MIDI[lowerNote]+12)
                    NOTE_TO_MIDI[higherNote] = NOTE_TO_MIDI[lowerNote]+12

    if errorsOccurred:
        # print out corrected dictionary to console
        print '{'
        for octave in range(-2, 8):
            for letter in ['C', 'C#', 'Db', 'D','D#', 'Eb' ,'E', 'F', 'F#', 'Gb','G', 'G#', 'Ab', 'A', 'A#', 'Bb','B']:
                note = letter+str(octave)
                print note +" : "+ str(NOTE_TO_MIDI[letter+str(octave)])
        print '}'
    else:
        print "No errors found in MIDI note conversion"
