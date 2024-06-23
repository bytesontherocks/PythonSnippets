import pytest



# A(bool)    B (Bool)   Expected (String)  
testdata = [    
    (False,      False,      "A and B are false!"),
    (False,      True,       "A is False B is false!"),
    (True,       False,      "A is true B is false!"),
    (True,       True,       "A and B are true!"),
]

@pytest.mark.parametrize("A, B, expected", testdata)
def test_function(A : bool, B: bool, expected: str) -> None:
    assert production_code_function(A, B) == expected

def production_code_function( A: bool, B: bool) -> str:
    if A is False:
        if B is False:
            return "A and B are false!"
        else:
            return "A is False B is false!"
    else:
        if B is False:
            return "A is true B is false!"
        else:
            return "A and B are true!"

