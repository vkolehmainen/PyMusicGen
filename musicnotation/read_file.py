import musicnotation.chords as chords
import musicnotation.keys as keys

def read_file(file):
    """ Reads chords from given file 
    @param file: *.txt
    @type file: String
    @return: String """
    
    with open(file, 'r') as f:
        words = f.read().split()
        
    valid_chords = []

    for word in words:
        if chords.is_valid(word):
            valid_chords.append(word)

    if not valid_chords:
        return False
    
    return ';'.join(valid_chords)

def main():
    
    print(chords.from_shorthand("Cm/G"))
    print(keys.get_notes("C"))
    
main()