def join_catalogs(*catalogs):
    combined_catalog = []
    for catalog in catalogs:
        combined_catalog.extend(catalog)
    return combined_catalog


catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))


combined_catalog = join_catalogs(catalog1, catalog2)


for product, price in combined_catalog:
    print('Product:', product, '\nPrice:', price, '\n-  -  -  -  -')