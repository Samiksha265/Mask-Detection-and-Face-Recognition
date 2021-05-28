# Mask-Detection-and-Face-Recognition
This project will help to recognize the faces without face masks and note their names into an excel sheet.
This project can be implemented only in small institutions or departments where the face data of students is available with the admin. Only admin will be able to access the excel sheets created with the names of students found without masks.
If any unknown person is captured in the camera without masks, then he/she will be recognized as 'Unknown'. 

There is also a small gui created to show the working of the project using Tkinter.
The model is trained using MobileNet and has used ImageNet weights for mask detection.The accuracy of model is calculated 98.4%.
For face detectio Viola-Jones algorithm is used in the format of haarcascade file. For face recognition, 'Face recognition' module is used.
