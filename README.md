# BattleStations

## Milestone Project 4 - Full Stack Development

## Bobby Jackson

<img src="#" alt="responsive-mockup">

The live site can be found [here]().

A site designed for use by anyone that is enthusiastic about reading, sharing and finding comic books.
The website contains comics from a variety of genres. 
The website features a gallery of various comic books with search function, user registration, comic book editing,
the ability to favourite comics and a contact page. editing
The primary goal of the website is to create a large collection of various comic books for a wide user base. 

## UX

The ideal user for this site is:
- Interested in sharing and recommending comic books they have read.
- Interested in searching for new comics to read.
- English speaking.

Visitors to the site are looking for:
- A place to return to for suggestions on the next comic book to read.
- The ability to make new entries on comics that may not be already on the site.
- The ability to favourite comics they are interested in reading, so they can easily find them in the future. 

The website should be:
- Easy to navigate.
- Have a simple registration and log in.
- Able to search through a collection of comics to find specific ones.
- Able to moderate content added to the site. 

### User Stories

#### New User

1. As a new visitor, I want to be able to navigate the site with ease.
2. As a new visitor, I want to be able to use the site before registering, 
   and still be able to use most features, so that I make an informed decision on whether to sign up. 
3. As a new visitor, I want to be able to sign up easily and get started browsing.

#### Returning User

1. As a returning user, I want to be able to favourite comics to know which ones I am interested in.
2. As a returning user, I want to provide my own entries to the collection.
3. As a returning user, I want to be able to edit my details should they change.
4. As a returning user, I want an easy to fill-in contact form, so I can contact the owner of the site for new ideas or to help moderate the site.

#### Moderator

1. As a moderator, I want to be able to edit or delete other user posts should they contain anything inappropriate.
2. As a moderator, I want to be able to give other users the moderator status should they be willing to help maintain the site.

### Design

- Colour Scheme
    - 

- Imagery
    - 

### Wireframe Mockups

- Site Map - [View]()
- Deskop Wireframe - [View]()
- Mobile Wireframe - [View]()

## Features



#### Home Page



#### Profile Page


#### Register Page

#### Login Page

The Login page contains a simple form that requires two inputs; username and password.
A submit button below the form brings the user to their Home page, if the login details are entered correctly.
If the details are incorrect the user is notified that either the username/password was incorrect. 
Below the submit button, there is a link to the registration page for users that are not registered. 

#### 404 Page

This page is used to handle 404 errors in the event that the user tries to open a page that does not exist.
It contains a button that redirects users to the Home page.

### Existing Features

### Features to add in the future.



## Technologies used (Frameworks, Libraries, Languages and Programs used)

- [HTML5](https://en.wikipedia.org/wiki/HTML)
    - To structure the content on each page of the site.
- [CSS](https://en.wikipedia.org/wiki/CSS)
    - To style the site in order to make it more appealing to the user.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - To initialise materialize functions and write custom functions to the site.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - To write and handle back end functions for the site.
- [Django]()
- [jQuery](https://en.wikipedia.org/wiki/JQuery)
    - Allows for easier DOM manipulation.
- [Bootstrap]()
- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
    - Helps writing code in Python by importing functions such as render_template and flash etc.
- [Heroku](https://www.heroku.com/)
    - Used for deploying and managing the project.
- [Balsamiq](https://balsamiq.com/)
    - Used to design the wireframe of the project during the design process.
- [GitHub](https://github.com/)
    - Used to store the projects code.
- [GitPod](https://www.gitpod.io/)
    - IDE used to build the site.

## Testing

Testing can be found in [TESTING.md]()

## Deployment

The project was developed using Gitpod IDE. It was committed and pushed to GitHub through the use of git using the functions in Gitpod.

It was then deployed on Heroku by connecting the GitHub repository to the Heroku app.

To deploy the app on Heroku, first clone the repository.

To Clone the repository:
1. Log into GitHub.
2. Install [Gitpod](https://www.gitpod.io/)
3. Select the [comics repository](https://github.com/bob134552/comics) from the list of repositories.
4. At the top of the page click the drop down button with "code". 

<img src="/static/images/dropdown-code.jpg" alt="code-button">

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

<img src="/static/images/config-vars.jpg" alt="config-vars">

7. Once filled in you can then return to the "Deploy" tab and scroll to the bottom and click "Deploy branch".

Your app should be deployed and a link will be available to view it.

### Notes:

## Credits

### Media


### Acknowledgements