from um import count

def test():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_word():
    assert count("yummy") == 0
    assert count("YUMMY") == 0
    assert count("nonconsumptions") == 0
    assert count("overdocumenting") == 0