# increment
Litary - A library management web app to organise a personal literature library

## Literary – The Literature Management App

# Table of Contents

**[Literary – The Literature Management App 1](#_Toc47937797)**

**[Content 1](#_Toc47937798)**

**[Resources: 1](#_Toc47937799)**

**[Requirements 1](#_Toc47937800)**

**[Literary App 2](#_Toc47937801)**

**[Project Tracking 2](#_Toc47937802)**

**[Database Structure 3](#_Toc47937803)**

**[Known Issues 5](#_Toc47937804)**

**[Future Improvements 5](#_Toc47937805)**

**[Author 5](#_Toc47937806)**

**[Acknowledgements 6](#_Toc47937807)**

## Resources:

- [Jira Board](https://jacobhpgrub.atlassian.net/jira/software/projects/LQA/boards/4)
- [Presentation](https://docs.google.com/presentation/d/1tmI6CsPoRDrYkRan2wcBzMjVTFV2sa-NJym296z4DCE/edit)
- [Literary Website](http://35.246.16.109:5000/)
- [Github](https://github.com/jcbgrub/increment)

## Requirements

The basic requirements set by the academy are to: &#39;To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.&#39; In more detail this means that the entire project requires the following features and structures:

- A project tracking board with full expansion on user stories, use cases and tasks needed to complete the project.

- A relational database (RDBMS) with at least 2 tables.
- Clear Documentation from a design phase describing the architecture
 you will use for you project as well as a detailed Risk Assessment.
- A functional CRUD application created in Python, following best
 practices and design principles, that meets the requirements set on
 the project tracking board
- Fully designed test suites for the application with at least 75% test coverage in your backend and provide consistent reports and evidence to support a TDD approach.
- A functioning front-end website and integrated API&#39;s, using Flask.
- Code fully integrated into a Version Control System using the
 Feature-Branch model which will subsequently be built through a CI
 server and deployed to a cloud-based virtual machine.

## Literary App

To satisfy the requirements I developed a simple app called &#39;Literary&#39; a neologism of &#39;literature&#39; and &#39;library&#39; the apps purpose is to enable the user to store and amend their personal library. In computer programming, create, read (aka retrieve), update, and delete, (CRUD) are the four basic functions of persistent storage. The app is split into 3 basic tables:

- USERS – **This satisfies CREATE.**
  - First Name _– user first name_
  - Last Name _– user last name_
  - Email
  - Password
- BOOKS - Add and Amend books **This satisfies CREATE and UPDATE.**
  - First Name _– author first name_
  - Surname – _author surname_
  - Title – _book title_
  - Pages – _number of pages_
  - Language
- RATING - Add a rating:
  - Rating _– rating between 1 and 6_
  - Comment
- List of Total Books in the library - **This satisfies READ.**
- Delete a Book entry and Rating entry **This satisfies DELETE.**

## Project Tracking

Jira was the chosen method when planning the project and tracking the progress **and to satisfy the brief.** This increment (v.1) has been set to be delivered within 1 standard length sprint of 2 weeks starting on the 27/7/20 to be completed on the 10/8/20 the delivery date for the first increment and project deadline. The current sprint named BPN Sprint 1, contains one epic which represent this release. These then are split in individual user stories focused on backend (routes, models and forms), front end (HTML) functionality, testing and documentation. Each user story has several children which represent the smaller steps which needed to be completed.

This release all user stories have been completed apart from one Front-End child, due to time constrains. This will be transferred backlog and completed in the next sprint.

![Screenshot 2020-08-10 at 07 59 49](https://user-images.githubusercontent.com/45181318/89758367-81e43400-dadf-11ea-8f5b-fccf79e568e0.png)

## Database Structure

A basic Entry Relation Diagram (ERD) was created to illustrate the relationship between the tables and to **satisfy the brief**  **model the**** relationship.** As seen below there are 3 main tables. The most important are the book-lib and main\_lib tables because part of the brief was to must create 2 different entities with a different relationship. This is satisfied here because book\_lib has a 0 to many relationships to main\_lib, as there can be many books, but

![Litary - ERD (6)](https://user-images.githubusercontent.com/45181318/89758504-e0a9ad80-dadf-11ea-90e4-c54157f0deff.png)

**Continuous Integration**

Below is the CI pipeline used for this project and includes the relationships between each tool and the frameworks used to create the app, perform sufficient tests and the deployment of the app and illustrated **how the requirements were satisfied.** Code was developed in python and pushed to Git hub using GIT which corresponded with Jira our project tracking app on which segments of code were related to which task. Next via the webhook Jenkins was informed which triggered automated testing of the code via pytest. If passed Jenkins triggered a build which send the updated testing via GCP (host) and flask (framework) to the live environment, while the dev continued to dynamically test using GC/Flask in python until the code was bug free.


![PI1](https://user-images.githubusercontent.com/45181318/89758583-12227900-dae0-11ea-9e11-32b253a595df.png)



**Testing**

The tools used for testing the application was Pytest when conducting unit tests, while selenium was used while performing integration tests. **The requirement was reach to the 78% coverage report.** While a total coverage of 78% percent was reached there was a fundamental problem with the integration tests which continued to fail. This is due to the registration and login xpaths of the HTML website which selenium was unable to find when following the main syntax offered on the QA Academy portal (Community).

![Screenshot 2020-08-10 at 07 27 25](https://user-images.githubusercontent.com/45181318/89758300-60834800-dadf-11ea-948e-8c1b1e0fcf9b.png)

**Risk Assessment**

The risk assessment produced for the project can be found below. It attempts to cover all risks or threats involved and what would be done to eliminate or reduce the impact of these threats.

| **Description** | **Assessment** | **Risk** | **Impact** | **Responsibility** | **Response** | **Tolerance** |
| --- | --- | --- | --- | --- | --- | --- |
| HTTPs traffic and data breach | Connecting to Googles VM are not secure. Any data transferred could be read by outsiders | Medium | High | Jacob grub | In this could we would need to take the website offline and make an overall root and user password reset | Treat |
| SQL Database crashes | If the cloud host goes down access to the database would fail and the website could not be accessed | Low | High | Google Cloud Platform | Switch to a different cloud provided while contacting GCP | Tolerable |
| Too much traffic on the app | If multiple users try to access the website it could be overloaded | Low | Low | Jacob Grub | We can increase the number of workers in Gunicron to avoid this | Tolerable |

## Known Issues

There are a few bugs with the current build of the app:

- When the user tries to look at the ratings of each book, the ratings are displayed by without the corresponding title.
- When the user enters a duplicate title instead of a warning an error page comes up

## Future Improvements

There are a number of improvements I would like to add:

- Design features. The website is too bland and not enjoyable at this stage
- New functionality as in entering the date a book has been completed

## Author

Jacob Grub

## Acknowledgements

Thanks to QA Consulting for their expertise and teaching

[1](#sdfootnote1anc)[https://jacobhpgrub.atlassian.net/jira/software/projects/LQA/boards/4](https://jacobhpgrub.atlassian.net/jira/software/projects/LQA/boards/4)

[2](#sdfootnote2anc)[https://docs.google.com/presentation/d/1tmI6CsPoRDrYkRan2wcBzMjVTFV2sa-NJym296z4DCE/edit](https://docs.google.com/presentation/d/1tmI6CsPoRDrYkRan2wcBzMjVTFV2sa-NJym296z4DCE/edit)

[3](#sdfootnote3anc)[http://35.246.16.109:5000/](http://35.246.16.109:5000/)

[4](#sdfootnote4anc)[https://github.com/jcbgrub/increment](https://github.com/jcbgrub/increment)

[5](#sdfootnote5anc)[https://portal.qa-community.co.uk/~/devops/projects/fundamental--devops](https://portal.qa-community.co.uk/~/devops/projects/fundamental--devops)
