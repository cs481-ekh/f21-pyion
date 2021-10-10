#!/bin/bash
python -m unittest src.unit_tests.main_unit_tests
python -m unittest src.unit_tests.excel_reader_unit_tests
python -m unittest src.unit_tests.voltage_stdev_unit_tests
exit 0
