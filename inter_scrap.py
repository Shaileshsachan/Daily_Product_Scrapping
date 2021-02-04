import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv
import pandas as pd
# FLIPKART
flipkart_dict = {
'Amul_Milk': 'https://www.flipkart.com/amul-taaza-homogenised-toned-milk/p/itmexak2hfpzbuhf?pid=MLKEUGQGM65M2QZC&lid=LSTMLKEUGQGM65M2QZCF9AHJM&marketplace=GROCERY&fm=productRecommendation%2Fsimilar&iid=R%3As%3Bp%3AMLKFG9T8CBZD8G9G%3Bl%3ALSTMLKFG9T8CBZD8G9GVNBZGI%3Bpt%3App%3Buid%3A7d78f97a-5fa3-11eb-b8f3-759015255b6e%3B.MLKEUGQGM65M2QZC&ppt=pp&ppn=pp&ssid=5jmpa8xdts0000001611562994947&otracker=pp_reco_Similar%2BProducts_2_32.productCard.PMU_HORIZONTAL_Amul%2BTaaza%2BHomogenised%2BToned%2BMilk_MLKEUGQGM65M2QZC_productRecommendation%2Fsimilar_1&otracker1=pp_reco_PINNED_productRecommendation%2Fsimilar_Similar%2BProducts_GRID_productCard_cc_2_NA_view-all&cid=MLKEUGQGM65M2QZC',
'Potatoes':'https://www.flipkart.com/potato-1-kg/p/itmf7fj5bggbzzs7?gclid=CjwKCAiA9bmABhBbEiwASb35VxNl5degOkN33jNdIdi6nSD4RP0wi2FaJUrZeCFtUte8_eWSBqdXqRoC8E0QAvD_BwE&pid=VEGF7FJ552GQ3ZGT&lid=LSTVEGF7FJ552GQ3ZGTJRMA2W&marketplace=GROCERY&cmpid=content_vegetable_730597647_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,476044024748,,,,c,,,,,,,&ef_id=CjwKCAiA9bmABhBbEiwASb35VxNl5degOkN33jNdIdi6nSD4RP0wi2FaJUrZeCFtUte8_eWSBqdXqRoC8E0QAvD_BwE:G:s&s_kwcid=AL!739!3!476044024748!!!g!293946777986!&gclsrc=aw.ds',
'Tomatoes':'https://www.flipkart.com/tomato-hybrid-1-kg/p/itmf7fj5suuvf3hg?gclid=CjwKCAiA9bmABhBbEiwASb35VywKeEjKvTkpNzT3iAlF2axP8xUHquwJoDdh17U-SZ6e8YLWyApkqRoCDBoQAvD_BwE&pid=VEGF7FJ5RXGUUGFA&lid=LSTVEGF7FJ5RXGUUGFANSYGQR&marketplace=GROCERY&cmpid=content_vegetable_730597647_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,476044024748,,,,c,,,,,,,&ef_id=CjwKCAiA9bmABhBbEiwASb35VywKeEjKvTkpNzT3iAlF2axP8xUHquwJoDdh17U-SZ6e8YLWyApkqRoCDBoQAvD_BwE:G:s&s_kwcid=AL!739!3!476044024748!!!g!293946777986!&gclsrc=aw.ds',
'Lady Fingers':'https://www.flipkart.com/shubh-bhakti-shubhbhakti-super-fine-lady-fingers-seeds-seed/p/itmehk9mkk8cavgf?gclid=CjwKCAiA9bmABhBbEiwASb35VwVAlVoM_aPPEX6Zi-OaS4hO4VExx1_P-51tt2esowlhvn26cXi1BBoCF9kQAvD_BwE&pid=PAEEHK9MUBRUQPJA&lid=LSTPAEEHK9MUBRUQPJAQART5E&marketplace=FLIPKART&cmpid=content_plant-seed_730597647_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,476044024748,,,,c,,,,,,,&ef_id=CjwKCAiA9bmABhBbEiwASb35VwVAlVoM_aPPEX6Zi-OaS4hO4VExx1_P-51tt2esowlhvn26cXi1BBoCF9kQAvD_BwE:G:s&s_kwcid=AL!739!3!476044024748!!!g!293946777986!&gclsrc=aw.ds',
'Aashirwad aata':'https://www.flipkart.com/aashirvaad-superior-mp-atta/p/itm2138546a91477?gclid=CjwKCAiA9bmABhBbEiwASb35V54SkBDwh-R5aMQoF9xowBaEuCPb_AKojDhjlxnNIIAiJCCgEaVsqxoCEyYQAvD_BwE&pid=FLREUC5PJYTYFBE2&lid=LSTFLREUC5PJYTYFBE2LHWMMN&marketplace=GROCERY&cmpid=content_flour_1758079601_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,341821069116,,,,c,,,,,,,&ef_id=CjwKCAiA9bmABhBbEiwASb35V54SkBDwh-R5aMQoF9xowBaEuCPb_AKojDhjlxnNIIAiJCCgEaVsqxoCEyYQAvD_BwE:G:s&s_kwcid=AL!739!3!341821069116!!!g!835847407374!&gclsrc=aw.ds',
'India Gate Rice':'https://www.flipkart.com/india-gate-regular-choice-basmati-rice/p/itmeuhhmvrnqhfvu?gclid=CjwKCAiA9bmABhBbEiwASb35V373KUZGlUZpjyre_xIMYP9jrBu2qlNM5aTK5OmSuby7R2DYJJCS2xoCOVUQAvD_BwE&pid=RICEUHHMHUQXGKXZ&lid=LSTRICEUHHMHUQXGKXZ5XMRMP&marketplace=GROCERY&cmpid=content_rice_730597647_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,476044024748,,,,c,,,,,,,&ef_id=CjwKCAiA9bmABhBbEiwASb35V373KUZGlUZpjyre_xIMYP9jrBu2qlNM5aTK5OmSuby7R2DYJJCS2xoCOVUQAvD_BwE:G:s&s_kwcid=AL!739!3!476044024748!!!g!293946777986!&gclsrc=aw.ds',
'Refined Oil':'https://www.flipkart.com/fortune-sunlite-refined-sunflower-oil-pouch/p/itmf8phyytkfbuy7?pid=EDOET83C9UHNFETC&lid=LSTEDOET83C9UHNFETCOJSRGH&marketplace=GROCERY&spotlightTagId=BestsellerId_eat%2F18p&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=a36782cd-6920-4540-8ca2-5111b5346f2b.EDOET83C9UHNFETC.SEARCH&ppt=sp&ppn=sp&ssid=npmz7vxgqo0000001611646064439&qH=6bd7eb215b3904f5',
'Mustard Oil':'https://www.flipkart.com/fortune-kachi-ghani-mustard-oil-pouch/p/itmevmnc4jthzy3w?pid=EDOET83CGGHPBAAV&lid=LSTEDOET83CGGHPBAAVSWNC43&marketplace=GROCERY&iid=b5bed4b4-a35c-48e1-82f4-35b85747b328.EDOET83CGGHPBAAV.SEARCH',
'Tur Dal':'https://www.flipkart.com/tata-sampann-toor-dal/p/itmf6verd4jgzt7y?pid=PLSEU7M4X7YWF2W6&lid=LSTPLSEU7M4X7YWF2W6CKQKB5&marketplace=GROCERY&iid=7dae3dbe-ea64-4a5e-a5d1-7887cb1c67d2.PLSEU7M4X7YWF2W6.SEARCH',
'Sugar':'https://www.flipkart.com/madhur-pure-hygienic-sugar/p/itme3f4d18778842?pid=SUGFTZ3QJAGGDYGC&lid=LSTSUGFTZ3QJAGGDYGC2GXMWF&marketplace=GROCERY&iid=3fc23224-12c7-43b1-9c95-509f1713cb78.SUGFTZ3QJAGGDYGC.SEARCH',
'Bhujia':'https://www.flipkart.com/haldiram-s-bhujia-sev/p/itmcf7427b395677?pid=SNSETFPNXG5SHCQ9&lid=LSTSNSETFPNXG5SHCQ9D4S5GC&marketplace=GROCERY&iid=4a6e33d5-2227-49cf-8709-b5ce87b5e6b5.SNSETFPNXG5SHCQ9.SEARCH',
'Amul Ghee':'https://www.flipkart.com/amul-pure-ghee-1-l-pouch/p/itmf7dvqpybgtgum?pid=GHEFG48VHC4G4U8S&lid=LSTGHEFG48VHC4G4U8SIDQVTR&marketplace=GROCERY&iid=1ec0932f-cf0c-43f0-b5ab-c4d656af8a90.GHEFG48VHC4G4U8S.SEARCH',
'Horlicks':'https://www.flipkart.com/horlicks-chocolate-delight-flavor/p/itmexyzekzmc8d9t?pid=MDMETGN5U9FHGNWE&lid=LSTMDMETGN5U9FHGNWE0MPCGO&marketplace=GROCERY&iid=44c2c41b-e936-4b0f-b411-57d72c917614.MDMETGN5U9FHGNWE.SEARCH',
}
# BIG basket
bigBasket_dict = {
'Potatoes':'https://www.bigbasket.com/pd/10000159/fresho-potato-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Onions':'https://www.bigbasket.com/pd/10000148/fresho-onion-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Lemon':'https://www.bigbasket.com/pd/10000127/fresho-lemon-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Cauliflower':'https://www.bigbasket.com/pd/10000074/fresho-cauliflower-1-pc/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Lady Finger':'https://www.bigbasket.com/pd/10000144/fresho-ladies-finger-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Brinjal':'https://www.bigbasket.com/pd/10000054/fresho-brinjal-bottle-shape-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Ginger':'https://www.bigbasket.com/pd/40023480/fresho-ginger-organically-grown-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Garlic':'https://www.bigbasket.com/pd/10000115/fresho-garlic-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Amul paneer':'https://www.bigbasket.com/pd/40096747/amul-fresh-paneer-200-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Apple':'https://www.bigbasket.com/pd/40033824/fresho-apple-red-delicious-regular-4-pcs/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Orange':'https://www.bigbasket.com/pd/10000384/fresho-orange-kinnow-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Bannnana':'https://www.bigbasket.com/pd/10000025/fresho-banana-robusta-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Grapes':'https://www.bigbasket.com/pd/10000288/fresho-grapes-sonaka-seedless-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Amul Milk':'https://www.bigbasket.com/pd/306926/amul-taaza-homogenised-toned-milk-1-l-carton/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Amul Paneer':'https://www.bigbasket.com/pd/40096747/amul-fresh-paneer-200-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Aashirwad aata':'https://www.bigbasket.com/pd/126906/aashirvaad-atta-whole-wheat-10-kg-pouch/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'India Gate Rice':'https://www.bigbasket.com/pd/220612/india-gate-basmati-rice-dubar-5-kg-pouch/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Refined Oil':'https://www.bigbasket.com/pd/274145/fortune-sunflower-refined-oil-1-l-pouch/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Mustard Oil':'https://www.bigbasket.com/pd/276756/fortune-kachi-ghani-mustard-oil-1-l-pet-bottle/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Tur Dal':'https://www.bigbasket.com/pd/10000412/bb-popular-toorarhar-dal-5-kg-pouch/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Sugar':'https://www.bigbasket.com/pd/70001579/mawana-sugar-premium-crystal-1-kg-pouch/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Bhujia':'https://www.bigbasket.com/pd/100022552/haldirams-namkeen-bhujia-sev-1-kg-pouch/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Amul ghee':'https://www.bigbasket.com/pd/40050536/amul-ghee-1-l-pouch/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
'Horlicks':'https://www.bigbasket.com/pd/119385/horlicks-health-nutrition-drink-classic-malt-1-kg-carton/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop',
}

