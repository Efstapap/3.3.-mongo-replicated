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

### pymongo

It is a Python driver for MongoDB. It provides an interface for interacting with MongoDB from Python.

### Tkinter

It is a standard Python library for creating GUI (Graphical User Interface) applications. In this code, Tkinter is used to create a window and display the results of MongoDB operations.

### MongoClient

It is a class from the pymongo library that represents a MongoDB client. It is used to establish a connection to the MongoDB replica set using the specified connection string.

### ReadPreference

It is an enumeration from the pymongo library that defines the read preference mode for MongoDB operations. In our code,
ReadPreference.SECONDARY is used to specify that the read operations should be directed to secondary nodes of the replica set.

### WriteConcern

It is a class from the pymongo library that specifies the write concern options for MongoDB operations. In our code, w=1 is used to ensure that write operations are acknowledged by the primary node.

## Repository Structure
- `README.md`: This README file.
- `docker-compose.yml`: The configuration file for the Docker services.
- `main.py`: The Python code for connecting to the MongoDB replica set.
- `INSTALL.md`: Installation instructions for the virtual laboratory.

## Installation

Follow the steps below to set up the virtual laboratory:

1. Install Docker on your machine. Instructions can be found at [Docker Installation Guide](https://docs.docker.com/get-docker/).
2. Clone this repository to your local machine.
3. Open a terminal and navigate to the repository directory.
4. Run the following command to start the Docker services:

   ```bash
   yarn up
