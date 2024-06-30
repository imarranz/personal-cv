#!/bin/bash

rm *.pdf
rm *.html

mym=$(date +'%B')

#echo 'La variables es:'
#echo $mym

MES=$(LANG=es_ES.UTF-8; date +"%B")
MES=$(LANG=en_EN.UTF-8; date +"%B")

echo $MES

cp './cv/000_Introduction.md' './000_Introduction.md'
cp './cv/011_Professional_Experience.md' './011_Professional_Experience.md'
cp './cv/021_Education.md' './021_Education.md'
cp './cv/022_Complementary_Education.md' './022_Complementary_Education.md'
cp './cv/031_Computer_Skills.md' './031_Computer_Skills.md'
cp './cv/032_Software_Development.md' './032_Software_Development.md'
cp './cv/041_Publications.md' './041_Publications.md'
cp './cv/051_R&D_Projects.md' './051_R&D_Projects.md'
cp './cv/061_Patents.md' './061_Patents.md'
cp './cv/071_Congress.md' './071_Congress.md'
cp './cv/081_Personal.md' './081_Personal.md'

pandoc \
	      '000_Introduction.md' \
	      '011_Professional_Experience.md' \
	      '021_Education.md' \
	      '022_Complementary_Education.md' \
	      '031_Computer_Skills.md' \
	      '032_Software_Development.md' \
	      '041_Publications.md' \
	      '051_R&D_Projects.md' \
	      '061_Patents.md' \
	      '071_Congress.md' \
	      '081_Personal.md' \
	      -f markdown -t html -s -c './css/cv.css' --self-contained -o 'Ibon Martínez-Arranz CV - '$(date +%Y%m%d)'.html'

/usr/bin/printf """
--- 
title: 
- type: main
  text: Ibon Martínez-Arranz
- type: subtitle
  text: Currículum Vitae
creator:
- role: author
  text: Ibon Martínez-Arranz
date: 2022-09-02
lang: en-EN
---
""" > "Ibon Martinez-Arranz CV.md"

cat '000_Introduction.md' >> "Ibon Martinez-Arranz CV.md"
cat '011_Professional_Experience.md' >> "Ibon Martinez-Arranz CV.md"
cat '021_Education.md' >> "Ibon Martinez-Arranz CV.md"
cat '022_Complementary_Education.md' >> "Ibon Martinez-Arranz CV.md"
cat '031_Computer_Skills.md' >> "Ibon Martinez-Arranz CV.md"
cat '032_Software_Development.md' >> "Ibon Martinez-Arranz CV.md"
cat '041_Publications.md' >> "Ibon Martinez-Arranz CV.md"
cat '051_R&D_Projects.md' >> "Ibon Martinez-Arranz CV.md"
cat '061_Patents.md' >> "Ibon Martinez-Arranz CV.md"
cat '071_Congress.md' >> "Ibon Martinez-Arranz CV.md"
cat '081_Personal.md' >> "Ibon Martinez-Arranz CV.md"
	      
pandoc \
	      'Ibon Martinez-Arranz CV.md' \
	      -f markdown -t epub -s -c './css/cv.css' --self-contained -o 'Ibon Martinez-Arranz CV.epub'	      

./wkhtmltox/bin/wkhtmltopdf -L 20 -R 20 -T 30 -B 30 \
	      --title 'Ibon Martínez-Arranz, CV' \
	      --footer-font-size 8 --no-footer-line --footer-spacing 10 \
	      --footer-center [fecha] \
	      --footer-right 'page [page] of [topage]' \
	      --header-font-size 8 --no-header-line --header-spacing 10 \
	      --header-right "Ibon Martínez-Arranz" \
	      --replace fecha '- '$MES' '$(date +%d)', '$(date +%Y)' -' \
	      --zoom 1 \
	      'Ibon Martínez-Arranz CV - '$(date +%Y%m%d)'.html' 'Ibon Martínez-Arranz CV - '$(date +%Y%m%d)'.pdf'
      
