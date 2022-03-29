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

[Back to Table of Content](#table-of-content)

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


[Back to Table of Content](#table-of-content)


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









