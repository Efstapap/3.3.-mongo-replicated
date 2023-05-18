# 3.3.-mongo-replicated

# Virtual Laboratory

This repository contains the code and documentation for the virtual laboratory assignment.

## Services and Tools Used

- MongoDB Replica Set
- Docker

## Repository Structure

- `assignment.adoc`: The main text of the assignment in AsciiDoc format.
- `main.py`: The Python code for connecting to the MongoDB replica set.
- `yarn.yml`: The configuration file for the Docker services.
- `README.md`: This README file.
- `INSTALL.md`: Installation instructions for the virtual laboratory.

## Installation

Follow the steps below to set up the virtual laboratory:

1. Install Docker on your machine. Instructions can be found at [Docker Installation Guide](https://docs.docker.com/get-docker/).
2. Clone this repository to your local machine.
3. Open a terminal and navigate to the repository directory.
4. Run the following command to start the Docker services:

   ```bash
   yarn up
