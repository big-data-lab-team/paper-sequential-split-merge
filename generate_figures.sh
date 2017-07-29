#!/bin/bash

set -e
set -u

figures/svg/export_svg_files.sh
scripts/model/model.gnplt
scripts/mreads/number_of_seeks.gnuplot
scripts/mreads/compare_breakdown_errbar.gnuplot
scripts/mwrites/compare_breakdown_errbar.gnuplot
#crash
#scripts/blocks-slices/createboxplot.gnplt

