# GitHub Profile Summary App

## Overview

The **GitHub Profile Summary App** allows users to quickly generate a summary of a GitHub profile by simply entering the GitHub username. It fetches the user's public data from GitHub using the GitHub API and displays a summarized version of the profile, including information such as public repositories, followers, following count, and more.

### Features:
- **GitHub Profile Summary**: Displays key statistics such as repositories, followers, and following.
- **Instant Profile Search**: Enter a GitHub username to fetch and display a summary of their profile.
- **Loading Message**: A dynamic loading message is displayed while fetching the profile data.
- **Clear Button**: Allows users to clear the displayed summary and start fresh.
- **Responsive UI**: The app is mobile-friendly, adjusting seamlessly to smaller screens.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Backend**: Python (Flask)
- **APIs**: GitHub REST API
- **Libraries/Tools**:
  - [FontAwesome](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css) for icons.
  - [Bootstrap](https://getbootstrap.com/) for responsive design (optional).

## Prerequisites

Before running the app locally, ensure you have the following installed:
- **Python** 3.x
- **pip** (Python package manager)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sawanjr/RepoDigest--Github-Profile-Summarizer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd github-profile-summary
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the App

1. Run the Flask server:

    ```bash
    python app.py
    ```

2. Open your browser and go to:

    ```bash
    http://127.0.0.1:5000
    ```

3. Enter a GitHub username in the input field to fetch the profile summary.

## Functionality

- **GitHub Profile Summary**: When a valid GitHub username is entered, the app fetches data from the GitHub API and displays the summary, including repositories, followers, following, and more.
- **Clear Button**: The "Clear" button is hidden initially and only appears after the profile summary is generated. Once clicked, it resets the input field and hides the summary, ready for a new search.
- **Mobile-Friendly**: The design adjusts automatically for smaller screens.

## Screenshots

### Desktop View
![Desktop View](images/desktop-view.png)

## Contributing

We welcome contributions to enhance the app! Feel free to fork the repository and submit a pull request. Here's how you can contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [GitHub REST API](https://docs.github.com/en/rest) for fetching user data.
- [FontAwesome](https://fontawesome.com/) for providing icons.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) for the backend web framework.
- [Bootstrap](https://getbootstrap.com/) for responsive design.

## Contact

If you have any questions or suggestions, feel free to reach out to me via:

- **GitHub**: [Your GitHub Profile](https://github.com/sawanjr)
- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/sawan-kumar-bb8793243/)

---

Thank you for using the **RepoDigest- GitHub Profile Summary App**! 🎉
