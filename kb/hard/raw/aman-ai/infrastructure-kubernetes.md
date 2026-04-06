# Infrastructure • Kubernetes

**Source:** https://aman.ai/infra/kubernetes/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** infrastructure

---

* [Kubernetes Overview](#kubernetes-overview)
  + [Key Features](#key-features)
* [Kubernetes Architecture](#kubernetes-architecture)
  + [Cluster Components](#cluster-components)
    - [Control Plane](#control-plane)
    - [Nodes](#nodes)
  + [Pods](#pods)
* [Core Concepts](#core-concepts)
  + [Deployments and Services](#deployments-and-services)
  + [Namespaces](#namespaces)
  + [ConfigMaps and Secrets](#configmaps-and-secrets)
  + [Volumes](#volumes)
  + [Kubernetes Management Tools](#kubernetes-management-tools)
* [Docker and K8](#docker-and-k8)
  + [Docker Overview](#docker-overview)
    - [Key Features of Docker](#key-features-of-docker)
  + [Kubernetes Overview](#kubernetes-overview-1)
    - [Key Features of Kubernetes](#key-features-of-kubernetes)
  + [How Docker and Kubernetes Work Together](#how-docker-and-kubernetes-work-together)
    - [Complementary Technologies](#complementary-technologies)
    - [Workflow Integration](#workflow-integration)
    - [Example Use Case](#example-use-case)

## Kubernetes Overview

**Kubernetes**, often abbreviated as **K8s**, is an open-source platform designed to automate the deployment, scaling, and management of containerized applications. Developed by Google and now maintained by the Cloud Native Computing Foundation, Kubernetes aims to provide a framework for running distributed systems resiliently, allowing for scaling and failover for your application, and providing deployment patterns.

### Key Features

* **Container Orchestration**: Automatically places containers based on their resource requirements and other constraints, while not sacrificing availability.
* **Load Balancing**: Supports service discovery and load balancing, which can distribute network traffic so that the deployment is stable.
* **Storage Orchestration**: Automatically mounts the storage system of choice, whether from local storage, public cloud providers, or network storage systems.
* **Automated Rollouts and Rollbacks**: Allows for changes to the application or its configuration while monitoring application health to ensure it does not kill all instances at the same time.
* **Self-healing**: Restarts containers that fail, replaces and reschedules containers when nodes die, kills containers that don’t respond to user-defined health checks, and doesn’t advertise them to clients until they are ready to serve.
* **Secret and Configuration Management**: Manages sensitive information such as passwords and API keys through secrets and application configuration without rebuilding your image and without exposing secrets in your stack configuration.

## Kubernetes Architecture

### Cluster Components

A Kubernetes cluster consists of the components that represent the control plane and a set of machines called nodes.

#### Control Plane

The control plane’s components make global decisions about the cluster (for example, scheduling), as well as detecting and responding to cluster events (for example, starting up a new pod when a deployment’s replicas field is unsatisfied).

* **kube-apiserver**: The API server is a component of the Kubernetes control plane that exposes the Kubernetes API.
* **etcd**: Consistent and highly-available key value store used as Kubernetes’ backing store for all cluster data.
* **kube-scheduler**: Watches for newly created Pods with no assigned node, and selects a node for them to run on.
* **kube-controller-manager**: Runs controller processes, which handle routine tasks in the cluster.
* **cloud-controller-manager**: Lets you link your cluster into your cloud provider’s API, and separates out the components that interact with that cloud platform from components that just interact with your cluster.

#### Nodes

Nodes are the workers that run applications. Each node has the components necessary to run pods and is managed by the master components.

* **kubelet**: An agent that runs on each node in the cluster. It makes sure that containers are running in a Pod.
* **kube-proxy**: kube-proxy maintains network rules on nodes. These network rules allow network communication to your Pods from network sessions inside or outside of your cluster.
* **Container Runtime**: The software that is responsible for running containers.

### Pods

The smallest and simplest Kubernetes object. A Pod represents a set of running containers on your cluster.

## Core Concepts

### Deployments and Services

* **Deployments**: A way to declare updates to applications declaratively. A Deployment provides declarative updates for Pods and ReplicaSets.
* **Services**: An abstraction that defines a logical set of Pods and a policy by which to access them - sometimes called a micro-service.

### Namespaces

Kubernetes supports multiple virtual clusters backed by the same physical cluster. These virtual clusters are called namespaces.

### ConfigMaps and Secrets

* **ConfigMaps**: Allow you to decouple configuration artifacts from image content to keep containerized applications portable.
* **Secrets**: Used to store and manage sensitive information, such as passwords, OAuth tokens, and ssh keys.

### Volumes

A directory containing data, accessible to the containers in a pod, which persists beyond the life of the pod.

### Kubernetes Management Tools

* **kubectl**: The CLI tool for Kubernetes. It allows users to run commands against Kubernetes clusters.
* **Helm**: A package manager for Kubernetes, allowing users to define, install, and upgrade complex Kubernetes applications.

## Docker and K8

* The image below [(source)](https://www.youtube.com/watch?v=9_s3h_GVzZc) helps provide an overview of how docker and kubernetes work together.

### Docker Overview

**Docker** is a platform designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package.

#### Key Features of Docker

* **Portability**: Once a Docker container is created, it can be run on any machine that has Docker installed, regardless of the operating environment.
* **Consistency**: Docker ensures that the application works seamlessly in any environment from development through staging to production.
* **Isolation**: Containers are isolated from each other and the host system, making them secure.
* **Resource Efficiency**: Containers share the host system’s kernel, and not each requires an OS of its own. This makes them lightweight and fast.

### Kubernetes Overview

**Kubernetes** (K8s) is an open-source system for automating deployment, scaling, and management of containerized applications. It groups containers that make up an application into logical units for easy management and discovery.

#### Key Features of Kubernetes

* **Container Orchestration**: Automatically places containers based on their resource requirements and other constraints while not sacrificing availability.
* **Service Discovery and Load Balancing**: Kubernetes can expose a container using the DNS name or using their own IP address. If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic so that the deployment is stable.
* **Storage Orchestration**: Kubernetes allows you to automatically mount a storage system of your choice.
* **Automated Rollouts and Rollbacks**: You can describe the desired state for your deployed containers using Kubernetes, and it can change the actual state to the desired state at a controlled rate.

### How Docker and Kubernetes Work Together

#### Complementary Technologies

Docker and Kubernetes are complementary technologies that can be used together to manage and scale containerized applications more efficiently than using either one alone.

1. **Containerization with Docker**: Docker provides the containerization technology through which you create containers. This includes packaging applications and their dependencies in Docker containers.
2. **Orchestration with Kubernetes**: Kubernetes manages these containers created by Docker. This includes deploying multiple instances of these containers, scaling them up or down, managing their lifecycle, and ensuring that they are running in a desired state.

#### Workflow Integration

Here’s how Docker and Kubernetes can be integrated in a typical workflow:

* **Development**: Developers write code on their local machines and use Docker to containerize the application. This includes defining a `Dockerfile` with the base image and dependencies.
* **Build and Test**: Docker builds the application into a container image. This image can then be tested to ensure it works as expected.
* **Deployment**: The Docker image is then pushed to a registry (like Docker Hub or a private registry).
* **Orchestration**: Kubernetes pulls the Docker image from the registry and deploys it across a cluster. Kubernetes handles the scheduling and running of containers on appropriate hosts in the cluster and manages the application’s availability and scalability.
* **Management**: Kubernetes provides load balancing, scaling, and monitoring, thus ensuring the application is healthy and meets load requirements.

#### Example Use Case

Consider a web application that needs to be highly available and scalable:

* Use Docker to containerize the web server, application code, and environment.
* Push the Docker container image to a registry.
* Use Kubernetes to pull the image and deploy it in a managed cluster. Kubernetes can manage multiple instances of this application, handle failover, provide service discovery, and scale the number of instances up or down based on traffic.
* Docker and Kubernetes together offer a powerful toolkit for deploying, managing, and scaling containerized applications. Docker simplifies the creation of container images and manages the application’s exact environment, while Kubernetes provides the framework to deploy and manage those containers at scale across a cluster of machines. This combination is essential for developing cloud-native applications that are scalable, resilient, and portable.
