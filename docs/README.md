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

## Mockup
I have already built the HTML part of the page and know what the page that potential customers or clients will visit. It can be seen live at [maria.maneobsessions.me](maria.maneobsessions.me) and can be seen below. This is the main interactive page that contians links to the content creators social media profiles, other websites, and online stores.

![Main Page](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/mainPage.PNG)

The site owner will need to then navigate to the administrative page which will prompt for a login.

![Login Page](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/loginpage.PNG)

Once authenticated the user will be directed to the /edit/ page where they can edit the number and content of links, change the color, font, and background or profile image.

![Edit Page](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/EditPage.PNG)

## Architecture Diagrams

### Level 1: System Context
![System Context](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/System%20Context%20Diagram.PNG)
### Level 2: Containers
![Containers](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/Container%20Diagram.PNG)

### Level 3: Components
![Components](https://github.com/cms-WebDesign/LinkTree/blob/main/docs/Component%20Diagram.PNG)
