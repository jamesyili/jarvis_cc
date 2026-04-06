# Aman&#39;s AI Journal • Model Deployment

**Source:** https://aman.ai/primers/ai/model-deployment/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Model deployment](#model-deployment)
  + [Multi-Service Deployment](#multi-service-deployment)
  + [Blue-Green Deployment](#blue-green-deployment)
  + [Canary Deployment](#canary-deployment)
  + [A/B Test](#ab-test)
* [References](#references)

## Model deployment

* Deploying or upgrading services is risky. In this post, we explore risk mitigation strategies.
* The diagram below illustrates the common ones.

### Multi-Service Deployment

* In this model, we deploy new changes to multiple services simultaneously. This approach is easy to implement. But since all the services are upgraded at the same time, it is hard to manage and test dependencies. It’s also hard to rollback safely.

### Blue-Green Deployment

* With blue-green deployment, we have two identical environments: one is staging (blue) and the other is production (green). The staging environment is one version ahead of production. Once testing is done in the staging environment, user traffic is switched to the staging environment, and the staging becomes the production. This deployment strategy is simple to perform rollback, but having two identical production quality environments could be expensive.

### Canary Deployment

* A canary deployment upgrades services gradually, each time to a subset of users. It is cheaper than blue-green deployment and easy to perform rollback. However, since there is no staging environment, we have to test on production. This process is more complicated because we need to monitor the canary while gradually migrating more and more users away from the old version, i.e., performing a staged rollout.

### A/B Test

* In the A/B test, different versions of services run in production simultaneously. Each version runs an “experiment” for a subset of users. A/B test is a cheap method to test new features in production. We need to control the deployment process in case some features are pushed to users by accident.

## References

* [How to design Google Docs (Episode 4)](https://blog.bytebytego.com/p/how-to-design-google-docs-episode?s=r)
* [Shipping to Production by The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/shipping-to-production?s=r)
* [What Is Canary Testing? A Detailed Explanation](https://launchdarkly.com/blog/what-is-canary-testing-a-detailed-explanation/)
