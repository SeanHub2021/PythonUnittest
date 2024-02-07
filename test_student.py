import unittest
from student import Student
from datetime import timedelta

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    #The @classmethod decorator in the setUpClass method is used in the context of Python's unittest framework to define a class-level setup method. 
    #This method is called once for the entire test class before any individual test methods are executed. 
    #Its purpose is to perform any setup actions that are common to all the test methods within that test class.
    #So we could move def setUp into the this classmethod instead.



    def setUp(self): #setUp must be written in camelCase format, as its from the olden times of coding.
        print('setUp')
        self.student = Student('John', 'Doe')
    #this is declared early on in the tests, and would run once for each test. its more efficient than declaring the self.student name in each test, but not as efficient as it being in the classmethod. 

    #def tearDown(self): #this would test deleting files, like the opposite of setUp
    #   print('tearDown')


    def test_full_name(self):
        # student = Student('John', 'Doe') - once def setUp is created, we can remove these declarations of example names
        # and replace any reference to the "student" variable to self.Student
        print('test_full_name') #add these console prints to test each function, in case the test data from setUp isnt working
        self.assertEqual(self.student.full_name, 'John Doe')


    def test_alert_santa(self):
        #student = Student('John', 'Doe')
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)


    def test_email(self):
        #student = Student('John', 'Doe')
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com') 
        #in this test, we want to check the student.py code returns a string equal to 'john.doe@email.com' if working

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5)) #checks if the student end date is the same as the old date + 5 days, as per the test above


if __name__ == '__main__':
    unittest.main()