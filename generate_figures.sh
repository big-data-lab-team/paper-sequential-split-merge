#!/bin/bash

set -e
set -u

scripts/experiment/generate_avg_var_data.py
figures/svg/export_svg_files.sh
scripts/model/model.gnplt &> data/seeks-model.dat
scripts/experiment/number_of_seeks.gnuplot # don't run this before the model as the model generates data to plot
scripts/experiment/compare_breakdown_errbar.gnuplot
scripts/mwrites/compare_breakdown_errbar.gnuplot
#crash
#scripts/blocks-slices/createboxplot.gnplt

