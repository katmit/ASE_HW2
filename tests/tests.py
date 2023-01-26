import random
import math
import os
import sys
import traceback

sys.path.append(os.path.abspath('../src'))

from src.cols import Cols
from src.num import Num
from src.sym import Sym
from src.data import should_dump, get_crashing_behavior_message, get_file, get_csv_contents, Data

def round_to(n, nPlaces = 3):
    mult = math.pow(10, nPlaces)
    return math.floor(n*mult + 0.5) / mult

def test_csv():
    csv_list = get_csv_contents(get_file())
    assert len(csv_list) == 399

def test_show_dump():
    test_exception = Exception("This is a test exception")
    try:
        raise test_exception
    except Exception as e:
        expected_output = str(test_exception)
        output = get_crashing_behavior_message(test_exception)

        if should_dump():
            assert len(output) > len(expected_output) and expected_output in output
        else:
            assert expected_output == output

def test_syms():
    sym = Sym()
    values = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    for value in values:
        sym.add(value)

    assert ('a' == sym.mid()) and (1.379 == round_to(sym.div(), 3))

def test_nums():
    num = Num()
    values = [1, 1, 1, 1, 2, 2, 3]
    for value in values:
        num.add(value)
    
    assert ((11/ 7) == num.mid()) and (0.787 == round_to(num.div(), 3))

def test_data():
    test_data = Data(get_file())

    y_mid_report = '{'
    y_div_report = '{'
    for y in test_data.cols.y:
        y_mid_report = y_mid_report + ' :' + y.txt + ' ' + str(y.rnd(y.mid(), 2))
        y_div_report = y_div_report + ' :' + y.txt + ' ' + str(y.rnd(y.div(), 2))
    y_mid_report = y_mid_report + '}'
    y_div_report = y_div_report + '}'

    x_mid_report = '{'
    x_div_report = '{'
    for x in test_data.cols.x:
        x_mid_report = x_mid_report + ' :' + x.txt + ' ' + str(x.rnd(x.mid(), 2))
        x_div_report = x_div_report + ' :' + x.txt + ' ' + str(x.rnd(x.div(), 2))
    x_mid_report = x_mid_report + '}'
    x_div_report = x_div_report + '}'

    print('y\tmid\t' + y_mid_report + '\n \tdiv\t' + y_div_report)
    print('x\tmid\t' + x_mid_report + '\n \tdiv\t' + x_div_report)

    assert True

def test_show_dump():
    test_exception = Exception("This is a test exception")
    try:
        raise test_exception
    except Exception as e:
        expected_output = str(test_exception)
        output = get_crashing_behavior_message(test_exception)

        if should_dump():
            assert len(output) > len(expected_output) and expected_output in output
        else:
            assert expected_output == output