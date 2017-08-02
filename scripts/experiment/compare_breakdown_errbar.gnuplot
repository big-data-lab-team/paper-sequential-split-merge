#!/usr/bin/env gnuplot

set terminal pdf color font ',13'
set border 3 front lt black linewidth 1.000 dashtype solid
set boxwidth 0.75 absolute
set style fill solid 1.00 border lt -1
set style histogram rowstacked
set style data histograms
set xlabel "Memory (GB)"
set ylabel "Merging time (s)"

## HDD
set output "./figures/benchmark-mreads/mreads-breakdown-hdd.pdf"
plot [][0:5500] \
     './data/mreads/mreads_hdd_avg_var.dat' using ($2):xtic(1) lt 2 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 2 fs solid 0.5 t "Read" , \
      '' using ($4) lt 2 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

## SSD
set output "./figures/benchmark-mreads/mreads-breakdown-ssd.pdf"
plot [][0:5500] \
     './data/mreads/mreads_ssd_avg_var.dat' using ($2):xtic(1) lt 2 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 2 fs solid 0.5 t "Read" , \
      '' using ($4) lt 2 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

set output "./figures/benchmark-creads/creads-breakdown-ssd.pdf"
plot [][0:5500] \
     './data/creads/creads_ssd_avg_var.dat' using ($2):xtic(1) lt 1 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 1 fs solid 0.5 t "Read" , \
      '' using ($4) lt 1 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

set output "./figures/benchmark-buff-slices/buff-slices-breakdown-ssd.pdf"
plot [][0:5500] \
     './data/buff-slices/buff-slices_ssd_avg_var.dat' using ($2):xtic(1) lt 5 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 5 fs solid 0.5 t "Read" , \
      '' using ($4) lt 5 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1