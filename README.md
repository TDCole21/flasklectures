# Skills Framework for the Information Age (SFIA) - Project 1
---
# Hollywood Film and Actor Database

This is a project, worked on independently of others, in reference to the QA Learning Academy training base project specification; Fundamental Project Specification - DevOps Core. The purpose of this project is to fulfill the specification defined for the assignment due Monday 23rd March 2020, 09:00.


## Contents
1. [Brief](#brief)
    1. [MVP](#mvp)
2. [Architecture](#architecture)
    1. [Entity Relationship Diagrams](#entity_relationship_diagrams)
    2. [Multi Tier Architechture Diagram](#multi_tier_architechture_diagram)
3. [Testing](#testing)
    1. [Report](#report)
4. [Deployment](#deployment)
    1. [Technologies Used](#technologies_used)
5. [Front End Design](#front_end_design)
6. [Improvements for the Future](#improvements_for_the_future)
7. [Authors](#authors)
8. [Acknowledgements](#acknowledgements)

## Brief <a name="brief"></a>
This section of the document will serve as the introduction for the requirements of the project.

The purpose of this project is to create an application that involves the concepts learnt from the core training modules; more specifically, this will involve:
+ Agile
+ Python Fundamentals, Testing and Web Development
+ Git
+ Basic Linux
+ Continuous Integration (CI)
+ Cloud Fundamentals
+ Databases

The resulting aim of the project is to produce an application that must manipulate two tables displaying full Create, Read, Update and Delete (CRUD) functionality with the utilisation of supporting tools, methodologies and technologies that encapsulate all the above modules.

### Minimum Viable Product (MVP) <a name="mvp"></a>
The Minimum Viable Product (MVP) for the project has the following requirements:
+ A kanban board with full expansion on user stories, use cases and tasks needed to complete the project.
+ A relational database used to store data persistently for the project, this database needs to have at least 2 tables and are also required to model the relationship using an Entity Relationship Diagram (ERD).
+ Clear Documentation describing the architecture used for the project in addition to a detailed Risk assessment.
+ A functional CRUD application created in Python.
+ Fully designed test suites for the application, as well as automated tests for validation of the application. Must also demonstrate high test coverage in the backend and provide consistent reports and evidence to support a Test Driven Development (TDD) approach.
+ A functioning front-end website and integrated Application Programming Interfaces (API), using Flask.
+ Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

### Tech Stack Requirements <a name="tech_stack"></a>
The Tech Stack requirements are the following:
|Technology Required|Used in this project|
|---|---|
|Kanban Board|Trello|
|Database|Google Cloud Platform (GCP) SQL Server|
|Programming language|Python (including MySQL)|
|Unit Testing with Python|Pytest|
|Integration Testing with Python|Unit, Database|
|Front-end|Flask (including Jinja2) and HTML (including CSS and Bootstrap)|
|Version Control System (VCS)|Git|
|CI Server|Jenkins|
|Cloud server|GCP Compute Engine|

## Project Management <a name="project_management"></a>
This section will detail the project management tools and techniques used to plan the project, and how they were utilised and adapted throughout the project.

I implemented an Agile methodology over the Waterfall methodology due to Agile's values and principles allowing for testing to be completed in the same iteration as programming, dynamic project aims and working code over comprehensive documentation; again adapting best industry practices.

Due to the nature of my project, some of the values and principles of Agile had to be adapted:
+ **Individuals and Interactions over processes and tools:**
The project was an individual project, so there was no need for team interactions such as daily scrums.
+ **Working Software over comprehensive documentation:**
The purpose of this project is to show my understanding of the content taught in the first five weeks.
So comprehensive documentation is important, however, I took adapted this value to mean that the application must be functional over beautiful.
+ **Customer Collaboration over contract negotiation:**
This project had no customer, other than users and the trainers at QA. So, I imagined virtual users and treated my trainer as a customer.
+ **Responding to Change over following a plan:**
Although I did not know at the start, the project objectives did not change throughout the five weeks, but my planning allowed for easy response to change.

### Kanban Board <a name="entity_relationship_diagrams"></a>
As stated for the MVP, I was required to follow best practices within industry and use a Kanban board to manage my project. I chose to use the Trello application to create my Kanban board, due to my familiarity with the software, having seen it used at QA.

The board is designed around user stories to test the CRUD functionalities of the application. These stories are then represented in the product backlog, along with other features needed for the specifics of the project (create this README file for example). These product backlogs are then further broken down in to a sprint backlog, tasks, progress, done and bugs list. These additional lists allow for dynamic progress updates of the project and to maintain specific obtainable objectives throughout the project to allow for a deliverable product by the deadline.

I defined "done" as to mean that the feature had been successfully implemented into the application, and had no negative effect on the pytest application which is detailed later.
Any implemented feature that negatively effected the performance of the application were logged into the bugs column.

#### Initial Plan

![Initial Kanban board designed with Trello.](https://i.imgur.com/LAkh6i3.jpg)


#### Dynamic Updates

+ TBA

#### Final Board









### Entity Relationship Diagrams <a name="entity_relationship_diagrams"></a>

### Multi Tier Architecture Diagram <a name="multi_tier_architecture_diagram"></a>

## Testing <a name="testing"></a>
I used both Pytest and a Coverage report to test my application

### Pytest <a name="pytest"></a>

### Coverage Report <a name="coverage_report"></a>

## Deployment <a name="deployment"></a>
Once I have edited my code in Visual Code, I push the changes up to my developer branch on GitHub. Once a feature has been completed, I merge the developer branch into the master branch which activates a GitHub webhook with my Jenkins CI server. Jenkins can then deploy the app as a service. With the use of the Pipeline, Jenkins is able to install all the necessary packages needed to run the application, wait for the packages to be installed, deploy the application as a service and finally perform the tests mentioned in the section above. The results of these tests are printed in the console output of Jenkis, giving the user the ability to improve the testing stage if results are not satisfactory.

### Branch Merge
At the start of the project I had a single branch on my version control; the master branch.
Once I had a functioning application running on a server and could be accessed through port 5000, I used git checkout -b developer to create a new developer branch from which all changes would be made too before merging with the master branch after a task had been placed into "done" on my kanban board.

## Front End Design <a name="front_end_design"></a>
The first paragraph text

## Improvements for the Future <a name="improvements_for_the_future"></a>
If I had more time dedicated to this project I would have implemented the following:
+ **A User/Developer log-in feature:**
This would have allowed for the Developer profiles to have have full access to the film and actors database, allowing them full CRUD functionalities.
The User profiles would have only been permitted to view the databases, and searched for which actors/films they would have wanted to see. Maybe even a request feature, so that they could suggests additions/updates/removals to the database.
+ **Increased Testing Coverage:**
As shown previous in the Coverage Report section of the readme file, there was little coverage of the application, even though a lot of its core features where tested. This is definitely an area i would like to improve in later projects.
+ **Improved UI:**
Due to the nature of Agile, I prioritised working CRUD functionality over the documentation and presentation of the project. This meant I did not spend time on the design aspects of the site.
+ **Selenium Testing:**
My testing protocol only included unit and database testing. Had more time been allowed, I would have researched and implemented further methods of testing.
+ **More Complex Tables and Relationships:**
My project uses a many-to-many relationship between two tables. However, given more time, I would have prioritised including new tables such as directors, which would have shown much greater understanding of the material covered.
Also included would have been more columns in the tables, genres for example, which would have allowed for more features on the the application.
+ **More CRUD Functionalities:**
Although, I included a diverse amount of CRUD functionalities in my project, there were more to be tested. An update many to many relationship for example, or a multi-select drop down list instead of either text boxes or single-select dropdown lists. 
+ **Complex Version Control Branch Model:**
I only used two branches in my project; a master branch and developer branch. To help prepare better for best practice in industry, I would have further branches underneath the developer branch for each product backlog then further branches for the sprint backlogs and then again for the tasks.


## Authors <a name="authors"></a>
Thomas Cole - QA Academy Trainee

## Acknowledgements <a name="acknowledgements"></a>
I would like to acknowledge the QA trainers and other members of my cohort, who were able to help me with any problems I had with my project.