from setuptools import  setup, find_packages
hyper_e_dot = "e ."
def get_packages(path):
    
    with open(path, 'r') as file_obj:
        requirements = file_obj.readlines()  
        requirements = [req.replace("\n","") for req in requirements]
        
        if hyper_e_dot in requirements:
            requirements.remove(hyper_e_dot)
            
setup(
    name="spam_classifier",
    version="0.0.1",
    author="Aziz Ashfak",
    author_email="azizashfak@gamil.com",
    description="A spam classifier",
    packages=find_packages(),
    install_requires=get_packages("requirements.txt"),
)
         
    