# The Vitamin Store

The Vitamin Store is an online e-commerce vitamin store. This site was developed for my milestone 4 project as part of the Code Institute - Full Stack Diploma in Software Development Course.
<br>
![Mockup](readme_images/mockup/mockup.png)

Link to [live site](https://the-vitamin-store.herokuapp.com/)


## **Table of Content**
* [User Experience Design (UX)](#User-Experience-Design)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [User stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframes)
        * [Database Design](#Database-Design)
        * [Security](#Security)
    * [The Surface Plane](#The-Surface-Plane)
        * [Design](#Design)
            * [Colour Scheme](#Colour-Scheme)
            * [Typography](#Typography)
            * [Imagery](#Imagery)
            * [Database](#Database)
    * [Differences to Design](#Differences-to-Design)
    * [Features](#Features)
    * [Existing Features](#Existing-Features)
    * [Future Features](#Features-Left-to-Implement)
* [Technologies](#Technologies)
* [Testing](#Testing)
    * [Test Strategy](#Test-Strategy)
    * [Test Results](#Test-Results)
    * [Isses and Resolutions](#Issues-and-Resolutions-to-issues-found-during-testing)
* [Deployment](#Deployment)
    * [Project Creation](#Project-Creation)
    * [GitHub Pages](#Deployment-To-Heroku)
    * [The Vitamin Store](#The-Vitamin-Store)
    * [Fork Project](#Fork-Project)
* [Credits](#Credits)
  * [Code](#Code)
  * [Acknowledgements](#Acknowledgements)

  ****
## User Experience Design
### **The Strategy Plane**

#### Project goals<br>

* Create a website that uses Stripe payments.
* To make a full-stack site that uses HTML, CSS, JavaScript, Python + Django.
* Create a website that uses a relational database.
* To make a full-stack site based around business logic used to control a centrally-owned database.

* This website was created for for the sole purpose of completing my Milestone 4 Project for the "Code Institute’s" full stack software developer program.
  The Vitamin Store is a eCommerce site aimed at everyone that wants too or need to maintain they’re health, so we keep it simple. We supply vitamins that are affordable, fun to take, easy to remember to take. The site is designed to be responsive and easy to navigate on a range of devices to make it easily accessible for all users.

* This site was built for educational purpose and no deliveries will be fulfilled. 

### User stories
![User stories 1](readme_images/user_stories/user-stories-1.png)<br>
![User stories 2](readme_images/user_stories/user-stories-2.png)<br>
![User stories 3](readme_images/user_stories/user-stories-3.png)<br>

<br>

### **The Skeleton Plane**
#### Wireframes
* Desktop size wireframes can be viewed [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/wireframes/desktop_wireframes_png)<br>
* Tablet size wireframes can be viewed [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/wireframes/tablet_wireframes_png)<br>
* Mobile size wireframes can be viewed [here](https://github.com/Sonicbasedrop/the_vitamin_store/tree/main/readme_images/wireframes/mobile_wireframes_png)<br>

### **The Surface Plane**
### Design

#### Planned Colour Scheme
* The main colours of the site <br> ![Colours](readme_images/colour_scheme/ms4_the_vitamin_store.png)
 
* The main website text is black.
#### Typography
* Headings: Lato<br>
* Main body text : Lato

#### Imagery
* The background image used on all pages is taken with permission from unsplash.com view [here](https://unsplash.com/) contributor by the name of Towfiqu barbhuiya view image [here](https://unsplash.com/photos/w8p9cQDLX7I) see his compplete unsplash portfolio [Here](https://unsplash.com/@towfiqu999999).

* The product image used with permission from bulk.com se view [here](https://www.bulk.com/) | view product image [here](https://www.bulk.com/uk/uc-ii-collagen-capsules.html).

### **The Scope Plane**

### **Features Implemented:**<br>
##### **Create Profile**
* Users are able to:
  * Create a profile to save their orders and personal information
  * Confirm their details are correct via email verification
  * Store details for faster checkout

##### **Log in to Profile**
* Users are able to:
  * Log in to profile to see their orders and personal information
  * Edit personal information if required

##### **Products Page**
* Users are able to:
  * Products displayed and searchable to all users.
  * Sort products by A-Z, Name, Category, Price, Rating.
  * Price of product
  * See rating of product

##### **Product Details Page**
* Users are able to:
  * Click the products to find out more information including
  * Name,  price, SKU, category, Rating
  * Add products to bag to buy
  * See reviews of products and also review the products if logged in

* Super users are able to:
  * Add, edit and delete products

##### **Products Management**
* If the user is a super user they can:
  * Add a product and image of product
  * Edit a product
  * Delete a Product

##### **Bag**
* Users are able to:
  * Adjust number of products in bag if they require
  * Find out delivery costs
  * Find out how much more they need to spend to get free delivery
  * Clearly see the total of their items by quantity and grand total

##### **Checkout**
* Users can:
  * Save time as personal details pulled from profile page if user is logged in
  * Save their delivery information to their profile
  * Clearly see how much they will be charged for their items and delivery

* Logged in users can:
  * Add a Review
 ##### **Navigation**

**Header**

* All users can:
  * Navigate to home, products, bag pages, Contact page, Faq page

* Users logged in can access:
  * Profile pages, review page

* Users not logged in can:
  * Access log in and register pages

### **Error Pages**

#### *404.html*

 * 404 page created to redirect users back to the main site in case of an error

#### *403.html*

 * 403 page created to redirect users back to the main site in case they try to access a page they are not authorised to

#### *500.html*

 * 500 error page created to redirect users to the main site after a server error
<br>
![Importance and Difficulty](readme_images/user_stories/dificulty_importance.png)<br>

[Back to Table of Content](#table-of-content)

### **Database Design**<br>
![](readme_images/database_schema/database_schema.png)

### **Differences to Design**<br>
* Footer was removed, and links that was planned for footer was moved up to the main navigation menu.
  I have added additional wireframes that shows my the changes (index page shows the overall changes -
  and the faq page wireframe is added to show the consolidation of about/privacy page)

## Technologies
* [HTML](https://en.wikipedia.org/wiki/HTML)
	* This project uses HTML as the main language used to complete the structure of the Website.
* [CSS](https://en.wikipedia.org/wiki/CSS)
	* This project uses custom written CSS to style the Website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    * JavaScript is used along with [emailjs](https://www.emailjs.com/) for the contact form. This sends an email to the site owner
    on form submit.
    * [jQuery](https://jquery.com/) is used for the following: 
        * Mobile side nav
        * Displaying Success/Fail message verifying contact form status.
        * Collapsible Materialize elements.
        * Materialize modal.
        * Datepicker functionality on forms.
        * To populate downdrops on select elements.
* [Python](https://www.python.org/)
* This projects core was created using Python, the back-end logic and the means to run/view the Website.
* Python Modules used (These can be found in the requirements.txt project file):
    * asgiref==3.5.0
    *  backports.zoneinfo==0.2.1
    * boto3==1.21.18
    * botocore==1.24.18
    * chardet==4.0.0
    * dj-database-url==0.5.0
    * Django==3.2
    * django-allauth==0.41.0
    * django-countries==7.3.2
    * django-crispy-forms==1.14.0
    * django-storages==1.12.3
    * gunicorn==20.1.0
    * jmespath==0.10.0
    * oauthlib==3.2.0
    * Pillow==9.0.1
    * psycopg2==2.9.3
    * psycopg2-binary==2.9.3
    * python-dateutil==2.1
    * python3-openid==3.2.0
    * pytz==2021.3
    * requests-oauthlib==1.3.1
    * s3transfer==0.5.2
    * sqlparse==0.4.2
    * stripe==2.67.0 

* [Bootstrap](https://getbootstrap.com/)
    * The Materialize framework was used through the website for layout and responsiveness.
* [Google Fonts](https://fonts.google.com/)
	* Google fonts are used throughout the project to import the *Inter* and *Bevan* fonts.
 * [Git](https://git-scm.com/)
	* Git is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [GitHub](https://github.com/)
	* GithHub is the hosting site used to store the source code for the Website.
* [MongoDB](https://www.mongodb.com/1)
    * MongoDB was used to create the document based databases(collections) used as data storage for this project.
* [Heroku](https://dashboard.heroku.com/apps)
    * Heroku was used to deploy the live website.
* [AWS](https://aws.amazon.com/)
    * A cloud application to hold media files.
* [TinyJPG](https://tinyjpg.com/)
	* TinyJPG/TinyPNG is used to reduce the file sizes of images before being deployed to reduce storage and bandwith.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
	* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
* [balsamiq Wireframes](https://balsamiq.com/wireframes/)
	* This was used to create wireframes for 'The Skeleton Plane' stage of UX design.
* [Font Awesome](https://fontawesome.com/)
    * All the Icons displayed throughout the website are Font Awesome icons.
* [Favicon](https://favicon.io/)
    * Favicon.io was used to make the site favicon 
* [Techsini](http://techsini.com/multi-mockup/index.php)
    * Multi Device Website Mockup Generator was used to create the Mock up image in this README 
* [tinypng](https://tinypng.com/)
  * Used to reduce the size of the images for better user experience.
* [JSHint](https://jshint.com/)
    * Used to detect errors in the JavaScript files
* [PEP8 Online](http://pep8online.com/)
    * Used to check PEP8 compliance in the code
* [W3C Markup Validator](https://validator.w3.org/)
    * Markup validation service for HTML5
* [Jigsaw Validator](https://jigsaw.w3.org/css-validator/)
    * CSS3 Validation Service
* [Wave](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh)
    * Accessibility validation service.

[Back to Table of Content](#table-of-content)