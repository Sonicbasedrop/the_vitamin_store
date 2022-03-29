# The Vitamin Store - Testing

Back to my main README.md click [here](https://github.com/Sonicbasedrop/the_vitamin_store/blob/main/README.md#the-vitamin-store)
<br>


## Table of Content
# Testing
* [Validator Testing](#validator-testing)
* [Lighthouse Testing](#lighthouse-testing)
* [Testing From User Stories](#testing-from-user-stories)
* [Manually Testing Functionality](#manually-testing-functionality)
* [Responsive Testing](#responsive-testing)
* [Bugs and Fixes](#bugs-and-fixes)<br>
---

### Validator Testing
The website's was tested with following validators:

### HTML Markup Validation Service
*  I used [Html Checker](https://validator.w3.org/) to validate the html files.
The files can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/html_validation)

### CSS Validation Service
* I used [CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate the css files.
The files can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/css_validation)

### JShint
* I used [JShint](https://jshint.com/) to check the JavaScript files
The files can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/jshint_test_reults)

### PEP8online
* I used [PEP8online](http://pep8online.com/) to check the files
#### Bag App
* Can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/bag_app_pep8_results)<br>
#### Checkout App
* Can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/checkout_app_pep8_results)<br>
#### Contact App
* Can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/contact_app_pep8_results)<br>
#### Home App
* Can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/home_app_pep8_results)<br>
#### Products App
* Can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/products_app_pep8_results)<br>
#### Profiles App
* Can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/profiles_app_pep8_results)<br>
#### Reviews App
* Can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/reviews_app_pep8_results)<br>

### Lighthouse Testing
*  I used [Lighthouse in Crome Dev Tools](https://developers.google.com/web/tools/lighthouse/?utm_source=devtools)
The files for the desktop test can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/lighthouse_desktop)<br>
The files for the mobile test can be found [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/lighthouse_mobile)<br>
---

* [Back to Table of Content](#table-of-content)

### Testing User Stories

#### Navigation
     * All users

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Home button    | To redirect to home page | Click the home button | Button navigates to home | Pass |
| Navbar links | Clicking All Products takes user to All Products page | Click All Products | Redirected to All Products page | Pass |
|  | Clicking All Category takes user to the specific category page | Click each category in turn | Redirected to specific category page | Pass |
|   | Click Bag takes user to Bag page | Click Bag | Redirected to Bag page | Pass |
|   | Searching using Search Bar displays the product in the products page | Type vegan | Redirected to Products page with all the vegan vitamins in the store | Pass |
|  | Redirect to Instagram in new tab | Click Instagram icon | Instagram page opened in new tab | Pass |
|  | Clicking on the Contact link | Redirects user to the contact page with a conatct form , were the user can query site owner| | Pass |
|  | Clicking on the Faq link | Redirects user to the faq page, were they can find "about us, privacy policy and return policy| | Pass |



#### Navigation
     * Users logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
|  Navbar links   | Clicking Profile takes user to their profile page | Click Profile | Redirected to Profile Page | Pass |
|  | Click Log Out logs out the user | Click Log Out | User logged out and redirected to Log In | Pass |




     * User not logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Navbar links | Click Log In redirects to log in page | Click Log In | User redirected to Log In Page | Pass |
|  | Click Register redirects to log in page | Click Register | User redirected to Register Page | Pass |


#### Home Page
    * Home

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- |:----:|
| Menu | Click on any link | rederecet correct page| User redirected to the correct page | Pass |
| Shopping Options | Clicking Categories | Click immune system vitamins| Redirected to the relevant products in shop | Pass |



#### Register Page
    * Register

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Register functionality | Form validation for email requires "@" symbol |  Attempt to register without "@" in input field | Form validation requests valid email address | Pass |
| | E-mail Again value must be same as Email value | Attempt to register with incorrect email in email again input field | Form validation requests email address must match | Pass |
| | Username must be between 4 and 15 characters | Attempt to enter username with less than 4 characters | Feedback error displayed | Pass |
| | Username must be between 4 and 15 characters | Attempt to enter username with more than 15 characters | Form restricts the user from using more than 15 characters | Pass |
| | Password must be longer than 8 characters | Attempt to enter password with less than 8 characters | Form restricts the user from using less than 8 characters | Pass |
| | Register with new user and password to be logged in and redirected the index page | Enter email address, name, username, password and click register | New account registered and profile page shown | Pass |


#### Log In Page
    * Log in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-----------------| ----------|  ---------- | :----: |
| Log in functionality | Correct user/pass combination directs user to the index page | Log in with correct username/password combination | Redirected to user to index page| Pass |
|   | Incorrect username/password combination shows error message | Attempt to log in with incorrect credentials | "The username and/or password you specified are not correct." error message appears| Pass |
| Link to Register | Redirect to Register page | Click link to register | Redirected to Register page | Pass |


#### Profile Page
     * Profile

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Personal Information | Personal information is visible if previously saved | Navigate to Profile page, view personal information | The personal information is visible in Personal Information section | Pass |
| | Personal information can be updated | Navigate to Profile page, change personal information, click update information. | The personal information is updated with the new details. | Pass |
| Order History | Order History is visible if order placed while logged in | Navigate to Profile page, view Order History Section | The Order History is visible | Pass |
| | Order information can be accessed by clicking order number | Navigate to Profile page, view Order History Section, click Order Number | Order Information is visible | Pass |


* [Back to Table of Content](#table-of-content)


#### Products Pages

##### Products
    * Products

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| All products visible | Products page shows all products | Open Products page and view products | All products visible | Pass |
|  | Searching by category shows products from that category | Select to search by each category | Products from each category successfully displayed | Pass |


##### Product Details
    * Product Details
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Product Details | Product description displayed for individual product | Open Product Detail page and view products | Product details visible | Pass |
| Add to bag | Clicking Add To Bag adds the product to the bag | Open Product Detail page click add to bag | Product available in bag | Pass |
| Reviews | Reviews for individual products available | Navigate to product review section | Reviews visible  | Pass |
| Reviews | Add a review form adds review to product details page | While logged in navigate to product review section, fill out form, click add review | Review visible in reviews section | Pass |
|  | User must be logged in to add review to product details page | While not logged in navigate to product review section, attempt to leave review | Message revealed "Please log in to add a review of a product." | Pass |


##### Add Product
    * Add Product

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Add Products | Only admin/site owner is allowed to visit add product page | Log in as non-superuser and attempt to access /products/add/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass |
| Form Validation | Required fields must be completed to add the product  | Attempt to add product without filling in a required field | Error message "Please fill in this field" | Pass |


##### Edit Product
    * Edit Product

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Edit Products | Only admin/site owner edit a product  | Log in as non-superuser and attempt to access /products//edit/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass |
| Form Validation | Required fields must be completed to edit the product  | Attempt to edit product without filling in a required field | Error message "Please fill in this field" | Pass |

#### Shopping Bag
    * Shopping Bag

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| View Items | Correct products are in the bag | Add product to bag and check quantity and total are in the bag | Expected products are in the bag | Pass |
| Update Items | Update the number of a product in the bag and it will reflect in bag and price | Change number of product in bag and check quantity and total has updated | Total and quantity updated | Pass |
| Remove Items | Click remove item for item to be removed from the bag | Click remove beside relevant product | Item removed from bag and notification to confirm this "Removed item from your bag" | Pass |

#### Checkout
    * Checkout

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| View Items | Correct products are in the checkout | Add products to bag, click Secure Checkout | Expected products are in the checkout product list | Pass |
| Form Validation | Required fields must be completed to complete  | Attempt to check out without filling in a required field | Error message "Please fill in this field" | Pass |


#### Reviews
    * Review

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | ---- |
| All reviews visible | Review section on product detail page show all reviews for the specific product | Open produt detail page and view reviews | Reviews visible | Pass |
| Add review | Only logged in users are allowed to add a review | Log out and attempt to add a review | User will se "Create an account or login to leave a review". | Pass |


##### Contact
    * Contact

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Contact site owner/admin | Abilaty to query site owner/admin about anything  | Send message via contact form | meaasge sent and recived by site owner/admin| Pass |




* [Back to contents](#contents)

### Manually Testing Functionality
    * MTF

| User Story ID  | As a/an  | I want to be able to...  | So that I can... |  Pass/Fail |
|-------------------|-------------------|-----------------|---------------|---------------|
|Viewing products and Navigation	|
| 1	|Shopper	|View a list of products|	Select some to purchase| pass|
| 3	|Shopper	|Easily find a product|Leave product reviews| pass|
| 2	|Shopper	|View indivudal product details|Identify the price, description, product rating, product image and available sizes|pass|
|4	|Shopper	|Easily view the total of my purchases at any time|	Take advantage of special saving on products I'd like to purchase| pass|
| 5	|Shopper	|Easily find contact page|	Contact site owner/admin|  pass|
|Registration and User Accounts|	
| 6	|Site User	|Easily register for an account	|Have a personal account and be able to view my profile| pass|
| 7	|Site User	|Easily login or logout|Access my personal account information| pass |
| 8	|Site User	|Easily recover my passowrd in case I forget it| Recover access to my account| pass|
| 9	|Site User	|Receive an email confirmation after registering| Verify that my account registration was successful| pass|
|10	|Site User	|Have a personalized user profile|	View my personal order history and order confirmations, save my payment information view my order history, and update my profile | pass|
|Sorting and Searching|	
| 11|Shopper	|Sort the list of available products|Easily identify the best rated, best priced and categorically sorted products| pass|
| 12|Shopper	|Sort a speific category of product	|Find the best-priced or best-rated product in a specific category, or sort the products in that category by name| pass|
| 13|Shopper	|Sort multiple categories of products simultaneously|Find the best-priced or best-rated products across broad categories, such as "vitamin-C" or "Vegan Vitamins"| pass|
| 14|Shopper	|Search for a product by name or description|Find a specific product I'd like to purchase| pass|
| 15|Shopper	|Easily see what I've serached for and the number of results|Quickly decide whether the product I want is available| pass|
|Purchasing and Checkout|	
| 16|Shopper	|Easily select the quantity of a product when purchasing it|Ensure I don't accidently select the wrong product, quantity| pass|
| 17|Shopper	|View items in my bag to be purchased| Identify the total cost of my purchase and all items I will receive| pass|
| 18|Shopper	|Adjust the quantity of individual items in my bag|	Easily make changes to my purchase before checkout| pass|
| 19|Shopper	|Easily enter my payment information|Check out quickly and with no hassle| pass|
| 20|Shopper	|Feel that my personal and payment information is safe and secure|	Confidently provide the needed information to make a purchase| pass|
| 21|Shopper	|View an order confirmation and checkout|	Verify that I haven't made any mistakes| pass|
| 22|Shopper	|Receive an email confirmation after checking out|	Keep the confirmation of what I have purchased for my records| pass|
| 23|Shopper	|View all products as a non-registered user| Purchase products without being registered| pass|
|	|Admin and Store Management	
| 24|Store Owner/admin	|Add a product	|Add new items to my store| pass|
| 25|Store Owner/admin	|Edit/update a product	|Change product prices, descriptions, images, and other product criteria| pass|
| 26|Store Owner/admin   | Delete a product | Remove items that are no longer for sale| pass|


# Responsive Testing
### Phone:
*  Samsung Galaxy S9
*  Iphone 8
*  I5hone 5
  
### Tablet:
* iPad Air

### Computer:
* Dell 27" Monitor
* Macbook  Air 13"

### Browsers:
* Google Crome
* Safari
* Opera
* Firefox

All testing was Passed.


* [Back to Table of Content](#table-of-content)












