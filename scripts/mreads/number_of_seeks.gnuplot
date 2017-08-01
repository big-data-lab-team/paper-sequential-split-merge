#!/usr/bin/env gnuplot

set terminal pdf color font ',13'
set boxwidth 0.5
set style fill transparent solid 0.5 noborder
unset key
set xtics ("3" 1, "6" 2, "9" 3, "12" 4)
unset format y
unset ydata
unset xrange
unset logscale x
unset format x
set xlabel "Memory (GB)"
set ylabel "Number of Seeks"

set output "./figures/benchmark-mreads/mreads-number-of-seeks.pdf"
plot './data/mreads/mreads_hdd.dat' using (1):4 w boxes lc "blue", '' using (2):9 w boxes lc "blue", '' using (3):14 w boxes lc "blue", '' using (4):19 w boxes lc "blue"




