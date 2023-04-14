# quizTrivia

quizTrivia is a web application for creating and managing quizzes. It allows users to register, create quizzes, take quizzes, and view quiz results and the right answers for each taken quiz.

## Features

- User registration and authentication with Django's built-in authentication system.
- Creation of quizzes with multiple choice questions.
- Taking quizzes and displaying results to users.
- Seeing the right answers for previously taken quizzes
- Profile management for users, including uploading profile picture.
- Creates Sessions containing the Questions taken for each quiz.
- Integration with Django forms for form validation and rendering.
- Use of Django's built-in database models for data persistence.
- Use of Django's built-in ORM for querying the database.

### You can demo the site at ``

## Usage

1. Register a new account or log in with an existing account.
2. Create a new quiz by providing a quiz name, questions, and choices.
3. Take quizzes by selecting choices for each question.
4. View quiz results to see the correct answers and user's score.
5. Manage user profile, including uploading a profile picture.
6. Logout of the application or get automatically logged out after 6 hours of inactivity.

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make changes and test thoroughly.
4. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

This project was developed by [Israel Omola](https://github.com/izzyskills).

## Contact

For any inquiries or feedback, please contact [izzskills@gmail.com](mailto:izzyskills@gmail.com).

## BUGS

-Wrong password leads you to registration page
-it doesn't tell you if a username is taken and just redirects yoy to login
-the forms registration and login could use some styling
-in the case of a blank pfp there should be a default when creating an account

-
