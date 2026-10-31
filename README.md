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



## 📦 AWS Cloud Learning Journey: Module 03 (Days 11–15)

### Project Overview
This module transitions from host-level server hosting (EC2) into cloud-native, serverless object storage using **Amazon Simple Storage Service (Amazon S3)**. The core deliverable for this module is a globally accessible, high-performance static portfolio website deployed directly on S3 without the overhead of an underlying operating system or web daemon.

---

### 📋 Completed Tasks Checklist
- [x] Task 1: Learn S3 buckets, objects, permissions, and storage classes.
- [x] Task 2: Create and configure an S3 bucket.
- [x] Task 3: Upload and manage files using S3.
- [x] Task 4: Understand basic S3 access control.
- [x] Task 5: Deploy a static portfolio website using Amazon S3.

---

### 🛠️ Technical Implementation & Architectural Choices

#### 1. Global Namespaces & Configuration
* **Global Uniqueness:** Provisioned an S3 storage container with a globally unique bucket identifier, aligning with the AWS DNS namespace rules.
* **Resiliency Lifecycle (S3 Versioning):** Enabled **S3 Versioning** on the bucket. This configuration instructs AWS to keep an immutable, version-controlled history of all object states, creating a safeguard against accidental file overwrites or data loss.

#### 2. Cost-Optimization & Storage Tiers
Architected data management strategies by understanding how data access patterns dictate cost metrics:
* **S3 Standard:** Selected for hosting active web files (`index.html`, assets) to guarantee low-latency public deliveries.
* **S3 Glacier Flexible / Deep Archive:** Documented for future cold-storage backups of systems logs, offering maximum cost reduction for inactive assets.

#### 3. Cloud Edge Access Controls (Security)
To transition the bucket from a secure private storage volume to a public web server, a multi-layered security modification was applied:
* **Deactivating Block Public Access (BPA):** Disabled the master account security override to allow specific public access controls.
* **Resource-Based JSON Policies:** Authored and attached a fine-grained, resource-based IAM Bucket Policy that grants explicit anonymous public read permissions (`s3:GetObject`) exclusively to objects residing inside the website root namespace.

#### 4. Serverless Static Hosting Execution
Flipped the S3 native hosting engine parameters to instruct the global endpoint to look for the primary document root layout (`index.html`). This decouples the website from standard computing instances, creating an instantly scalable, maintenance-free web application.

---

### 🚀 Verification & Live Deliverables
* **Deployment Method:** Serverless AWS Object Storage Engine
* **Infrastructure Configuration:** See `/s3-config/bucket-policy.json`
