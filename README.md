# Social Links

Social links is designed to be an open-source version of the [LinkTree](https://linktr.ee/) web application. The goal of the application is to give content creators and business owners the ability to consolidate all their links behind a single customizable website. The main page of the website is used to contain links to Instagram, Facebook, Twitter, Pinterest, Other websites, or whatever the user wants all behind a single easy to remember domain that is unique for each user. Currently LinkTree only offers users to have a linktr.ee/<username> URL for around $8 - $10 USD. A user can purchase a custom domain name and hosting service from websites like [NameCheap](https://www.namecheap.com/) for the same monthly price as LinkTree. Social Links is a designed to be easy to deploy, use, and customize regardless of a user’s technical ability. It contains an admin interface that gives the user the ability to change the text, links, background image, and color scheme on the main page.

## Inspiration
My wife is a Hair and Makeup Artist, and her industry relies heavily on the use of social media for marketing and to display her portfolio of work. Because of this she has an Instagram, Facebook, Website, and other links to products she sells. My goal was to create a custom made LinkTree under her own custom domain [maria.maneobsessions.me](https://maria.maneobsessions.me/) and give her the ability to update those links, profile pictures, background images, and color schemes without directly editing the HTML file. Creating a basic HTML page was easy but I wanted to add more functionality to the page and give her the ability update the page herself without relying on me. My end goal is to create an easy-to-use web application that gives other stylist the ability to create a single easy to use webpage. I have plans for more customization and other functionality that I want to bring in the future.

Note: The Installation and Getting Started steps assume the user has already secured a website domain and hosting provider via NameCheap. NameCheap offers shared hosting servers that handle SSL and offer a cPanel for customization. Due to this being a cPanel and shared hosting environment the Apache configuration file was not editable on my end so I had to rely on `whitenoise` to server the static files and urlpatterns to server the `media` files.

This application was designed to be used with the NameCheap cPanel Python Web Application Plug. I included a `docker-compose.yaml` and `dockerfile` if you want to run the application on AWS or another hosting provider via Docker. NameCheap does not support Docker so I had to settle with the cPanel Python Application. See the `docker` folder for the files and instructions. Note: If using docker you will need to serve your static and media files using Nginx or Apache. 

## Repository Installation
Login to your cPanel and scroll down to the `Files` section and select `Git Version Control`. We will need to `Create` a new repository.
  1. Click `Create` in the top-right corner of the interface.
  2. Ensure that the `Clone a Repository` is enabled and enter the `ssh` or `https` repo URL listed below.
  3. In the `Repository Path` text bos enter the path to the directory that will contain the repository.
  4. Enter the desired `Repository Name` (Note: The name does not impact functionality, and instead only functions as a display name)
  5. Select `Create` and the repository will be created.
Refer to [NameCheap Git Documentation](https://docs.cpanel.net/cpanel/files/git-version-control/) for any issues.

```
git@github.com:cms-WebDesign/SocialLinks.git
https://github.com/cms-WebDesign/SocialLinks.git
```

## Setting up the Python Web Application
Once the repository is installed go back to the cPanel homepage and scroll down to the `Software` section and select `Setup Python App`. From the `Setup Python App` page select `Create Application` and follow the steps below.
  1. Select Python version `3.8.6`. (Note: Per NameCheap support this is the only version of Python that works with `Pillow` which is used for image uploading)
  2. Set the `Application Root` to the location of the Django Web App. (i.e. the repository we just cloned `repositories/SocialLinks` was mine)
  3. `Application URL` will be the domain name to your application. Don't forget to add this domain name to your `settings.py` `ALLOWED_HOSTS` section.
  4. Set the `Application startup file` will be `passenger_wsgi.py`.
  5. `Application Entry point` is set to `application`.
  6. Select `Create` to create the web application and then click `Stop App` if the app is running.
  6. Type in `requirements.txt` underneath the `Configuration files` section and select the `Run Pip Install`. (Note: pip may need to be updated. To do so enter your Python virtual environment via the terminal plugin using the command at the top of the webpage and upgrade pip)
  7. Create an `Environment variable` for your `SECRET_KEY`.
  8. In the `Execute Python Script` type in the following commands
      * `manage.py collectstatic —no-input`

## Creating a Superuser/Admin account
To create a superuser account we will need to access the cPanel Terminal or SSH into our host.
  1. Before leaving the `Python Web Application Creation` page scroll to the top and copy the command in the blue box.
      * `source /home/<USERNAME>/virtualenv/repositories/SocialLinks/3.8/bin/activate && cd /home/<USERNAME>/repositories/SocialLinks`
      Note: This is what the command should look like, this will enter the `Python` virtual environment via the command line.
  2. Scroll down to the `Advanced` tab and select `Terminal`.
  3. Enter the command above in step 1.
  4. Run the following commands:
    Note: Be sure to enter a secure username and password as this is the master account to the web application.
    This is also how you would upgrade pip if needed to in the previous section `python -m pip install --upgrade pip`.

```
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
```

  5. The web application should be ready to go. Head on over back to the `Python Web Application` and select `Start App`

## Getting Started
Once the application is up and the admin account is created head on over to the websitedomain/admin/ tab and login.
Once logged in the administrative user can customize the links, background, colors, or text on the page to their choosing. Simply save the changes and the website will be updated with the new changes. An explanation of the objects can be seen below.

## Setting up the Webpage

In order to customize the webpage to your liking log into the admin interface and change the default values for the admin models described below. The admin interface has 5 different models that allow customization of the main page. Currently only the contents of `object (1)` (the default one) will be rendered on the webpage. In the future I hope to add the option for users to create templates and chose the object (i.e. `object (1)` or `object (2)`) they want rendered on the webpage.   

#### styleEditor
The `styleEditor object (1)` contains the following CSS style options.
  * `Title` - Changes the title of the webpage.
  * `Link_Color` - Changes the color of the links.
  * `Link_Font_Style` - Changes the Font Style of the links.
  * `Link_Background_Color` - Changes the background color of the section where the links are displayed.
  * `Link_Hover_Color` - Changes the color of the link when a user hovers over it with a mouse.

#### backgroundPic
The `backgroundPic object (1)` stores the image used for the background of the webpage.

#### profilePic
The `profilePic object (1)` stores the profile picture displayed on the webpage.

#### Linkss
The `linkss object (1)` stores the website address for the 7 links on the main webpage.

#### linkText
The `linkText object (1)` stores the names for each of the website addresses set in the `linkss` object above.

## Future Features to Add at a Later Date
Due to my technical ability, experience with Django/Python, and time constraints for the class I was not able to implement everything that I wanted for this project. Below are a couple features I plan on developing after this class ends as a side project.
  * Ability to change the Number of Links displayed on the main page.
  * Ability to adjust the favicon icon next to each link.
  * Ability to create templates (saved as object numbers) and chose which template is displayed.
  * Font Selector in the admin page that lets the admin user select the font instead of typing it in.

# License
The MIT License (MIT)

Copyright (c) Christopher H. Schmitt 2021

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
