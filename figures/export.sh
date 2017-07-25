#!/bin/bash

for name in buffer case1-a case2-a case3 incomplete-rows overlap
do
  echo "Exporting ${name}.svg"
  inkscape -D -z --file=figures/${name}.svg --export-pdf=figures/${name}.pdf --export-latex
  sed s,${name}\.pdf,figures/${name}\.pdf,g figures/${name}.pdf_tex > figures/${name}.pdf_tex.new
  \mv figures/${name}.pdf_tex.new figures/${name}.pdf_tex
done
