#!/bin/bash

set -e
set -u

figures/svg/export_svg_files.sh
scripts/blocks-slices/createboxplot.gnplt
scripts/model/model.gnplt
scripts/mreads/number_of_seeks.gnuplot
scripts/mreads/generate_avg_var_data.py
scripts/mreads/compare_total_time.gnuplot
scripts/mreads/compare_breakdown_errbar.gnuplot
scripts/mwrites/generate_avg_data.py
scripts/mwrites/compare_total_time.gnuplot
scripts/mwrites/compare_breakdown_errbar.gnuplot





