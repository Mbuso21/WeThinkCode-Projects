# problem-102-java-002-001
Module 102
Topic 002: Introduction to Java
Problem 001: FizzBuzz

## Getting Started
This project is a `Java` project using `maven` as build tool.

The structure is as follow:
* `src/main/java` - in here is some skeleton code that you must use as starting point for the problem.
* `src/test/java` - in here are unit tests code that you must complete and extend (your unittests will also be reviewed)
* `src/test/java/za/co/wethinkcode/lms/tests` - the files in this directory are special and should _not be edited by you_. These are the LMS tests that will need to succeed against your code as well. The LMS system will use the original (unedited) tests to test your submissions.

### IntelliJ
To open it in `IntelliJ` IDE:
1. _File_ -> _New_ -> _Project from Existing Sources..._
1. Select the directory where this code has been checked out to by the LMS
1. Choose _External Model_ as *Maven*

## Build, Test & Run
You may use IntelliJ to run your code and tests, but alternatively you can use the Maven build tool:
* First ensure you are in the root directory of the project
* To compile your code, run: `mvn compile` 
* To run the tests: `mvn test`
* To run your application: `mvn compile exec:java`

