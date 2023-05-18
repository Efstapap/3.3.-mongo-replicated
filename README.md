# 3.3.-mongo-replicated

# Virtual Laboratory README

This repository contains the configuration and setup for a MongoDB replica set using Docker.

## Overview

This repository aims to demonstrate the setup of a basic MongoDB replica set with two nodes: a primary and a secondary node. This setup allows for high availability and fault tolerance by replicating data across multiple nodes.


## Services and Tools Used

### Docker

Docker is used to containerize the MongoDB instances and facilitate easy deployment and management. It provides a lightweight and isolated environment for running the replica set nodes.

### MongoDB

MongoDB is a popular NoSQL database that offers high performance, scalability, and flexibility. In this virtual laboratory, we utilize the MongoDB database to create a replica set.

### Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications. It allows us to define the replica set configuration and easily spin up the required containers with a single command.

### Volumes

In this virtual laboratory, volumes are used to provide persistent data storage for the MongoDB replica set. The following volumes are defined:

- `datadb01`: This volume is mounted to the `/data/db` directory within the `db01` container, ensuring that the data for the primary node is stored persistently.

- `datadb02`: This volume is mounted to the `/data/db` directory within the `db02` container, ensuring that the data for the secondary node is stored persistently.

### Tkinter

It is a standard Python library for creating GUI (Graphical User Interface) applications. In this code, Tkinter is used to create a window and display the results of MongoDB operations.


## Repository Structure
- `README.md`: This README file.
- `docker-compose.yml`: The configuration file for the Docker services.
- `main.py`: The Python code for connecting to the MongoDB replica set.
- `INSTALL.md`: Installation instructions for the virtual laboratory.

## Files

- `main.py`: This file contains the main script of the virtual laboratory. It establishes a connection to a MongoDB replica set and performs various operations on the primary and secondary nodes.

  Here are some key points about the `main.py` file:
  - It utilizes the `pymongo` library to interact with MongoDB.
  - It establishes a connection to the MongoDB replica set using the specified connection string.
  - It performs an insert operation, read operations, and a delete operation on the primary node.
  - It demonstrates reading from the secondary node after a deletion with a delay.
  - It displays the results in a GUI created with Tkinter.

- `docker-compose.yml`: This file defines the Docker services for the virtual laboratory. It specifies the MongoDB version, volumes, ports, and container names for the primary and secondary nodes.

  Here are some key points about the `docker-compose.yml` file:
  - It defines two services: `db01` and `db02`, representing the primary and secondary nodes respectively.
  - Each service uses the `mongo:3.0` image.
  - Volumes are mounted to store the MongoDB data and configuration files.
  - Ports are exposed to allow communication with the primary and secondary nodes.
  - The `command` specifies the configuration and port settings for each node.
