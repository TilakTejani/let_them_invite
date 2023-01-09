# let_them_invite
An automated digital invitation sender  

Invitation sent through whatsapp in automated edited PDF forms.

It takes a tamplet of invitation card in pdf and edit it (like writing name on invitation) using CSV data file and sends it through whatsapp to individuals.

TechStek: Python, Selenium and PyTorch 

Main Window

<img src="https://user-images.githubusercontent.com/76736715/211374029-b566a0a8-338a-4ffb-b018-d9141ba383ba.png"  width="25%" height="25%">


File Input 
Taking file inputs of template pdf and csv file containing name(to be written on pdfs) and number/name(saved name) on which the pdf needs to be sent

<img src="https://user-images.githubusercontent.com/76736715/211374458-bf03b89c-2355-41af-8ab7-2afede5171f0.png"  width="25%" height="25%">

After taking template pdf and csv of name and number list the pdf of invitation will converted into images
After which location will have to be inputed inorder to write names on proper position

Loc Input

<img src="https://user-images.githubusercontent.com/76736715/211374830-16aa3bb3-49c2-435c-8fa9-b539c958328c.png"  width="50%" height="50%">


After location input the pdfs with proper names will be generated and saved in folder
Then on connecting to whatsapp web using selenium all the edited pdfs will be sent to all particular invites using details in csv
