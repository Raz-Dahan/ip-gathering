# IP Gathering with Ansible and Python in Docker

This repository demonstrates how to create a Docker container that uses Ansible and Python to gather IP information and save it to a CSV file on the host machine.

## Prerequisites

- Docker and Git installed on your Ubuntu server

## Getting Started

1. Clone this repository to your local machine:

   ```sh
   git clone https://github.com/Raz-Dahan/ip-gathering.git
   cd ip-gathering
   ```

2. If any changes have been made to the project since the last build, run the initialization script to build the Docker image:

   ```sh
   chmod u+x init.sh
   ./init.sh
   ```

3. Start the Docker container using the `start.sh` script:

   ```sh
    chmod u+x start.sh
   ./start.sh
   ```

## Project Structure

```
ip_gathering/
├── playbook.yml
├── GetData.py
├── dockerfile
├── init.sh
├── start.sh
└── csv_data/
```

- `playbook.yml`: Ansible playbook to gather IP information.
- `GetData.py`: Python script to interact with IP data and save to a CSV file.
- `dockerfile`: Dockerfile for building the Docker image.
- `init.sh`: Initialization script for building the Docker image and starting the container.
- `start.sh`: Script to start the Docker container.
- `csv_data/`: Directory for saving CSV data on the host machine.

## License

This project is licensed under the [MIT License](LICENSE).
