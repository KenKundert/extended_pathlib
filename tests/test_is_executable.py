from extended_pathlib import Path
import pytest

def test_is_executable_downturn():
    # setup
    f1 = Path('f1')
    d1 = Path('d1')
    f1.touch()
    d1.mkdir()

    # run tests
    f1.chmod(0o000)
    assert not f1.is_executable()
    f1.chmod(0o100)
    assert f1.is_executable()
    f1.chmod(0o010)
    assert not f1.is_executable()
    f1.chmod(0o001)
    assert not f1.is_executable()

    d1.chmod(0o000)
    assert not d1.is_executable()
    d1.chmod(0o100)
    assert d1.is_executable()
    d1.chmod(0o010)
    assert not d1.is_executable()
    d1.chmod(0o001)
    assert not d1.is_executable()

    # cleanup
    f1.chmod(0o777)
    d1.chmod(0o777)
    f1.unlink()
    d1.rmdir()
