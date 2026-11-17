# Docker Foundations — Ubuntu Lab

This repository contains practical notes and repeatable exercises covering Docker Engine, container lifecycle, images, Dockerfiles, networking, storage, Compose, registries, and troubleshooting.

The purpose is to demonstrate foundational Docker knowledge and experimentation in a personal Ubuntu Linux lab. This is a learning portfolio, not a production deployment guide.

## Lab

- Host: `VAN-DOCKER-TEST` (Ubuntu 24.04.3 LTS virtual machine)
- Docker Engine: 28.4.0; Compose: 2.39.2; Buildx: 0.27.0
- 4 vCPUs; approximately 8 GiB RAM; `overlay2` storage driver
- Remote test machine: `VAN-ROCKY-TEST` (Rocky Linux 8.10 (Green Obsidian) virtual machine)
- Environment was reset by removing previous training containers/images before repeating exercises.


## Documentation

1. [Container fundamentals](docs/01-Container-Fundamentals.md)
2. [Docker architecture](docs/02-Docker-Architecture.md)
3. [Lab environment](docs/03-Lab-Environment.md)
4. [Container management](docs/04-Container-Management.md)
5. [Images and Dockerfiles](docs/05-Docker-Images-and-Dockerfiles.md)
6. [Storage](docs/06-Docker-Storage.md)
7. [Networking](docs/07-Docker-Networking.md)
8. [Compose](docs/08-Docker-Compose.md)
9. [Registries](docs/09-Registries-and-Image-Distribution.md)
10. [Troubleshooting](docs/10-Docker-Troubleshooting.md)
11. [Orchestration overview](docs/11-Container-Orchestration-Overview.md)
12. [Original multi-container application — planned](docs/12-Multi-Container-Application.md)

## Scope and attribution

The content in this repository is based on independent review and hands-on exercises guided by a Udemy/KodeKloud Docker course. Examples have been adapted and simplified for this lab. The multi-container application exercise has been deferred for future development. Commands and results are documented only after being tested in the lab.

## References

- [Docker documentation](https://docs.docker.com/)
- [Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [Compose Specification](https://docs.docker.com/reference/compose-file/)
