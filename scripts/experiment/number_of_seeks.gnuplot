#!/usr/bin/env gnuplot

set terminal pdf color font ',10'
a=0.1
set boxwidth a
set style fill transparent solid 0.5 border rgb "black"
set xtics ("3" 1, "6" 2, "9" 3, "12" 4)
set xlabel "Memory (GB)"
set ylabel "Number of seeks"

set logscale y
set xtics ("0.6" 0, "3" 1, "6" 2, "9" 3, "12" 4, "16" 5)

set output "./figures/number-of-seeks.pdf"
plot [0-4*a:5+5*a][1:]\
                 './data/creads/creads_ssd.dat'\
		                      using (0-2*a):4 w boxes lt 3 title "Naive blocks",\
    	         './data/seeks-model.dat'\
				      using (0-a):1 w boxes lt 3 fs transparent notitle,\
                 './data/buff-slices/buff-slices_ssd.dat'\
		                      using (0):4 w boxes lt 4 title "Naive slices",\
    	         './data/seeks-model.dat'\
   				      using (a):11 w boxes lt 4 fs transparent notitle,\
                 './data/creads/creads_ssd.dat'\
                                      using (1-2*a):9 w boxes lt 1 title "Cluster reads",\
				   '' using (2-2*a):14 w boxes lt 1 notitle,\
				   '' using (3-2*a):19 w boxes lt 1 notitle,\
				   '' using (4-2*a):24 w boxes lt 1 notitle,\
   				   '' using (5-2*a):29 w boxes lt 1 notitle,\
                 './data/seeks-model.dat'\
		                      using (1-a):2 w boxes lt 1 fs transparent notitle,\
	                           '' using (2-a):3 w boxes lt 1 fs transparent notitle,\
				   '' using (3-a):4 w boxes lt 1 fs transparent notitle,\
				   '' using (4-a):5 w boxes lt 1 fs transparent notitle,\
				   '' using (5-a):6 w boxes lt 1 fs transparent notitle,\
	   	 './data/mreads/mreads_hdd.dat'\
		                      using (1):4 w boxes lt 2 title "Multiple reads",\
     	    			   '' using (2):9 w boxes lt 2 notitle,\
				   '' using (3):14 w boxes lt 2 notitle,\
				   '' using (4):19 w boxes lt 2 notitle,\
				   '' using (5):24 w boxes lt 2 notitle,\
    	         './data/seeks-model.dat'\
				   using (1+a):7 w boxes lt 2 fs transparent notitle,\
	                           '' using (2+a):8 w boxes lt 2 fs transparent notitle,\
				   '' using (3+a):9 w boxes lt 2 fs transparent notitle,\
				   '' using (4+a):10 w boxes lt 2 fs transparent notitle,\
				   '' using (5+a):11 w boxes lt 2 fs transparent notitle,\
                 './data/buff-slices/buff-slices_ssd.dat'\
			              using (1+2*a):9 lt 5 w boxes title "Buffered slices",\
    	                           '' using (2+2*a):14 lt 5 w boxes notitle	,\
       	                           '' using (3+2*a):19 lt 5 w boxes notitle	,\
       	                           '' using (4+2*a):24 lt 5 w boxes notitle	,\
				   '' using (5+2*a):29 lt 5 w boxes notitle	,\
      	         './data/seeks-model.dat'\
				   using (1+3*a):13 w boxes lt 5 fs transparent notitle,\
	                           '' using (2+3*a):14 w boxes lt 5 fs transparent notitle,\
				   '' using (3+3*a):15 w boxes lt 5 fs transparent notitle,\
				   '' using (4+3*a):16 w boxes lt 5 fs transparent notitle,\
   				   '' using (5+3*a):17 w boxes lt 5 fs transparent notitle

