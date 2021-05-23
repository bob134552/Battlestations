# BattleStations

## Milestone Project 4 - Full Stack Development

## Bobby Jackson

<img src="/media/responsive-mockup.png" alt="responsive-mockup">

The live site can be found [here](https://battlestations-mp4.herokuapp.com/).

A site designed to allow users to view and purchase computer components, pre-built desktops or create their own custom
build from the parts provided within the store.
The website contains products recently released and aims to keep up to date with all recent releases of PC parts. 
The website features a catalogue of recently released product, user registration including social media integration 
and email authentication and the ability to create your own custom desktop PC.
The primary goal of the website is to create a easy platform for users to browse, buy and comment on products available
on the site. 

## UX

The ideal user for this site is:
- Interested in either building or purchasing desktops or components for their own builds.
- Interested in leaving their thoughts on products to help other users.
- English speaking.

Visitors to the site are looking for:
- Other users thoughts on products being sold on the site.
- The ability to purchase any available product on the site.
- The ability to create personal PC builds based on items within the store. 

The website should be:
- Easy to navigate.
- Have a simple registration and log in with the possibility of using a social account to log in with.
- Able to search through a database of PC components to find specific ones.
- Able to add or remove products as required.

### User Stories

#### New User

1. As a new visitor, I want to be able to navigate the site with ease.
2. As a new visitor, I want to be able to use the site before registering and being able to purchase products without signing up. 
3. As a new visitor, I want to be able to sign up easily.

#### Returning User

1. As a returning user, I want to be able to quickly purchase any product I may need.
2. As a returning user, I want to be able to edit my details should they change.
3. As a returning user, I want to be able to leave a review on the site based on my order experience.
4. As a returning user, I wish to be able to leave comments on the products I've purchased and view other users opinions too.

#### Site Admin

1. As a site admin, I want to be able to edit or delete other user comments and reviews should they contain anything inappropriate.
2. As a site admin, I want to be able to manage items within the store be it adding, updating or deleting.

### Design

- Colour Scheme

    From researching designs of other PC building/parts selling sites, the colour scheme of orange-yellow and black was chosen to give a sharper,
    minamalistic look.

### Wireframe Mockups

- Site Map - [View](https://github.com/bob134552/Battlestations/tree/master/wireframes/site-map.pdf)
- Deskop Wireframe - [View](https://github.com/bob134552/Battlestations/tree/master/wireframes/desktop-wf.pdf)
- Mobile Wireframe - [View](https://github.com/bob134552/Battlestations/tree/master/wireframes/mobile-wf.pdf)

## Features

#### Navbar

The navbar is available throughout the site as a means for the user to be able to search the site through the available search bar, access their basket
and the user's personal profile page. Users are also able to move through the site using the navigation links available to them. The navbar is 
responsive and will collapse on smaller screens.

#### Footer

Contains social media links to Facebook, Google and Instagram.

#### Home Page

The Home page features a carousel featuring recent pre-built PCs available for purchase, a section allowing users to choose a category to view,
and a site review section where the 4 most recent reviews are visible for new or returning users to view. The site reviews section also allows 
a logged in user be able to write their own review and give a star rating which adds to the average rating above the reviews.

#### Site Review Page (add and update)

The site review page is a form consisting a radio button star rating and a text field for users to write their review of the site. The update page is the same
but prefilled with the users initial review. There are 2 buttons available to the user, a home button should they wish to not submit or edit their review 
and a submit button to save their review.

#### Profile Page

The Profile page is accessable from the profile option in the navbar, it features a form of the users previously saved delivery details, an order
history that they can click on to view previous orders and 3 buttons that bring them to the email management, password change and social account 
management pages.

#### Email Management page

The Email Management page allows users to select a primary email to be used, add/remove and verify additional emails if required and change primary email
address.

#### Social Accounts page

The Social Accounts page allows users to manage their social connections and connect or remove their Facebook and Google accounts to their profile.

#### Sign up

The Sign Up page consists of a form to gather a users email, desired username and password in order to allow them to register for an account. Alternatively
there is a link that redirects to the log in page so they can log in with a social account.

#### Login Page

The Login page contains a simple form that requires two inputs; username and password.
A submit button below the form takes the user back to the home page, if the login details are entered correctly.
If the details are incorrect the user is informed that either the username/password was incorrect. 
There is a link to the sign up page, 2 social buttons(Facebook and Google) that allow a user to login with a social account and a link to the 
password reset page that allows users to reset their password through email.

#### All Products page

The All Products page displays a list of all available products to the user excluding Pre-built PCs. The user is able to see core information on each product, add a specified quantity 
of the product to the basket and be able to sort the products by name, price and category in either ascending or descending order. Through the dropdown in the navbar
the user is able to search a specific category (such as cooling, cpus etc.)

### Product Details page

The Product Details page is a page to display all details of a selected product should a user wish to know more. There is a quantity and add to basket button available for the user
should they wish to purchase the product that they are viewing. A comment section is also available for each product should users wish to leave messages regarding the product
or ask questions.

#### Build a PC page

The Build a PC page consists of a form containing dropdowns for each component category for a user to pick from and create their own unique PC build.

####  Search Page

The search page is used to display user queries through the use of the search bar. If no results are returned the user is notified and there is a link to go back to 
all products.

#### Basket Page

The Basket page displays all current items in the users basket and allows them to either remove or update the quantity of each item in the basket. The final costs 
are also displayed to the user. If there are no items in the users basket the user is notified that the basket is empty and given a button to go back to the products
should they wish to add anything to their basket.

#### Checkout Page

The checkout page cosists of a form asking user for delivery details, Stripe card payment input and a card featuring the users order summary.
On submit of an order the page is overlayed with a loading spinner until the payment intent webhook from stripe is received and user is redirected to the
checkout success page for their order.

#### Checkout Success/Order History page

The checkout success page is displayed after a successful purchase. the order history page is displayed when checking your purchase from the profile page.
Both pages contain similar information such as order summary and delivery details. One of the notable differences is that the order history page contains a
button back to the profile page.

### Existing Features

- Comment section for products.
- Social account login.
- Stripe Payment handling.
- Build a custom PC.
- Site reviews.
- Site management for admins.

### Features to add in the future.

- The ability to edit custom builds instead of restarting the build.
- The ability to edit pre built PCs if required.
- The ability to give thumbs up/down to products and comments using Facebook like system.
- A chat box for visitors so they can talk about upcoming releases and keep site traffic up.

## Technologies used (Frameworks, Libraries, Languages and Programs used)

- [HTML5](https://en.wikipedia.org/wiki/HTML)
    - To structure the content on each page of the site.
- [CSS](https://en.wikipedia.org/wiki/CSS)
    - To style the site in order to make it more appealing to the user.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - To initialise some bootstrap5 elements and write custom functions to the site.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - To write and handle back end functions for the site.
- [Django](https://www.djangoproject.com/)
    - To allow for easier creation of the site.
- [jQuery](https://en.wikipedia.org/wiki/JQuery)
    - Allows for easier DOM manipulation.
- [Bootstrap5](https://getbootstrap.com/)
    - To make a responsive mobile first site and allow for a simpler structure.
- [Heroku](https://www.heroku.com/)
    - Used for deploying and managing the project.
    - Postgres database used outside of developement.
- [Balsamiq](https://balsamiq.com/)
    - Used to design the wireframe of the project during the design process.
- [GitHub](https://github.com/)
    - Used to store the projects code.
- [GitPod](https://www.gitpod.io/)
    - IDE used to build the site.
- [Amazon Web Services](https://aws.amazon.com/)
    - Used to store static and media files through S3
- [Stripe](https://stripe.com/en-gb)
    - Handles card payments.
- [Facebook Developers](https://developers.facebook.com/?no_redirect=1)
    - To allow Facebook log in to the site.
- [Google Developers](https://developers.google.com/)
    - To send verification and checkout success emails through Google and allow log in with a Google account.
- [SQLite3](https://www.sqlite.org/index.html)
    - For database management during developement.
- [Tailor Brands](https://www.tailorbrands.com/)
    - For brand logo design.
- [Google Fonts](https://fonts.google.com/)
    - To apply a different font to the site than the standard font.

## Testing

Testing can be found in [TESTING.md](https://github.com/bob134552/Battlestations/blob/master/TESTING.md)

## Deployment

The project was developed using Gitpod IDE. It was committed and pushed to GitHub through the use of git using the functions in Gitpod.

It was then deployed on Heroku by connecting the GitHub repository to the Heroku app.

To deploy the app on Heroku, first clone the repository.

To Clone the repository:
1. Log into GitHub.
2. Install [Gitpod](https://www.gitpod.io/)
3. Select the [Battlestations repository](https://github.com/bob134552/Battlestations) from the list of repositories.
4. At the top of the page click the drop down button with "code". 

5. Copy the HTTPS link provided.
6. Open your IDE and change the current directory to the location where you want the cloned directory to be.
7. Type ```git clone``` and paste the copied HTTPS link after.

    Example:

    ```git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY```

8. Hit Enter and your clone of the repository will be made.

If any problems occur refer [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for help.

To deploy on Heroku.

1. Log into Heroku.
2. Click on "New" button and "Create new app" on the drop down.
3. Write your apps name and select a region close to you.
4. From the app page select "Deploy" and connect to the GitHub cloned repository from before.
5. For the app to work there are a few settings required, Select the "Settings" tab.
6. Click Reveal Config Vars to show this.

<img src="README_TESTING_IMAGES/config-vars.png" alt="config-vars">

7. Once filled in you can then return to the "Deploy" tab and scroll to the bottom and click "Deploy branch".

Your app should be deployed and a link will be available to view it.

Depending on the database you use you will need to follow some extra steps.

### Notes:

## Credits

### Media


### Acknowledgements