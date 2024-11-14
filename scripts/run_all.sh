#!/bin/bash

echo "Starting full pipeline for market regime detection..."

# Step 1
echo "Running data exploration..."
jupyter nbonvert --to notebook
--exectue notebooks/1_data_exploration.ipynb

# !TODO ...