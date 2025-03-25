# Software Requirements Specification (SRS)

## Smart Waste Management System

### Table of Contents

1. [Introduction](#introduction)
    1. [Purpose](#purpose)
    2. [Scope](#scope)
    3. [Definitions, Acronyms, and Abbreviations](#definitions-acronyms-and-abbreviations)
    4. [References](#references)
2. [Overall Description](#overall-description)
    1. [Product Perspective](#product-perspective)
    2. [Product Functions](#product-functions)
    3. [User Classes and Characteristics](#user-classes-and-characteristics)
    4. [Operating Environment](#operating-environment)
    5. [Design and Implementation Constraints](#design-and-implementation-constraints)
    6. [Assumptions and Dependencies](#assumptions-and-dependencies)
3. [Specific Requirements](#specific-requirements)
    1. [Functional Requirements](#functional-requirements)
    2. [Non-Functional Requirements](#non-functional-requirements)
4. [Appendices](#appendices)

## 1. Introduction

### 1.1 Purpose

The purpose of this Software Requirements Specification (SRS) document is to provide a detailed description of the Smart Waste Management System. It outlines the system's functionality, performance, and constraints, serving as a guide for developers, stakeholders, and users.

### 1.2 Scope

The Smart Waste Management System is a web-based application designed to streamline waste management processes. It includes features for user authentication, waste request submissions, illegal dumping reports, and tracking of garbage trucks. The system aims to improve efficiency, reduce costs, and enhance environmental sustainability.

### 1.3 Definitions, Acronyms, and Abbreviations

- **SRS**: Software Requirements Specification
- **API**: Application Programming Interface
- **REST**: Representational State Transfer
- **CRUD**: Create, Read, Update, Delete

### 1.4 References

- [Django Documentation](https://docs.djangoproject.com/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 2. Overall Description

### 2.1 Product Perspective

The Smart Waste Management System is a standalone web application built using the Django framework. It integrates with a PostgreSQL database for data storage and uses Docker for containerization. The system provides a REST API for integration with other systems.

### 2.2 Product Functions

- User authentication and role-based access control
- Waste collection request submissions
- Illegal dumping report submissions
- Garbage truck tracking
- Admin dashboard for managing users and requests
- REST API for integration with other systems

### 2.3 User Classes and Characteristics

- **Admin**: Manages users, waste requests, and illegal dumping reports.
- **User**: Submits waste collection requests and illegal dumping reports.
- **Driver**: Tracks garbage trucks and updates their status.

### 2.4 Operating Environment

- **Server**: Linux-based server with Docker installed
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django framework

### 2.5 Design and Implementation Constraints

- The system must be built using the Django framework.
- The database must be PostgreSQL.
- The system must be containerized using Docker.
- The frontend must be responsive and compatible with modern web browsers.

### 2.6 Assumptions and Dependencies

- Users have access to the internet.
- The server hosting the application has sufficient resources.
- The PostgreSQL database is properly configured and accessible.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Authentication

- The system shall allow users to register and log in.
- The system shall provide role-based access control.

#### 3.1.2 Waste Collection Requests

- The system shall allow users to submit waste collection requests.
- The system shall allow admins to view and manage waste collection requests.

#### 3.1.3 Illegal Dumping Reports

- The system shall allow users to submit illegal dumping reports.
- The system shall allow admins to view and manage illegal dumping reports.

#### 3.1.4 Garbage Truck Tracking

- The system shall allow drivers to update the status of garbage trucks.
- The system shall allow admins to track the location and status of garbage trucks.

#### 3.1.5 Admin Dashboard

- The system shall provide an admin dashboard for managing users, waste requests, and illegal dumping reports.

#### 3.1.6 REST API

- The system shall provide a REST API for integration with other systems.

### 3.2 Non-Functional Requirements

#### 3.2.1 Performance

- The system shall handle up to 1000 concurrent users.
- The system shall respond to user actions within 2 seconds.

#### 3.2.2 Security

- The system shall use HTTPS for secure communication.
- The system shall store passwords using strong hashing algorithms.

#### 3.2.3 Usability

- The system shall have a user-friendly interface.
- The system shall be accessible on both desktop and mobile devices.

#### 3.2.4 Reliability

- The system shall have an uptime of 99.9%.
- The system shall provide error handling and logging.

## 4. Appendices

### 4.1 Glossary

- **Admin**: A user with administrative privileges.
- **User**: A regular user of the system.
- **Driver**: A user responsible for operating garbage trucks.

### 4.2 References

- [Django Documentation](https://docs.djangoproject.com/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

This SRS document provides a comprehensive overview of the Smart Waste Management System, detailing its functionality, performance, and constraints. It serves as a guide for developers, stakeholders, and users to ensure the successful implementation and operation of the system.