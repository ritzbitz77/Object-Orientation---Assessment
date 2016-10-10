"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Encapsulation: Encapsulation is a way to organize code in the most efficient way possible. It allows
   us to only use the necessary code needed to complete a task at hand. The pieces of data we need for a task
   are close to the functions that use that data. 

   Abstraction: The wonderful thing about abstracting in Python is that it hides uncessary details that 
   are not needed in the code we are using. It allows us to work with more complicated ideas in programming
   without having to actually understand them. These ideas make the code we are writing more efficient and 
   clear. When thinking about abstraction, I think about .self in classes. It means something very important
   in making our code work but it's not entirely neccessary that I know exactly what it maens or does.

   Polymorphism: Polymorphism is so interesting! This concept allows us to "plug" in code to make things run 
   faster and for us to have as much DRY code as possible. We can take code from an abstract class and use it 
   in a subclass allowing __init__ to take different arguments. Polymorphism allows us to take the common
   factor in our code and spread it throughout our subclasses for easier reading ability and more efficient
   coding.

2. What is a class? 
A class is a type of thing that could be a string or a file. They are a way for us to group 
methods/functions so we can access the data within one another. There are super classes and subclasses in Python. 
Generally, the superclass holds the greatest common factor. The wonderful thing about classes is that you can 
pull information from the super class into your subclass. You can take a class and make mini versions of each and 
make them all different with common factors. 

3. What is an instance attribute? 
An instance attribute is a a characteristic within a class or method. An example of this would be a name of a cat.
Here is the breakdown - Animal > Cat > Whiskers. Animal is the class, cat is the class attribute (shares commonality
in that class) and Whiskers is the name of the cat. Whiskers is an instance attribute because not all the cats are named
Whiskers. 

4. What is a method?
A method is a function within a class. It does something similar to the super class that it is in but 
not the exact same thing. A method can take attributes of its class but do things differently in the detailed sense. 


5. What is an instance in object orientation?
An instance in object orientation is a general idea or word that will be used within the methods of that class.
In the previous question, Animal is the class instance of what methods or subclasses are to come after. It is an
overarching definition of what the code is related to. It is the output of the class essentially. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
A class attribute is a broader definition of what we get the code while the instance attribute is more specific.
As mentioned above, animal is the class attribute and name of a cat is an instance attribute. You would use a class
attribute at the beginning of creating your code. This is the general idea or definition of what the code will use 
to describe what's going on in the code. An instance attribute is a detail associated with the class instance that 
keeps our code related but different at the same time. 


"""


# Parts 2 through 5:
# Create your classes and class methods


class Student():
    """A class for all students taking an assessment"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address




class Question():
    """A class where questions are created and evaluated."""
   
    def __init__ (self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        response = raw_input(self.question + " > ")

        if response == self.correct_answer:
            return True
        else:
            return False




class Exam(object):
    """A class where exam is created and evaluated"""
    
    def __init__(self, name):
        self.questions = []
        self.name = name

    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        score = 0

        for question in self.questions:
            answer = question.ask_and_evaluate()

            if answer is True:
                score = score + 1

        return score 

def take_test(self, exam, student):
    score = exam.administer()
    student.score = score

class Quiz(Exam):
    """A class where a quiz is created but takes characteristics of the exam

    True/False determines if the student passed (more than 50% correct) or failed
    (less than 50% correct)"""
    
    def __init__(self, name):
        super(Quiz, self).__init__(name)
    
    
    def administer(self):
        score = super(Quiz, self).administer()
        percent_correct = score/len(self.questions)
        return percent_correct >= .5












































