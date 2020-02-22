from extended_pathlib import Path


def test_is_readable_downturn():
    # setup
    f1 = Path("f1")
    d1 = Path("d1")
    f1.touch()
    d1.mkdir()

    # run tests
    f1.chmod(0o000)
    assert not f1.is_readable()
    f1.chmod(0o400)
    assert f1.is_readable()
    f1.chmod(0o040)
    assert not f1.is_readable()
    f1.chmod(0o004)
    assert not f1.is_readable()

    d1.chmod(0o000)
    assert not d1.is_readable()
    d1.chmod(0o400)
    assert d1.is_readable()
    d1.chmod(0o040)
    assert not d1.is_readable()
    d1.chmod(0o004)
    assert not d1.is_readable()

    # cleanup
    f1.chmod(0o777)
    f1.unlink()
    d1.chmod(0o777)
    d1.rmdir()
