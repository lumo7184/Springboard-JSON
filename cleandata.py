data = [{ "_id" : { "$oid" : "52b213b38594d8a2be17c780" },
 "boardapprovaldate" : "2013-11-12T00:00:00Z", 
 "borrower" : {"FEDERAL DEMOCRATIC REPUBLIC OF ETHIOPIA"},
 "closingdate" : {"2018-07-07T00:00:00Z"}, 
 "country_namecode" : {"Federal Democratic Republic of Ethiopia!$!ET"},
 "countrycode" : {"ET"}, 
 "countryname" : {"Federal Democratic Republic of Ethiopia"}, 
 "countryshortname" : {"Ethiopia"}, 
 "docty" : {"Project Information Document,Indigenous Peoples Plan,Project Information Document"},
"impagency" : {"MINISTRY OF EDUCATION"}, 
"lendinginstr" : {"Investment Project Financing"}, 
"lendinginstrtype" : {"IN"}, 
"lendprojectcost" : {550000000}, 
"majorsector_percent" :
     [ { "Name" : "Education", "Percent" : 46 }, 
     { "Name" : "Education", "Percent" : 26 }, 
     { "Name" : "Public Administration, Law, and Justice","Percent" : 16 },
      { "Name" : "Education", "Percent" : 12 } ],
"mjsector_namecode" : [ { "name" : "Education", "code" : "EX" },
                        { "name" : "Education", "code" : "EX" },
                        { "name" : "Public Administration, Law, and Justice", "code" : "BX" }, 
                        { "name" : "Education", "code" : "EX" }]}]

 json_normalize(data, ['_id', ['boardapprovaldate'], 'borrower', 'closingdate', 'country_namecode', 'countrycode', 'countryname', 'countryshortname', 'docty', 'impagency', 'lendinginstr', 'lendinginstrtype', 'lendprojectcost', 'majorsector_percent', ['Name', 'Education', 'Percent']])
