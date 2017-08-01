#!/usr/bin/env gnuplot

set terminal pdf color font ',13'
set border 3 front lt black linewidth 1.000 dashtype solid
set boxwidth 0.5 absolute
set style fill solid 0.50 border lt -1
unset key
set pointsize 0.5
set style data boxplot
set xtics border in scale 0,0 nomirror norotate  autojustify
set xtics  norangelimit


set xtics ("3" 1, "6" 2, "9" 3, "12" 4)
unset format y
unset ydata
unset xrange
unset logscale x
unset format x
set boxwidth 0.5

set xtics font ", 10"
set xlabel "Memory (GB)"
set ylabel "Number of Seeks"
set output "./figures/benchmark-mreads/mreads-number-of-seeks.pdf"


plot './data/mwrites/mwrites_hdd.dat' using (1):4 , '' using (2):9 , '' using (3):14 , '' using (4):19
