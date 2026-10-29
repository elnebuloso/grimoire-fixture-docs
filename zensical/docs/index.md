---
title: Platform handbook
description: How the platform team runs its services, deploys and rollbacks.
tags:
  - platform
  - operations
---

# Platform

The platform team runs the shared services every product team builds on: authentication,
deployment tooling and the internal service mesh. This handbook covers how those services are
operated, how changes reach production and what to do when a change goes wrong.

## Getting access to the platform

New team members need an account in the identity provider and membership in the group
`platform-operators` before any `platformctl` command works. Ask your lead to file the request;
access is granted within one working day. The [auth service](auth-service.md) page describes how
the tokens behind that access are issued, and [rolling back a deploy](runbooks/rollback.md#rolling_back_a_deploy)
explains what the access is needed for most often.

## Installing platformctl

`platformctl` is the command line tool for every platform operation. Install it with the package
manager of your system and check the version afterwards; the tool refuses to run when it is more
than two minor versions behind the platform.

=== "Linux"

    ```sh
    curl -fsSL https://example.com/platformctl/install.sh | sh
    platformctl version
    ```

=== "macOS"

    ```sh
    brew install example/tap/platformctl
    platformctl version
    ```

## Where to ask for help

Questions about the platform go to the `#platform-help` channel, which the on-call engineer
watches during working hours. Outside working hours, page the on-call engineer only for incidents
that affect production; everything else waits for the next working day. See the
[glossary](glossary.md) for the terms the team uses, and the [service list](services.md) for who
owns what.
