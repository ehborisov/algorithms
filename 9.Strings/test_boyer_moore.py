from boyer_moore_pattern_matching import boyer_moore


def test_boyer_moore(text, pattern, match_locations):
    matches = boyer_moore(text, pattern)
    assert sorted(matches) == sorted(match_locations)
