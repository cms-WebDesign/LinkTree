# User Stories

## User Story 1
As an **user**, I want to **consolodate all of my social media and website links** so I can **present them to potential customers on a single website**.

### Acceptance Criteria
**Given** the app is running **when** visiting the webpage **then** all of my social media links should be displayed. 

### Mis-User Stories
As a **malicious user**, I want to **maliciously edit the links** so I can **redirect the customer to a malicious website and decredit the users buisiness or social media presence.**

### Mitigation Criteria
Implement an administration page and ensure all of the edits done to the main link page are performed by an authenticated user. 

## User Story 2
As a **customer**, I want to **easily view all of a clients work** so I can **select the perfect client**.

### Acceptance Criteria
**Given** the app is running **when** visiting the webpage **then** the potential clients social media and websites should be easily accessible.

## User Story 3
As an **administrator**, I want to **customize of my links** so I can **easily update them whenever my social media names change**.

### Acceptance Criteria
**Given** the app is running **when** I visit the admin page **then** I can customize and edit my links, background image, and color scheme. 

### Mis-User Stories
As a **malicious user**, I want to **compromise the admin account** so I can **maliciously edit links and redirect them to my sites.**

### Mitigation Criteria
Implement server side authentication for the admin page to ensure it is only accessible by the authenticated user using a secure password. 

# Diagrams

## Mockups
I have already built the HTML and CSS parts of the main landing page; it can be seen live at [maria.maneobsessions.me](https://maria.maneobsessions.me/maria.maneobsessions.me) and can be seen below in the image. This is the main interactive page that contains links to the content creator’s social media profiles, other websites, and online stores. The goal is to add more functionality so my spouse can edit the links, color schema, and background/profile images without having to ask me to edit the HTML directly. 

### Main Landing Page
![Main Page](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/mainPage.PNG)

This is the main landing page that the user in User Story 1 will use to present their social media links to customers in User Story 2. In order to edit the links, the administrative user will need to navigate to the administrative page which will prompt for a login seen in the next image.

### Login Page
![Login Page](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/loginpage.PNG)

The administrator in User Story 3 would authenticate on this page to access the /edit/ page in order to change the main landing page.

### Editing Page
![Edit Page](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/EditPage.PNG)

The edit page is where the administrator in User Story 3 can edit the number and content of links, change the color, font, and background or profile image.

## Architecture Diagrams

### Level 1: System Context
![System Context](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/System%20Context%20Diagram.PNG)
### Level 2: Containers
![Containers](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/Container%20Diagram.PNG)

### Level 3: Components
![Components](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/Component%20Diagram.PNG)
