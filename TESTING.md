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


| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- |:----:|
| Menu | Click on any link | rederecet correct page| User redirected to the correct page | Pass |
| Shopping Options | Clicking Categories | Click immune system vitamins| Redirected to the relevant products in shop | Pass |













[Back to Table of Content](#table-of-content)
