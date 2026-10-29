# Invoices

An invoice lists the usage of one customer in one month, priced with the rates of the customer's
contract. Invoices are created by the monthly billing run and are never edited after they were
sent; a correction is always a new document.

## Correcting an invoice

A wrong invoice is corrected with a credit note that cancels it and a new invoice that replaces
it. Both are created with `billing-api correct --invoice <number>`, which asks for the reason and
the corrected usage. The customer receives both documents in one email, so they never see a credit
note without the replacement.

=== "Partial correction"

    Credit only the wrong positions and leave the rest of the invoice standing.

=== "Full correction"

    Credit the whole invoice and issue a new one with every position.

## Payment provider outages

When the payment provider is down, payment requests queue up in `billing-api` and are sent once
the provider answers again. Nothing has to be done by hand for outages shorter than a day. For
longer outages, follow the [on-call notes](notes/oncall.md#payment-provider-down), tell support
in advance, and check the [late fee rules](invoices.md#late-fees) before the queue is released.
Customers must not be charged twice: see the [refund process](refunds.md) and the general
[caution note](../shared/caution.md) for production changes.
