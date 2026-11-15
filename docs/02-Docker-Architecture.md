# 02 — Docker Architecture

## Components

- **Docker CLI (`docker`):** client used to issue commands.
- **Docker daemon (`dockerd`):** manages images, containers, networks, and volumes and exposes an API.
- **containerd:** container lifecycle and runtime management.
- **runc:** OCI-compatible low-level runtime that creates containers using Linux kernel facilities.
- **Docker Buildx / BuildKit:** modern image-building tooling.

Conceptual flow: `docker CLI → dockerd → containerd → runc → Linux kernel` (simplified).

## Kernel isolation and resources

Namespaces provide separate views of processes, networking, mounts, etc. Cgroups account for and limit resources. For example:

```bash
docker run --rm --cpus=0.5 --memory=128m alpine sh -c 'echo Resource-limited container'
```

This applies limits to the container; it does not guarantee sustained performance.

## Inspect the running engine

```bash
docker version
docker info
docker context ls
```

**[SCREENSHOT TO ADD]** Selected `docker info` lines showing client/server, runtime, cgroups, and storage driver. Do not publish the entire output if it includes information you prefer to keep private.

## Security notes

Access to a rootful Docker daemon is highly privileged; membership in the `docker` group effectively grants root-level access. Avoid publishing the daemon API on an unprotected TCP port. Prefer SSH contexts or properly secured TLS for remote administration. Rootless Docker is an alternative security model, but is not configured in this lab.

## Storage backend note

This lab previously reported `overlay2` on Engine 28.4.0. Fresh Engine 29+ installations default to the containerd image store and snapshotters; do not assume all hosts have the same on-disk layout.

References: https://docs.docker.com/engine/security/ ; https://docs.docker.com/engine/storage/containerd/
