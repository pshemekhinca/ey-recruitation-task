## Sample tests set for recruitment task

---

Contains several sample test cases for three subpages.

Tests are ordered according to Page-object-model (POM) assumptions. 

---


### Table of Contents

- [Technologies](#Technologies)
- [Files Structure](#Files-Structure)
- [How To Run Tests](#How-To-Run-Tests)
- [Autho Info](#author-info)

---



### Technologies

- pytest 6.2
- selenium 3.141
- allure-pytest==2.8.4


  
[Back to the Top ^](#Table-of-Contents)

---

### Files Structure

The project files should be ordered as below:


    
    EY-recrutation-task
    |
    |--- libs
    |    `---  allure-2.13.9 # not commited on github
    |    
    |--- results
    |    `---  # files generated for allure report
    | 
    |--- src
    |    `---  pages
    |          |--- authentication_page.py
    |          |--- create_account_page.py
    |          `--- home_page.py
    |      
    |--- tests
    |    |---  pages
    |    |     |--- base_test_class.py
    |    |     |--- tests_authentication_page.py
    |    |     |--- test_create_account_page.py
    |    |     `--- test_home_page.py
    |    | 
    |    `---  test_suites
    |          |--- testsuite_all_tests.py
    |          |--- testsuite_sanity_tests.py
    |          `--- testsuite_smoke_tests.py
    |
    |---  utils
    |     |--- inputs.py
    |     |--- locators.py
    |     |--- page_factory.py
    |     |--- web_urls.json
    |     `--- web_reader.py
    |
    `--- README.md

[Back to the Top ^](#Table-of-Contents)

---

### How To Run Tests
To run all tests, type:

```
pytest -v tests
```

or choosing specific file, add file path;

```
pytest -v tests/test_suites/testsuite_all_tests.py 
```

- To screen Allure tests report, prepare report data:
```
python -m pytest tests/test_suites/testsuite_all_tests.py --alluredir ./results
```
- then call to screen it in default web browser
```
libs/allure-2.13.9/bin/allure serve ./results  
```
[Back to the Top ^](#Table-of-Contents)

---

### Author Info

- Przemyslaw Hinca -> Github: [pshemekhinca](https://github.com/pshemekhinca)

[Back to the Top ^](#Table-of-Contents)
