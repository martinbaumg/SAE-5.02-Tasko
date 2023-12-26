### Introduction

Welcome to the TASKO User Documentation ! This guide will walk you through the installation and usage of TASKO, your go-to reminder application. Whether you need help setting up TASKO on your device or want to make the most of its features for task management, this documentation has you covered. Let's get started on a journey to streamline your task organization and reminders.

# TASKO Installation Guide

TASKO is a reminder management application that helps you keep track of important tasks and never miss a beat. You can install TASKO in two different ways: from the official website or by cloning the GitHub repository.

## Installation from GitHub Repository

1. Open your terminal.

2. Clone the TASKO GitHub repository using the following command:
   ```shell
   git clone https://github.com/martinbaumg/SAE-5.02-Tasko
   ```
   
   
## To get started

### Step 1 : Navigate to the Project Directory 

Open your terminal and navigate to the project directory using the `cd` command.
For example: `cd /path/to/project/BACKEND/Tasko`

### Step 2 : Create the Conda Environment

`conda env create -f tasko_env.yml`


### Step 3 : Activate the Virtual Environment

`conda activate task_env`

### Step 4 : Launch the application

To start Tasko, simply use `python main.py`in the folder /BACKEND/Tasko when your virtual environment is enabled. 

## Tutorial 

When launching the application, it is necessary to log in. This step involves providing your credentials, such as a username and password, to gain access to the application's features and functionalities. Logging in ensures that the application can identify and authenticate the user, providing a personalized and secure experience.

![[login.png]]
After successfully logging in, you will be directed to the application's homepage. Here, you have the ability to perform various actions, including adding tasks to your list. The homepage serves as a central hub where you can manage your tasks, view important information, and navigate through the application's features.

![[add.png]]
You have the option to add a due date to specify when a task should be completed, provide a detailed description to elaborate on the task's requirements, or if necessary, delete the task : 

![[edit.png]]
In addition to task management and customization, you also have the flexibility to organize your tasks into different sections. Typically, these sections include 'Pas encore fait' for tasks that are pending or not completed, and 'Fait' for tasks that have been successfully completed. This feature allows you to track the progress of your tasks, categorizing them based on their status. By moving tasks between these sections, you can easily monitor your accomplishments and prioritize your work effectively.

This application provides a user-friendly platform for managing tasks efficiently. After logging in, you can access the homepage to create, modify, and organize tasks. Features such as adding due dates, descriptions, and moving tasks between sections like 'Pas encore fait' and 'Fait' enhance productivity and organization. Whether you're tackling a personal to-do list or managing tasks in a professional setting, this application simplifies the process, helping you stay on top of your goals and responsibilities.