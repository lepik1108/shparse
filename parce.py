import os
import urllib
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import links

import categories_pils
import categoryf
import pillf
import sitemap

def download_img(img_url, filename):
    try:
        image_on_web = urllib.urlopen(img_url)
        if image_on_web.headers.maintype == 'image':
            buf = image_on_web.read()
            path = os.getcwd() + "./content/100x125/"
            file_path = "%s%s" % (path, filename)
            downloaded_image = file(file_path, "wb")
            downloaded_image.write(buf)
            downloaded_image.close()
            image_on_web.close()
        else:
            return False    
    except:
        return False
    return True


binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
bro = webdriver.Firefox(firefox_binary=binary)
print(links.pool[0])


cat_id = 33

product_id = 100

page = 1

for item in links.pool:
    if type(item) is str:
#set cat_id        
        cat_id+=1
        print 'Entering category ' + str(cat_id)
#goto cat page
        bro.get(item+"#/?_=1&page="+str(page))
#get cat name
        category_name = bro.find_element_by_class_name("search-results-header").get_attribute('innerHTML')
        print category_name
#set cat uri
        category_uri = item[39:-5]
        print category_uri
#get cat descr if exist
        try:
            category_descr = bro.find_element_by_css_selector(".category-short-description.hidden-xs.clearfix").find_element_by_tag_name("p").get_attribute('innerHTML')
            print category_descr
        except:
            category_descr = ''
###write categoryf
        f = open('./data/categoryf_'+str(cat_id)+'.php', 'w')    
        categoryf_php = categoryf.make(cat_id,category_name,category_descr,category_uri)
        f.write(categoryf_php)
        f.close()
#get num of pages
        pages_num = bro.find_element_by_css_selector(".searchspring-total_pages").get_attribute('innerHTML')
        print 'Total pages ' + str(pages_num)
        
        for page in range(int(pages_num)):        
#get product_info       
            products = bro.find_elements_by_class_name("product-tile")
            i=0
            
            for product in products[:8]:
#set product_id
                product_id+=1
                print "Product id: "+str(product_id)
#get product url 
                product_link = bro.find_elements_by_css_selector(".name-link.ss-product-name")[i].get_attribute("href")
                print product_link
#set product uri
                product_uri = product_link[39:-5]
                print product_uri
###get product full name           
##                product_full_name = bro.find_elements_by_css_selector(".name-link.ss-product-name")[i].get_attribute('innerHTML')
##                print product_full_name
###get product name           
##                product_name = bro.find_elements_by_css_selector(".hidden.ss-product-reference")[i].get_attribute('innerHTML')
##                print product_name
###get product price       
##                product_price = bro.find_elements_by_class_name("product-sales-price")[8+i].get_attribute('innerHTML')
##                print product_price
                
#get manufacturer if exist
                try:
                    product_manufacturer = bro.find_elements_by_css_selector(".manufacturer")[8+i].get_attribute('innerHTML')
                    print product_manufacturer
                except:
                    product_manufacturer=''            
#goto product page
                bro.get(product_link)
#get name
                product_name = bro.find_element_by_css_selector(".product-name.main").get_attribute('innerHTML')
                print product_name              
###get ingredient                
##                product_ingredient = bro.find_element_by_css_selector(".nutrition-facts").find_elements_by_tag_name("p")[0].get_attribute('innerHTML')[35:]
##                print product_ingredient
                
#get price if exist
                try:
                    product_price = bro.find_element_by_css_selector(".price").get_attribute('innerHTML')[18:]
                except:
                    product_price = 1
                print float(product_price)
#get retail_price if exist
                try:
                    product_r_price = bro.find_element_by_css_selector(".retail").get_attribute('innerHTML')[9:] 
                except:
                    product_r_price = float(product_price)*0.88
                print float(product_r_price)
#get desc short if exist
                try:
                    product_desc_s = bro.find_element_by_css_selector(".product-description-short-content").get_attribute('innerHTML')[33:-120]
                except:
                    product_desc_s = ''
                    print product_desc_s             
#get desc full if exist
                try:    
                    product_desc_f = bro.find_element_by_css_selector(".description").get_attribute('innerHTML')[13:-8]
                except:
                    product_desc_f = ''
                print product_desc_f 
#get image if exist
                try:    
                    product_img_url = bro.find_element_by_css_selector(".sp-large").find_element_by_tag_name("a").get_attribute('href')
                    download_img(product_img_url, product_uri+'.jpg')
                except:
                    pass
                print product_img_url 
###write pillf
                f = open('./data/pillf_'+str(product_id)+'.php', 'w')    
                pillf_php = pillf.make(product_id,product_name,product_desc_f,product_desc_s,product_manufacturer,product_uri,product_price,product_r_price)
                f.write(pillf_php)
                f.close()
#go back to cat page
                bro.get(item+"#/?_=1&page="+str(page))
                i+=1
        page+=1
            
##        else:
##            bro.close()
##            sys.exit(0)
##        print len(prod_blocks)



##    else:
##        i=0
##        for link in item:
##            i+=1
##            print 'Enrering sub-category '+ str(i) + ' of ' + str(len(item))
            
