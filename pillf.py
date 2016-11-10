def make(pill_id, name, description_f, description_s, manufacturer, uri, price, price_min):
    config = """<?php 
     $data = array (
      'description' => 
      array (
        'en' => 
        array (
          'pill_id' => '"""+str(pill_id)+"""',
          'name' => '"""+str(name)+"""',
          'ingredient' => '',
          'description' => '"""+str(description_f)+"""',
          'info' => '"""+str(description_s)+"""',
          'manufacturer' => '"""+str(manufacturer)+"""',
          'generic' => 'none',
          'img_icon' => 'yes',
          'img_tab' => 'no',
          'uri' => '"""+str(uri)+"""',
          'seo' => 
          array (
            'title' => '"""+str(name)+""" * shop.com',
            'description' => '',
            'keywords' => '',
            'seo_text' => '',
          ),
        ),
      ),
      'related' => 
      array (
      ),
      'price' => 
      array (
        'items' => 
        array (
          1 => 
          array (
            'price_id' => '1',
            'pill_id' => '1',
            'quantity' => '1',
            'type' => 'jar',
            'dose' => '',
            'dose_type' => '',
            'free' => '',
            'hitsale' => '0',
            'price_next' => NULL,
            'campaign' => 
            array (
              '1_0' => 
              array (
                'price_per_pill' => '"""+str(price)+"""',
                'price_per_packet' => '"""+str(price)+"""',
              ),
            ),
          ),
        ),
        'price_min' => '"""+str(price_min)+"""',
        'package' => 
        array (
          '200_mg' => 
          array (
            0 => '1',
          ),
        ),
      ),
    );"""
    return config
