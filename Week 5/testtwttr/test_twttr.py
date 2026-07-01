from twttr import shorten

def test_shorten():
    assert shorten("Hoggen") == "Hggn"
    assert shorten("Super") == "Spr"

def test_shorten_lower():
    assert shorten("humanbeing") == "hmnbng"
    assert shorten("mytwitteraccount") == "mytwttrccnt"


def test_shorten_upper():
    assert shorten("BADIDEA") == "BDD"
    assert shorten("BESTTIMEEVER") == "BSTTMVR"

def test_shorten_numeric():
    assert shorten("Ho0gge4n") == "H0gg4n"
    assert shorten("My3twi467tter") == "My3tw467ttr"

def test_shorten_punctuation():
    assert shorten("Maxi*mal!!") == "Mx*ml!!"
    assert shorten("Ha:R/V(ar)+D") == "H:R/V(r)+D"