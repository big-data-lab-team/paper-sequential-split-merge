#!/bin/bash

for name in buffer case1-a case2-a case3 incomplete-rows overlap
do
  #echo "Exporting ${name}.svg"
  inkscape -D -z --file=figures/svg/${name}.svg --export-pdf=figures/svg/${name}.pdf --export-latex
  sed s,${name}\.pdf,figures/svg/${name}\.pdf,g figures/svg/${name}.pdf_tex > figures/svg/${name}.pdf_tex.new
  \mv figures/svg/${name}.pdf_tex.new figures/svg/${name}.pdf_tex
done
