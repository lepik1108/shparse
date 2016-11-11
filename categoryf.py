def make(cat_id, name, descr, uri):
    config = """<?php 

     $data = array (
      'description' => 
      array (
        'en' => 
        array (
          'name' => '"""+str(name)+"""',
          'description_full' => '"""+str(descr)+"""',
          'description_short' => '"""+str(descr)+"""',
          'uri' => '"""+str(uri)+"""',
          'category_id' => '"""+str(cat_id)+"""',
          'seo' => 
          array (
            'title' => 'Category """+str(name)+""" * onlinecareshop.com',
            'description' => '',
            'keywords' => '',
            'seo_text' => '',
          ),
        ),
        
      ),
    );"""
    return config

