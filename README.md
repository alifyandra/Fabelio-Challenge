# Fabelio Internship Challenge

#### [Website Link](alifyandra-fabelio.herokuapp.com)

This is a Django Website that displays a single product that changes with every refresh, the next product is based on the similarity with the previous product. A user won't see the same product twice unless the user has seen all products in the database.

The similarity between the next products with the previously seen product is judged by using the Python difflib library and summing the SequencerMatcher ratio between the string attributes of the Product relation.

##### This a sample of the database scheme for relation Product:

| **id** | **product name**         | **price** | **dimension** | **colours**                                  | **material** | **image**                                                    | **sold** |
| ------ | ------------------------ | --------- | ------------- | -------------------------------------------- | ------------ | ------------------------------------------------------------ | -------- |
| **1**  | Sofa 2 dudukan Vienna    | 3899000   | 162 x 95 x 86 | custard vienna, graphite vienna, ruby vienna | solid wood   | https://fabelio.com/media/catalog/product/w/i/wina_2_seater_sofa__custard__1_1.jpg | t        |
| **2**  | Sofa Tempat Tidur Mochi  | 3500000   | 160 x 95 x 90 | custard vienna, graphite vienna, ruby vienna | solid wood   | https://fabelio.com/media/catalog/product/r/2/r2710.jpg      | f        |
| **3**  | Sofa 2 dudukan Zelado    | 4299000   | 162 x 95 x 86 | graphite vienna, teal vienna                 | hollow steel | https://fabelio.com/media/catalog/product/z/e/zelado-2-seater-sofa---custard-01.jpg | f        |
| **4**  | Sofa 2 dudukan Toril     | 2899000   | 160 x 95 x 90 | blue jay, ruby vienna                        | solid wood   | https://fabelio.com/media/catalog/product/t/o/Toril_2_Seater_Sofa_(Paradise)_1.jpg | f        |
| **5**  | Sofa Tempat Tidur Deacon | 3299000   | 150 x 90 x 80 | custard vienna, graphite vienna              | hollow steel | https://fabelio.com/media/catalog/product/d/e/deacon_white_1_1_1.jpg | f        |
| **6**  | Sofa Java                | 3869100   | 142 x 90 x 80 | custard vienna, graphite vienna              | solid wood   | https://fabelio.com/media/catalog/product/t/a/Taby_Java_2_Seater_Living_Set_(Sugar)_1.jpg | f        |
| **7**  | Sofa 1 dudukan Hughes    | 2500000   | 90 x 82 x 58  | custard vienna, graphite vienna, ruby vienna | solid wood   | https://fabelio.com/media/catalog/product/h/u/Hughes_Armchair_(Wood)_0.jpg | f        |
| **8**  | Sofa 1 dudukan Taby      | 2399000   | 90 x 82 x 58  | brown vienna, ruby vienna                    | solid wood   | https://fabelio.com/media/catalog/product/t/a/Taby_Armchair_(Jezebel)_1.jpg | f        |
| **9**  | Sofa 1 dudukan Zoey      | 2399000   | 90 x 82 x 58  | brown vienna, ruby vienna                    | hollow steel | https://fabelio.com/media/catalog/product/k/u/Kursi_Zoey_Armchair_(Brown)_0.jpg | f        |
| **10** | Sofa 1 dudukan Vienna    | 2199000   | 90 x 82 x 58  | custard vienna, graphite vienna, ruby vienna | solid wood   | https://fabelio.com/media/catalog/product/w/i/wina_armchair__graphite__1_1.jpg | f        |

To store what the user has seen and has not seen, everytime a new anonymous user opens the website, a 'device' cookie is created in the form of UUIDv4. This cookie is then parsed in the django views and created as a new Customer relation with a device attribute that holds that previous cookie, this Customer relation has an attribute that holds an array of the id's of all seen products. 

The customer relation holds a user, name, email attribute just in case you would like to convert the anonymous user into a proper user in the database in the future.

##### Here is the schema of the Customer relation:

| user                      | name   | email  | device         | seen    |
| ------------------------- | ------ | ------ | -------------- | ------- |
| Django inherited User obj | String | String | String(UUIDv4) | Boolean |



#### Things I would add:

Given the 24 hours to complete this challenge, it was quite fun. I applied my knowledge in databases and got to learn more about cookies and sessions. 

If I had more time I would of certainly used React as the frontend, but because I've never really combined Django and React, it was very complicated and risky to try for the 24 hours. The reason I used Django was because I was more comfortable and familiar with the ORM feature that Django has compared to using Node.js.

Hit me up at alifyandra@gmail.com or connect with me at https://www.linkedin.com/in/alifyandra/

Cheers! 👋

