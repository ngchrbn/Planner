"""Class that handles the creation, manipulation and deletion of the subjects.
Data are stored in a file called Subject Records.txt
"""


class Subject:
    def __init__(self):
        self.filename = "Subject Records.txt"

    def add_subject(self):
        """To store data in a dictionary"""

        subject_id = input("Subject ID: ")
        subject_name = input("Subject Name: ")
        subject_level = input("Subject Level: ")
        subject_department = input("Subject Department: ")

        outputfile = open(self.filename, 'a')   # open the file to write all the contents
        outputfile.write(subject_id)
        outputfile.write(" ")
        outputfile.write(subject_name)
        outputfile.write(" ")
        outputfile.write(subject_level)
        outputfile.write(" ")
        outputfile.write(subject_department)
        outputfile.write(" # ")
        outputfile.close()  # close the file




    def get_subject(self, subj_id):
        """To print a subject's information."""
        pass
