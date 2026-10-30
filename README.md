# AWS Cloud Learning Journey: Module 02 (Days 6–10)

## Project Overview
This repository contains the practical implementation, architectural notes, and deployment code for Module 02 of my AWS Cloud learning track. The hands-on engineering lab was executed directly on a live Amazon Web Services (AWS) EC2 instance, focusing heavily on Identity and Access Management (IAM), cloud security protocols, and host-level system administration.

---

## 📋 Completed Tasks Checklist
- [x] Task 1: Learn IAM users, groups, roles, policies, and permissions.
- [x] Task 2: Understand basic AWS security and the principle of least privilege.
- [x] Task 3: Launch and configure an Amazon EC2 instance.
- [x] Task 4: Configure a Security Group and connect to EC2.
- [x] Task 5: Install a web server and deploy a basic HTML website.

---

## 🛠️ Deep Dive & Implementation Details

### Task 1 & 2: AWS IAM & Cloud Security Philosophy
* **Principle of Least Privilege (PoLP):** Implemented access controls by ensuring identities are granted *only* the minimum system permissions required to execute their specific functions.
* **IAM Structure Breakdown:**
  * **Users & Groups:** Created distinct IAM human identities grouped by operational function to streamline permission boundaries.
  * **Policies:** Attached strict, fine-grained JSON permission policies to control access to AWS resources.
  * **Roles vs. Users:** Configured an IAM Role specifically for service-to-service communication. Because IAM Roles are designed for trusted resources/applications and Users are intended for humans, an IAM Role was attached directly to the EC2 instance rather than embedding long-lived access keys.

### Task 3 & 4: Compute Provisioning & Infrastructure Edge Security
* **Host Specifications:** Provisioned an Amazon Elastic Compute Cloud (EC2) instance utilizing a **10 GiB gp3 root volume** running at 3000 IOPS.
* **Firewall Security Groups:** Engineered a stateful virtual firewall (Security Group) acting as the first line of network defense with the following rule matrix:

| Direction | Protocol | Port Range | Source / Destination | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| Inbound | TCP | `22` | My IP / Workstation | Secure Remote SSH Management |
| Inbound | TCP | `80` | `0.0.0.0/0` (Anywhere) | Public Web Traffic HTTP |
| Outbound | All | All | `0.0.0.0/0` | Unrestricted Internet Access |

* **Remote Connectivity:** Established a secure connection from a local Fedora Workstation to the running EC2 server using native SSH utilities and private keypair certificates.

### Task 5: System Administration, Web Server Setup & Deployment
Once remote shell access to the instance was secured, the local environment was initialized and configured to run an active web service:
1. Updated system repositories and installed a production-ready HTTP web server daemon.
2. Enabled the service utility to persist across system reboots and initialized the active runtime process.
3. Created and configured the primary layout file (`index.html`) containing the basic web architecture.
4. Placed the application code within the web server's public document root directory to serve live client requests over the internet.

---

## Verification & Live Status
The deployment can be verified by routing traffic directly to the Public IP address of the managed AWS infrastructure. 

* **Hosting Environment:** Live AWS EC2 Instance
* **Access Protocol:** `http://51.20.129.245/`

---
*Maintained by Kennedy Odhiambo Aura — Advancing from Network Infrastructure to Cloud Systems Architecture.*