# # price = soup.find(class_='_30jeq3 _16Jk6d').get_text()


def bigBasket_scraper():
    for key in bigBasket_dict.keys():
        URL = bigBasket_dict[key]
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        price = soup.find(class_='IyLvo').get_text()
        # print(price[3:])
        bigBasket_dict[key] = price[3:]
        headers = ["Products", "Price"]
    print(tabulate(bigBasket_dict.items(), headers = headers))
    to_csv(bigBasket_dict, name='BigBasket')

def flipkart_scraper():
    for key in flipkart_dict.keys():
        URL = flipkart_dict[key]
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find(class_='_30jeq3 _16Jk6d').get_text()
        flipkart_dict[key] = price[1:]
        headers = ["Products", "Price"]
    print(tabulate(flipkart_dict.items(), headers = headers))
    to_csv(flipkart_dict,name='Flipkart')

def to_csv(diict, name):
    # df = pd.DataFrame('ProductName': products, 'Price':prices, 'Rating':ratings, 'Discount': discounts}))
    # df.to_csv('products.csv', index=False, encoding='utf-8')
    with open(f'{name}.csv', 'w') as f:
        w = csv.writer(f)
        # w.writeheader()
        w.writerows(diict.items())
        f.close()


bigBasket_scraper()
flipkart_scraper()