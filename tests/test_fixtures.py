import pytest

from .utils import load_rpc_tests, methods
import json

rpc_public_tests = load_rpc_tests("public")
rpc_private_tests = load_rpc_tests("private")


@pytest.mark.parametrize(
    "action,test",
    [
        *(
            (action, test)
            for action, tests in rpc_public_tests.items()
            for test in tests
        ),
        *(
            (action, test)
            for action, tests in rpc_private_tests.items()
            for test in tests
        ),
    ],
)
def test_rpc_methods(action, test):
    try:
        method = methods[action]
    except NotImplementedError:
        raise Exception("`%s` not yet implemented" % action)

    try:
        expected = test["expected"]
        arguments = {k: v for (k, v) in test["request"].items() if k != "action"} or {}

    except KeyError:
        raise Exception(
            "invalid test for %s: %s" % (action, json.dumps(test, indent=2))
        )

    result = method(**arguments)

    if result != expected:
        print("result:")
        print(json.dumps(result, indent=2, sort_keys=True))
        print("expected:")
        print(json.dumps(expected, indent=2, sort_keys=True))

    assert result == expected
