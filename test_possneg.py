from poss_neg import positive_negative

def test_positive_negative():
    assert positive_negative(10) == "Positive"
    assert positive_negative(-10) == "Negative"
    assert positive_negative(0) == "Zero"