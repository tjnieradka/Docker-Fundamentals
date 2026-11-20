# Docker Foundations — Ubuntu Lab

Practical Docker notes and hands-on exercises covering container management, images, Dockerfiles, networking, storage, Compose, registries, and troubleshooting.

## 1. Overview

This repository documents foundational Docker concepts and repeatable exercises performed in a personal Ubuntu Linux lab. It demonstrates container lifecycle management, image creation and distribution, persistent storage, networking, multi-container configuration, and basic troubleshooting.

The repository is intended as a learning portfolio, not a production deployment guide.

## 2. Technologies and Tools

- Docker Engine, Docker Compose, and Docker Buildx
- Dockerfiles and container registries
- Ubuntu Linux and Rocky Linux
- Linux command-line tools

## 3. Documentation

1. [Container Fundamentals](docs/01-Container-Fundamentals.md)
2. [Docker Architecture](docs/02-Docker-Architecture.md)
3. [Lab Environment](docs/03-Lab-Environment.md)
4. [Container Management](docs/04-Container-Management.md)
5. [Docker Images and Dockerfiles](docs/05-Docker-Images-and-Dockerfiles.md)
6. [Docker Storage](docs/06-Docker-Storage.md)
7. [Docker Networking](docs/07-Docker-Networking.md)
8. [Docker Compose](docs/08-Docker-Compose.md)
9. [Registries and Image Distribution](docs/09-Registries-and-Image-Distribution.md)
10. [Docker Troubleshooting](docs/10-Docker-Troubleshooting.md)
11. [Container Orchestration Overview](docs/11-Container-Orchestration-Overview.md)

## 4. Lab Environment and Scope

- **Docker host:** `VAN-DOCKER-TEST`, Ubuntu 24.04.3 LTS virtual machine
- **Docker versions:** Engine 28.4.0, Compose 2.39.2, Buildx 0.27.0
- **Resources:** 4 vCPUs, approximately 8 GiB RAM; `overlay2` storage driver
- **Remote test machine:** `VAN-ROCKY-TEST`, Rocky Linux 8.10 (Green Obsidian) virtual machine

The lab was reset by removing earlier training containers and images before repeating the exercises. Configurations and results reflect a controlled learning environment rather than a hardened production deployment.

## 5. Project Status and Attribution

The documented foundational exercises were completed through hands-on practice and independent review guided by a Udemy/KodeKloud Docker course. Examples were adapted and simplified for this lab; commands and results were documented after testing.

An original multi-container application has been deferred for future development and is not included among the completed guides.

## 6. References and Learning Resources

- [Docker Documentation](https://docs.docker.com/)
- [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [Docker Compose File Reference](https://docs.docker.com/reference/compose-file/)
