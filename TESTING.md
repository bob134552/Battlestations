Expanded from [README.md](https://github.com/bob134552/Battlestations/blob/master/README.md)

# Testing section

The site was tested on desktop using Google Chrome's developer tools.
It was also tested on several devices: Samsung Galaxy S10+, iPhone 12, Samsung Tab A and iPhone 11.

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to ensure there was no errors in CSS files.  
[W3C HTML Validator](https://validator.w3.org/) was used to check for errors in all templates, any error left is due to django templating.
[BeautifyTools](https://beautifytools.com/javascript-validator.php) was used to validate all written javascript.
[PEP8 online check](http://pep8online.com/) was used to check for errors in python code for all apps.
- Some errors due to length of lines ignored due to not being able to be shortened.

### Manual Testing Based On User Stories

#### New User

1. As a new visitor, I want to be able to navigate the site with ease.

    Navbar:

    - The navbar is always available to the user throughout the site.
        - Clicking on the brand logo of the site (available on large screens) or on the home link brings the user to the front page of the site.
    - Clicking on the dropdown for products allows the user to view either all products or a specified category.
    - Clicking on the Pre-Built nav link filters to show only pre-built PCs.
    - Clicking on the Build a PC nav link takes the user to a form where they are able to pick PC components for a personal custom build.
    - Clicking on the My Profile drop down gives users the option to sign up or login if the user isn't logged in.
        - Meanwhile if the user is logged in they are given to option to view their own profile and log out.
        - If user is a site admin they are able to access product management too and add a product.

2. As a new visitor, I want to be able to use the site before registering and being able to purchase products without signing up.

    - All features of the site are available to the user except for being able to leave a review or comment on products.
    - Able to purchase products without signing up and able to see order summary through the link provided in the confirmation email sent after purchase.

3. As a new visitor, I want to be able to sign up easily.

    Sign up and log in page:

    - The sign up page is easy to access and is available through the "My Profile" dropdown on the top right of the site.
        - Signing up is simple to do and only requires and username, email and password.
    - Alternatively if user wishes to log in with a social account the option is available on the log in page.

#### Returning User

1. As a returning user, I want to be able to quickly purchase any product I may need.

    Checkout Form:

    - User delivery information is stored and displayed on the user profile page.
    - Information is saved if the user specified for it to be saved during their first purchase on the checkout form.
    - Delivery information can be manually added by the user in the user's profile page.

2. As a returning user, I want to be able to edit my details should they change.

    User Profile Page:

    - Delivery details are available on the user's profile page and can be updated as needed.
    - Below the delivery details form there is options of change password, email and connect a social account to the user account.
    - Each form for change password and email is straight forward and easy to use.

3. As a returning user, I want to be able to leave a review on the site based on my order experience.
    
    Review Form:

    - At the bottom of the home page, users are able to leave 1 review should they wish. The review also includes a star rating they
        can select.
    - Users are limited to 1 review per user to prevent multiple reviews from the same user.
    - Attempting to submit the review form with an empty text input or no star rating prompts the user that both are required.

4. As a returning user, I wish to be able to leave comments on the products I've purchased and view other users opinions too.

    Product Details Comment Section:

    - Logged in users are able to submit as many comments as they wish on each product's details page.
    - Most recent comments are shown at the top.
    - Submitting a blank comment requires notifies user that there needs to be some input for a comment to be submitted.
    - Clicking on update allows the user to edit their comment and after submitting the update it is correctly displayed.
    - Deleting a comment removes it from the comment section.

#### Site Admin

1. As a site admin, I want to be able to edit or delete other user posts should they contain anything inappropriate.

    - For both the site review section on the home page and the comment section for each product, a site admin is given the 
        option to either delete or update another users review or comment.

2. As a site admin, I want to be able to manage products within the store be it adding, updating or deleting.

    Product Management Add/Update Form:

    - Attempting to access this page if user is not a site admin will return user to the login page.
    - The site admin is able to access both these pages, both are similar but the update page is prefilled with the selected products information.
    - Submitting the form without a required field informs the user.
    - Should the image for a product need to be changed, the new image's file name is shown so user knows what its changing to.
    - Clicking remove on a product opens a modal asking the user if they are sure to prevent accidental deletion of a product.

## Testing Elements on each page

### Home page

#### Navbar

- Clicking on the logo returns user to home page.
- Clicking on the home nav link takes user to home page.
- Clicking on the products dropdown gives users access to all products or a cetain category.
- Clicking on the pre built PCs filters all products for pre built PCs.
- Clicking on Build a PC takes users to the build a PC page.
- Clicking on the My Profile presents the users options respective of if they are logged in or not.
    - Sign up and log in when not logged in.
    - My profile and log out if logged in with Product Management if user is admin.
- Clicking on the basket takes the user to the basket page.

#### Carousel

- Clicking on the left or right button slides to the next or previous product.
- Clicking on the product image takes the user to the selected product's details page.

#### Site Review Section

- If not logged in user will be asked to log in or sign up.
- If user is logged in they are able to access the add/update review page.


### Products/Search page

- Clicking on the products image or name takes the user to the product's detail page.

#### Sort dropdown

- Clicking on the Sort by dropdown shows options to sort the products currently displayed.
- Clicking on Name(A-Z) or Name(Z-A) will sort products in ascending or descending order.
- Clicking on Category(A-Z) or Category(Z-A) will sort products into categories in ascending or descending order.
- Clicking on Price(low to high) or Price(high to low) wil sort products in ascending or descending order based on cost.


### Add to basket button and quantity selector on multiple pages(products, search and product details page).

- Clicking the add to basket button adds the specified product and its quantity to the basket.
- Clicking on the plus or minus button on the quantity selector increments or decrements the quantity value.
- Clicking on add to basket button with a selected quantity adds that product and that quantity to the basket.

### Basket Page

- Clicking on update changes the quantity of the selected product to the new quantity specified.
- Clicking on remove removes the selected product from the basket.
    - Removing a custom built pc also deletes it from the database.
- Clicking on the products name takes user to the product's details page.

### Checkout page.

- Filling form out correctly and submitting takes users to checkout success page.
- Leaving a required field blank notifies user of a missing field.
- Filling the card details input incorrectly notifies user when they submit.
- Commenting out the form.submit() in the stripe_elements.js stops the user from being taken to the checkout success.
    - The order is still submitted as the webhook handler adds it to the database and sends a confirmation email to the user should the form fail.

### Profile page

- Filling the delivery details and submitting adds or updates the details based on user input.
- Clicking on a order number if available takes user to a page similar to the checkout success page that displays the users order details.

### Problems and bugs encountered.

