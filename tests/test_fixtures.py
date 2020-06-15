import pytest

from .utils import load_tests, _test_method
from bananopy.banano import NodeException

rpc_public_tests = load_tests("public")
rpc_private_tests = load_tests("private")
util_tests = load_tests("other")


@pytest.mark.parametrize(
    "action,test",
    [(action, test) for action, tests in rpc_public_tests.items() for test in tests],
)
def test_rpc_methods(action, test):
    _test_method(action, test)


@pytest.mark.parametrize(
    "action,test",
    [(action, test) for action, tests in rpc_private_tests.items() for test in tests],
)
def test_fail_rpc_methods(action, test):
    with pytest.raises(NodeException):
        _test_method(action, test)


@pytest.mark.parametrize(
    "action,test",
    [(action, test) for action, tests in util_tests.items() for test in tests],
)
def test_utils(action, test):
    _test_method(action, test)
