# Frontend Application for Spend Tracker

This is the frontend application for the Spend Tracker project, built using React. It allows users to manage their spending data by adding, editing, deleting, and visualizing their expenses.

## Getting Started

To get started with the frontend application, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd spend-tracker-app/frontend
   ```

2. **Install Dependencies**
   Make sure you have Node.js installed. Then, run the following command to install the necessary dependencies:
   ```bash
   npm install
   ```

3. **Run the Application**
   Start the development server with:
   ```bash
   npm start
   ```
   This will launch the application in your default web browser at `http://localhost:3000`.

## Features

- **Add Spending**: Users can add new spending entries through a form.
- **Edit Spending**: Users can edit existing entries to update their spending information.
- **Delete Spending**: Users can delete entries they no longer want to keep.
- **View Spending List**: A comprehensive list of all spending entries is displayed for easy tracking.

## Folder Structure

- `public/`: Contains the static files, including `index.html`.
- `src/`: Contains the React components and services.
  - `components/`: Contains individual components for adding, editing, deleting, and listing spending entries.
  - `services/`: Contains API service functions for backend communication.
  
## API Integration

The frontend communicates with the backend using RESTful API calls. Ensure that the backend server is running to interact with the database.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.