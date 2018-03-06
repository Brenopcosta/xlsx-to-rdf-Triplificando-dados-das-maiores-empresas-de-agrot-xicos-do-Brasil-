import xlrd
def triplifica():
    workbook = xlrd.open_workbook("C:\\Users\\OSMAR COSTA\\Desktop\\AGROTRETA\\agroempresas.xlsx")
    sheet = workbook.sheet_by_index(0)
    arquivo= open("C:\\Users\\OSMAR COSTA\\Desktop\\lean.txt","a")
    for i in range (0,119):
        arquivo.write("<dbpedia:Organization rdf:about=http://www.monocromo.com.br/temp/Empresas.rdf#%d> \n  <foaf:name>%s</foaf:name> \n  <skos:prefLabel>%s</skos:prefLabel> \n  <vcard:Address>%s</vcard:Address> \n  <smg:TelephoneNumber> %s </smg:TelephoneNumber> \n  <dbpedia:owner> %s </dbpedia:owner>  \n  <vcard:email> %s </vcard:email>  \n  <foaf:document> %s </foaf:document> \n  <gn:locationMap>%s</gn:locationMap>  \n</dbpedia:Organization>  \n\n\n" %(sheet.cell_value(i,0),sheet.cell_value(i,1),sheet.cell_value(i,2),sheet.cell_value(i,3),sheet.cell_value(i,4),sheet.cell_value(i,5),sheet.cell_value(i,6),sheet.cell_value(i,7),sheet.cell_value(i,8)))
    arquivo.close()
    return



