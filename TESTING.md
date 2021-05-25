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

#### Site Admin

1. As a site admin, I want to be able to edit or delete other user posts should they contain anything inappropriate.
2. As a site admin, I want to be able to manage items within the store be it adding, updating or deleting.

### Problems and bugs encountered.