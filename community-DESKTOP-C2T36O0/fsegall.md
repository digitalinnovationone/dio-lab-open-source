# Hi, I'm Felipe!

Felipe Segall Corrêa
Full-stack engineer

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fsegall)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/felipe-segall-075005239/)


## TECHS:

  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
  ![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  - Front-end
  - Back-end
  - SQL and NoSQL

## About me:

I decided to become a web devoloper in 2016 in an attempt to make a career change. Since then every day has been an exciting and challenging learning experience. I have full-stack expertise acquired by building APIs with Node.js and client-side applications, mostly with ReactJS. Recently I finished a back-end and DevOps with Python bootcamp to consolidate prior experience with the language and frameworks while learning CI/CD, and improving cloud skills. I strive to have good problem-solving skills to approach tasks with the right questions and mindset. I respect the programming craft and enjoy combining technical knowledge with creativity.

## Work Experience:

Software engineer with 9+ years of experience. I'm a self-taught motivated person who strives to get things done and deliver high-quality solutions. I have created, maintained, and selected team members for a personal project that has evolved into a professional application, and I enjoy having similar challenges and responsibilities. I'm flexible about the technology stack and can quickly pick up new technologies.

# Main Projects

**2020 - 2025**

[Penssan Web App](https://aplicativo-vigisan.pesquisassan.net.br/)


The ReactJS progressive web app is a full-stack application designed to collect data for a research group. This project has a ReactJS client hosted at Netlify that sends collected data to a Node.js TypeScript back-end (TypeORM, PostgreSQL) hosted on Digital Ocean. The client-side uses current ReactJS best practices with functional components and React Hooks.

The project was challenging and rewarding. I had to deal with all aspects of full-stack development, DevOps, back-end, and front-end tasks.

DevOps configuration and provisioning of cloud resources rely on Github Actions for CI/CD, Digital Ocean for hosting the application server, and the managed database as a service PostgreSQL. I also used Amazon AWS to store users' Avatars in S3 buckets and send emails.

This infrastructure served the API built based on Domain-Driven Design and SOLID principles. All to be exposed through a well-documented RESTful API following Open API 3.0 guidelines.

Researchers wanted to use desktop computers and cellphones (Android and IOS) to conduct interviews. There was also the need to use the app offline in remote areas with no internet connection.

This offline necessity made me choose a client-side ReactJS progressive web app that uses React Hooks to manage state and user interactions. CSS styling is fully responsive for mobile screens and uses the Styled Components library. React Hooks are also used to reuse UI components such as toast messages to the user.

The choice for a PWA means it can be downloaded and accessed on any platform, even offline. Since the app is downloadable to the user's desktop or cellphone, it was possible to develop offline functionality through the browser's Local Storage API. The app uses the browser to persist data from interviews and send them in batches to the server. It also has interesting role-based authorization and access control features validated both front-end and back-end. Standard interfaces, DTOs (data transfer objects), allow validation for client-side forms to send data to be persisted in the database reliably.

The app is now in the maintenance and database management phase. I have helped to onboard two developers to work with me part-time on the project. The application has been used recently in a research to successfully collect food security data of 500 indigenous families living in areas with no internet connection.

**2016 - 2020**

[code](https://github.com/fsegall/materias-webpack)

This project is a ReactJS dashboard used by journalists linked to a Python-based CMS designed to allow viewing and updating news articles, revision statuses, and publishing content. Redux's actions sent network requests to trigger changes in the publishing status of news articles in the Python backend. These actions by the user affected the visibility of news that the CMS published on the Brazilian Senate website.

By the end of the project, I had learned how to use Redux combined with Redux-thunk to deal with async requests and state management in ReactJS. I also made e simple server to test the application during development using Express.js and MongoDB/Mongoose. It was done before the release of the ReactJS Hooks API and uses mostly class components connected to the Redux store with the React-Redux library.

[ReactJS Elections Results Dashboard](https://github.com/fsegall/eleicao)

The challenge was that we had to fetch a large amount of data from an API and display it for each of the 27 Brazilian States.
The application was a client-side responsive web app built with ReactJS and Styled Components library for CSS. We also configured Webpack to serve the static files and JS bundle (using a starter kit).

A team of two developers and a web designer were responsible for developing the application. I built the React components of the UI and set them to fetch and display data correctly.  
I learned the hard way it was complicated to rely only on props drilling and lifting up application state in this kind of scenario.

In the end, we built a ReactJS dashboard to poll data from an external API and display the national election results in real-time. It worked as expected, but I realized the importance of using state management libraries such as Redux to reduce complexity when dealing with large amounts of data that must be displayed instantly while sharing data among several components.

## Courses

- [Python Fundamentals Course Completion](https://learn.nucamp.co/badges/badge.php?hash=e2bd9dc7c49b2898879aacda9cd6dffbad9b78b4)

- [SQL and Data Course Completion](https://learn.nucamp.co/badges/badge.php?hash=63e802cf357359b3750e3e9d5e2fa0115740e9bf)

- [DevOps with Python](https://learn.nucamp.co/badges/badge.php?hash=3994965cd2dd5aa10428a4e512ca5943b2c049c1)

- [Typescript: The Complete Developer's Guide | Dec 2019](https://www.udemy.com/certificate/UC-6UXX9G9E/)

- [The Complete Developers Guide to MongoDB | Nov 2018](https://www.udemy.com/certificate/UC-W90EYKZR/)

- [Modern JavaScript Bootcamp | Aug 2018](https://www.udemy.com/certificate/UC-E53ZG8NQ/)

- [The Complete React Js & Redux Course - Build Modern Web Apps | Apr 2018](https://www.udemy.com/certificate/UC-NQ4LNFSU/)

- [Learn and Understand NodeJS| Apr 2018](https://www.udemy.com/certificate/UC-TDXG2F8M/)

- [Datacamp | 2022](https://app.datacamp.com/)

  - SQL for Joining Data
  - Intermediate SQL queries
  - Statistical Thinking in Python (Part 1)
  - Intermediate Python
  - Introduction to Python

## Education:

MBA – Software Architecture and DevOps – [FullCycle](https://plataforma.fullcycle.com.br/). 

Bootcamp – [Modern Software Engineering with DevOps](https://www.nucamp.co/) – Nucamp.

Bachelor Degree in Communication Studies
Graduate Degree in Translation English - Portuguese