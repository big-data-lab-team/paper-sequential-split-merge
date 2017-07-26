#!/bin/bash

set -e
set -u

figures/svg/export_svg_files.sh
scripts/blocks-slices/createboxplot.gnplt
scripts/model/model.gnplt
scripts/mwrites/compare_total_time.gnuplot
scripts/mwrites/comparasion_break_down.gnuplot
scripts/mwrites/generate_avg_data.py
scripts/mreads/compare_total_time.gnuplot
scripts/mreads/comparasion_break_down.gnuplot
scripts/mreads/generate_avg_data.py
#./scripts/mreads/number_of_seeks.gnuplot # crashes for now
