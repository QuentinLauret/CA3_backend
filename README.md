# Testing

In order to test the functionality of the guitar shop app, I utilized the TestCase module, which allowed me to simulate potential user actions. I created a class that includes the following methods to thoroughly test the app:

    test_creation: checks that a Guitar object created with valid data is saved successfully to the database.

    test_gid_error: checks that attempting to create a Guitar object with the same gid as the valid guitar raises an exception.

    test_invalid_creation: checks that attempting to create a Guitar object with invalid data raises an exception.

    test__update: checks that updating the valid Guitar object with new data works correctly and that the updated data is saved to the database.

    test_guitar_deletion: checks that deleting the valid Guitar object works correctly and that the object is removed from the database.

During this process, I found that understanding the TestCase module was challenging. However, after reading the documentation, primarily on the Django website, I was able to complete the work.

#Security

In addressing security concerns, I focused on preventing SQL injection attacks. To achieve this, I utilized the Django auth library, which automatically guards against SQL injections. In addition, I also prevented CSRF attacks by including {% csrf_token %} in my files. To protect against CSS attacks, I utilized two methods:

First, I used the premade formsof Django classes whenever possible.

Second, I added |safe at certain locations in my HTML files to ensure that they are rendered correctly.
