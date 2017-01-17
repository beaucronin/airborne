# Airborne - real time flights

## Components

The fetcher is a lambda function that periodically fetches current flight info from the [Opensky Network](https://opensky-network.org/apidoc/index.html) and writes these flight states to Dynamo.

The provider is a [chalice](https://github.com/awslabs/chalice) microservice that serves these results on demand, with CORS enabled.

The infrastructure directory contains a simple [Terraform](https://www.terraform.io/) config to define the flight states Dynamo table.

## Deploy

- Install apex, chalice, terraform

- Deploy the fetcher lambda

```
cd fetcher
apex init
apex deploy
```

- Add dynamo db full access to lambda role

- Add CloudWatch timer trigger to lambda 

- Deploy the chalice microservice

```
cd provider
chalice deploy
```

## Possible extensions

- Use terraform to define CloudWatch event rule, Lambda trigger, Lambda role
- Store and display historical flight states, not just current


