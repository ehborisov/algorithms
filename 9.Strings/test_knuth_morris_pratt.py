from knuth_morris_pratt_pattern_matching import knuth_morris_pratt


def test_boyer_moore(text, pattern, match_locations):
    matches = knuth_morris_pratt(text, pattern)
    assert sorted(matches) == sorted(match_locations)
