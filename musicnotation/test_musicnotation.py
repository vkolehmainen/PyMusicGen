import unittest
import musicnotation.chords as chords

class TestMusicnotation(unittest.TestCase):
    
    def test_from_shothand(self):
        self.assertEqual(chords.from_shorthand("C"), ['C', 'E', 'G'], "wrong notes in chord")
        self.assertEqual(chords.from_shorthand("Cm"), ['C', 'Eb', 'G'], "wrong notes in chord")
        self.assertEqual(chords.from_shorthand("C/G"), ['G', 'C', 'E'], "wrong notes in chord")
        self.assertEqual(chords.from_shorthand("Cm/G"), ['G', 'C', 'Eb'], "wrong notes in chord")
        self.assertEqual(chords.from_shorthand("C/E"), ['E', 'G', 'C'], "wrong notes in chord")
        self.assertEqual(chords.from_shorthand("Cdim"), ['C', 'Eb', 'Gb'], "wrong notes in chord")
        
        # More from_shorthand tests should be written
        
if __name__ == '__main__':
    unittest.main()