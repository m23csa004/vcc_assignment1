# Microservices Application Deployment

This project demonstrates the deployment of a simple microservices-based application across multiple Virtual Machines (VMs) using Flask.

## Architecture Overview

The system consists of three microservices:
1. **User Service** (`userinfo.py`) - Handles user-related data.
2. **Order Service** (`orderhandler.py`) - Manages orders and transactions.
3. **API Gateway** (`gateway.py`) - Routes requests to the appropriate microservices.

## Setup and Execution

### 1. Virtual Machine Setup
- Installed **VirtualBox** and created multiple VMs.
- Configured **network settings** to enable communication between VMs.

### 2. Running the Services
On each VM, start the respective service:

#### **VM 1: User Service**
python3 userinfo.py

#### **VM 2: order Service**
python3 orderhandling.py

#### **VM 3: gateway Service**
python3 gateway.py

 ### **Testing the API**
Use curl or a browser to test the endpoints:
curl -X GET http://<gateway-ip>:8079/users
curl -X GET http://<gateway-ip>:8079/orders