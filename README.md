# Akto.io API Security


# What is Akto ?

[How it works](https://docs.akto.io/#how-it-works) • [Getting-Started](https://docs.akto.io/#how-to-get-started) • [API Inventory](https://docs.akto.io/api-inventory/api-collections) • [API testing](https://docs.akto.io/testing/run-test) • [Add Test](https://docs.akto.io/testing/test-library) • [Join Slack community](https://join.slack.com/t/aktocommunity/shared\_invite/zt-1nqfw3knb-XO\~r7UZyzD9f8\_Ddm4R1lg) •

Akto is a plug-n-play API security platform that takes only 60 secs to get started. Akto is used by security teams to maintain a continuous inventory of APIs, test APIs for vulnerabilities and find runtime issues. Akto offers tests for all OWASP top 10 and HackerOne Top 10 categories including BOLA, authentication, SSRF, XSS, security configurations, etc. Akto's powerful testing engine runs variety of business logic tests by reading traffic data to understand API traffic pattern leading to reduced false positives. Akto can integrate with multiple traffic sources - burpsuite, AWS, postman, GCP, gateways, etc.

Akto enables security and engineering teams to secure their APIs by doing three things:

1. [API inventory](https://docs.akto.io/api-inventory/api-collections)
2. [Run business logic tests in CI/CD](https://docs.akto.io/testing/run-test)
3. [Find vulnerabilities in run-time](https://docs.akto.io/api-inventory/sensitive-data)

## How it works?

Step 1: Create inventory

<figure><img src="https://2145800921-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRc4KTKGprZI2sPWKoaLe%2Fuploads%2FRXIYBFFP0cIi5gyJ02ZD%2FScreenshot%202023-01-26%20at%205.07.03%20PM.png?alt=media&token=d2976b86-d0cf-40f6-b17a-2611adceea05" alt=""><figcaption></figcaption></figure>

Step 2: Run tests

<figure><img src="https://2145800921-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRc4KTKGprZI2sPWKoaLe%2Fuploads%2FPBJv5INL2k1UZOUXPbOG%2FScreenshot%202023-01-26%20at%205.08.19%20PM.png?alt=media&token=511b637c-1558-434a-b606-7983d24006a9" alt=""><figcaption></figcaption></figure>

## How to get Started?

Local deploy:

Run this script to create Akto at ~/akto and run the docker containers. You'll need to have Docker installed in order to run the container. 

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/akto-api-security/infra/feature/self_hosting/cf-deploy-akto)"`

## License

This project is licensed under the [MIT License](LICENSE).
