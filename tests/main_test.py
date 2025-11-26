from refactor_test.main import main, divide, summ
from hypothesis import given, example, settings, strategies as st
import pytest

def test_main():
    assert main() is None


@example(1, 0)
@given(st.integers(), st.integers())
@settings(max_examples=200)
def test_divide(n, m):
    if m == 0:
        with pytest.raises(ZeroDivisionError):
            assert divide(n, m) == 0
    else:
        assert divide(n, m) == n / m


@pytest.mark.parametrize(
    "value,result",
    [
        ((1, 2, 3), 6),
        (((1, 2, 3)), 6),
        ((), 0),
    ]
)
def test_summ(value, result):
    if len(value) > 1:
        assert summ(*value) == result
    else:
        assert summ(value) == result