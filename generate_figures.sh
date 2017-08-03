#!/bin/bash

set -e
set -u

scripts/experiment/generate_avg_var_data.py
scripts/experiment/generate_total_avg_var_data.py # for total merge time figure
figures/svg/export_svg_files.sh
scripts/model/model.gnplt &> data/seeks-model.dat
scripts/experiment/number_of_seeks.gnuplot # don't run this before the model as the model generates data to plot
scripts/experiment/merge_total_time.gnuplot
scripts/experiment/compare_breakdown_errbar.gnuplot
scripts/mwrites/compare_breakdown_errbar.gnuplot
#crash
#scripts/blocks-slices/createboxplot.gnplt

