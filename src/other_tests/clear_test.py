from other import clear
from global_data import users, channels, messages
def test_clear():
    clear()
    assert users == []
    assert channels == []
    assert messages == []