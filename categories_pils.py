def make(cat, pill_ids):
    i=0
    config = """<?php 
     $exp = 1314292341; 

     $data = array (
      """+str(cat_ids[i])+""" => 
      array ("""
    for pill_id in pill_ids:
        config+=str(i)+" => "+str(pill_id)+","
    config=config +"  ),"

    #);
    return config
