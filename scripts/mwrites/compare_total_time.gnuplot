#!/usr/bin/env gnuplot

set terminal pdfcairo color
set border 3 front lt black linewidth 1.000 dashtype solid
set boxwidth 0.5 absolute
set style fill solid 0.50 border lt -1

unset key
set pointsize 0.5

set style data boxplot
set xtics border in scale 0,0 nomirror norotate  autojustify
set xtics  norangelimit

set xtics("naive-blocks" 1, "3g-mwrites" 2, "6g-mwrites" 3, "9g-mwrites" 4, "12g-mwrites" 5, "naive-slices" 6)
unset format y
unset ydata
unset xrange
unset logscale x
unset format x
set boxwidth 0.5
set xtics font ", 10"
set xlabel "Split strategy - Comparision between multiple writes and naive blocks, slices on HDD" font ",10"
set ylabel "Total Time (s)" font ",10"
set output "./figures/benchmark-mwrites/mwrites-comparision-hdd.pdf"
#plot '../../data/blocks-slices/totaltime.dat' using (1):7 , '' using (6):6 , '../../data/mreads/mreads_hdd.dat' using (2):5 , '' using (3):10 , '' using (4):15 , '' using (5):20
plot './data/mwrites/mwrites_hdd.dat' using (2):5 , '' using (3):10 , '' using (4):15 , '' using (5):20


set xtics ("naive-blocks" 1, "3g-mwrites" 2, "6g-mwrites" 3, "9g-mwrites" 4, "12g-mwrites" 5, "naive-slices" 6)
unset format y
unset ydata
unset xrange
unset logscale x
unset format x
set boxwidth 0.5
set xtics font ", 10"
set xlabel "Split strategy - Comparision between multiple writes and naive blocks, slices on SSD" font ",10"
set ylabel "Total Time (s)" font ",10"
set output "./figures/benchmark-mwrites/mwrites-comparision-ssd.pdf"
#plot '../../data/blocks-slices/totaltime.dat' using (1):2 , '' using (6):1 , '../../data/mreads/mreads_ssd.dat' using (2):5 , '' using (3):10 , '' using (4):15 , '' using (5):20
plot './data/mwrites/mwrites_ssd.dat' using (2):5 , '' using (3):10 , '' using (4):15 , '' using (5):20
