from setuptools import setup, find_packages
setup(name="dab_project", 
        version="0.1",
        description="DataBricks Asset Bundle Project",  
        author="Avmoni",
        author_email="vaikunda.moni@dxc.com",
        packages=find_packages(where="./src"),
        package_dir={"":"./src"} ,
        install_requires=["setuptools", "wheel"],
        entry_points={
            "packages": [
                 "main = dab_project.main:main"
            ]
        }
     ) 

