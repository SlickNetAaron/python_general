import dice_v2_simple_functional as d
import pytest

def test_get_input():
    pass

@pytest.mark.parametrize("valid_inputs, expected_return", [("1", 1), ("5", 5), ("6",6)])
def test_parse_valid_inputs(valid_inputs, expected_return):
    parse = d.parse_input(valid_inputs)
    assert parse == expected_return

@pytest.mark.parametrize("exiting_inputs", ["8", "", "x", "123asef", "-3"])
def test_parse_input_exiting_inputs(exiting_inputs):
    with pytest.raises(SystemExit) as e:
        d.parse_input(exiting_inputs)
    assert e.type == SystemExit

# Original test example... converted to parametrize above
# def test_parse_input_anything():
#     with pytest.raises(SystemExit) as e:
#         d.parse_input("")
#     assert e.type == SystemExit

@pytest.mark.parametrize("dice_count", [1,6])
def test_roll_dice(dice_count):
    dice_out = d.roll_dice(dice_count)
    assert len(dice_out) == dice_count
    assert max(dice_out) <= 6
    assert min(dice_out) > 0

# Simple test example
# def test_roll_dice():
#     dice_out = d.roll_dice(6)
#     assert len(dice_out) == 6
#     assert max(dice_out) <= 6
#     assert min(dice_out) > 0

