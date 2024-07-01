import re

def format_article_to_html(text):
    # Primero, extraemos el año, título y resto del contenido
    year = re.search(r"`(\d{4})`", text).group(1)
    title = re.search(r"\*\*(.*?)\*\*", text).group(1)

    # Extraemos el resto del contenido después del título hasta el primer "|"
    authors_and_journal = text.split("**,")[-1].split("|")[0]

    # Los autores están antes del primer asterisco "*", y los detalles de la publicación están entre los asteriscos "*"
    authors = authors_and_journal.split("*")[0].strip() + ' <em><b><span style="color: #0094C6">' + authors_and_journal.split("*")[1].strip() + '</span></b></em>' + authors_and_journal.split("*")[2].strip()
    publication_details = authors_and_journal.split("*")[3].strip()

    # Manejamos los enlaces al final del texto
    links_section = text.split("|")[1:]
    links_html = ''
    for link in links_section:
        if '[' in link and ']' in link:
            link_text = link.split('[')[1].split(']')[0]
            link_url = link.split('(')[1].split(')')[0]
            links_html += f'<a href="{link_url}" target="_blank">{link_text}</a> | '

    # Limpiar el último "|" sobrante en los enlaces, si existe
    links_html = links_html.strip().rstrip('|').strip()

    # Construir el HTML
    html_output = f'''
<article class="publication">
    <header>
        <time datetime="{year}">{year}</time> |
        <h2><strong>{title}</strong></h2>
        <button class="toggle-button" onclick="toggleDetails(this)"><i class="fa fa-plus-square"></i></button>
    </header>
    <div class="details" style="display:none;">
        <p class="authors">{authors}</p>
        <p class="journal">Published in: <em>{publication_details}</em></p>
        <nav class="links">
            {links_html}
        </nav>
    </div>
</article>
'''
    return html_output

# Test the function with a sample input
input_text = "`2023` **Serum identification of At-Risk MASH: The Metabolomics-Advanced steatohepatitis fibrosis score (MASEF)**, Mazen Noureddin, Emily Truong, Rebeca Mayo, *Ibon Martínez-Arranz*, Itziar Mincholé, Jesus M Banales, Marco Arrese, Kenneth Cusi, María Teresa Arias-Loste, Radan Bruha, Manuel Romero-Gómez, Paula Iruzubieta, Rocio Aller, Javier Ampuero, José Luis Calleja, Luis Ibañez-Samaniego, Patricia Aspichueta, Antonio Marín-Duce, Tatyana Kushner, Pablo Ortiz, Stephen A Harrison, Quentin M Anstee, Javier Crespo, José M Mato, and Arun J Sanyal *Hepatology 79(1):p 135-148, January 2024.* | [doi](https://doi.org/10.1097/hep.0000000000000542) | [pubmed](https://pubmed.ncbi.nlm.nih.gov/37505221/) |"
formatted_html = format_article_to_html(input_text)
print(formatted_html)

