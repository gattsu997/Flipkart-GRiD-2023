import json



class_mapping_list = [
    ('male', ['Men']),
    ('man', ['Men']),
    ('boy', ['Boys']),
    ('guy', ['Men']),
    ('gentleman', ['Men']),
    ('female', ['Women']),
    ('woman', ['Women']),
    ('girl', ['Girls']),
    ('lady', ['Women']),
    ('clothing', ['Apparel']),
    ('apparel', ['Apparel']),
    ('outfit', ['Apparel']),
    ('dress', ['Apparel']),
    ('wear', ['Apparel']),
    ('attire', ['Apparel']),
    ('accessory', ['Accessories']),
    ('accessories', ['Accessories']),
    ('shoe', ['Footwear', 'Shoes', 'Casual Shoes', 'Sports Shoes']),
    ('footwear', ['Footwear']),
    ('personal care', ['Personal Care']),
    ('beauty', ['Personal Care']),
    ('skin care', ['Personal Care']),
    ('cosmetic', ['Personal Care']),
    ('sporting goods', ['Sporting Goods']),
    ('sports', ['Sporting Goods']),
    ('home', ['Home']),
    ('shirt', ['Topwear']),
    ('t-shirt', ['Topwear']),
    ('tee', ['Topwear']),
    ('top', ['Topwear']),
    ('blouse', ['Topwear']),
    ('jeans', ['Bottomwear']),
    ('pant', ['Bottomwear','Jeans','Pants']),
    ('trousers', ['Bottomwear']),
    ('watch', ['Watches']),
    ('timepiece', ['Watches']),
    ('sock', ['Socks']),
    ('sneaker', ['Shoes', 'Casual Shoes']),
    ('flip flop', ['Flip Flops']),
    ('bag', ['Bags']),
    ('handbag', ['Bags']),
    ('purse', ['Bags']),
    ('innerwear', ['Innerwear']),
    ('underwear', ['Innerwear']),
    ('lingerie', ['Innerwear']),
    ('fragrance', ['Fragrance']),
    ('perfume', ['Fragrance']),
    ('jewellery', ['Jewellery']),
    ('necklace', ['Jewellery']),
    ('earrings', ['Jewellery']),
    ('lipstick', ['Lips']),
    ('lip gloss', ['Lips']),
    ('saree', ['Saree']),
    ('eyewear', ['Eyewear']),
    ('sunglasses', ['Eyewear']),
    ('scarf', ['Scarves']),
    ('dress', ['Dress']),
    ('gown', ['Dress']),
    ('robe', ['Loungewear and Nightwear']),
    ('nightwear', ['Loungewear and Nightwear']),
    ('pajama', ['Loungewear and Nightwear']),
    ('loungewear', ['Loungewear and Nightwear']),
    ('wallet', ['Wallets']),
    ('money holder', ['Wallets']),
    ('apparel set', ['Apparel Set']),
    ('headwear', ['Headwear']),
    ('hat', ['Headwear']),
    ('cap', ['Headwear']),
    ('muffler', ['Mufflers']),
    ('scarf', ['Scarves']),
    ('skin care', ['Skin Care']),
    ('makeup', ['Makeup']),
    ('cosmetics', ['Makeup']),
    ('gift', ['Free Gifts']),
    ('present', ['Free Gifts']),
    ('tie', ['Ties']),
    ('necktie', ['Ties']),
    ('accessory', ['Accessories']),
    ('water bottle', ['Water Bottle']),
    ('hydration container', ['Water Bottle']),
    ('umbrella', ['Umbrellas']),
    ('rain shield', ['Umbrellas']),
    ('wristband', ['Wristbands']),
    ('bracelet', ['Wristbands']),
    ('Kurta', ['Men']),
    ('Kurtas', ['Men']),
    ('sherwani', ['Men']),
    ('dhoti', ['Men']),
    ('dhotis', ['Men']),
    ('lungis', ['Men']),
    ('modi jacket', ['Men']),
    ('nehru jacket', ['Men']),
    ('Thermals', ['Unisex']),
    ('boxers', ['Unisex']),
    ('bottoms', ['Unisex']),
    ('vests', ['Unisex']),
    ('trunks', ['Unisex']),
    ('Sweater', ['Unisex']),
    ('Jacket', ['Unisex']),
    ('Sweatshirt', ['Unisex']),
    ('Kurtis', ['Women']),
    ('Tunics', ['Women']),
    ('Tops', ['Women']),
    ('Saree', ['Women']),
    ('Ethnic', ['Women']),
    ('Leggings', ['Women']),
    ('Salwar', ['Women']),
    ('Churidar', ['Women']),
    ('Skirts', ['Women']),
    ('Plazzo', ['Women']),
    ('Lehenga', ['Women']),
    ('Choli', ['Women']),
    ('Dupatta', ['Women']),
    ('Shawls', ['Women']),
    ('Blazer', ['Women']),
    ('Waist-Coat', ['Women']),
    ('Jumpsuit', ['Women']),
    ('Capris', ['Women']),
    ('jooti', ['Footwear']),
    ('jhumkas', ['Wearables']),
    ('payals', ['Wearables']),
    ('maang tikka', ['Wearables']),
    ('nath', ['Wearables']),
    ('bangles', ['Wearables']),
    ('kadas', ['Wearables']),
    ('churis', ['Wearables']),
    ('anklets', ['Wearables']),
    ('necklace', ['Wearables']),
    ('choker', ['Wearables']),
    ('haars', ['Wearables']),
    ('earrings', ['Wearables']),
    ('rings', ['Wearables']),
    ('bracelets', ['Wearables']),
    ('armlets', ['Wearables']),
    ('maang patti', ['Wearables']),
    ('bajubandh', ['Wearables']),
    ('chandbali', ['Wearables']),
    ('kamarbandh', ['Wearables']),
    ('hathphool', ['Wearables']),
    ('ankle chains', ['Wearables']),
    ('jadau', ['Wearables']),
    ('polki', ['Wearables']),
    ('temple jewelry', ['Wearables']),
    ('kundan', ['Wearables']),
    ('Diwali', ['Ethnic']),
    ('Holi', ['Ethnic']),
    ('Eid', ['Ethnic']),
    ('Navratri', ['Ethnic']),
    ('Pongal', ['Ethnic']),
    ('Baisakhi', ['Ethnic']),
    ('Onam', ['Ethnic']),
    ('Ganesh Chaturthi', ['Ethnic']),
    ('Raksha Bandhan', ['Ethnic']),
    ('Durga Puja', ['Ethnic']), ('Lohri', ['Ethnic']),
    ('Bihu', ['Ethnic']),
    ('Gudi Padwa', ['Ethnic']),
    ('Makar Sankranti', ['Ethnic']),
    ('Puthandu', ['Ethnic']),
    ('Ugadi', ['Ethnic']),
    ('Vishu', ['Ethnic']),
    ('Bathukamma', ['Ethnic']),
    ('Chhath Puja', ['Ethnic']),
    ('Pongal', ['Ethnic']), ('Birthday', ['Ethnic']),
    ('Wedding', ['Ethnic']),
    ('Anniversary', ['Ethnic']),
    ('Baby Shower', ['Ethnic']),
    ('Engagement', ['Ethnic']),
    ('Sangeet', ['Ethnic']),
    ('Mehendi', ['Ethnic']),
    ('Sangeet', ['Ethnic']),
    ('Sangeet', ['Ethnic']),
    ('Sangeet', ['Ethnic']),
    ('Graduation', ['Ethnic']),
    ('Retirement', ['Ethnic']),
    ('voucher', ['Vouchers']),
    ('coupon', ['Vouchers']),
    ('shirt', ['Shirts']),
    ('t-shirt', ['Tshirts']),
    ('tee', ['Tshirts']),
    ('polo', ['Shirts']),
    ('jeans', ['Jeans']),
    ('watch', ['Watches']),
    ('timepiece', ['Watches']),
    ('track pants', ['Track Pants']),
    ('trouser', ['Bottomwear']),
    ('pants', ['Bottomwear']),
    ('tights', ['Bottomwear']),
    ('sock', ['Socks']),
    ('sneaker', ['Casual Shoes']),
    ('belt', ['Belts']),
    ('flip flop', ['Flip Flops']),
    ('handbag', ['Handbags']),
    ('bag', ['Bags']),
    ('purse', ['Bags']),
    ('top', ['Tops']),
    ('blouse', ['Tops']),
    ('bra', ['Bra']),
    ('sandal', ['Sandals']),
    ('sweatshirt', ['Sweatshirts']),
    ('deodorant', ['Deodorant']),
    ('formal shoe', ['Formal Shoes']),
    ('bracelet', ['Bracelet']),
    ('lipstick', ['Lipstick']),
    ('lip gloss', ['Lip Gloss']),
    ('flat', ['Flats']),
    ('kurta', ['Kurtas']),
    ('waistcoat', ['Waistcoat']),
    ('sports shoe', ['Sports Shoes']),
    ('shorts', ['Shorts']),
    ('briefs', ['Briefs']),
    ('saree', ['Sarees']),
    ('perfume', ['Perfume and Body Mist']),
    ('heeled shoe', ['Heels']),
    ('heel', ['Heels']),
    ('sunglasses', ['Sunglasses']),
    ('innerwear', ['Innerwear Vests']),
    ('nail polish', ['Nail Polish']),
    ('laptop bag', ['Laptop Bag']),
    ('scarf', ['Scarves']),
    ('rain jacket', ['Rain Jacket']),
    ('dress', ['Dresses']),
    ('night suit', ['Night suits']),
    ('skirt', ['Skirts']),
    ('wallet', ['Wallets']),
    ('blazer', ['Blazers']),
    ('ring', ['Ring']),
    ('kurti', ['Kurtis']),
    ('clutch', ['Clutches']),
    ('shrug', ['Shrug']),
    ('backpack', ['Backpacks']),
    ('cap', ['Caps']),
    ('trouser', ['Trousers']),
    ('pants', ['Trousers']),
    
    ('earrings', ['Earrings']),
    ('camisole', ['Camisoles']),
    ('boxer', ['Boxers']),
    ('jewellery set', ['Jewellery Set']),
    ('dupatta', ['Dupatta']),
    ('lipstick', ['Lipstick']),
    ('bath robe', ['Bath Robe']),
    ('muffler', ['Mufflers']),
    ('tunic', ['Tunics']),
    ('jacket', ['Jackets']),
    ('trunk', ['Trunk']),
    ('lounge pant', ['Lounge Pants']),
    ('face wash', ['Face Wash and Cleanser']),
    ('necklace', ['Necklace and Chains']),
    # ... (continued for the rest of the mappings)
    ('duffel bag', ['Duffel Bag']),
    ('sports sandal', ['Sports Sandals']),
    ('foundation', ['Foundation and Primer']),
    ('sweater', ['Sweaters']),
    ('gift', ['Free Gifts']),
    ('trolley bag', ['Trolley Bag']),
    ('tracksuit', ['Tracksuits']),
    ('swimwear', ['Swimwear']),
    ('shoe laces', ['Shoe Laces']),
    ('fragrance', ['Fragrance Gift Set']),
    ('bangle', ['Bangle']),
    ('nightdress', ['Nightdress']),
    ('tie', ['Ties']),
    ('baby doll', ['Baby Dolls']),
    ('leggings', ['Leggings']),
    ('highlighter', ['Highlighter and Blush']),
    ('travel accessory', ['Travel Accessory']),
    ('kurta', ['Kurtis']),
    ('mobile pouch', ['Mobile Pouch']),
    ('messenger bag', ['Messenger Bag']),
    ('lip care', ['Lip Care']),
    ('face moisturizer', ['Face Moisturisers']),
    ('compact', ['Compact']),
    ('eye cream', ['Eye Cream']),
    ('accessory', ['Accessory Gift Set']),
    ('beauty accessory', ['Beauty Accessory']),
    ('jumpsuit', ['Jumpsuit']),
    ('kajal', ['Kajal and Eyeliner']),
    ('water bottle', ['Water Bottle']),
    ('suspenders', ['Suspenders']),
    ('lip liner', ['Lip Liner']),
    ('robe', ['Robe']),
    ('salwar', ['Salwar']),
    ('dupatta', ['Dupatta']),
    ('patiala', ['Patiala']),
    ('stockings', ['Stockings']),
    ('eyeshadow', ['Eyeshadow']),
    ('headband', ['Headband']),
    ('tights', ['Tights']),
    ('nail essentials', ['Nail Essentials']),
    ('churidar', ['Churidar']),
    ('lounge t-shirt', ['Lounge Tshirts']),
    ('face scrub', ['Face Scrub and Exfoliator']),
    ('lounge short', ['Lounge Shorts']),
    ('gloves', ['Gloves']),
    ('mask', ['Mask and Peel']),
    ('wristband', ['Wristbands']),
    ('tablet sleeve', ['Tablet Sleeve']),
    ('tie', ['Ties']),
    ('football', ['Footballs']),
    ('stole', ['Stoles']),
    ('shapewear', ['Shapewear']),
    ('nehru jacket', ['Nehru Jackets']),
    ('salwar', ['Salwar']),
    ('cufflinks', ['Cufflinks']),
    ('jeggings', ['Jeggings']),
    ('hair color', ['Hair Colour']),
    ('concealer', ['Concealer']),
    ('romper', ['Rompers']),
    ('body lotion', ['Body Lotion']),
    ('sunscreen', ['Sunscreen']),
    ('booties', ['Booties']),
    ('waist pouch', ['Waist Pouch']),
    ('hair accessory', ['Hair Accessory']),
    ('rucksack', ['Rucksacks']),
    ('basketball', ['Basketballs']),
    ('lehenga choli', ['Lehenga Choli']),
    ('clothing set', ['Clothing Set']),
    ('mascara', ['Mascara']),
    ('toner', ['Toner']),
    ('cushion cover', ['Cushion Covers']),
    ('key chain', ['Key chain']),
    ('makeup remover', ['Makeup Remover']),
    ('lip plumper', ['Lip Plumper']),
    ('umbrella', ['Umbrellas']),
    ('face serum', ['Face Serum and Gel']),
    ('hat', ['Hat']),
    ('grooming kit', ["Men's Grooming Kit"]),
    ('rain trouser', ['Rain Trousers']),
    ('body wash', ['Body Wash and Scrub']),
    ('suit', ['Suits']),
    ('ipad', ['Ipad'])
]



# Specify the path to the JSON file
json_file_path = 'class_mapping_list.json'

# Write the list to the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(class_mapping_list, json_file)

print(f"Data written to {json_file_path}")
