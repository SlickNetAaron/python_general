from unittest import mock
from testingwithhfc import multiply_two, name_reverse
import pytest
from unittest.mock import MagicMock, patch, call

def test_multiply_two():
    with pytest.raises(ValueError):
        multiply_two("stringies", 42)
    with pytest.raises(ValueError):
        multiply_two(42,"stringies")
    assert multiply_two(3, -3) == -9
    assert multiply_two(1235412341245123413, 0) == 0
    assert multiply_two(-81723123441234, -12) == 980677481294808
    # assert False
    # assert multiply_two(-0.2314, 0.7332) == -0.16966248

def test_name_reverse():
    assert name_reverse('Berland, Aaron') == 'Aaron Berland'
    assert name_reverse('Berland,Aaron') == 'Aaron Berland'
    assert name_reverse('Camacho, Henry F.') == 'Henry F. Camacho'
    assert name_reverse('Berland') == 'Berland'
    assert name_reverse('Berland,') == 'Berland'
    assert name_reverse(', Aaron') == 'Aaron'

# test_multiply_two()
# print(multiply_two(-0.2314, 0.7332))
# print(multiply_two(3,-3))
# print(name_reverse('Berland-Bob, Aaron'))