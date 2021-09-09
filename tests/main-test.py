import sys
sys.path.insert(1, '../src/')

from main import add_nums

def test_add():
    assert add_nums(2,3) == 5
    print("Add Function Works Correctly")

if __name__ == '__main__':
    test_add()
