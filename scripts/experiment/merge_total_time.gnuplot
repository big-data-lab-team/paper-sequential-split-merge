#!/usr/bin/env gnuplot
set terminal pdf color font ',10'

set style data histogram
set style histogram cluster gap 1 errorbars
set xlabel "Memory (GB)"
set ylabel "Merging time (s)"
set style fill solid border rgb "black"
set auto x
set yrange [0:*]
set key autotitle columnheader

set output "./figures/total-merge-time-ssd.pdf"
plot './data/total-merge-time-ssd.dat' using 2:3:xtic(1) lt 3 title col(2),\
        '' using 4:5 lt 4 title col(4), \
        '' using 6:7 lt 1 title col(6), \
        '' using 8:9 lt 2 title col(8), \
        '' using 10:11 lt 5 title col(10)

