import pypyodbc


def test_always_true():
    assert True


def test_connect(fmdb):
    assert fmdb.cursor()
