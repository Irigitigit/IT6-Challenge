After figuring the server out (The port and access to the server) 

1. I first tried to access the server with python, so i tried making a post request. On where, when i execute the file it posts the given PIN that i've
    inputted from the python file to the server. A basic POST request...

    My goal here was to test how do i send a POST request to the server, so my next step is to loop the POST request of PIN from 0 - 999

2. I made 3 functions specifically for each step to POST request.

   FUNCTION 1- Is where my messages to the server are, it is encoded here to be sent to the server
   
   FUNCTION 2- This the where the connection is built between me and the server, this is where the socket library is used...
   
   FUNCTION 3- the main function that iterates from 0 to 999 or 999 to 0. The fucntion that sets up the communication between me and the server...
               This is what prints the output in the terminal...
