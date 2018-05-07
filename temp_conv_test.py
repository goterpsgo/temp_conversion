#!/usr/bin/env python

import pytest
from .temp_conversion import TempConvertor

def test_f_to_r_correct():
    params = {'input': '84.2 fahrenheit', 'response': 543.5, 'unit': 'rankine'}
    tc = TempConvertor(params)
    tc.check_response_to_answer()
    assert round(tc.answer) == round(tc.response)
    assert tc.is_response_correct == "correct"

def test_c_to_k_correct():
    params = {'input': '-45.14 celsius', 'response': 227.51, 'unit': 'kelvin'}
    tc = TempConvertor(params)
    tc.check_response_to_answer()
    assert round(tc.answer) == round(tc.response)
    assert tc.is_response_correct == "correct"

def test_k_to_f_incorrect():
    params = {'input': '317.33 kelvin', 'response': 110.5, 'unit': 'fahrenheit'}
    tc = TempConvertor(params)
    tc.check_response_to_answer()
    assert round(tc.answer) != round(tc.response)
    assert tc.is_response_correct == "incorrect"

def test_r_to_c_incorrect():
    params = {'input': '444.5 rankine', 'response': -30.9, 'unit': 'celsius'}
    tc = TempConvertor(params)
    tc.check_response_to_answer()
    assert round(tc.answer) != round(tc.response)
    assert tc.is_response_correct == "incorrect"

def test_f_to_r_incorrect():
    params = {'input': '6.5 fahrenheit', 'response': 'dog', 'unit': 'rankine'}
    tc = TempConvertor(params)
    tc.check_response_to_answer()
    assert tc.is_response_correct == "incorrect"

def test_dog_to_c_invalid():
    params = {'input': 'dog', 'response': 45.32, 'unit': 'celsius'}
    tc = TempConvertor(params)
    tc.check_response_to_answer()
    assert tc.is_response_correct == "invalid"
