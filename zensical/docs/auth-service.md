# Auth service

`auth-service` issues and checks the access tokens of every internal service. It runs in three
replicas behind the service mesh and keeps no state of its own besides its signing keys.

## Deploying the auth service

A new version of `auth-service` is deployed with `platformctl`. Deploy during working hours only,
because a broken release locks every operator out of the other services until it is rolled back.

--8<-- "shared/caution.md"

The commands for a deploy, a rollback and a status check:

```sh
--8<-- "shared/commands.md:3:5"
```

The deploy script in the platform repository does the same in two steps:

```python
--8<-- "shared/deploy.py:main"
```

## Ports of the platform services

Every platform service listens on a fixed port inside the mesh. Firewall rules and health checks
refer to these numbers, so a service never changes its port without a migration plan.

--8<-- "zensical/docs/snippets/ports.txt"

## Rotating the signing keys

The signing keys of `auth-service` are rotated every 90 days. The new key is published first and
used for signing only after every replica has loaded it, so tokens signed with either key stay
valid during the switch. The [rollback runbook](runbooks/rollback.md#when_to_roll_back) applies if
a rotation breaks token checks; the details of the switch are in
[key rotation](#rotating_the_signing_keys) above and in the
[token lifetime section](auth-service.md#token-lifetime).
