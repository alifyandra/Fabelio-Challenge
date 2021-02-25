# Fabelio Challenge

#### [Website Link](alifyandra-fabelio.herokuapp.com)

This is a Django Website that displays a single product that changes with every refresh, the next product is based on the similarity with the previous product. A user won't see the same product twice unless the user has seen all products in the database.

The similarity between the next products with the previously seen product is judged by using the Python difflib library and summing the SequencerMatcher ratio between the string attributes of the Product relation.

```Python
similar_sorted = sorted(filtered, key=lambda x:
        difflib.SequenceMatcher(None,x.name,last_seen.name).ratio()+
        difflib.SequenceMatcher(None,x.colours,last_seen.colours).ratio()+
        difflib.SequenceMatcher(None,x.material,last_seen.material).ratio(), reverse=True)
```



#### This a sample of the database scheme for relation Product:

| **id** | **product name**        | **price** | **dimension** | **colours**                                  | **material** |
| ------ | ----------------------- | --------- | ------------- | -------------------------------------------- | ------------ |
| **1**  | Sofa 2 dudukan Vienna   | 3899000   | 162 x 95 x 86 | custard vienna, graphite vienna, ruby vienna | solid wood   |
| **2**  | Sofa Tempat Tidur Mochi | 3500000   | 160 x 95 x 90 | custard vienna, graphite vienna, ruby vienna | solid wood   |
| **3**  | Sofa 2 dudukan Zelado   | 4299000   | 162 x 95 x 86 | graphite vienna, teal vienna                 | hollow steel |

The RDBMS used in this project is PostgreSQL. To store what the user has seen and has not seen, everytime a new anonymous user opens the website, a 'device' cookie is created in the form of UUIDv4. This cookie is then parsed in the django views and created as a new Customer relation with a device attribute that holds that previous cookie, this Customer relation has an attribute that holds an array of the id's of all seen products. 

The customer relation holds a user, name, email attribute just in case you would like to convert the anonymous user into a proper user in the database in the future.

#### Here is the schema of the Customer relation:

| user                      | name   | email  | device         | seen      |
| ------------------------- | ------ | ------ | -------------- | --------- |
| Django inherited User obj | String | String | String(UUIDv4) | Int Array |



#### Things I would add:

Given the 24 hours to complete this challenge, it was quite fun. I applied my knowledge in databases and got to learn more about cookies and sessions. 

If I had more time I would of certainly used React as the frontend, but because I've never really combined Django and React, it was very complicated and risky to try for the 24 hours. The reason I used Django was because I was more comfortable and familiar with the ORM feature that Django has compared to using Node.js, if I would do this project in my free time I would of certainly also used Node and Express as the backend.

Hit me up at alifyandra@gmail.com or connect with me at https://www.linkedin.com/in/alifyandra/

Cheers! 👋

