from pyzotero import zotero

api_key="ItQRKf7vSZhubttQ28OE2eUy"
library_type="user"
library_id="7483450"
print("Hello World")
zot = zotero.Zotero(library_id, library_type, api_key)
print(zot)
items = zot.top(limit=5)
print(items)
# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
for item in items:
    print("hola")
    print(item['data'])
   # print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))