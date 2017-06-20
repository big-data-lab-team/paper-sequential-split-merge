#!/bin/bash

for name in buffer-cluster-reads case1 case2 case3-a case3-b case4 case5 case6-a case6-b case7
do
  echo "Exporting ${name}.svg"
  inkscape -D -z --file=figures/${name}.svg --export-pdf=figures/${name}.pdf --export-latex
  sed s,${name}\.pdf,figures/${name}\.pdf,g figures/${name}.pdf_tex > figures/${name}.pdf_tex.new
  \mv figures/${name}.pdf_tex.new figures/${name}.pdf_tex
done
