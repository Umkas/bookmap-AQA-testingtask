#!/bin/bash

echo "Unit-tests rinning (Python)"
echo "-----------------------------"

if python unit-tests.py; then
  echo "All tests complite"
else
  echo "Error. One or some tests falled"
  exit 1
fi