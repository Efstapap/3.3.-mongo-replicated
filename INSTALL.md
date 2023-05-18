# Virtual Laboratory - Installation Guide

This guide provides step-by-step instructions for installing and setting up the virtual laboratory project.

## Prerequisites

Before proceeding with the installation, ensure that you have the following prerequisites:

- Docker: The virtual laboratory project relies on Docker for containerization. Make sure Docker is installed and running on your system. You can download Docker from the official website: [https://www.docker.com/](https://www.docker.com/)

## Installation Steps

To install and set up the virtual laboratory, follow these steps:

1. Clone the Repository:
   - Open a terminal or command prompt.
   - Change to the directory where you want to clone the repository.
   - Run the following command to clone the repository:

     ```
     git clone <repository_url>
     ```

2. Navigate to the Project Directory:
   - Change to the directory of the cloned repository:
   
     ```
     cd <repository_directory>
     ```

3. Run Docker Compose:
   - Execute the following command to start the virtual laboratory services:
   
     ```
     docker-compose up -d
     ```
     
   This command will build and start the Docker containers defined in the `docker-compose.yml` file. It will set up the MongoDB replica set with a primary and secondary node.

4. Verify the Installation:
   - After the Docker containers are up and running, you can check the status of the MongoDB replica set by running the following command:
   
     ```
     docker-compose exec db01 mongo --port 30001 --eval "rs.status()"
     ```
   
   This command will connect to the primary node and display the status of the replica set.

5. Run the Virtual Laboratory:
   - You are now ready to run the virtual laboratory. Execute the following command to start the main script:
   
     ```
     python main.py
     ```
   
   The script will establish a connection to the MongoDB replica set and perform various operations on the primary and secondary nodes. The results will be displayed in a graphical user interface (GUI) window.

6. Cleanup and Shutdown:
   - To stop the virtual laboratory and clean up the Docker containers, run the following command:
   
     ```
     docker-compose down
     ```
     
   This command will stop and remove the Docker containers associated with the virtual laboratory.

## Additional Configuration

If you need to customize any configuration settings, you can modify the `docker-compose.yml` file and the `main.py` script according to your requirements.

## Troubleshooting

If you encounter any issues during the installation or usage of the virtual laboratory, refer to the project's documentation or check for any error messages in the terminal or command prompt.

## Contributing

If you would like to contribute to the virtual laboratory project, please follow the guidelines outlined in the project's README file. Contributions such as bug fixes, feature enhancements, and documentation improvements are welcome.

## License

[Specify the license under which the virtual laboratory project is distributed]

