#!/usr/bin/env gnuplot

set terminal pdfcairo color


set border 3 front lt black linewidth 1.000 dashtype solid
set boxwidth 0.75 absolute
set style fill   solid 1.00 border lt -1
set grid nopolar
set grid noxtics nomxtics ytics nomytics noztics nomztics nortics nomrtics \
 nox2tics nomx2tics noy2tics nomy2tics nocbtics nomcbtics
set grid layerdefault   lt 0 linecolor 0 linewidth 0.500,  lt 0 linecolor 0 linewidth 0.500
set key outside right top vertical Left reverse noenhanced autotitle columnhead box lt black linewidth 1.000 dashtype solid
set style histogram columnstacked title textcolor lt -1
set style data histograms
set xtics border in scale 1,0.5 nomirror norotate  autojustify
set xtics  norangelimit
set xtics   ()
set ytics border in scale 0,0 mirror norotate  autojustify
set ztics border in scale 0,0 nomirror norotate  autojustify
set cbtics border in scale 0,0 mirror norotate  autojustify
set rtics axis in scale 0,0 nomirror norotate  autojustify



set key noinvert box
set yrange [0:*]
set ylabel "time(s)" font ", 10"
set xlabel "Mreads break down - on hdd" font ", 10"
set tics scale 0.0
set ytics
unset xtics
set xtics norotate nomirror font ", 10"


set output "./figures/benchmark-mreads/mreads-breakdown-hdd.pdf"
plot [][0:3500] './data/blocks-slices/blocks_slices_avg_hdd.dat' using 3, './data/mreads/mreads_hdd_avg.dat' using 2 ,'' using 3 ,'' using 4, '' using 5, './data/blocks-slices/blocks_slices_avg_hdd.dat' using 2:key(1)

set key noinvert box
set yrange [0:*]
set ylabel "time(s)" font ", 10"
set xlabel "Mreads break down - on ssd" font ", 10"
set tics scale 0.0
set ytics
unset xtics
set xtics norotate nomirror font ", 10"


set output "./figures/benchmark-mreads/mreads-breakdown-ssd.pdf"
plot [][0:3500] './data/blocks-slices/blocks_slices_avg_ssd.dat' using 3, './data/mreads/mreads_ssd_avg.dat' using 2 ,'' using 3 ,'' using 4, '' using 5, './data/blocks-slices/blocks_slices_avg_ssd.dat' using 2:key(1)
