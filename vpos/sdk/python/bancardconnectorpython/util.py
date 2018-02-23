# MIT License
#
# Copyright (c) [2018] [Victor Manuel Cajes Gonzalez - vcajes@gmail.com]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from decimal import Decimal
from bancardconnectorpython.exceptions import BancardAPIInvalidParameterException


# number of decimals for an amount of a given currency
CURRENCIES_DECIMALS = {
	"PYG": 0,
}


def merge_dict(first_dict, *next_dicts):
	"""
	Returns the merge of all the dictionaries
	Usage::
		>>> util.merge_dict({"key1": "val1"}, {"key2": "val2"}, {"Bancard": "API"})
		{'key1': 'val1', 'key2': 'val2', 'Bancard': 'API'}
	"""
	result_dict = dict()
	for curr_dict in (first_dict,) + next_dicts:
		result_dict.update(curr_dict)
	return result_dict


def currency_decimal_to_string(currency, decimal_value):
	if currency not in CURRENCIES_DECIMALS:
		raise BancardAPIInvalidParameterException("The currency is not allowed.")

	if not isinstance(decimal_value, Decimal):
		raise BancardAPIInvalidParameterException("The amount is not a Decimal value.")

	decimals = CURRENCIES_DECIMALS[currency] if currency in CURRENCIES_DECIMALS else 2
	ret = ("%." + str(decimals) + "f") % decimal_value
	return ret