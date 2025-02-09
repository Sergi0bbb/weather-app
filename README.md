# Weather App

## Description
Weather App is a service for retrieving and processing weather data using external APIs. It supports Redis caching and utilizes Docker for easy deployment.

## Features
- Fetch current weather conditions via API
- Cache data in Redis
- Background tasks for processing and saving data
- Containerization with Docker
- Store weather data as JSON files

## Installation and Running
### Environment Configuration
### Before running the application, ensure you configure the .env file with the required environment variables.
### Local Setup
1. Clone the repository:
   ```bash
   git clone <https://github.com/Sergi0bbb/weather-app>
   cd weather-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the service:
   ```bash
   python src/main.py
   ```

### Running with Docker
1. Build the Docker image:
   ```bash
   docker build -t weather-app .
   ```
2. Start the container:
   ```bash
   docker-compose up -d
   ```

## Project Structure
```
weather-app/
│── api/                # API and routes
│── src/                # Main application code
│   ├── configs/        # Configurations
│   ├── models/         # Data models
│   ├── redis_tools/    # Redis utilities
│   ├── services/       # Services and business logic
│── Dockerfile          # Container configuration
│── docker-compose.yaml # Docker Compose file
│── requirements.txt    # Dependencies
```

## Usage
Once started, the API documentation will be available at:
```
http://localhost:8000/docs
```
You can access API documentation with GET and POST methods there.
