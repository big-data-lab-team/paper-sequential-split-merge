#!/usr/bin/env gnuplot

set terminal pdfcairo color
set border 3 front lt black linewidth 1.000 dashtype solid
set boxwidth 0.75 absolute
set style fill solid 1.00 border lt -1
set style histogram rowstacked
set style data histograms


## HDD
set output "./figures/benchmark-mreads/mreads-breakdown-hdd.pdf"
plot [][0:3500] \
     './data/mreads/mreads_hdd_avg_var.dat' using ($2):xtic(1) t "calculation time" , \
     '' using ($3) t "read time" , \
      '' using ($4) t "write time",\
      '' using ($5) t "seek time",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

## SSD
set output "./figures/benchmark-mreads/mreads-breakdown-ssd.pdf"
plot [][0:3500] \
     './data/mreads/mreads_ssd_avg_var.dat' using ($2):xtic(1) t "calculation time" , \
     '' using ($3) t "read time" , \
      '' using ($4) t "write time",\
      '' using ($5) t "seek time",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1