# System design • Tooling

**Source:** https://aman.ai/sysdes/tooling/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Data](#data)
* [A/B testing](#ab-testing)
* [Load Balancers for Web Servers:](#load-balancers-for-web-servers)
* [Load Balancers for Databases:](#load-balancers-for-databases)
* [Offline testing](#offline-testing)
* [Cache](#cache)
* [Data prep](#data-prep)
  + [Feature store](#feature-store)
  + [Parquet](#parquet)
* [Model](#model)
* [Bloom filter](#bloom-filter)
* [Hyperparameter](#hyperparameter)
* [Database:](#database)
* [Queues:](#queues)
* [Application Server:](#application-server)
* [DNS server:](#dns-server)
* [CDN:](#cdn)
* [Web Server:](#web-server)
* [Spark:](#spark)
* [Combine data for teams:](#combine-data-for-teams)
* [ETL pipeline:](#etl-pipeline)

## Overview

* This page will go over tools needed to design a system

## Data

* Consent GDPR
* AWS Data Lake: Non-relational and relational from IoT devices, web sites, mobile apps, social media, and corporate applications

## A/B testing

* split.io
* weblab: internal tool
* Sagemaker:
  + A/B testing with Amazon SageMaker
* In production ML workflows, data scientists and engineers frequently try to improve their models in various ways, such as by performing hyperparameter tuning, training on additional or more recent data, or improving feature selection. Performing A/B testing on the new model and the old model with production traffic can be an effective final step in the validation process for a new model. In A/B testing, you test different variants of your models and compare how each variant performs relative to each other. If the new version delivers performance that is better or equal to the previously existing version, you replace the older model.
* Amazon SageMaker enables you to test multiple models or model versions behind the same endpoint using production variants. Each ProductionVariant identifies an ML model and the resources deployed for hosting the model. You can distribute endpoint invocation requests across multiple production variants by providing the traffic distribution for each variant or invoking a variant directly for each request. In the following sections, we look at both methods for testing ML models.
* Testing models by distributing traffic to variants
* To test multiple models by distributing traffic between them, specify the percentage of the traffic to route to each model by specifying the weight for each production variant in the endpoint configuration. Amazon SageMaker distributes the traffic between production variants based on the respective weights that you provided. This is the default behavior when using production variants. The following diagram shows how this works in more detail. Each inference response also contains the name of the variant that processed the request.
* split.io: A feature flagging and experimentation platform that enables A/B testing and feature rollouts.
* weblab: An internal tool for conducting A/B testing and experimentation within an organization.
* Sagemaker A/B testing: Amazon SageMaker provides A/B testing capabilities for testing multiple models or model versions behind the same endpoint. It allows data scientists and engineers to compare the performance of different model variants and validate new models.

## Load Balancers for Web Servers:

1. Nginx: Nginx is a powerful open-source web server and reverse proxy that can also be used as a load balancer. It supports various load balancing algorithms and can distribute client requests across multiple backend web servers, improving performance and scalability.
2. HAProxy: HAProxy is a widely used open-source load balancer that excels at handling high traffic and providing advanced load balancing features for web servers. It supports TCP and HTTP load balancing, and offers features like SSL termination, health checks, session persistence, and dynamic reconfiguration.
3. Apache HTTP Server with mod\_proxy\_balancer: Apache HTTP Server is a popular web server that can be configured as a load balancer using the mod\_proxy\_balancer module. It provides basic load balancing capabilities and can distribute client requests across multiple backend servers using various algorithms.

## Load Balancers for Databases:

1. ProxySQL: ProxySQL, mentioned earlier, can be used not only for database load balancing but also as a reverse proxy for web servers. It offers advanced load balancing capabilities specifically designed for databases, supporting query routing, connection pooling, and read/write splitting.
2. Pgpool-II: Pgpool-II, as mentioned earlier, is a load balancer and connection pooler for PostgreSQL databases. It provides load balancing of queries across multiple PostgreSQL servers, connection pooling, and features like replication and failover management.
3. Microsoft SQL Server Always On Availability Groups: Microsoft SQL Server offers its own built-in load balancing capabilities through Always On Availability Groups. It allows for the distribution of client connections and workload across multiple SQL Server replicas, ensuring high availability and scalability.
4. Amazon RDS Read Replicas: For cloud-based databases on Amazon RDS, read replicas can be used for load balancing read traffic. Amazon RDS automatically handles the load balancing of read queries across the replicas, providing scalability and performance improvements.

## Offline testing

* AIM.io framework
* Weights and Biases: A platform that helps track and visualize machine learning experiments, including offline testing and evaluation

## Cache

* Elasti Cache
* Amazon ElastiCache is a web service that makes it easy to deploy, operate, and scale an in-memory data store and cache in the cloud. The service improves the performance of web applications by allowing you to retrieve information from fast, managed, in-memory data stores, instead of relying entirely on slower disk-based databases. Amazon ElastiCache supports two open-source in-memory engines:
* Redis - a fast, open source, in-memory data store and cache. Amazon ElastiCache for Redis is a Redis-compatible in-memory service that delivers the ease-of-use and power of Redis along with the availability, reliability and performance suitable for the most demanding applications. Both single-node and up to 15-shard clusters are available, enabling scalability to up to 3.55 TiB of in-memory data. ElastiCache for Redis is fully managed, scalable, and secure - making it an ideal candidate to power high-performance use cases such as Web, Mobile Apps, Gaming, Ad-Tech, and IoT.
* Memcached - a widely adopted memory object caching system. ElastiCache is protocol compliant with Memcached, so popular tools that you use today with existing Memcached environments will work seamlessly with the service.
* Amazon ElastiCache automatically detects and replaces failed nodes, reducing the overhead associated with self-managed infrastructures and provides a resilient system that mitigates the risk of overloaded databases, which slow website and application load times. Through integration with Amazon CloudWatch, Amazon ElastiCache provides enhanced visibility into key performance metrics associated with your Redis or Memcached nodes.

## Data prep

* Apache Spark: A distributed data processing framework that enables large-scale data processing, including data preparation tasks like reading, transforming, and analyzing data stored in various formats.
* Amazon SageMaker Data Wrangler: A visual interface for data preparation that simplifies the process of exploring, cleaning, and transforming data. It integrates with other SageMaker tools and services to streamline the machine learning workflow.

* Data preparation is a crucial step in the data science workflow, and it involves transforming raw data into a format suitable for analysis and model training. AWS SageMaker Data Wrangler and Feature Store can be used together to facilitate data preparation tasks.

If your data is stored in a data lake in Parquet format, you can leverage SageMaker Data Wrangler to perform various data preparation operations.

### Feature store

* SageMaker feature store:
  + SageMaker Feature Store: A fully managed service that simplifies the storage, retrieval, and management of machine learning features. It supports batch and streaming ingestion, online and offline features, feature metadata and data cataloging, feature discovery and reuse, security and access control, and is fully managed.

### Parquet

## Model

* Train on notebook

## Bloom filter

## Hyperparameter

* Optuna: A hyperparameter optimization framework that automates the search for optimal hyperparameter configurations for machine learning models.

Certainly! Here’s a brief explanation of each technology mentioned:

## Database:

* **MySQL**: MySQL is an open-source relational database management system. It is known for its stability, performance, and ease of use. MySQL is widely used for various applications, from small-scale websites to large-scale enterprise systems.
* **PostgreSQL**: PostgreSQL is an advanced open-source relational database system. It offers features like ACID compliance, extensibility, and support for complex queries. PostgreSQL is highly customizable and suitable for applications that require robust data integrity and advanced functionality.
* **MongoDB**: MongoDB is a document-oriented NoSQL database. It stores data in flexible, JSON-like documents and provides high scalability and performance. MongoDB is often used in modern web applications and scenarios where flexible data models and horizontal scalability are essential.
* **Amazon RDS**: Amazon RDS (Relational Database Service) is a managed database service provided by AWS. It supports multiple database engines, including MySQL, PostgreSQL, Oracle, and more. RDS takes care of database administration tasks such as backups, patching, and replication, allowing developers to focus on application development.
* **Microsoft Azure SQL Database**: Azure SQL Database is a fully managed relational database service provided by Microsoft Azure. It offers high-performance, scalable, and secure database hosting. Azure SQL Database is compatible with SQL Server, making it easy to migrate existing applications to the cloud.

## Queues:

* **RabbitMQ**: RabbitMQ is an open-source message broker that implements the AMQP (Advanced Message Queuing Protocol) standard. It provides a reliable and scalable way to exchange messages between different systems or components asynchronously.
* **Apache Kafka**: Kafka is a distributed streaming platform designed for high-throughput, fault-tolerant messaging. It enables real-time data streaming and processing, making it suitable for scenarios like log aggregation, event sourcing, and stream processing.
* **Amazon Simple Queue Service (SQS)**: SQS is a fully managed message queuing service provided by AWS. It allows decoupling of application components by enabling asynchronous communication through message queues. SQS ensures message durability and provides high availability and scalability.
* **Microsoft Azure Service Bus**: Azure Service Bus is a fully managed enterprise message queuing service on Microsoft Azure. It offers reliable message storage and delivery, with features like queues and topics. Service Bus provides a flexible messaging infrastructure for building scalable and decoupled systems.

## Application Server:

* **Apache Tomcat**: Tomcat is an open-source Java application server that provides a runtime environment for Java-based web applications. It supports the Java Servlet, JavaServer Pages (JSP), and Java WebSocket technologies.
* **Nginx**: Nginx is a high-performance web server and reverse proxy server. It can handle high volumes of concurrent connections and is often used as a load balancer or for serving static content. Nginx is known for its efficiency and low resource consumption.
* **Microsoft IIS**: Internet Information Services (IIS) is a web server and application server provided by Microsoft. It is specifically designed for hosting ASP.NET applications and supports various web technologies, such as ASP.NET Core, PHP, and Node.js.
* **Node.js**: Node.js is a JavaScript runtime built on Chrome’s V8 JavaScript engine. It allows running JavaScript on the server-side, making it suitable for building scalable and efficient web applications. Node.js provides a non-blocking, event-driven architecture that enables high concurrency.

## DNS server:

* **BIND**: BIND (Berkeley Internet Name Domain) is an open-source DNS server software. It is one of the most widely used DNS server implementations and provides a robust and reliable DNS infrastructure. BIND supports features like zone transfers, DNSSEC (Domain Name System Security Extensions), and IPv6.
* **Microsoft DNS Server**: Microsoft DNS

Certainly! Here’s a brief explanation of each technology mentioned:

## CDN:

* **Cloudflare**: Cloudflare is a content delivery network (CDN) that helps improve the performance, security, and availability of websites and web applications. It works by caching static content at edge locations worldwide, reducing latency and improving load times for users across the globe. Cloudflare also provides DDoS protection, SSL/TLS encryption, and various optimization features.
* **Akamai**: Akamai is a leading global CDN provider that offers edge caching, content acceleration, and security services. Akamai’s vast network of servers helps deliver content efficiently, reduce latency, and handle high traffic loads. Additionally, Akamai provides features like DDoS protection, web application firewall, and content optimization tools.

## Web Server:

* **Apache HTTP Server**: Apache HTTP Server, often referred to as Apache, is the most widely used open-source web server software. It provides a robust and secure platform for hosting websites and web applications. Apache supports various modules and extensions, allowing customization and integration with different technologies.
* **Nginx**: Nginx, besides being a popular reverse proxy server, can also function as a web server. It is known for its high performance, scalability, and efficient handling of concurrent connections. Nginx is often used to serve static content, act as a load balancer, or as a reverse proxy in front of other web servers.
* **Microsoft IIS**: Internet Information Services (IIS) is a web server and application server provided by Microsoft. It is specifically designed for hosting websites and applications built on Microsoft technologies such as ASP.NET and .NET Core. IIS offers features like application pool management, request processing, and integration with other Microsoft technologies.

## Spark:

* **Apache Spark**: Apache Spark is an open-source distributed computing framework designed for big data processing and analytics. It provides an in-memory computing engine that allows for fast and scalable data processing across a cluster of machines. Spark supports various programming languages and offers libraries for batch processing, real-time streaming, machine learning, and graph processing.

## Combine data for teams:

* **Data Collaboration Platforms**: There are several data collaboration platforms available that enable teams to collaborate, share, and work together on data-related tasks. These platforms provide features like data sharing, version control, collaboration workflows, and access control. Examples include Databricks, Collabedit, and Dataiku.
* **Version Control Systems**: Version control systems like Git provide a way for teams to manage and collaborate on code and data. Teams can use Git repositories to share and track changes in data files, scripts, and other artifacts. Git also enables branching, merging, and conflict resolution, making it suitable for collaborative data workflows.
* **Data Catalogs**: Data catalogs help teams discover, organize, and collaborate on data assets. These tools provide a centralized repository where teams can document and share metadata, data definitions, and data lineage. Data catalogs also support search and exploration capabilities, making it easier for teams to find and access relevant data.

## ETL pipeline:

* **Apache Airflow**: Apache Airflow is an open-source platform for creating, scheduling, and monitoring data pipelines. It provides a rich set of features for defining workflows, managing dependencies, and executing tasks in a distributed manner. Airflow supports various data processing frameworks and allows for easy integration with other tools and services.
* **AWS Glue**: AWS Glue is a fully managed extract, transform, and load (ETL) service provided by Amazon Web Services. It simplifies the process of building and managing ETL pipelines by providing features like data cataloging, data transformation, and job orchestration. Glue integrates with other AWS services, making it a convenient choice for data pipelines on the AWS cloud

To go from a data lake to preprocessing data with Parquet and Spark, and then making embeddings with collaborative filtering, you can follow these steps using AWS tooling:

1. **Data Lake Setup**: Set up an AWS data lake using services like Amazon S3 to store your raw data. Create a bucket in S3 and organize your data in appropriate directories and files.
2. **Data Extraction**: Use AWS Glue, a fully managed extract, transform, and load (ETL) service, to extract data from various sources and load it into your data lake in S3. AWS Glue can handle diverse data sources, perform data discovery, and automatically generate and execute ETL code.
3. **Data Preprocessing with Spark**: Utilize Apache Spark, which integrates with AWS Glue, to preprocess the data stored in the data lake. Spark provides powerful data processing capabilities such as filtering, transformations, feature engineering, and aggregations. Use Spark to read the data from S3, perform preprocessing tasks, and prepare the data for collaborative filtering.
4. **Parquet Conversion**: Convert the preprocessed data into Parquet format using Spark. Parquet is a columnar storage format that provides efficient storage and processing of structured data. Write the preprocessed data as Parquet files to the S3 data lake using Spark’s Parquet read/write APIs.
5. **Matrix Factorization with Spark**: Use Spark’s machine learning library (MLlib) to perform matrix factorization on the Parquet data. MLlib provides implementations of matrix factorization algorithms such as Alternating Least Squares (ALS) for collaborative filtering. Load the Parquet data into Spark, apply the matrix factorization algorithm, and train a model to learn latent factors or embeddings for users and items.
6. **Embedding Generation**: Once the matrix factorization model is trained, use it to generate embeddings for users and items. These embeddings capture the underlying patterns and relationships in the data. You can extract the learned latent factors from the model for each user and item as the embeddings.
7. **Model Application**: Apply the generated embeddings for various tasks such as personalized recommendations, item similarity calculations, or other downstream applications. Use the embeddings to make predictions for new user-item interactions and provide personalized recommendations based on collaborative filtering.

In this workflow, AWS Glue is used for data extraction and integration, Spark is used for data preprocessing, Parquet conversion, and matrix factorization, and S3 serves as the storage for the data lake and Parquet files. Additionally, AWS SageMaker provides the Amazon SageMaker Factorization Machines algorithm, which can be used for matrix factorization on Parquet data at scale.

By combining AWS Glue, Spark, Parquet, and the appropriate machine learning algorithms, you can effectively go from a data lake to preprocessing data, perform matrix factorization on Parquet data, and generate embeddings for collaborative filtering using AWS tooling.
