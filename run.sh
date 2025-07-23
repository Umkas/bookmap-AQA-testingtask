#!/bin/bash

echo "🚀 Unit-tests rinning (Python)"
echo "-----------------------------"

if python unit-tests.py; then
  echo " All tests complite"
else
  echo " Error. Test falled"
  exit 1
fi