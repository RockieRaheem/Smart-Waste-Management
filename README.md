# Smart Waste Management System

The Smart Waste Management System is a Django-based web application designed to streamline waste management processes. It includes features for user authentication, waste request submissions, illegal dumping reports, and tracking of garbage trucks.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and role-based access control
- Waste collection request submissions
- Illegal dumping report submissions
- Garbage truck tracking
- Admin dashboard for managing users and requests
- REST API for integration with other systems

## Installation

### Prerequisites

- Docker
- Docker Compose
- Python 3.8+
- Node.js (for frontend assets)

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/RockieRaheem/Smart-Waste-Management.git
    cd Smart-Waste-Management
    ```

2. Build and run the Docker containers:

    ```sh
    docker-compose up --build
    ```

3. Apply database migrations:

    ```sh
    docker-compose exec web python manage.py migrate
    ```

4. Create a superuser:

    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

5. Collect static files:

    ```sh
    docker-compose exec web python manage.py collectstatic
    ```

6. Access the application at `http://localhost:8000`.

## Usage

### Running the Development Server

To run the development server locally without Docker, follow these steps:

1. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```sh
    python manage.py migrate
    ```

4. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```sh
    python manage.py runserver
    ```

6. Access the application at `http://localhost:8000`.

## API Endpoints

The application provides a REST API for integration with other systems. Below are some of the key endpoints:

- `POST /api/login/`: User login
- `POST /api/signup/`: User signup
- `GET /api/waste-requests/`: List waste requests
- `POST /api/waste-requests/`: Create a new waste request
- `GET /api/illegal-dumping-reports/`: List illegal dumping reports
- `POST /api/illegal-dumping-reports/`: Create a new illegal dumping report
- `GET /api/garbage-trucks/`: List garbage trucks
- `POST /api/garbage-trucks/`: Create a new garbage truck

## Contributing

We welcome contributions to the Smart Waste Management System! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear commit messages.
4. Push your changes to your fork.
5. Create a pull request to the main repository.


## License

Unfortunately, we are not yet licenced.



<img width="910" alt="Image" src="https://github.com/user-attachments/assets/d55226d5-e634-457d-a669-46aca4920df6" />
<img width="818" alt="Image" src="https://github.com/user-attachments/assets/7fd99a1a-9f2b-4c98-b3f0-a26fb9fef54e" />
<img width="904" alt="Image" src="https://github.com/user-attachments/assets/3ac3d23d-e17a-4638-a9a7-a20c91813f43" />
<img width="885" alt="Image" src="https://github.com/user-attachments/assets/668fa531-668b-4c23-9da2-9ac9cdb6dd19" />
<img width="889" alt="Image" src="https://github.com/user-attachments/assets/9a725b56-6aec-4e8f-9fe6-09a0db9cbe64" />
<img width="589" alt="Image" src="https://github.com/user-attachments/assets/a3ffb225-caf0-4e0e-a41e-d1dfbda0a9e9" />
<img width="885" alt="Image" src="https://github.com/user-attachments/assets/668fa531-668b-4c23-9da2-9ac9cdb6dd19" />

