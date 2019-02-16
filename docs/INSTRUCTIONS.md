### Instructions

1. Clone repository `https://github.com/flatigal70/devops-challenge-igal.git`.
2. Download `env.zip` from the returning mail, unzip and launch it.
   Script will create `key` and `encripted` environmens.
3. Run `verification.sh` to test application.

To verify that CI/CD process work properly you can download docker from dockerhub
and run it:
1. `docker pull flatigal/devops-challenge-igal:latest`
2. `docker run -d -p 5000:5000 flatigal/devops-challenge-igal:latest`