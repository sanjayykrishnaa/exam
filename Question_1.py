"""
create a new  array of dictionary by extracting data from data,json
new dictionay thus created should be as shown below


[
    {
     "name": "Organic Honeycrisp Apples Bag",
     "categories": ["Produce","Fruits","Apples",
     "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
     "base_price":0.64,
     "availability_status":true
    },
    {
     "name": "Granny Smith Apples",
     "categories": ["Produce","Fruits","Apples",
     "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
     "base_price":0.64,
     "availability_status":true
    }
    .
    .
    .
    .
    
]


Remember to extract all items above illustrated are just sample
"""


import json


with open("data.json","r") as file:
    content = file.read()
    data = json.loads(content)
    
    items = data["items"]
    
    extracted_array = []
    
    for item in items:
        products = {"Name : ": item["name"], "Category : ": item["categories"], "Image : " : item["images"], "Price : " : item["base_price"], "Availability : " : item["availability_status"]}

        # print(products)
        
        
        extracted_array.append(products)
        print(extracted_array)
        
        


