# Pixela API Desktop Client

A Python desktop application built with CustomTkinter that provides a graphical interface for interacting with the [Pixela API](https://pixe.la/).

The application allows users to create and manage Pixela accounts, create habit-tracking graphs, record daily measurements, and open their graphs in a web browser.

## Features

- Create a Pixela account from the application.
- Generate an alphanumeric API token.
- Keep local details for multiple Pixela usernames.
- Create habit-tracking graphs with a graph ID, habit name, measurement unit, and colour.
- Submit a quantity for a selected graph and date.
- Insert the current date with a button.
- Display the measurement unit associated with a selected graph.
- Open a selected graph on the Pixela website.

## Technologies

- **Python** – application logic.
- **CustomTkinter** – desktop graphical user interface.
- **Requests** – HTTP requests to the Pixela API.
- **JSON** – local storage of usernames, API tokens, and graph metadata.
- **Tkinter** – GUI variables and message dialogs.
- **Webbrowser** – opening graph pages in the default browser.

## How it works

The application communicates with the Pixela API to create users, create graphs, and submit graph data. It stores account tokens and graph metadata locally in a `users.json` file so that the user can select previously configured accounts and graphs.

## Requirements

- Python 3
- The third-party packages listed in `requirements.txt`
- An internet connection
- A Pixela account (or the ability to create one through the application)

## Setup

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python pixela_api_client.py
   ```

The application creates/uses `users.json` in its working directory to store local account and graph details.

## Local configuration and security

The application stores Pixela API tokens in `users.json` as plain text. This was an educational project and the original implementation does not encrypt those tokens.

- Do not commit your real `users.json` file.
- Do not share screenshots or sample files containing real API tokens.
- The included `users.example.json` contains placeholder data only.
- Do not use this application as a secure credential-storage system.

## Project context

This project was developed as a Python desktop application to make common Pixela habit-tracking operations accessible through a graphical interface rather than requiring users to make API requests manually.

## Known limitations

This repository preserves the original project implementation. It has not been comprehensively refactored or security-hardened.

Some areas that could be improved in a future iteration include:

- Secure storage of API tokens.
- Stronger input validation for dates and quantities.
- More comprehensive handling of network errors and API responses.
- Request timeouts and improved responsiveness during network operations.
- Separation of the GUI, API communication, and local data-storage logic.

## Future improvements

- Add encrypted credential storage.
- Improve validation and user feedback.
- Add clearer API error handling.
- Refactor the application into separate modules.
- Add screenshots and a short demonstration video if they become available.

## Acknowledgements

- [Pixela](https://pixe.la/) for providing the habit-tracking API.
- [CustomTkinter](https://customtkinter.tomschimansky.com/) for the modern Tkinter-based UI toolkit.

## Some Visuals
<img width="735" height="813" alt="image" src="https://github.com/user-attachments/assets/e1a52d36-7d0f-42c5-b37b-5d100d947b54" />
<img width="730" height="799" alt="image" src="https://github.com/user-attachments/assets/c25e9835-15d9-4fac-ad6a-94b56f6852b9" />
<img width="733" height="808" alt="image" src="https://github.com/user-attachments/assets/e6dbf6b7-8809-4f08-a126-f15aee31170e" />


