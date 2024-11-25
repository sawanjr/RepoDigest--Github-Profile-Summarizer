# Email Generator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

The Email Generator is a powerful tool that uses Large Language Models (LLMs) to craft customized email content based on user-defined subjects and tones. Whether you need a formal business email, a friendly message, or something with a touch of humor, this tool has you covered.

This repository provides the code and instructions to use the Email Generator, which leverages OpenAI's GPT-3 language model for generating email content. The project is integrated with Streamlit, making it easy for users to input their preferences and generate tailored email text.

## How It Works

The Email Generator operates in two main steps:

1. **Email Generation**: The heart of the system is a Python script that uses Langchain, a framework for working with LLMs. The script takes user inputs for the subject and tone of the email. It then uses the OpenAI GPT-3 model to generate a brief, two-line email, ensuring that the tone and content align with the user's preferences.

2. **User Interface with Streamlit**: To make the Email Generator accessible and user-friendly, we've built a Streamlit web application. Users can input the subject (up to 30 characters) and select their desired tone from a range of options, such as formal, informal, friendly, and more. Upon clicking the "Generate Email" button, the application calls the email generation script and displays the generated email along with the chosen subject and tone.

## Getting Started

### Prerequisites

Before using the Email Generator, you need to have Python and a few dependencies installed. Make sure you have the following:

- Python 3.6 or higher
- Required Python packages (install with `pip install -r requirements.txt`):
  - `langchain`
  - `streamlit`
  - `dotenv`

### Usage

1. Clone this repository to your local machine.

2. Create a `.env` file with your OpenAI API key and any other necessary environment variables. You can use the provided `.env.example` as a template.

3. Run the Streamlit application:


4. Access the Email Generator in your web browser at the provided URL (usually `http://localhost:8501`).

5. Enter the subject and choose the tone for your email, then click the "Generate Email" button to see the generated content.

## Developer Information

This Email Generator project is maintained by Sawan Kumar, a passionate explorer of machine learning and Large Language Models. You can connect with the developer via:

- [GitHub](https://github.com/sawanjr)
- [LinkedIn](https://www.linkedin.com/in/sawan-kumar-bb8793243)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the GPT-3 model, enabling innovative language generation applications.
- Streamlit for simplifying the creation of interactive web applications.
- The open-source community for contributing to the tools and libraries used in this project.
