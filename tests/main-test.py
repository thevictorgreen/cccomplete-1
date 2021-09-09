import sys
sys.path.insert(1, '../src/')

from main import Add

def TestAdd():
    assert Add(2,3) == 5
    print("Add Function Works Correctly")

if __name__ == '__main__':
    TestAdd()
