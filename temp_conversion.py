#!/usr/bin/env python
import argparse
import re

class TempConvertor:
    def __init__(self, kwargs):
        try:
            (self.input_value, self.input_unit) = kwargs['input'].split(" ")
            self.input_value = self.input_value
            self.input_unit = self.input_unit.lower()
            self.response = kwargs['response']
            self.answer = 0.0
            self.is_response_correct = "correct"
            self.output_unit = kwargs['unit']
            self.units_list = ("fahrenheit", "celsius", "kelvin", "rankine")
        except ValueError as e:
            self.is_response_correct = "invalid"
            print("[ValueError / __init__()] " + str(e) + ". Exiting.")

    # check if provided unit name is .units_list collection
    def is_unit_name_valid(self, unit_name):
        try:
            self.units_list.index(unit_name.lower())
        except ValueError as e:
            self.is_response_correct = "incorrect"
            print("[ValueError / is_unit_name_valid()] " + str(e) + ". Exiting.")
        except Exception as e:
            self.is_response_correct = "incorrect"
            print("[Exception / is_unit_name_valid()] " + str(e) + ". Exiting.")
        return self

    # check if input and response values are numeric
    def is_numeric(self, value):
        return bool(re.match("^[0-9\-\.]+$", str(value)))

    def is_input_numeric(self):
        return self.is_numeric(self.input_value)

    def is_response_numeric(self):
        return self.is_numeric(self.response)

    # chooses the right formula to do the temp conversion
    def convert_input_to_answer(self):
        if not self.is_input_numeric():
            self.is_response_correct = "invalid"
        if not self.is_response_numeric():
            self.is_response_correct = "incorrect"

        if self.is_response_correct == "correct":
            self.input_value = float(self.input_value)
            self.response = float(self.response)
            exec("self." + self.input_unit[0] + "_to_" + self.output_unit[0].lower() + "()")
        return self

    # check unit names
    # check if values are numeric - if so, then run conversion to get answer
    # check if answer matches student response
    def check_response_to_answer(self):
        if self.is_response_correct == "correct":
            self.is_unit_name_valid(self.input_unit)
            self.is_unit_name_valid(self.output_unit)

        if self.is_response_correct == "correct":
            self.convert_input_to_answer()

        if self.is_response_correct == "correct":
            if round(self.response) != round(self.answer):
                self.is_response_correct = "incorrect"
        return self


    def c_to_k(self):
        self.answer = self.input_value + 273.15
        return self

    def k_to_c(self):
        self.answer = self.input_value - 273.15
        return self

    def f_to_k(self):
        self.answer = round(self.input_value * 1.8 - 459.67)
        return self

    def k_to_f(self):
        self.answer = round((self.input_value + 459.67) / 1.8)
        return self

    def f_to_c(self):
        self.answer = round((self.input_value - 32) / 1.8)
        return self

    def c_to_f(self):
        self.answer = round(1.8*self.input_value + 32)
        return self

    def r_to_k(self):
        self.answer = round(self.input_value * 1.8)
        return self

    def k_to_r(self):
        self.answer = round(self.input_value / 1.8)
        return self

    def f_to_r(self):
        self.answer = self.input_value + 459.67
        return self

    def r_to_f(self):
        self.answer = self.input_value - 459.67
        return self

    def c_to_r(self):
        self.answer = round((self.input_value + 273.15) * 1.8)
        return self

    def r_to_c(self):
        self.answer = round((self.input_value - 491.67) / 1.8)
        return self


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Temperature input and unit")
    ap.add_argument("-u", "--unit", required=True, help="Unit input (Fahreheit, Celsius, Kelvin, Rankine)")
    ap.add_argument("-r", "--response", required=True, help="Response input")
    args = vars(ap.parse_args())
    tc = TempConvertor(args)
    tc\
        .check_response_to_answer()

    print(tc.is_response_correct)
