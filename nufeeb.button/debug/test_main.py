#coding=utf-8
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.mark.xfail(("6*9", 42)),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected



@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print("teardown_function called.")
    request.addfinalizer(teardown_function)
    print('setup_function called.')

@pytest.fixture(scope='module')
def setup_module(request):
    def teardown_module():
        print("teardown_module called.")
    request.addfinalizer(teardown_module)
    print('setup_module called.')

@pytest.fixture(scope='class')
def setup_class(request):
    def teardown_class():
        print("teardown_class called.")
    request.addfinalizer(teardown_class)
    print('setup_class called.')


'''
@pytest.mark.usefixtures("setup_class")
def test_1(setup_function):
    print('Test_1 called.')

def test_2(setup_module):
    print('Test_2 called.')

def test_3(setup_module):
    print('Test_3 called.')
'''

class Testclass():

    def test_four(self,setup_module):
        print('Test_4 called.')

    def test_five(self):
        print('Test_5 called.')


class Testclass2():
    def test_four2(self):
        print('Test_42 called.')

    def test_five2(self):
        print('Test_52 called.')
