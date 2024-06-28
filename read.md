
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Linkedin: Ajay](https://img.shields.io/badge/-Ajay-blue?style=flat-square&logo=Linkedin&logoColor=white&)](https://www.linkedin.com/in/ajay-mulgir2312/)
[![GitHub: Priya730](https://img.shields.io/github/followers/RockersAj23?label=Follow%20%40RockersAj23&style=social)](https://github.com/RockersAj23)
<hr>
<h1 align="center"><a href="https://summerofcode.withgoogle.com/programs/2022/projects/YNXT2TFX" target="_blank">Build Access and Entitlements for Hosted version of Augur</a></h1>
<figure>
  <img src="project/chaoss-gsoc.png" align="center">
</figure>
<p align="center">Check out my <a href="https://medium.com/@shivikapriya730">blog</a> or follow me on <a href="https://twitter.com/shivikapriya">Twitter</a> for more updates.</p>
<p align="center">
  <a href="project/Priya_Srivastava_GSoCproposal_CHAOSS.pdf"> Proposal </a>|
  <a href="#project-details"> Project Details</a> |
  <a href="activity-reports/"> Blogs</a> |
  <a href="#additional-info-"> Links</a>
</p>
<!--[![Twitter: shivikapriya](https://img.shields.io/twitter/follow/shivikapriya?style=social)](https://twitter.com/shivikapriya)-->

## CONTENTS
* [Project Details](#project-details)
* [Objectives](#objectives-)
* [Objectives Accomplished](#objectives-accomplished-)
* [Work](#work-)
* [Activity Reports](#activity-reports-)
* [Mentors and Team](#mentors-and-team-)
* [Acknowledgment](#acknowledgment-)
* [Additional Info](#additional-info-)
* [Student Developer Info](#student-developer-info-)
  
## PROJECT DETAILS[&uarr;](#contents)
### [Augur](https://github.com/chaoss/augur):
The aim of the project is to build login and access for users. Augur is a software suite for collecting and measuring structured data about free and open-source software (FOSS) communities. We do this by gathering data about project repositories and normalizing that into our data model to provide useful metrics about your project’s health. [augur_view](https://github.com/augurlabs/augur_view) is the hosted version of augur with HTML frontend, written with Bootstrap and served by Flask. The branch I am contributing to is [augur-new](https://github.com/chaoss/augur/tree/augur-new). The project will help the users to login using CLI and API. The project aims at creating login feature for users. This is implemented as CLI subcommands and through an API. Using these, user will be added to the database. With login functionality, the user experience will be improved. The project focused to add and improve access and authorisation functionalities for hosted version of augur (augur_view). As a future development, the new version of Augur- augur-new, will make it possible to install a single instance for CHAOSS Community members to leverage for initial experimentation with CHAOSS metrics.

## OBJECTIVES [&uarr;](#project-details)
### Primary
| \# | Status  | Objectives                    
| --- | --- | ----------------------------- | 
| 1 | :heavy_check_mark: | Develop login functionalities so that admins and users can access augur. Populate the tables with information from the user. |
| 2 | :heavy_check_mark: | Connect the login to the augur_data.chaoss_user table instead of the sqllite3 database. |
| 3 | :heavy_check_mark: | Implement the endpoints necessary for account creation and authentication on the backend. |
| 4 | :heavy_check_mark: | Work on the CLI components for creating admin and user accounts. |

### Secondary
- :heavy_check_mark: Augur enpoints to be deployed from augur-new. Install augur-new and test the schema creation with SQLAlchemy, and see if it at least creates a schema with all the data integrity protections we engineered into it.

## OBJECTIVES ACCOMPLISHED [&uarr;](#objectives-)

### 1. Subcommand to add users:
<hr>
<p align="center" style="font-size:15px"> <b> augur user add </b></p>

<p align="center">  The augur user add CLI group is for adding user to Augur's database.</p>

<hr>
<p align="center"> 
  <img src="project/assets/usercli.gif" width="800" height="450">
</p>
* All commands are invoked like:

``augur user add <username> <email> <firstname> <lastname>`` <br>
``augur user add <username> <email> <firstname> <lastname>  --admin ``
<br>
<hr>
<h3 align="center"> Resulting Database: <h3> <hr> <br>
<p align="center"> 
  <img src="project/assets/dbresults.jpeg" width="800" height="450">
</p>
<hr>

### 2. Installing augur-new:
<br>
Worked on setting up the environment for augur-new. Gone through the Augur Database Schemas
<p align="center">
  <img src="project/assets/installingAugur-new.gif" width="800" height="450">
</p>
<hr>

### 3. API Endpoints:
<b>Approach:</b>
<p>- I was supposed to create API endpoints for integration of login with backend. The API would generate token --> hit HTTPS --> validate user (example for validate). <br>
- This would ultimately use Postgres. So connect to Postgres instead of sqlite.<br>
- Frontend should talk to backend API <--> database.<br>
- User to repo to schema to have 4 endpoints: add, remove, update and validate (passing in hashkey (SSL))<br>
- The updated file structure as per augur-new required me to install augur-new.<hr>
<p align="center" style="font-size:25px"> <b> User schema </b><p><hr>
<p align="center">
    <img src="project/assets/schema.jpeg" width="400" height="350"> 
</p>
<hr>
</p>
<p align="center" style="font-size:25px"> <b> Create User </b> <p>
<p align="center">  Allows to create user with unique username and email, password, firstname, lastname</p>
<b>Approach:</b>
<p>- Use engine to connect to db<br>
- arguments required are username, password, email, firstname, lastname.<br>
- check if the compulsory arguments are not None (error 400)<br>
- hash password<br>
- add user to db<br>
- Imp point: username and email need to be unique!
<p align="center">
    <img src="project/assets/createuser.gif" width="800" height="450"> 
</p>
<hr>

<p align="center" style="font-size:25px"> <b> Validate User </b> <p>
<p align="center">  Allows to validate user with given username and password</p>
<b>Approach:</b>
<p>- Use engine to connect to db<br>
- Input username and password.<br>
- Hash password, check password<br>
- ``if not pass_hash == password:
      
      return jsonify({"status": "invalid password"})``
<p align="center">
    <img src="project/assets/validateuser.gif" width="800" height="450"> 
</p>
<hr>

<p align="center" style="font-size:25px"> <b> Remove User </b></p>

<p align="center">  Allows to remove user with given username </p>
<b>Approach:</b>
<p>- Use engine to connect to db<br>
- Input username and password.<br>
- check user exists<br>
- validate user<br>
- if validated, session.delete(user), session.commit(), 200
<p align="center">
    <img src="project/assets/userremove.gif" width="800" height="450"> 
</p>
<hr>
<p align="center" style="font-size:25px"> <b> Update User </b> <p>

* Allows to update username, password, email as arguments: new_username, new_password, new_email 
* Either one or all of the above attributes can be provided as arguments to the API.
* NOTE: Only valid username and password will allow updation of new values.
* For example to update username command invoked like:

``http://127.0.0.1:5000/api/unstable/user/create?username=<username>&password=<password>&new_username=<new_username>``

<hr>

## WORK [&uarr;](#objectives-accomplished-)
### What Was Done
During these three months I have completed all the essential objectives which includes

| \# | Objectives | PR/Commit/Link | Associated Deliverables | Status |
|----|-------------|----------------|---------|--------|
| 1 | Installation of augur_view | [PR Link](https://github.com/augurlabs/augur_view/pull/22) |  | <span style="color: purple;">Completed</span> |
| 2 | Add user subcommand with username functionality | [Link](https://github.com/chaoss/augur/pull/1912/commits/8ad805770a2a87790b2aab7340021df2b4a71bff) |  | Completed |
| 3 | Add user with email | [Link](https://github.com/chaoss/augur/pull/1912/commits/2f21f567305bdf56dd6f8524ab587114139a5756) | Add user with unique email and username command | Completed |
| 4 | Add Password hashing for the user| [Link](https://github.com/chaoss/augur/pull/1912/commits/1e57f9a073ebcf651eb6b92fe0353d6053bf185f) | Password hashing added | Completed |
| 5 | augur user add <username> <email> subcommand | [PR Link](https://github.com/chaoss/augur/pull/1912) | CLI components for creating admin and user accounts. add_user method takes username as argument as adds it to the table user. | <span style="color: purple;">Completed</span> |
| 6 | Added Create user endpoint | [Link](https://github.com/chaoss/augur/pull/1953/commits/c5a7d1d74a5a2e1c4ac52bd27de9d401f98eead5) | API endpoint for creating user as per user schema (does not use ORM) | Completed |
| 7 | Added Validate user endpoint  | [Link](https://github.com/chaoss/augur/pull/1953/commits/64741898326de4ce215fb18f4f5652a9e149d7a8) | API endpoint for validating user email, username and password(does not use ORM) | Completed |
| 8 | Added remove user endpoint  | [Link](https://github.com/chaoss/augur/pull/1953/commits/23a0cf3540fc93c1105956b4b00839b886e1aa48) | API endpoint for deleting user from database(does not use ORM) | Completed |
| 9 | Added update user endpoint  | [Link](https://github.com/chaoss/augur/pull/1953/commits/a9634068e5e2b0f9d62a15ebc68c699474050f3f) | API endpoint for updating user details like email, username and password.(does not use ORM) | Completed |
| 10 | User create endpoint ORM | [Link](https://github.com/chaoss/augur/pull/1953/commits/a4c049334efe86d678e99ffe09b947e43b9e07bb) | API endpoint for creating user using ORM | Completed |
| 11 | User validate endpoint ORM  | [Link](https://github.com/chaoss/augur/pull/1953/commits/ea5e72ff52b757ca836aa4a1a0b80b2c5d110252) | API endpoint for validating user using ORM | Completed |
| 12 | User remove endpoint ORM   | [Link](https://github.com/chaoss/augur/pull/1953/commits/557d966510924215ca43ff3d03873b580bcc3cc5) | API endpoint for remove user using ORM | Completed |
| 13 | User update endpoint ORM   | [Link](https://github.com/chaoss/augur/pull/1953/commits/2cf9afe432cc853e79f1ca68c9ba69e7d48ebbae) | API endpoint for updating user using ORM | Completed |
| 14 | Augur user API  | [PR Link](https://github.com/chaoss/augur/pull/1953/) |  | <span style="color: purple;">Completed</span> |
| 15 | Augur user CLI as per new schema  | [PR Link](https://github.com/chaoss/augur/pull/1968) |  | <span style="color: purple;">Completed</span> |


## ACTIVITY REPORTS [&uarr;](#work-)
- Community Bonding Phase (May 21, 2021 - June 12, 2021) - [Report](weeklyReport/communityBonding/communityBondingReports.md)
- Coding Period
  - Week 1 (June 13, 2022 - June 20, 2022) - [Blog](weeklyReport/codingPeriod/week1.md)
  - Week 2 (June 21, 2022 - June 26, 2022) - [Blog](weeklyReport/codingPeriod/week2.md)
  - Week 3 (June 27, 2022 - July 3, 2022) - [Blog](weeklyReport/codingPeriod/week3.md)
  - Week 4 (July 4, 2022 - July 10, 2022) - [Blog](weeklyReport/codingPeriod/week4.md)
  - Week 5 (July 11, 2022 - July 17, 2022) - [Blog](weeklyReport/codingPeriod/week5.md)
  - Week 6 (July 18, 2022 - July 24, 2022) - [Blog](weeklyReport/codingPeriod/week6.md)
  - Week 7 (July 25, 2022 - July 31, 2022) - [Blog](weeklyReport/codingPeriod/week7.md)
  - Week 8 (1 August, 2022 - August 7, 2022) - [Blog](weeklyReport/postMidEval/week8.md)    
  - Week 9 (August 8, 2022 - August 14, 2022) - [Blog](weeklyReport/postMidEval/week9.md)    
  - Week 10 (August 15, 2022 - August 21, 2022) - [Blog](weeklyReport/postMidEval/week10.md)
  - Week 11 (August 22, 2022 - August 28, 2022) - [Blog](weeklyReport/postMidEval/week11.md)
  - Week 12 (August 29, 2022 - August 4, 2022) - [Blog](weeklyReport/postMidEval/week12.md)    
- [Final Report](https://github.com/Priya730/GSoC22/blob/main/README.md)
 
## Mentors and Team [&uarr;](#activity-reports-)
- [Sean Goggins](https://github.com/sgoggins)
- [John Kieran](https://github.com/Ulincsys)
- [Andrew Brain](https://github.com/ABrain7710)

## Acknowledgment [&uarr;](#mentors-and-team-)
I would like to thank my mentors Sean Goggins, John Kieran & Andrew Brain for helping and guiding me throughout the GSoC Journey :)
Thanks to other mentees and mentors for collaboration.
I am thankful to Google Summer Of Code for providing me with an opportunity to work with CHAOSS.


## Additional Info [&uarr;](#acknowledgment-)
<b>This repository will be regularly updated with blogs and meetings summaries during the project.</b>
    
- [GSoC'22 Project Proposal](project/Priya_Srivastava_GSoCproposal_CHAOSS.pdf)
- [Microtasks](https://github.com/Priya730/chaoss-micro-task)
- [Project Link](https://summerofcode.withgoogle.com/programs/2022/projects/YNXT2TFX)

## Student Developer Info: [&uarr;](#additional-info-)
  * Linkedin: [Priya Srivastava](https://www.linkedin.com/in/priyasrivastava730/)
  * Github: [@Priya730](https://github.com/Priya730)
  * Twitter: [@shivikapriya](https://twitter.com/shivikapriya)
  * Blog: [@shivikapriya](https://medium.com/shivikapriya)
  * Mail: [shivikapriya730@gmail.com](mailto://shivikapriya730@gmail.com)

### GO TO TOP [&uarr;](#project-details)
