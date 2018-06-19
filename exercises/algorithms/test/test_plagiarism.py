from exercises.algorithms.src.rabin_karp import search

def test_is_plagiarism():
    pat = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of " \
          "foolishness,"
    txt = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of " \
          "foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of " \
          "Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, " \
          "we had everything before us, we had nothing before us, we were all going direct to Heaven, we " \
          "were all going direct the other way – in short, the period was so far like the present period, " \
          "that some of its noisiest authorities insisted on its being received, for good or for evil, in the " \
          "superlative degree of comparison only."

    plagiarism = search(pat, txt, 101)
    assert len(plagiarism) == 1
    assert plagiarism.pop() == 0

def test_is_not_plagiarism():
    pat = "Two households, both alike in dignity " \
          "In fair Verona, where we lay our scene " \
          "From ancient grudge break to new mutiny " \
          "Where civil blood makes civil hands unclean."
    txt = "From forth the fatal loins of these two foes " \
          "A pair of star-cross'd lovers take their life " \
          "Whose misadventured piteous overthrows " \
          "Do with their death bury their parents' strife."

    plagiarism = search(pat, txt, 101)
    assert len(plagiarism) == 0