# Test the function with a sample input
input_text = """`2023` **Role of Intracellular Drug Disposition in the Response of Acute Myeloid Leukemia to Cytarabine and Idarubicin Induction Chemotherapy**, Gabriela Rodríguez-Macías, Oscar Briz, Candela Cives-Losada, María C. Chillón, Carolina Martínez-Laperche, *Ibon Martínez-Arranz*, Ismael Buño, Marcos González-Díaz, José L. Díez-Martín, Jose J. G. Marin and Rocio I. R. Macias
*Cancers, 2023, 15(12), 3145* | [doi](https://doi.org/10.3390/cancers15123145) | [pubmed](https://pubmed.ncbi.nlm.nih.gov/37370755/) | [pdf](https://www.mdpi.com/2072-6694/15/12/3145/pdf?version=1686470457) |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2022`
**Metabolic subtypes of nonalcoholic fatty liver disease patients exhibit distinctive cardiovascular risk profiles**, *Ibon Martínez-Arranz*, Chiara Bruzzone, Mazen Noureddin, Ruben Gil-Redondo, Itziar Mincholé, Maider Bizkarguenaga, Enara Arretxe, Marta Iruarrizaga-Lejarreta, David Fernández-Ramos, Fernando Lopitz-Otsoa, Rebeca Mayo, Nieves Embade, Elizabeth Newberry, Bettina Mittendorf, Laura Izquierdo-Sánchez, Vaclav Smid, Jorge Arnold, Paula Iruzubieta, Ylenia Pérez Castaño, Marcin Krawczyk, Urko M Marigorta, Martine C Morrison, Robert Kleemann, Antonio Martín-Duce, Liat Hayardeny, Libor Vitek, Radan Bruha, Rocío Aller de la Fuente, Javier Crespo, Manuel Romero-Gomez, Jesus M Banales, Marco Arrese, Kenneth Cusi, Elisabetta Bugianesi, Samuel Klein, Shelly C Lu, Quentin M Anstee, Oscar Millet, Nicholas O Davidson, Cristina Alonso, José M Mato *Hepatology, 2022 Oct 76(4): 1121-1134* | [doi](https://doi.org/10.1002/hep.32427) | [pubmed](https://pubmed.ncbi.nlm.nih.gov/35220605/) | [pdf](https://aasldpubs.onlinelibrary.wiley.com/doi/epdf/10.1002/hep.32427) |  """
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2020`
**The lipidome of endometrial fluid differs between implantative and non-implantative IVF cycles**, Roberto Matorras, *Ibon Martinez-Arranz*, Enara Arretxe, Marta Iruarrizaga-Lejarreta, Blanca Corral, Jone Ibañez-Perez, Antonia Exposito, Begoña Prieto, Felix Elortza, Cristina Alonso
*Journal of Assisted Reproduction and Genetics, 2020 Feb 37(2): 385-394*
| [doi](https://doi.org/10.1007/s10815-019-01670-z) | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/31865491) |  """
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2020`
**A novel serum metabolomic profile for the differential diagnosis if distal cholangiocarcinoma and pancreático ductal adenocarcinoma**, Rocío IR Macías, Luis Muñoz-Bellvis, Anabel Sánchez-Martin, Enara Arretxe, *Ibon Martínez-Arranz*, Ainhoa Lapitz, M Laura Gutiérrez Adelaida La Casta, Cristina Alonso, Luis M González, Matías A Ávila, María L Martinez-Chantar, Rui E Castro, Luis Bujanda, Jesus M Bañales, Jose J.G. Marín.
*Cancers, 2020*.
| [doi](https://doi.org/10.3390/cancers12061433) |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2020`
**Agonist of RORA Attenuates Non-Alcoholic Fatty Liver Progression in Mice via Upregulation of microRNA 122** , Chofit Chai, Bryan Cox, Dayana Yaish,  Devora Gross,  Nofar Rosenberg,  Franck Amblard, Zohar Shemuelian, Maytal Gefen, Amit Korach, Oren Tirosh, Tali Lanton, Henrike Link,  Joseph Tam,  Anna Permikov, Gunes Ozhan, Jonathan Citrin, Haixing Liao, Mirna Tannous, Michal Hahn, Jonathan Axelrod, Enara Arretxe, Cristina Alonso, *Ibon Martinez-Arranz*, Pablo Ortiz Betés, Rifaat Safadi, Ahmad Salhab, Johnny Amer, Zahira Tber, Seema Mengshetti, Hilla Giladi, Raymond F. Schinazi, Eithan Galun
*Gastroenterology, 2020*
| [doi](https://doi.org/10.1053/j.gastro.2020.05.056) |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2020`
**CA19-9 capability as predictor of pancreatic cancer resectability in a Spanish cohort**, Herreros-Villanueva M., Ruiz-Rebollo L., Montes M., Rodriguez-Lopez M., Francisco M., Cubiella J., Iyo E., Garabitos E., Martínez Moneo E., Martos M., de Madaria E., *Martínez-Arranz I*., García-Cougil M., Iglesias-Gómez A., Bujanda L.
*Molecular Biology Report, 2020 Mar 47(3): 1583-1588.*
| [doi](https://doi.org/10.1007/s11033-020-05245-5) | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/31915999) |  """
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2019`
**Metabolomics Discloses a New Non-invasive Method for the Diagnosis and Prognosis of Patients with Alcoholic Hepatitis**, Javier Michelena, Cristina Alonso, *Ibon Martínez-Arranz*, José Altamirano, Rebeca Mayo, Pau Sancho-Bru, Ramón Bataller, Pere Ginès, Azucena Castro, Juan Caballería,
*Annals of Hepatology, Annals of Hepatology, 2019 Feb-Mar 18 (1): 144-154*
| [doi](https://doi.org10.5604/01.3001.0012.7906) | [abstract]() | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/30596625) |  """
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2019`
**Metabolomics discloses potential biomarkers to predict the acute HVPG response to propranolol in patients with cirrhosis**,
Enric Reverter, Juan José Lozano, Cristina Alonso, Annalisa Berzigotti, Susana Seijo, Fanny Turon, Anna Baiges, Mari Luz Martínez-Chantar, José M. Mato, *Ibon Martínez-Arranz*, Vincenzo La Mura, Virginia Hernández-Gea, Jaume Bosch, Juan Carlos García-Pagán,
*Liver International, Jan. 13, 2019*
| [doi](https.//doi.org101111/liv.14042) | [abstract]() | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/30637923) |  """
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2019`
**Plasma miRNAs signature validation for early detection of colorectal cancer**, Marta Herreros-Villanueva, Saray Duran-Sanchon, Ana Carmen Martín, Rosa Pérez-Palacios, Elena Vila-Navarro, María Marcuello, Mireia Diaz-Centeno, Joaquín Cubiella, Maria Soledad Diez, Luis Bujanda, Angel Lanas, Rodrigo Jover, Vicent Hernández, Enrique Quintero, Juan José Lozano, Marta García-Cougil, *Ibon Martínez-Arranz*, Antoni Castells, Meritxell Gironella and Rocio Arroyo
*Clinical and Translational Gastroenterology, Jan. 10, 2019*
| [doi](https://doi.org/10.14309/ctg.0000000000000003) | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6369870/) | [pdf](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6369870/pdf/ct9-10-e00003.pdf) |  """
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2018`
**Serum metabolites as diagnostic biomarkers for cholangiocarcinoma, hepatocellular carcinoma and primary sclerosing cholangitis**,
Jesus M Banales, Mercedes Iñarrairaegui, Ander Arbelaiz, Piotr Milkiewicz, Jordi Muntane, Luis Muñoz‐Bellvis, Adelaida La Casta, Luis M Gonzalez, Enara Arretxe, Cristina Alonso, *Ibon Martínez‐Arranz*, Ainhoa Lapitz, Alvaro Santos‐Laso, Matias A Avila, Maria L Martínez‐Chantar, Luis Bujanda, Jose J G Marin, Bruno Sangro, Rocio I R Macias,
*Hepatology*
| [doi](https://doi.org/10.1002/hep.30319) | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/30325540) |  """
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2018`
**Obeticholic Acid Modulates Serum Metabolites and Gene Signatures Characteristic of Human NASH and Attenuates Inflammation and Fibrosis Progression in Ldlr‐/‐.Leiden Mice**,
Martine C. Morrison, Lars Verschuren, Kanita Salic, Joanne Verheij, Aswin Menke, Peter Y. Wielinga, Marta Iruarrizaga‐Lejarreta, Laurent Gole, Wei‐Miao Yu, Scott Turner, Martien P.M. Caspers, *Ibon Martínez‐Arranz*, Elsbet Pieterman, Reinout Stoop, Arianne van Koppen, Anita M. van den Hoek, José M. Mato, Roeland Hanemaaijer, Cristina Alonso, Robert Kleemann,
*Hepatology Communications, Vol. 2, no. 12, 2018*
| [doi](https://doi.org/10.1002/hep4.1270) | [abstract]() | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/30556039) | [pdf](https://aasldpubs.onlinelibrary.wiley.com/doi/epdf/10.1002/hep4.1270) |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2018`
**Targeted UPLC-MS metabolic analysis of human faeces reveals novel low-invasive candidate markers for colorectal cancer**, Joaquin Cubiella, Marc Clos-Garcia, Cristina Alonso, *Ibon Martínez-Arranz*, Miriam Perez-Cormenzana, Ziortza Barrenetxea, Jesus Berganza, Isabel Rodríguez-Llopis, Mauro D'Amato, Luis Bujanda, Marta Diaz-Ondina, Juan M. Falcón-Pérez,
*Cancers*
| [doi](https://doi.org/10.3390/cancers10090300) | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/30200467) | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6162413/) |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2018`
**Metabolomic-based noninvasive serum tests to diagnose nonalcoholic steatohepatitis: Results from discovery and validation cohorts**, Rebeca Mayo, Javier Crespo, *Ibon Martínez-Arranz*, Jesus M Banales, Mayte Arias, Itziar Mincholé, Rocío Aller de la Fuente, Raúl Jimenez-Agüero, Cristina Alonso, Daniel A de Luis, Libor Vitek, Jan Stritesky, Joan Caballería, Manuel Romero-Gómez, Antonio Martín-Duce, Jose Maria Mugüerza Huguet, José Ignacio Busteros-Buraza, Michael O. Idowu, Azucena Castro, M Luz Martínez-Chantar, Pablo Ortiz, Radan Bruha, Shelly C Lu, Pierre Bedossa, Mazen Noureddin, Arun J. Sanyal, José M Mato,
*Hepatology Communications 2018 Jul; 2(7): 807--820*
| [doi](https://doi.org/10.1002/hep4.1188) | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/30027139) | [pdf](https://aasldpubs.onlinelibrary.wiley.com/doi/epdf/10.1002/hep4.1188) |  """
formatted_html = format_article_to_html(input_text)
print(formatted_html)

input_text = """`2018`
**Use of a Metabolomic Approach to Non-invasively Diagnose Nonalcoholic Fatty Liver Disease in Patients with Type 2 Diabetes Mellitus**,
Fernando Bril, Laura Millán, Srilaxmi Kalavalalli, Michael J. McPhaul, Michael P. Caulfield, *Ibon Martínez-Arranz*, Cristina Alonso, Pablo Ortíz Betes, José M Mato, Kenneth Cusi,
*Diabetes, Obesity and Metabolism*
| [doi](http://dx.doi.org/10.1111/dom.13285) | [abstract](http://onlinelibrary.wiley.com/doi/10.1111/dom.13285/full) | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/29527789 "Use of a Metabolomic Approach to Non-invasively Diagnose Nonalcoholic Fatty Liver Disease in Patients with Type 2 Diabetes Mellitus") | [pdf](https://onlinelibrary.wiley.com/doi/epdf/10.1111/dom.13285 "Use of a Metabolomic Approach to Non-invasively Diagnose Nonalcoholic Fatty Liver Disease in Patients with Type 2 Diabetes Mellitus") |  """
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2017`
**Role of aramchol in steatohepatitis and fibrosis in mice**,
Marta Iruarrizaga-Lejarreta, Marta Varela-Rey, David Fernández-Ramos, *Ibon Martínez-Arranz*, Teresa C Delgado, Jorge Simon, Virginia Gutiérrez-de Juan, Laura delaCruz-Villar, Mikel Azkargorta, José L. Lavin, Rebeca Mayo, Sebastiaan M. Van Liempd, Igor Aurrekoetxea, Xabier Buqué, Donatella Delle Cave, Arantza Peña, Juan Rodríguez-Cuesta, Ana M. Aransay, Felix Elortza, Juan M. Falcón-Pérez, Patricia Aspichueta, Liat Hayardeny, Mazen Noureddin,  Arun J. Sanyal, Cristina Alonso, Juan Anguita, María Luz Martínez-Chantar, Shelly C. Lu, and José M. Mato,
*Hepatology Communications, Volume 1, number 9, November 2017, Pages 911--927*
| [doi](http://dx.doi.org/10.1002/hep4.1107) | [abstract](http://onlinelibrary.wiley.com/doi/10.1002/hep4.1107/abstract) | [html](http://onlinelibrary.wiley.com/doi/10.1002/hep4.1107/full "Role of aramchol in steatohepatitis and fibrosis in mice") | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/29159325 "Role of aramchol in steatohepatitis and fibrosis in mice") | [pdf](http://onlinelibrary.wiley.com/doi/10.1002/hep4.1107/epdf "Role of aramchol in steatohepatitis and fibrosis in mice") |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2017`
**Serum extracellular vesicles contain protein biomarkers for primary sclerosing cholangitis and cholangiocarcinoma**,
Ander Arbelaiz, Mikel Azkargorta, Marcin Krawczyk, Álvaro Santos-Laso, Ainhoa Lapitz, Maria J. Perugorria, Oihane Erice, Esperanza Gonzalez, Raúl Jimenez-Agüero, Adelaida Lacasta, César Ibarra, Alberto Sánchez-Campos, Juan P. Jimeno, Frank Lammert, Piotr Milkiewicz, Marco Marzioni, Rocio I.R. Macias, José J.G.Marín, Tushar Patel, Gregory J. Gores, *Ibon Martinez*, Félix Elortza, Juan M. Falcón-Pérez, Luis Bujanda, and Jesus M. Banales,
*Hepatology, Volume 66, issue 4, October 2017, Pages 1125--1143*
| [doi](http://dx.doi.org/10.1002/hep.29291) | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/28555885 "Serum extracellular vesicles contain protein biomarkers for primary sclerosing cholangitis and cholangiocarcinoma") |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2017`
**A Metabolomics Signature Linked To Liver Fibrosis In The Serum Of Transplanted Hepatitis C Patients**,
Ainara Cano, Zoe Mariño, Oscar Millet, *Ibon Martínez-Arranz*, Miquel Navasa, Juan Manuel Falcón-Pérez, Miriam Pérez-Cormenzana, Joan Caballería, Nieves Embade, Xavier Forns, Jaume Bosch, Azucena Castro & José María Mato,
*Scientific Reports 7, article number: 10497.*
| [doi](https://doi.org/10.1038/s41598-017-10807-y) | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/28874799 "A Metabolomics Signature Linked To Liver Fibrosis In The Serum Of Transplanted Hepatitis C Patients") | [pdf](https://www.nature.com/articles/s41598-017-10807-y.pdf "A Metabolomics Signature Linked To Liver Fibrosis In The Serum Of Transplanted Hepatitis C Patients") |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2017`
**Metabolomic Identification of Subtypes of Nonalcoholic Steatohepatitis**,
Alonso C, Fernández-Ramos D, Varela-Rey M, *Martínez-Arranz I*, Navasa N, Van Liempd SM, Lavin JL, Mayo R, Ilisso CP, de Juan VG, Iruarrizaga-Lejarreta M, delaCruz-Villar L, Mincholé I, Robinson A, Crespo J, Martín-Duce A, Romero-Gomez M, Sann H, Platon J, Van Eyk J, Aspichueta P, Noureddin M, Falcón-Pérez JM, Anguita J, Aransay AM, Martínez-Chantar ML, Lu SC, Mato JM.,
*Gastroenterology, Volume 152, issue 6, May 2017, Pages 1449--1461.e7*
| [doi](http://dx.doi.org/10.1053/j.gastro.2017.01.015) | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/28132890 "Metabolomic Identification of Subtypes of Nonalcoholic Steatohepatitis") | [pdf](http://www.gastrojournal.org/article/S0016-5085(17)30072-0/pdf) |
"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2016`
**Metabolically active extracellular vesicles released from hepatocytes under drug-induced liver-damaging conditions modify serum metabolome and might affect different pathophysiological processes**,
Felix Royo, Laura Palomo, Justyna Mleczko, Esperanza Gonzalez, Cristina Alonso, *Ibon Martínez-Arranz*, Miriam Pérez-Cormenzana, Azucena Castro, Juan M. Falcon-Perez,
*European Journal of Pharmaceutical Sciences, Volume 98, February 2017, Pages 51--57*.
| [doi](http://dx.doi.org/10.1016/j.ejps.2016.10.020 "http://dx.doi.org/10.1016/j.ejps.2016.10.020") | [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/27771515 "Metabolically active extracellular vesicles released from hepatocytes under drug-induced liver-damaging conditions modify serum metabolome and might affect different pathophysiological processes") |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2015`
**Enhancing metabolomics research through data mining**,
*Martínez-Arranz, I.*, Mayo, R., Pérez-Cormenzana, M., Mincholé, I., Salazar, L., Alonso, C., José M Mato,
*Journal of Proteomics, Volume 127 (Part B), September 2015, Pages 275--288*.
| [doi](http://dx.doi.org/10.1016/j.jprot.2015.01.019 "dx.doi.org/10.1016/j.jprot.2015.01.019") | [pubmed](http://www.ncbi.nlm.nih.gov/pubmed/25668325 "Enhancing metabolomics research through data mining") |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2015`
**Data in support of enhancing metabolomics research through data mining**,
*Martínez-Arranz, I.*, Mayo, R., Pérez-Cormenzana, M., Mincholé, I., Salazar, L., Alonso, C., José M Mato,
*Data in Brief, Volume 3, June 2015, Pages 155--164*.
| [doi](http://dx.doi.org/10.1016/j.dib.2015.02.008 "dx.doi.org/10.1016/j.dib.2015.02.008") | [pubmed](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4510074/ "Data in support of enhancing metabolomics research through data mining") | [pdf](http://www.sciencedirect.com/science/article/pii/S2352340915000190/pdfft?md5=0eb6c576f46649571086f2e479cefc66&pid=1-s2.0-S2352340915000190-main.pdf "data in support of enhancing metabolomics research through data mining") | [web application](http://rstudio.owlmetabolomics.com:8031/AgingAnalysis/) |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2013`
**Excess S-adenosylmethionine reroutes phosphatidylethanolamine towards phosphatidylcholine and triglyceride synthesis**,
Maite Martínez-Uña, Marta Varela-Rey, Ainara Cano, Larraitz Fernández-Ares, Naiara Beraza, Igor Aurrekoetxea, *Ibon Martínez-Arranz*, Juan L García-Rodríguez, Xabier Buqué, Daniela Mestre, Zigmund Luka, Conrad Wagner, Cristina Alonso, Richard H Finnell, Shelly C Lu, M Luz Martínez-Chantar, Patricia Aspichueta, José M Mato,
*Hepatology, Octubre de 2013. HEPATOLOGY, Vol. 58, No. 4, 2013*
| [doi](http://dx.doi.org/10.1002/hep.26399 "dx.doi.org/10.1002/hep.26399") | [pubmed](http://www.ncbi.nlm.nih.gov/pubmed/23505042 "Excess S-adenosylmethionine reroutes phosphatidylethanolamine towards phosphatidylcholine and triglyceride synthesis") | [pdf](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3720726/pdf/nihms457099.pdf) |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2013`
**Solute carrier family 2 member 1 (SLC2A1) is involved in the development of nonalcoholic fatty liver disease**,
Vazquez-Chantada, M., Gonzalez-Lahera, A., *Martinez-Arranz, I.*, Garcia-Monzon, C., Maria Regueiro, M., Garcia-Rodriguez, J.L., Karin Anna Schlangen, Mendibil, I., Rodriguez-Ezpeleta, N., Lozano, J.L., Karina Banasik, Johanne M Justesen, Torben Joergensen, Daniel R Witte, Torsten Lauritzen, Torben Hansen, Oluf Pedersen, Nicolas Veyrie, Karine Clement, Joan Tordjman, Albert Tran, Yannik Le Marchand-Brustel, Xabier Buque, Aspichueta, P., Echevarria-Uraga, J.J., Martin-Duce, A., Caballería, J., Philippe Gual, Castro, A., Mato, J.M., Martinez-Chantar, M.L., Aransay, A.M.,
*Hepatology, Febrero de 2013. HEPATOLOGY, Vol. 57, No. 2, 2013*.
| [doi](http://dx.doi.org/10.1002/hep.26052 "dx.doi.org/10.1002/hep.26052") | [pubmed](http://www.ncbi.nlm.nih.gov/pubmed/22961556 "Solute carrier family 2 member 1 (SLC2A1) is involved in the development of nonalcoholic fatty liver disease") |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2012`
**Metabolic profile associated with alcoholic hepatitis and the response to treatment. Preliminary results**,
Javier Michelena, Cristina Alonso, José Altamirano, *Ibon Martínez-Arranz*, Ramón Bataller, MariaLuz Martínez-Chantar, Azucena Castro, Jose M. Mato, Juan Caballería,
*Journal of Hepatology, Volume 56, Supplement 2, Pages S535--S536*.
| [doi](http://dx.doi.org/10.1016/S0168-8278(12)61374-9 "dx.doi.org/10.1016/S0168-8278(12)61374-9") | """
formatted_html = format_article_to_html(input_text)
print(formatted_html)


input_text = """`2012`
**Obesity dependent metabolic signatures associated with nonalcoholic fatty liver disease progression**,
Barr, J., Caballería, J., *Martínez-Arranz, I.*, Domínguez Díez, A., Alonso, C., Muntané, J., Pérez Cormenzana, M., García Monzón, C., Mayo, R., Martín Duce, A., Romero Gómez, M., Lo Iacono, O., Tordjman, J., Andrade, R.J., Pérez Carreras, M., le Marchand Brustel, Y., Tran, A., Fernández Escalante, C., Arévalo, E., García Unzueta, M., Clement, K., Crespo, J., Gual, P.,Gómez Fleitas, M., Martínez Chantar, M.L., Castro, A., S.C. Lu, Vázquez Chantada, M., Mato, J.M.,
*Journal of Proteome Research, Febrero de 2012. J. Proteome Res. 2012, 11, 2521--2532*.
| [doi](http://dx.doi.org/10.1021/pr201223p) | [pubmed](http://www.ncbi.nlm.nih.gov/pubmed/22364559 "Obesity dependent metabolic signatures associated with nonalcoholic fatty liver disease progression") |"""
formatted_html = format_article_to_html(input_text)
print(formatted_html)




