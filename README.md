This is my Portfolio Honors project which is an online store that I designed using Python Django Framework and Postgresql database. Online shopping is a popular way for vendors and clients to benefit from each other. In my project, I focus on making the search for the desired products easily accessible to the user, making pricing and discounts transparent, and making checkout easy to manage.

The class Product is responsible to uploading and storing new products into the store database. The class Product is linked to the class AddCart via ForeignKey. The class AddCart enables the user to select the quantity and add the product to the cart. When the user intends to add an item to the cart, the program checks if an identical item already exists in the cart. If so, the program updates the number of items in the cart instead of adding a new item to the cart. 

To manage the shopping cart, the user can click the plus and minus buttons to change the quantity of the items or click remove to remove the item from the cart. Upon respective requests, the class methods enable the recalculation of the number of items in the cart and the total price. 



