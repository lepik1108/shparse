def generate():
    sitemap = """<?php 

     $data = array (
      0 => 
      array (
        'url' => 'cart.html',
        'module' => 'cart',
        'action' => 'index',
        'lang' => 'get',
      ),
      1 => 
      array (
        'url' => '',
        'module' => 'index',
        'action' => 'index',
        'lang' => 'get',
      ),
      2 => 
      array (
        'url' => 'checkout.html',
        'module' => 'checkout',
        'action' => 'index',
        'lang' => 'get',
      ),
      3 => 
      array (
        'url' => 'contact_us.html',
        'module' => 'contact_us',
        'action' => 'index',
        'lang' => 'get',
      ),

      4 => 
      array (
        'url' => 'ingredient.html',
        'module' => 'ingredient',
        'action' => 'index',
        'lang' => 'get',
      ),
      5 => 
      array (
        'url' => 'letter.html',
        'module' => 'letter',
        'action' => 'index',
        'lang' => 'get',
      ),
      6 => 
      array (
        'url' => 'news.html',
        'module' => 'news',
        'action' => 'index',
        'lang' => 'get',
      ),
      7 => 
      array (
        'url' => 'order.html',
        'module' => 'order_status',
        'action' => 'index',
        'lang' => 'get',
      ),
      8 => 
      array (
        'url' => 'order_product.html',
        'module' => 'product',
        'action' => 'get',
        'lang' => 'get',
      ),
      9 => 
      array (
        'url' => 'search.html',
        'module' => 'search',
        'action' => 'index',
        'lang' => 'get',
      ),
      10 => 
      array (
        'url' => 'sitemap.html',
        'module' => 'sitemap',
        'action' => 'index',
        'lang' => 'get',
      ),
      11 => 
      array (
        'url' => 'about_us_en.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'about_us',
        'lang' => 'en',
      ),
      12 => 
      array (
        'url' => 'privacy_en.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'our_policies',
        'lang' => 'en',
      ),
      13 => 
      array (
        'url' => 'terms_and_conditions_en.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'terms_and_conditions',
        'lang' => 'en',
      ),
      14 => 
      array (
        'url' => 'faq.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'faq',
        'lang' => 'get',
      ),
      15 => 
      array (
        'url' => 'new_page/mybonus.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'new_page',
        'lang' => 'get',
      ),
      16 => 
      array (
        'url' => 'testimonials.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'testimonials',
        'lang' => 'get',
      ),
      17 => 
      array (
        'url' => 'about_us_de.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'about_us',
        'lang' => 'de',
      ),
      18 => 
      array (
        'url' => 'privacy_de.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'our_policies',
        'lang' => 'de',
      ),
      19 => 
      array (
        'url' => 'terms_and_conditions_de.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'terms_and_conditions',
        'lang' => 'de',
      ),
      20 => 
      array (
        'url' => 'about_us_fr.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'about_us',
        'lang' => 'fr',
      ),
      21 => 
      array (
        'url' => 'privacy_fr.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'our_policies',
        'lang' => 'fr',
      ),
      22 => 
      array (
        'url' => 'terms_and_conditions_fr.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'terms_and_conditions',
        'lang' => 'fr',
      ),
      23 => 
      array (
        'url' => 'about_us_it.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'about_us',
        'lang' => 'it',
      ),
      216 => 
      array (
        'url' => 'privacy_it.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'our_policies',
        'lang' => 'it',
      ),
      24 => 
      array (
        'url' => 'terms_and_conditions_it.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'terms_and_conditions',
        'lang' => 'it',
      ),
      25 => 
      array (
        'url' => 'about_us_es.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'about_us',
        'lang' => 'es',
      ),
      26 => 
      array (
        'url' => 'privacy_es.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'our_policies',
        'lang' => 'es',
      ),
      27 => 
      array (
        'url' => 'terms_and_conditions_es.html',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'terms_and_conditions',
        'lang' => 'es',
      ),
      28 => 
      array (
        'url' => 'omoss',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'about_us',
        'lang' => 'get',
      ),
      29 => 
      array (
        'url' => 'sekretess',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'our_policies',
        'lang' => 'get',
      ),
      30 => 
      array (
        'url' => 'villkor',
        'module' => 'static_page',
        'action' => 'get',
        'oid' => 'terms_and_conditions',
        'lang' => 'get',
      ),
      31 => 
      array (
        'url' => 'subscribe.html',
        'module' => 'subscribe',
        'action' => 'index',
        'lang' => 'get',
      ),
      32 => 
      array (
        'url' => 'checkout.html',
        'module' => 'Checkout',
        'action' => 'Index',
        'lang' => 'get',
      ), """
    ##  
    ####category  
    ##  3 => 
    ##  array (
    ##    'url' => 'medicine-products-herbals-en.html',
    ##    'module' => 'category',
    ##    'action' => 'get',
    ##    'oid' => '23',
    ##    'lang' => 'en',
    ##  ),
    ##  
    ##);
    return sitemap

