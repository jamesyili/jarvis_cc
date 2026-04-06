# Primers • Data Drift

**Source:** https://aman.ai/primers/ai/drift/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Types of Data Drift](#types-of-data-drift)
  + [Covariate Drift (Feature Drift)](#covariate-drift-feature-drift)
  + [Concept Drift](#concept-drift)
  + [Prior Probability Drift (Label Drift)](#prior-probability-drift-label-drift)
  + [Feature Interaction Drift](#feature-interaction-drift)
* [Drift Detection/Monitoring](#drift-detectionmonitoring)
  + [Tests and Techniques](#tests-and-techniques)
    - [Practical Techniques to Measure Data Drift](#practical-techniques-to-measure-data-drift)
    - [Statistical Tests to Detect Data Drift](#statistical-tests-to-detect-data-drift)
    - [Libraries for Data Drift Detection](#libraries-for-data-drift-detection)
      * [Key Libraries and Tools](#key-libraries-and-tools)
      * [Criteria for Tool Selection](#criteria-for-tool-selection)
  + [AWS Services to Monitor, Detect, and Notify Stakeholders about Data Drift](#aws-services-to-monitor-detect-and-notify-stakeholders-about-data-drift)
    - [Amazon SageMaker Model Monitor](#amazon-sagemaker-model-monitor)
    - [AWS Config](#aws-config)
    - [Amazon CloudWatch](#amazon-cloudwatch)
    - [Amazon EventBridge](#amazon-eventbridge)
    - [Amazon Simple Notification Service (SNS)](#amazon-simple-notification-service-sns)
    - [Amazon S3](#amazon-s3)
    - [AWS Lambda](#aws-lambda)
    - [AWS Glue](#aws-glue)
    - [AWS Step Functions](#aws-step-functions)
    - [Amazon Kinesis](#amazon-kinesis)
    - [Example](#example)
* [References](#references)

## Overview

* Data drift refers to changes in the statistical properties of data over time, which can negatively impact the performance of machine learning models. It is a significant challenge in real-world machine learning systems, as models trained on historical data may fail to perform reliably when the underlying data distribution evolves.
* To maintain model reliability and performance, it is essential to understand the types of data drift and implement effective detection and monitoring techniques. By proactively addressing data drift, data scientists can build resilient models that adapt to changing environments, ensuring their long-term effectiveness.
* Not all drifts require model retraining or relabeling, but all require monitoring. By identifying and understanding the type of drift occurring, teams can implement the appropriate strategies to mitigate its effects. This could involve retraining with updated data, designing more robust features, or deploying monitoring systems to detect drift before it significantly impacts performance.
* Regular retraining plays a crucial role in mitigating the effects of distribution shifts by enabling models to adapt to evolving data patterns. Incorporating periodic retraining as part of the machine learning pipeline ensures that models remain aligned with current data distributions, reducing the risk of performance degradation over time.

## Types of Data Drift

### Covariate Drift (Feature Drift)

* **Definition**: The distribution of input features (\(P(X)\)) changes, but the relationship between the input features and target (\(P(Y \mid X)\)) remains constant.
* **Examples**:
  + A model trained on website traffic where the percentage of mobile users increases over time, altering feature distributions like screen size or click rates.
  + Predicting customer churn, where the distribution of customer demographics shifts.
  + Service launched in a new country or features missing unexpectedly.
* **Detection**:
  + Compare feature distributions between training and incoming data using statistical tests like the Kolmogorov-Smirnov test or Jensen-Shannon divergence.
* **Equation**:
  + If \(X\) is the set of features, then:
    \(P\_{\text{train}}(X) \neq P\_{\text{current}}(X)\)
* **Additional Considerations**:
  + Different features drift at different rates; for example, an app ranking may be useful for predicting downloads but can drift quickly.
  + In production, less accurate but more stable features may sometimes be preferable.

### Concept Drift

* **Definition**: The relationship between input features and the target (\(P(Y \mid X)\)) changes over time, even if \(P(X)\) remains unchanged.
* **Examples**:
  + A spam detection model: Spammers change strategies, altering the relevance of certain features like keywords.
  + Loan default prediction: Economic downturns or policy changes affect customer behavior.
  + Predicting life expectancy using geographic regions: as development levels change, the model’s predictive power diminishes.
  + Users searching for “Wuhan” pre- and post-Covid expect different outputs.
* **Detection**:
  + Track changes in model accuracy or loss over time.
  + Use metrics like Hellinger distance or Wasserstein distance on the conditional probability distributions.
* **Equation**:
  + If \(X\) represents features and \(Y\) the target, then:
    \(P\_{\text{train}}(Y|X) \neq P\_{\text{current}}(Y|X)\)
* **Additional Considerations**:
  + Concept drift can occur suddenly (e.g., new competitors, pricing policy changes, new memes) or gradually (e.g., changes in social norms, cultures, or languages).
  + It may also be cyclic, such as differences in ride-share demand between weekdays and weekends.

### Prior Probability Drift (Label Drift)

* **Definition**: The distribution of the target variable (\(P(Y)\)) changes while \(P(X \mid Y)\) remains constant.
* **Examples**:
  + A fraud detection system: The proportion of fraudulent transactions in the dataset increases due to better reporting.
  + Seasonal demand prediction: Sales for specific products change during different times of the year.
  + New or outdated classes emerge, especially in high-cardinality tasks (e.g., categorizing new diseases).
* **Detection**:
  + Compare the proportions of labels in the training data and new data using chi-squared tests.
* **Equation**:
  + If \(Y\) is the target variable:
    \(P\_{\text{train}}(Y) \neq P\_{\text{current}}(Y)\)

### Feature Interaction Drift

* **Definition**: Changes in the relationships or interactions between multiple features, even if their individual distributions remain the same.
* **Examples**:
  + A recommender system: The correlation between user preferences for two products changes due to a new marketing campaign.
  + Predicting house prices: The relationship between square footage and location shifts due to urban development.
* **Detection**:
  + Monitor pairwise correlations or mutual information between features in training and live data.
* **Equation**:
  + For features \(X\_1\) and \(X\_2\):
    \(P\_{\text{train}}(X\_1, X\_2) \neq P\_{\text{current}}(X\_1, X\_2)\)

## Drift Detection/Monitoring

* Model drifts are not uncommon, and several measures can be taken for monitoring:

  1. **Data Quality and Integrity Checks**:
     + Implement checks on feature collection and inference services to detect unexpected inputs or outcomes.
  2. **Manual Reviews**:
     + Maintain a hold-out set reviewed manually by stakeholder teams on a monthly or quarterly basis to detect changes in business models.
  3. **Automated Detection Using Classifiers**:
     + Combine training data (\(X\)) with pseudo-label 1 and production data (sampled similarly) with pseudo-label 0.
     + Fit a classifier and measure its ability to distinguish between the two datasets. A high separation ability (e.g., measured by [MCC](https://en.wikipedia.org/wiki/Matthews_correlation_coefficient)) indicates drift.
  4. **Kolmogorov–Smirnov Test**:
     + Netflix reportedly monitors drift using the Kolmogorov–Smirnov test, as shared at the Spark + AI Summit.
* By implementing these techniques, you can effectively identify and address data drift to maintain model performance in dynamic production environments.

### Tests and Techniques

* To effectively manage and maintain machine learning systems in production, detecting data drift is essential. This involves identifying deviations in data distributions and relationships that can impact model performance. The choice of test depends on the type of feature (categorical or continuous), the nature of the drift, and the domain requirements. Monitoring data drift should be an integral part of a machine learning system’s lifecycle, with automated alerts and regular retraining pipelines to address performance degradation. Statistical tests like the K-S test, chi-squared test, JSD, and PSI provide robust tools to identify and quantify data drift effectively.
* Below, we expand the initial discussion with a deeper dive into specific statistical tests, their mechanics, and practical implementations.

#### Practical Techniques to Measure Data Drift

* Effective measurement of data drift starts with selecting the right approach based on the problem’s complexity, including univariate, multivariate, or machine learning-based methods. These techniques enable teams to track shifts in feature distributions and interactions, ensuring timely interventions to maintain model reliability:

  1. **Univariate Analysis**:
     + Focuses on individual feature distributions.
     + Methods:
       - Histogram comparison.
       - Statistical tests (e.g., KS test, t-test).
  2. **Multivariate Analysis**:
     + Examines interactions between multiple features.
     + Methods:
       - Covariance matrix comparison.
       - Mutual information drift detection.
  3. **Machine Learning-based Approaches**:
     + Train a “drift detector” classifier to distinguish between training and live data.
     + Use metrics like area under the receiver operating characteristic curve (AUC-ROC).

#### Statistical Tests to Detect Data Drift

1. **Kolmogorov-Smirnov (K-S) Test**

   **Purpose**:

   * A non-parametric test to compare two probability distributions, assessing whether they originate from the same distribution.
   * Useful for detecting covariate drift in continuous features.

   **Mechanics**:

   * The K-S statistic measures the maximum absolute difference between the cumulative distribution functions (CDFs) of two datasets (\(F\_1(x)\) and \(F\_2(x)\)).
   * Null Hypothesis (\(H\_0\)): Both samples are drawn from the same distribution.

   **Equation**:
   \(D = \sup\_x |F\_1(x) - F\_2(x)|\)
   where \(F\_1(x)\) and \(F\_2(x)\) are the empirical CDFs of the two datasets.

   **Example**:

   * **Scenario**: A model predicting customer churn might experience changes in customer age distribution over time.
   * **Process**:
     1. Split the data into historical (training) and recent data.
     2. Compute the CDF for the age feature in both datasets.
     3. Calculate the \(D\)-statistic and p-value.
     4. If the p-value is below a predefined threshold (e.g., 0.05), reject \(H\_0\) and flag drift.

   **Implementation (Python)**:

   ```
   from scipy.stats import ks_2samp

   # Training and current data
   ks_statistic, p_value = ks_2samp(train_data['age'], current_data['age'])
   if p_value < 0.05:
       print("Significant drift detected in the 'age' feature.")
   ```
2. **Chi-Squared Test**

   **Purpose**:

   * Tests for independence between categorical variables or checks if the observed distribution of a feature matches the expected distribution.

   **Mechanics**:

   * Compares observed frequencies (\(O\)) with expected frequencies (\(E\)).
   * Null Hypothesis (\(H\_0\)): The observed and expected distributions are the same.

   **Equation**:
   \(\chi^2 = \sum \frac{(O\_i - E\_i)^2}{E\_i}\)

   **Example**:

   * **Scenario**: A loan default prediction model may experience shifts in the proportion of default and non-default labels.
   * **Process**:
     1. Count the frequencies of labels in training and live data.
     2. Compute the \(\chi^2\)-statistic and p-value.
     3. A low p-value indicates significant label drift.

   **Implementation (Python)**:

   ```
   from scipy.stats import chi2_contingency

   # Contingency table: rows=categories, columns=datasets
   contingency_table = [[train_data['label'].value_counts()[0], current_data['label'].value_counts()[0]],
                        [train_data['label'].value_counts()[1], current_data['label'].value_counts()[1]]]
   chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)
   if p_value < 0.05:
       print("Significant label drift detected.")
   ```
3. **Jensen-Shannon Divergence (JSD)**

   **Purpose**:

   * Measures the similarity between two probability distributions. A low JSD indicates similarity, while a high JSD signals drift.

   **Mechanics**:

   * Symmetrized and smoothed version of Kullback-Leibler (KL) divergence.
   * Always produces values in the range [0, 1].

   **Equation**:
   \(D\_{\text{JS}}(P || Q) = \frac{1}{2} D\_{\text{KL}}(P || M) + \frac{1}{2} D\_{\text{KL}}(Q || M)\)
   where \(M = \frac{1}{2}(P + Q)\).

   **Example**:

   * **Scenario**: Compare distributions of transaction amounts between training and live data.
   * **Process**:
     1. Create probability distributions for the feature (e.g., histograms).
     2. Compute the JSD.
     3. Monitor thresholds to flag drift.

   **Implementation (Python)**:

   ```
   from scipy.spatial.distance import jensenshannon

   # Histograms as probability distributions
   p_train, _ = np.histogram(train_data['amount'], bins=10, density=True)
   p_current, _ = np.histogram(current_data['amount'], bins=10, density=True)
   js_divergence = jensenshannon(p_train, p_current)
   if js_divergence > 0.1:
       print("Significant drift detected in 'amount' distribution.")
   ```
4. **Earth Mover’s Distance (EMD, Wasserstein Distance)**

   **Purpose**:

   * Quantifies the “effort” needed to transform one distribution into another, making it suitable for detecting drift in continuous variables.

   **Mechanics**:

   * Measures the minimum cost of transporting mass in one distribution to match another.

   **Example**:

   * **Scenario**: Monitor drift in product prices in an e-commerce dataset.

   **Implementation (Python)**:

   ```
   from scipy.stats import wasserstein_distance

   emd = wasserstein_distance(train_data['price'], current_data['price'])
   if emd > threshold:
       print("Significant drift detected in 'price' distribution.")
   ```

#### Libraries for Data Drift Detection

* Detecting data drift is a critical part of managing machine learning systems in production, as it ensures that models remain reliable and accurate in the face of changing data. In addition to statistical methods, a variety of tools and libraries are available to automate, visualize, and manage data drift detection. These tools simplify the implementation of drift detection techniques and integrate seamlessly into machine learning workflows.

##### Key Libraries and Tools

1. **Evidently AI**
   * **Overview**:
     Evidently AI is an open-source Python library designed for monitoring and analyzing data and model performance in production. It provides pre-built templates for drift detection and detailed visualizations.
   * **Features**:
     + Preconfigured reports for data drift, target drift, and feature importance drift.
     + Supports multiple drift detection methods, including statistical tests.
     + User-friendly visualizations for understanding drift metrics.
   * **Example Usage**:

     ```
     from evidently import ColumnMapping
     from evidently.dashboard import Dashboard
     from evidently.dashboard.tabs import DataDriftTab

     column_mapping = ColumnMapping()
     data_drift_dashboard = Dashboard(tabs=[DataDriftTab()])
     data_drift_dashboard.calculate(train_data, current_data, column_mapping=column_mapping)
     data_drift_dashboard.show()
     ```
2. **Alibi-Detect**
   * **Overview**:
     Alibi-Detect is a flexible library for outlier detection, adversarial example detection, and drift detection. It supports a variety of statistical and deep learning-based techniques.
   * **Features**:
     + Drift detection for both tabular and non-tabular data (e.g., images, text).
     + Includes advanced methods such as Maximum Mean Discrepancy (MMD) and Classification-based Drift Detection (C2ST).
     + Supports both offline and online drift detection scenarios.
   * **Example Usage**:

     ```
     from alibi_detect.cd import KSDrift

     detector = KSDrift(train_data.to_numpy())
     preds = detector.predict(current_data.to_numpy(), return_p_val=True)
     if preds['data']['p_val'] < 0.05:
         print("Drift detected.")
     ```
3. **Scikit-Multiflow**
   * **Overview**:
     A library tailored for data stream mining, scikit-multiflow provides tools for detecting concept drift, a specific type of data drift affecting model decision boundaries.
   * **Features**:
     + Focused on streaming data scenarios.
     + Implements drift detection algorithms like DDM (Drift Detection Method) and ADWIN (Adaptive Windowing).
   * **Example Usage**:

     ```
     from skmultiflow.drift_detection.adwin import ADWIN

     adwin = ADWIN()
     for sample in data_stream:
         adwin.add_element(sample)
         if adwin.detected_change():
             print("Change detected in data stream.")
     ```
4. **River**
   * **Overview**:
     River is a library for online machine learning, offering tools for continuous learning and drift detection.
   * **Features**:
     + Suitable for real-time environments.
     + Includes adaptive learning algorithms that handle drift automatically.
     + Detects both abrupt and gradual drift.
   * **Example Usage**:

     ```
     from river.drift import PageHinkley

     ph = PageHinkley()
     for x in data_stream:
         ph.update(x)
         if ph.drift_detected:
             print("Drift detected.")
     ```
5. **WhyLabs AI Observatory**
   * **Overview**:
     WhyLabs provides a managed platform for monitoring data quality and drift, with a focus on enterprise-level deployments.
   * **Features**:
     + Automatic drift detection and logging.
     + Supports integration with Python SDK and APIs for seamless monitoring.
     + Scalable for large datasets and pipelines.
6. **Deepchecks**
   * **Overview**:
     Deepchecks is an open-source library that helps validate and monitor machine learning models and datasets.
   * **Features**:
     + Prebuilt checks for data drift and model performance degradation.
     + Offers integration with most common machine learning libraries.
   * **Example Usage**:

     ```
     from deepchecks import Dataset
     from deepchecks.checks import TrainTestFeatureDrift

     train_ds = Dataset(train_data, label='target')
     test_ds = Dataset(current_data, label='target')
     drift_check = TrainTestFeatureDrift().run(train_ds, test_ds)
     drift_check.show()
     ```

##### Criteria for Tool Selection

* Choosing the right tool depends on several factors:
  + **Data Type**: Libraries like Alibi-Detect and River are well-suited for non-tabular and streaming data, respectively, while Evidently and Deepchecks excel with tabular data.
  + **Integration Needs**: For production systems, libraries with API support or managed platforms like WhyLabs offer seamless integration.
  + **User Expertise**: Evidently and Deepchecks provide user-friendly interfaces, whereas tools like Alibi-Detect may require more familiarity with statistical concepts.
* By leveraging these tools, organizations can establish robust data monitoring systems, ensuring that their machine learning models remain accurate and resilient in changing environments.

### AWS Services to Monitor, Detect, and Notify Stakeholders about Data Drift

* AWS offers a robust ecosystem of services that can be integrated to monitor, detect, and notify stakeholders about data drift in machine learning pipelines. From real-time monitoring and drift detection with SageMaker Model Monitor to infrastructure compliance via AWS Config to automating notifications and responses via CloudWatch, EventBridge, and SNS, stakeholders can be kept informed about drift events. These services enable users to ensure their models remain reliable and perform optimally as data distributions change over time.
* Below is a detailed explanation of the key AWS services and how they can be leveraged for this purpose.

#### Amazon SageMaker Model Monitor

* Amazon SageMaker Model Monitor is a specialized service designed to continuously monitor the quality of ML models in production. It can detect data drift, model drift, and other anomalies in input features or predictions.
* **Key Features**:
  + Detects changes in data distributions and model behavior.
  + Provides baseline constraints and compares them with live data.
  + Generates detailed reports and metrics.
* **Integration Steps**:
  1. **Set Up Baselines**:
     + Use historical training data to create baseline constraints (e.g., feature distributions, missing values).
  2. **Enable Monitoring Schedules**:
     + Configure monitoring jobs to run at specified intervals, evaluating incoming data against the baseline.
  3. **Notifications**:
     + When drift is detected, SageMaker Model Monitor integrates with Amazon CloudWatch to log metrics and trigger alarms.
     + Use CloudWatch alarms to publish notifications to Amazon SNS.
* **Example Use Case**:
  + Monitoring the distribution of age or income in a customer dataset for drift and sending alerts when the distribution deviates significantly from the training data.

#### AWS Config

* AWS Config tracks and records configuration changes in AWS resources and can also detect resource-level drift, ensuring compliance with specified rules. While not ML-specific, it plays a supporting role in monitoring changes to the underlying infrastructure or configurations.
* **Key Features**:
  + Detects drift in resource configurations (e.g., IAM roles, S3 bucket policies).
  + Supports rule-based notifications for non-compliance.
* **Integration Steps**:
  1. Define AWS Config rules for ML infrastructure, such as ensuring specific permissions or data storage configurations.
  2. Use Amazon SNS for notifications when drift or non-compliance is detected.
* **Example Use Case**:
  + Ensuring that an S3 bucket storing live data for a model maintains encryption and access policies as defined during training.

#### Amazon CloudWatch

* Amazon CloudWatch is a comprehensive monitoring and observability service that collects metrics, logs, and events from AWS resources and applications.
* **Key Features**:
  + Monitors system metrics (e.g., CPU, memory usage) and custom ML metrics (e.g., prediction accuracy, data drift).
  + Triggers alarms based on thresholds.
* **Integration Steps**:
  1. Publish custom metrics from SageMaker Model Monitor or other sources, such as data drift scores or feature statistics.
  2. Set alarms for drift thresholds.
  3. Configure notifications to stakeholders using Amazon SNS.
* **Example Use Case**:
  + Sending alerts when the Kolmogorov-Smirnov statistic for a feature exceeds a predefined threshold, indicating significant drift.

#### Amazon EventBridge

* Amazon EventBridge is a serverless event bus that connects applications using event-driven architectures.
* **Key Features**:
  + Routes events from AWS services (e.g., SageMaker, CloudWatch) to target services.
  + Filters and processes events in real time.
* **Integration Steps**:
  1. Configure SageMaker Model Monitor or AWS Config to send events to EventBridge.
  2. Set rules to detect specific events, such as a data drift alert.
  3. Route the events to targets like SNS (for notifications) or Lambda (for custom workflows).
* **Example Use Case**:
  + Automatically retraining a model using an AWS Lambda function triggered by a drift alert sent via EventBridge.

#### Amazon Simple Notification Service (SNS)

* Amazon SNS provides a fully managed messaging service for sending notifications to multiple subscribers, such as email addresses, mobile devices, or other services.
* **Key Features**:
  + Sends notifications to stakeholders about detected drift or related events.
  + Supports multiple delivery protocols, including email, SMS, HTTP, and AWS Lambda.
* **Integration Steps**:
  1. Create an SNS topic.
  2. Subscribe stakeholders (email addresses, Lambda functions) to the topic.
  3. Integrate the SNS topic with CloudWatch or EventBridge to trigger notifications.
* **Example Use Case**:
  + Sending an email to the data science team whenever data drift is detected in a monitored feature.

#### Amazon S3

* Amazon S3 is a storage service often used to store data for ML training and predictions. While it doesn’t directly detect drift, its logging and event notification capabilities are valuable in data pipelines.
* **Key Features**:
  + Enables logging of access and modification events.
  + Notifies stakeholders when data changes occur.
* **Integration Steps**:
  1. Enable S3 event notifications for data upload or modification.
  2. Route events to SNS or Lambda for further processing or analysis.
* **Example Use Case**:
  + Notifying stakeholders when new data is added to an S3 bucket, triggering data drift analysis.

#### AWS Lambda

* AWS Lambda provides serverless compute capabilities to execute custom workflows in response to events, such as drift detection.
* **Key Features**:
  + Executes custom logic for data processing or remediation.
  + Integrates seamlessly with EventBridge, CloudWatch, and SNS.
* **Integration Steps**:
  1. Create a Lambda function to analyze drift metrics or retrain a model.
  2. Trigger the function using events from SageMaker Model Monitor or EventBridge.
* **Example Use Case**:
  + Automating model retraining when significant drift is detected in input features.

#### AWS Glue

* AWS Glue is a data integration service that supports ETL workflows. While it doesn’t directly monitor drift, it can preprocess data and generate metrics for drift detection.
* **Key Features**:
  + Processes and cleans incoming data for drift monitoring.
  + Integrates with SageMaker for feature engineering.
* **Integration Steps**:
  1. Use Glue jobs to preprocess incoming data.
  2. Store processed data in S3 or feed it to SageMaker Model Monitor for drift analysis.
* **Example Use Case**:
  + Extracting and cleaning incoming transactional data before sending it to SageMaker for drift monitoring.

#### AWS Step Functions

* AWS Step Functions orchestrate workflows across multiple AWS services, enabling end-to-end automation.
* **Key Features**:
  + Combines SageMaker, Lambda, SNS, and EventBridge for drift detection workflows.
  + Handles branching logic for complex processes.
* **Integration Steps**:
  1. Create a Step Functions workflow to orchestrate drift detection, notification, and remediation.
  2. Include stages for SageMaker monitoring, SNS notifications, and Lambda-triggered retraining.
* **Example Use Case**:
  + A workflow that monitors data drift, sends alerts, and triggers model retraining in response to significant drift.

#### Amazon Kinesis

* Amazon Kinesis supports real-time data streaming, enabling continuous monitoring of live data for drift detection.
* **Key Features**:
  + Streams data from applications to SageMaker for real-time monitoring.
  + Handles high-throughput data streams.
* **Integration Steps**:
  1. Stream data to SageMaker Model Monitor using Kinesis Data Streams.
  2. Analyze the streamed data for drift and trigger alarms via CloudWatch or EventBridge.
* **Example Use Case**:
  + Monitoring real-time clickstream data for changes in user behavior and alerting stakeholders.

#### Example

* **Scenario**: Monitoring a production ML model for drift in customer demographic data.

1. **Data Ingestion**:
   * Use AWS Kinesis to stream incoming data to S3.
   * Use AWS Glue to preprocess the data.
2. **Drift Detection**:
   * Use AWS SageMaker Model Monitor to compare incoming data with baseline distributions.
   * Publish drift metrics to AWS CloudWatch.
3. **Event Handling**:
   * Use AWS EventBridge to route drift alerts to AWS SNS or Lambda.
4. **Notifications**:
   * SNS sends email notifications to the data science team.
5. **Automation**:
   * Lambda function triggers model retraining workflows if drift exceeds a threshold.

## References

* [Data Drift vs. Concept Drift: What Are the Main Differences?](https://deepchecks.com/data-drift-vs-concept-drift-what-are-the-main-differences/)
* [Matthews Correlation Coefficient](https://en.wikipedia.org/wiki/Matthews_correlation_coefficient)
