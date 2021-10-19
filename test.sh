#!/bin/bash
python -m unittest src.unit_tests.main_unit_tests 2> output.txt
if [grep -q "FAILED" output.txt]
then
  cat output.txt
  rm output.txt
  exit 1;
fi
python -m unittest src.unit_tests.excel_reader_unit_tests 2> output.txt
if [grep -q "FAILED" output.txt]
then
  cat output.txt
  rm output.txt
  exit 2;
fi
python -m unittest src.unit_tests.voltage_stdev_unit_tests 2> output.txt
if [grep -q "FAILED" output.txt]
then
  cat output.txt
  rm output.txt
  exit 3;
fi
rm output.txt
exit 0
