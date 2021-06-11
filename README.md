# Assessment 2: Object Oriented Programming + CSV Reading/Writing
- **Video Inventory Manager**

## Important Grading Information
- Make sure you read the [Assessment-2 Grading Rubric](https://docs.google.com/spreadsheets/d/1AlAQukmB3SS7IyW2hu0zY-9RaQnHY3lLeTi2O1fUb30/edit?usp=sharing).
  - Application Correctness (40%)
  - Code Design (40%)
  - CSV Files (10%)
  - Testing (10%)
- This assessment is worth 15% of your final grade. You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - *5% penalty*: If you complete and submit the retake **within one week** of receiving your grade. 
  - *10% penalty*: If you complete and submit the retake **by 8:30am, July 12th, 2021** (end of the middle week break). A retake for this assessment WILL NOT be accepted after this date.

## Rules / Process
- This test is fully open notes and open Google, but is not to be completed with the help of other students/individuals.
- Push your solution up to your personal Github. Do not submit a pull request. 

## Requirements
- This assessment should be completed using Python.

## Challenge
*Back in the day*, humans would actually leave their homes to go rent a physical video copy of movies (what a strange concept, right?). Blockbuster was the leading video rental company in this era. Today, there is only one Blockbuster location left which is located in Bend, Oregon. Today, we are going to ask you to build a video inventory application for this Blockbuster!

Your Video Inventory Management application should manage the following data:
- Manage customer information:
  - customer id
  - first name
  - last name
  - current list of video rentals (*by title*)
- Manage the store's video inventory:
  - video id
  - video title
  - video rating
  - number of copies currently available in-store

Your application should allow:
- Viewing the current video inventory for the store
- Viewing a customer's current rented videos
  - customer *by id*
- Renting a video out to a customer
  - video *by title*
  - customer *by id*
  - **IMPORTANT:** Customers should not be allowed to have more than 3 videos rented at any given time. Your application should enforce this limitation!
- Returning a video from a customer
  - video *by title*
  - customer *by id*
- Adding a new customer
  - CUSTOMERS MAY NOT HAVE THE SAME ID
  - You should not have an initial list of video rentals assigned to a newly created customer
- Exiting the application

Be sure to give careful consideration into what data structures & data types (classes) you might need to use in your application logic. Also, your application should always keep the CSV data files updated! You need data records to be backed up in a file, in case your application were to crash (and lose data internally).

Your menu should look something like this: 
```
Welcome to Code Platoon Video!
1. View video inventory
2. View customer's rented videos
3. Rent video
4. Return video
5. Add new customer
6. Exit
```
