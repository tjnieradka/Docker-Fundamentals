# 11 — Container Orchestration Overview

## Why orchestration?

A single Docker host is suitable for small labs, but multi-host services need coordinated scheduling, scaling, networking, and recovery. Orchestration systems manage desired application state across multiple nodes.

| Technology | Overview |
|---|---|
| Docker Swarm | Docker-native clustering and replicated services |
| Kubernetes | Broadly adopted platform for declarative container workloads |

## Key Kubernetes concepts

- **Control plane:** API server, scheduler, controllers, and etcd coordinate cluster state.
- **Worker node:** runs workloads using a kubelet and a supported CRI runtime (commonly containerd or CRI-O).
- **Pod:** basic Kubernetes scheduling unit; contains one or more containers.
- **Deployment:** declares and maintains replicated application Pods.

Kubernetes does **not** require Docker Engine or always use containerd. Docker Engine itself uses containerd as part of its runtime architecture, which is a separate point.

## Lab status

This repository does not currently demonstrate a Swarm or Kubernetes cluster. No orchestration screenshots are required. Commands such as `kubectl get pods` should only be shown as executed after a real cluster is configured.

References: https://kubernetes.io/docs/concepts/overview/components/ ; https://docs.docker.com/engine/swarm/
