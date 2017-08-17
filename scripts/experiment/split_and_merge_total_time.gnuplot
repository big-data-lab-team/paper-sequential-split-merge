#!/usr/bin/env gnuplot
set terminal pdf color font ',10'

set style data histogram
set style histogram cluster gap 1 errorbars
set boxwidth 1
set xlabel "Memory (GB)"
set ylabel "Merge time (s)"
set style fill solid 0.75 border rgb "black"
set auto x
set yrange [0:*]
set key autotitle columnheader

maxy=13500

set output "./figures/total-merge-time-ssd.pdf"
plot [][0:maxy] './data/total-merge-time-ssd.dat' using 2:3:xtic(1) lt 3 title col(2),\
        '' using 4:5 lt 4 title col(4), \
        '' using 6:7 lt 1 title col(6), \
        '' using 8:9 lt 2 title col(8), \
        '' using 10:11 lt 5 title col(10)

set output "./figures/total-merge-time-ssd-compressed.pdf"
plot [][0:maxy] './data/total-merge-time-ssd-compressed.dat'\
           using 4:5:xtic(1) lt 4 fillstyle pattern 2 title col(4), \
        '' using 6:7 lt 1 fillstyle pattern 2 title col(6), \
        '' using 8:9 lt 2 fillstyle pattern 2 title col(8), \
        '' using 10:11 lt 5 fillstyle pattern 2 title col(10),\
        './data/total-merge-time-ssd.dat' using 4:5:xtic(1) lt 4 title col(4), \
        '' using 8:9 lt 2 title col(8), \
        '' using 10:11 lt 5 title col(10)

set output "./figures/total-merge-time-hdd.pdf"
plot [][0:maxy] './data/total-merge-time-hdd.dat' using 2:3:xtic(1) lt 3 title col(2),\
        '' using 4:5 lt 4 title col(4), \
        '' using 6:7 lt 1 title col(6), \
        '' using 8:9 lt 2 title col(8), \
        '' using 10:11 lt 5 title col(10)

maxy=4000

set ylabel "Split time (s)"
set output "./figures/total-split-time-ssd.pdf"
plot [][0:maxy] './data/total-split-time-ssd.dat' using 2:3:xtic(1) lt 3 title col(2),\
        '' using 4:5 lt 4 title col(4), \
        '' using 6:7 lt 1 title col(6), \
        '' using 8:9 lt 2 title col(8), \
        '' using 10:11 lt 5 title col(10)

set output "./figures/total-split-time-hdd.pdf"
plot [][0:maxy] './data/total-split-time-hdd.dat' using 2:3:xtic(1) lt 3 title col(2),\
        '' using 4:5 lt 4 title col(4), \
        '' using 6:7 lt 1 title col(6), \
        '' using 8:9 lt 2 title col(8), \
        '' using 10:11 lt 5 title col(10)
