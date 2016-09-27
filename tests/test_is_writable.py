from extended_pathlib import Path
import pytest

def test_is_writable_downturn():
    # setup
    f1 = Path('f1')
    d1 = Path('d1')
    f1.touch()
    d1.mkdir()

    # run tests
    f1.chmod(0o000)
    assert not f1.is_writable()
    f1.chmod(0o200)
    assert f1.is_writable()
    f1.chmod(0o020)
    assert not f1.is_writable()
    f1.chmod(0o002)
    assert not f1.is_writable()

    d1.chmod(0o000)
    assert not d1.is_writable()
    d1.chmod(0o200)
    assert d1.is_writable()
    d1.chmod(0o020)
    assert not d1.is_writable()
    d1.chmod(0o002)
    assert not d1.is_writable()

    # cleanup
    f1.chmod(0o777)
    f1.unlink()
    d1.chmod(0o777)
    d1.rmdir()
