from .. import db


def test_summer_looks():
    assert db.summer_looks() == len(db.top()) * \
        len(db.bottom()) * len(db.shoes())


def test_winter_looks():
    assert db.winter_looks() == len(db.top()) * len(db.bottom()) * \
        len(db.shoes()) * len(db.outwear()) * len(db.hats())


def test_sorted():
    for f in db.top, db.bottom, db.outwear, db.hats, \
            db.bags, db.shoes, db.accessories:
        res = f()
        sorted = f()
        sorted.sort()
        assert 2 <= len(res)
        assert res == sorted


def test_closet():
    n = 0
    for f in db.top, db.bottom, db.outwear, db.hats, \
            db.bags, db.shoes, db.accessories:
        n += len(f())
    assert len(db.closet()) == n
