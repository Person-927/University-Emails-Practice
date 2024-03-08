import random

class ceaser():
  def __init__(self,text,key):
    self.text = text
    self.key_num = key
    self.cipher_text = ""
    
  def encrypt(self):
    character_value = ord(self.text)
    if character_value >= 97 and character_value <= 122:
      character_value = character_value + int(self.key_num)
      if character_value < 97:
        difference = 97 - character_value
        character_value = 123 - difference
      elif character_value > 122:
        difference = character_value - 122
        character_value = 96 + difference
    
    elif character_value >= 65 and character_value <= 90:
      character_value = character_value + int(self.key_num)
      if character_value < 65:
        difference = 65 - character_value
        character_value = 91 - difference
      elif character_value > 90:
        difference = character_value - 90
        character_value = 64 + difference
      
    return chr(character_value)

class account_creator():
  def __init__(self, filename):
    self.filename = filename + ".txt"
    self.Fname = []
    self.Lname = []
    self.course = []
    self.emails = []
    self.__password = []
    
  def fetch(self): # Fetches all details(First & Last name + Course) from a file
    file = open(self.filename, "r")
    data = file.readlines() # Gatheres all data from file into an array
    file.close()
    count = 1
    for i in range(0,len(data)): # Goes through the data and groups it into 3 seperate lists
      if data[i].strip() == "END":
        count = 1
        continue
      elif count == 1:
        self.Fname.append(data[i].strip())
        count += 1
      elif count == 2:
        self.Lname.append(data[i].strip())
        count += 1
      elif count == 3:
        self.course.append(data[i].strip())
        count += 1
    self.create_emails() # Causes the class to create emails for all names
  
  def create_emails(self):
    for i in range(0,len(self.Fname)): # goes through all the people
      occurance = 0
      email = self.Fname[i] + self.Lname[i] + "@uni.ac.uk" # Creates temporary email
      for j in range(0,len(self.emails)): # Checks to see if that temp email exists
        if self.emails[j] == email:
          occurance += 1 
      if email in self.emails:
        email = self.Fname[i] + self.Lname[i] + str(j) + "@uni.ac.uk" # adds a number to the email based on the amount of occurances
      self.emails.append(email)# adds emails to a list
    self.create_passwords() # Causes class to run create_password function
  
  def create_passwords(self):
    for i in range(0,len(self.Lname)): # Goes through all names
      Lintial = self.Lname[i][0].upper() # isolates first intial of last name
      self.__password.append(Lintial + self.course[i]) # creates a password based on course and last name
    self.encrypt() # runs encrypt function for passwords

  def encrypt(self):
    for i in range(0,len(self.__password)): # goes through all passwords
      random_num = random.randint(1,25) # random key for ceasure cipher
      new_password = ""
      for j in range(0,len(self.__password[i])): # goes through each letter of a password
        letter = self.__password[i][j]
        if self.__password[i][j] in ["a","e","i","o","u","A","E","I","O","U"]: # checks if letter is vowel
          encyption = ceaser(self.__password[i][j],random_num) # encrypts letter if vowel based on random key
          letter = encyption.encrypt() 
        
        new_password = new_password + letter # creates new password that is encrypted
      self.__password[i] = new_password # changes password list with new passwords
    self.new_file() # runs function
  
  def new_file(self):
    file = open("StudentList.txt", "w") # creates a file for all student details
    for i in range(0,len(self.Fname)): # goes through each person
      file.write(self.Fname[i]+"\n"+self.Lname[i]+"\n"+self.emails[i]+"\n"+self.course[i]+"\n"+self.__password[i]+"\nEND\n") # add all deails to the file
    file.close() # saves file and closes it
    print("Student List has been created.")
    
  def output(self,password,course):
    if password == "Cours3L3ad": # checks to see if it is a password of a courseleader
      file = open("StudentList.txt","r") # opens file in read mode 
      data = file.readlines() # turns all data into arary
      file.close()
      print("\n\nStudents:\n")
      file = open(course.title()+".txt","w") # opens a file called the course to hold all student details that do that course
      for i in range(0,len(data)-1,6): # Goes through each persons details
        if course.title() == data[i+3].strip(): # writes the detail into the new course file
          print("Name: " + data[i].strip() + " " + data[i+1].strip() + "\nEmail: " + data[i+2].strip() + "\n")
          file.write(data[i] + data[i+1] + data[i+2] + "\n")
      file.close()
      return False
    else:
      return True
 
valid = False
while not valid:
  choice = input("Would you like to geneate accounts(G) or output names & emails(N): ")
  choice = choice.strip()
  if choice.upper() == "G":
    valid = True
    while valid:
      file = input("\nEnter File name for data input: ")
      file = file.strip()
      try: # checks to see if file exists and can be accessed
        students = account_creator(file)
        students.fetch() # starts off the account creation function
        valid = False
      except:
        print("Invalid File")
    valid = True
  elif choice.upper() == "N": # inputs for outputting details
    valid = True
    course = input("\nEnter Course: ")
    while valid:
      password = input("Enter password: ")
      password = password.strip()
      students = account_creator("InputList")
      valid = students.output(password,course)
    valid = True
