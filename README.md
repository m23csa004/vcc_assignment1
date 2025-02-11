Microservices Deployment Across Virtual Machines
Overview
This project demonstrates the deployment of a microservices-based application across multiple virtual machines (VMs) using Flask. It consists of three microservices:

User Service (userinfo.py) – Manages user data.
Order Service (orderhandler.py) – Handles order processing.
Gateway Service (gateway.py) – Acts as an API gateway to route requests to the appropriate microservice.
The services communicate over a network configured within VirtualBox to simulate a distributed system.

Architecture
The architecture consists of three VMs, each running a different microservice:

VM1 (User Service) → Provides user information (/users).
VM2 (Order Service) → Provides order information (/orders).
VM3 (Gateway Service) → Routes requests to the correct microservice.
Microservice Communication Flow
A client makes a request to the Gateway Service.
The Gateway forwards the request to either the User Service or Order Service based on the endpoint.
The respective service processes the request and returns a response.
