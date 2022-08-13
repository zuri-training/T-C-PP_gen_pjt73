# Project Team 73
## Project overview 
The goal of this project is to create a platform that allows users to generate terms & conditions and privacy policy. One of the challenges faced by some business owners is the high cost of generating T&C and Privacy Policy on the already existing platforms which we seek to bring solutions to by allowing users generate these documents on our platform freely.
check  out the full details of the project https://docs.google.com/document/d/1mrrL7DMUgK_YUIF1nZMxtSsAxN-qaaHn1L9blHwyq50/edit?usp=drivesdk

# Table of contents 
1. General information 
2. Technologies used
3. Features 
4. product specification 
5. Usage 
6. Project status 
7. Collaborations
8. Contributors 
9. Acknowledgment 
# General information 
T&C and privacy policy generator is a platform that allows users to easily generate terms and conditions and privacy policy without having to hire a lawyer or subscribe to a Compliance generator website.

The goal of this project is to make easy T&C and privacy policy generator accessible to users ant to help users to generate either T&C or Privacy Policy easily on any format without any form of payment attached to the service.

# Technologies used 
- figma/figjam (Design)
- HTML/CSS/JavaScript (Frontend)
- Django (Backend)
- MySQL (Database)
- Bootstrap (Frontend Library)

# Features
 User: Unauthenticated
- Visit the platform to view basic information about it
- View and Interact with the documentation
- Register to view more details
- No access to use until registered

 User: Authenticated
- Full access to the platform
- Allow users enter basic information
- Generate selected files with the right data and information
- Allow export, download, share and website embed
- Allow user save data and come back to download

# Product Specification
- Phones
- Tablets
- Computers


# User Flow 
- Visit the Website (Hosted link here)
- Browse through
- Sign Up
- Verify your Email
- Sign In
- Customize your profile
- Generate terms and conditions
- Generate Privacy policy
- Proceed to download 

# Project Deployment(Locally)
- Homepage at 127.0.0.1:8000(python localhost)
- The homepage nav links
  - Services @ http://127.0.0.1:8000/blog/service/
  - About Us @ http://127.0.0.1:8000/blog/about/
  - Reviews @ http://127.0.0.1:8000/#reviews
  - Contact Us @ http://127.0.0.1:8000/#reviews
  - Login @ http://127.0.0.1:8000/accounts/signin/
  
- All the "Get Started" links on the homepage are redirect to:
  - http://127.0.0.1:8000/accounts/dashboard/ (if the user is authenticated)
  - http://127.0.0.1:8000/accounts/signin/?next=/accounts/dashboard/ (if the user is not authenticated)

- For the Sign in page, links:
  - Forgot Password (@ http://127.0.0.1:8000/password-reset/)
      The Forgot Password page has 3 pages rendered while following the procedure to reset the user's password:
          - Password Reset Done @ http://127.0.0.1:8000/password-reset-done/
          - Password Reset Confirm @ http://127.0.0.1:8000/password-reset/confirm/<uidb64>/<token>/
          - Password Reset Complete @ http://127.0.0.1:800/password-reset-complete/
          
  - Google Authentication (@ http://127.0.0.1:8000/social_auth/login/google-oauth2/)
  - Facebook Authentication (@ http://127.0.0.1:8000/social_auth/login/facebook/)
  - Sign In (@ http://127.0.0.1:8000/accounts/signup/)

# Project Status 
Project is: in progress

# Collaborations
# Contributors
Oladapo Itunuoluwa	
- Email - runcaus16@gmail.com
- GitHub - https://github.com/ditoruncaus
- Stack -  Product Design

Ekundayo Opeyemi	
- Email - Opeyemimessi@gmail.com
- GitHub - https://github.com/OpeyemiE
- Stack -  Product Design

Eze Michael	
- Email - ezemickey09@gmail.com
- GitHub - https://github.com/Michael-Kings
- Stack - Product Design

Unique-Gift Amah     	
- Email - uniquegift4amah2016@gmail.com
- GitHub - https://github.com/Unique-Gift
- Stack - Product Design

Mong Samuel Onwu	  	
- Email - info.samuelonwu@icloud.com
- GitHub - https://github.com/kingoftwins
- Stack - Product Design

Angela Abasiama Okon
- Email - adiahaokon9@gmail.com
- GitHub - https://github.com/Adiaha-okon
- Stack - Product Design

Annette shadeya	
- Email - ashadeya@gmail.com
- GitHub - https://github.com/AnnieUXUI
- Stack - Product Design

Dorcas Owolabi
- Email - owolabidorcas40@gmail.com
- GitHub - https://github.com/Dorcaslas22
- Stack - Product Design

Esther Adekunle 
- Email - estheradeks360@gmail.com
- GitHub - https://github.com/estheradeks
- Stack - Product Design

Joe Judith	 
- Email - joejudithc@gmail.com
- GitHub - https://github.com/Chi-joe
- Stack - Product Design

Ogechi Marry Eze 
- Email - ezeogechi57@gmail.com
- GitHub - https://github.com/Ogeeze
- Stack - Product Design

Onyenama Victor
- Email - onyenamavic@gmail.com
- GitHub - https://github.com/sventreprise14
- Stack - Product Design

Kolapo Goodness
- Email -goodnesskolapo@gmail.com
- GitHub - https://github.com/Goodness5
- Stack - Fullstack

Ayodele Kadiri
- Email -ayodelekadiri.ak@gmail.com
- GitHub - https://github.com/Grttechie
- Stack - Fullstack

 Mariam Smith
- Email -mariams58@yahoo.com
- GitHub - https://github.com/mariams58 
- Stack - Fullstack

Abdullah
- Email -olam4461@gmail.com
- GitHub - https://github.com/Cruxcodes
- Stack - Fullstack

Favour
- Email -divinephavor@gmail.com
- GitHub - https://github.com/Phav4
- Stack - Fullstack

Adnan Ahmad
- Email -ahmadadnan2235@gmail.com
- GitHub - https://github.com/deekay25
- Stack - Fullstack

Ogbe Jude
- Email -ogbejude24@gmail.com
- GitHub - https://github.com/ogbe
- Stack - Fullstack

Nenne A
- Email -nne.akuma@gmail.com
- GitHub - https://github.com/NneneA
- Stack - Frontend

Olorunsola Taiwo Joshua 
- Email -scholeraw001@gmail.com
- GitHub - https://github.com/Oboc
- Stack - Fullstack


# Acknowledgment
This project was inspired by Zuri
Our sincere gratitude God Almighty, and to Zuri & Ingressive4Good for this wonderful opportunity to explore tech in a dynamic way.
