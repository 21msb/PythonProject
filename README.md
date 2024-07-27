
# **TuwaiqBot** is a chatbot web-based that enables Tuwaiq Academy users to know what's new in the academy, what are the available bootcams, programs, and new events. It can help the users who want to join as a trainee to apply fast, and ask us about anything directly. 
This idea helps users to access anything directly without taking time to search in the website.


## What does the TuwaiqBot provide?
1. The user can select what option he/she wants to know about it, e.g bootcamps or programs or events.
2. The user can select one of them and see the list of availablity bootcamps or programs or event.
3. The content of each selection will provide the details of them.
4. The user also can fill a form to contact directly with the academy.
5. If the user want to join as a trainee in the academy, he/she can select the option join as a trainee.

 
 
### The important functionalities used in this project are: 
- def display_bootcamp_details and def display_program_details:
  These two functions uses a build in function .write() to write the keys and values from the dictionaries bootcamp and program when the user click on one of them.

- elif selected_option == "🧐Ask us!":
  
- elif selected_option == "✌️Join us as a Trainee!":
  This selection will make the bot return the content written in the .markdown function.
  
-  elif selected_option == "🦾Team":
  When the user press the option Team, the bot will return a list of the team names with their contact info.

- def meetings():
  This is a simple function that provides the data for the meetings. This function returns a dictionary where each key is the name of a meeting, and the value is a list containing detailed information 
  about that meeting. Users can select a meeting from a dropdown list to see its details and click an "Enroll" button to go to the enrollment page for that meeting. 


