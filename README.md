# Social Links

Social links is designed to be an open-source version of the [LinkTree](https://linktr.ee/) web application. The goal of the application is to give content creators and business owners the ability to consolidate all their links behind a single customizable website. The main page of the website is used to contain links to Instagram, Facebook, Twitter, Pinterest, Other websites, or whatever the user wants all behind a single easy to remember domain that is unique for each user. Currently LinkTree only offers users to have a linktr.ee/<username> URL for around $8 - $10 USD. A user can purchase a custom domain name and hosting service from websites like [NameCheap](https://www.namecheap.com/) for the same monthly price as LinkTree. Social Links is a designed to be easy to deploy, use, and customize regardless of a user’s technical ability. It contains an admin interface that gives the user the ability to change the text, links, background image, and color scheme on the main page.

## Inspiration
My wife is a Hair and Makeup Artist, and her industry relies heavily on the use of social media for marketing and to display her portfolio of work. Because of this she has an Instagram, Facebook, Website, and other links to products she sells. My goal was to create a custom made LinkTree under her own custom domain [maria.maneobsessions.me](https://maria.maneobsessions.me/) and give her the ability to update those links, profile pictures, background images, and color schemes without directly editing the HTML file. Creating a basic HTML page was easy but I wanted to add more functionality to the page and give her the ability update the page herself without relying on me. My end goal is to create an easy-to-use web application that gives other stylist the ability to create a single easy to use webpage. I have plans for more customization and other functionality that I want to bring in the future.

Note: The Installation and Getting Started steps assume the user has already secured a website domain and hosting provider.

## Installation
```
git clone git@github.com:cms-WebDesign/SocialLinks.git
docker-compose run app django-admin startproject app .
```
Note: If on Linux you will need to adjust the file permissions as they are owned by root. To do so execute the following command
```
sudo chown -R $USER:$USER .
```

## Getting Started
```
docker-compose build
docker-compose up
```
Open another terminal and run the following commands to create the database superuser.
```
docker-compose exec app python manage.py migrate
docker-compose exec app bash
python manage.py createsuperuser --username admin --email admin
```
To run other django commands simply type:
```
docker-compose exec app [cmd]
```

Once the container is up and the admin account is created head on over to the /admin/ tab and login.

Once logged in the user can customize the links, background, colors, or text on the page to their choosing. Simply save the changes and the website will be updated with the new changes.

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

# License
The MIT License (MIT)

Copyright (c) Christopher H. Schmitt 2021

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