./wkhtmltox/bin/wkhtmltopdf -L 20 -R 20 -T 30 -B 30 \
	      --title 'Ibon Martínez-Arranz, CV' \
	      --footer-font-size 8 --no-footer-line --footer-spacing 10 \
	      --footer-center [fecha] \
	      --footer-right 'page [page] of [topage]' \
	      --header-font-size 8 --no-header-line --header-spacing 10 \
	      --header-right "Ibon Martínez-Arranz" \
	      --replace fecha '- '$MES' '$(date +%d)', '$(date +%Y)' -' \
	      --zoom 1 \
	      'Ibon Martínez-Arranz CV - '$(date +%Y%m%d)'.html' 'Ibon Martinez-Arranz CV.pdf'      

python ./code/last_five_years.py

pandoc \
	      '000_Introduction.md' \
	      '011_Professional_Experience.md' \
	      '021_Education.md' \
	      '022_Complementary_Education.md' \
	      '031_Computer_Skills.md' \
	      '032_Software_Development.md' \
	      '041_Publications_last_five_years.md' \
	      '051_R&D_Projects.md' \
	      '061_Patents.md' \
	      '071_Congress_last_five_years.md' \
	      '081_Personal.md' \
	      -f markdown -t html -s -c './css/cv.css' --self-contained -o 'Ibon Martínez-Arranz CV (5y) - '$(date +%Y%m%d)'.html'	      

./wkhtmltox/bin/wkhtmltopdf -L 20 -R 20 -T 30 -B 30 \
	      --title 'Ibon Martínez-Arranz, CV' \
	      --footer-font-size 8 --no-footer-line --footer-spacing 10 \
	      --footer-center [fecha] \
	      --footer-right 'page [page] of [topage]' \
	      --header-font-size 8 --no-header-line --header-spacing 10 \
	      --header-right "Ibon Martínez-Arranz" \
	      --replace fecha '- '$MES' '$(date +%d)', '$(date +%Y)' -' \
	      --zoom 1 \
	      'Ibon Martínez-Arranz CV (5y) - '$(date +%Y%m%d)'.html' 'Ibon Martinez-Arranz CV (5y).pdf'    	      
	      
     
rm "000_Introduction.md"
rm "011_Professional_Experience.md"
rm "021_Education.md"
rm "022_Complementary_Education.md"
rm "031_Computer_Skills.md"
rm "032_Software_Development.md"
rm "041_Publications.md"
rm "041_Publications_last_five_years.md"
rm "051_R&D_Projects.md"
rm "061_Patents.md"
rm "071_Congress.md"
rm "071_Congress_last_five_years.md"
rm "081_Personal.md"


# BIOSKETCH


cp './cv/091_Biosketch.md' './091_Biosketch.md'

pandoc \
	      '11_Biosketch.md' \
	      -f markdown -t html -s -c './css/cv.css' --self-contained -o 'Ibon Martínez-Arranz Biosketch - '$(date +%Y%m%d)'.html'

	      
mym=$(date +'%B')

#echo 'La variables es:'
#echo $mym

MES=$(LANG=es_ES.UTF-8; date +"%B")
MES=$(LANG=en_EN.UTF-8; date +"%B")

echo $MES

./wkhtmltox/bin/wkhtmltopdf -L 20 -R 20 -T 30 -B 30 \
	      --title 'Ibon Martínez-Arranz, Biosketch' \
	      --footer-font-size 8 --no-footer-line --footer-spacing 10 \
	      --footer-center [fecha] \
	      --footer-right 'page [page] of [topage]' \
	      --header-font-size 8 --no-header-line --header-spacing 10 \
	      --header-right "Ibon Martínez-Arranz" \
	      --replace fecha '- '$MES' '$(date +%d)', '$(date +%Y)' -' \
	      --zoom 1 \
	      'Ibon Martínez-Arranz Biosketch - '$(date +%Y%m%d)'.html' 'Ibon Martínez-Arranz Biosketch - '$(date +%Y%m%d)'.pdf'
      
#mv 'Ibon Martínez CV - '$(date +%Y%m%d)'.html' '/media/imarranz/TOSHIBA EXT/Documentos/CV/CV/cv_markdown/tex/Ibon Martínez CV - '$(date +%Y%m%d)'.html'

#pandoc -H \
#	      './tex/Ibon Martínez-Arranz Biosketch.tex' \
#	      './tex/Ibon Martínez-Arranz Biosketch - '$(date +%Y%m%d)'.html' \
#	      -o './tex/Ibon Martínez-Arranz Biosketch - '$(date +%Y%m%d)'.pdf'
     
rm "091_Biosketch.md"

