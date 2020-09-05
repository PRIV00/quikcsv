import unittest
import csv

from quikcsv.decorator import QuikCSV


class Test_One(unittest.TestCase):

    def test_just_data(self):
        data = [
            ['A', 'B', 'C'],
            ['1', '2', '3']
        ]

        @QuikCSV.one(data)
        def stub(csv_):
            reader = csv.reader(csv_)
            output = [row for row in reader]
            self.assertEqual(data, output)
        stub()

    def test_with_arg(self):
        data = [
            ['A', 'B', 'C'],
            ['1', '2', '3']
        ]

        @QuikCSV.one(data, arg='two')
        def stub(one, two):
            reader = csv.reader(two)
            output = [row for row in reader]
            self.assertEqual(data, output)
            self.assertEqual(1, one)

        @QuikCSV.one(data, arg='two')
        def stub_two(one, two, three):
            reader = csv.reader(two)
            output = [row for row in reader]
            self.assertEqual(data, output)
            self.assertEqual(1, one)
            self.assertEqual(3, three)

        stub(1)
        stub_two(1, 2, 3)

    def test_with_opts_copy_pattern(self):
        data = [['a', 'b', 'c']]

        @QuikCSV.one(data, opts=dict(
            row_pattern='copy',
            add_rows=2
        ))
        def stub(csv_):
            expected = [
                ['a', 'b', 'c'],
                ['a', 'b', 'c'],
                ['a', 'b', 'c']
            ]
            reader = csv.reader(csv_)
            output = [row for row in reader]
            self.assertEqual(expected, output)
        stub()

    def test_with_opts_func_pattern_no_increment(self):
        data = [['a', 'b', 'c']]
        @QuikCSV.one(data, opts=dict(
            row_pattern=lambda x: [i + 'a' for i in x],
            add_rows=2
        ))
        def stub(csv_):
            expected = [
                ['a', 'b', 'c'],
                ['aa', 'ba', 'ca'],
                ['aa', 'ba', 'ca']
            ]
            reader = csv.reader(csv_)
            output = [row for row in reader]
            self.assertEqual(expected, output)
        stub()

    def test_with_opts_func_pattern_with_increment(self):
        data = [['a', 'b', 'c']]
        @QuikCSV.one(data, opts=dict(
            row_pattern=lambda x: [i + 'a' for i in x],
            add_rows=2,
            increment=True
        ))
        def stub(csv_):
            expected = [
                ['a', 'b', 'c'],
                ['aa', 'ba', 'ca'],
                ['aaa', 'baa', 'caa']
            ]
            reader = csv.reader(csv_)
            output = [row for row in reader]
            self.assertEqual(expected, output)
        stub()
