# Billing

<!-- This page is the entry point of the billing documentation. -->

The billing team runs `billing-api`, which turns usage records into invoices and collects
payments. These pages describe how the monthly billing run works, how invoices are corrected and
what the on-call engineer of the billing team does when a payment provider fails.

![Flow of a usage record from the meter to the invoice](images/billing-flow.png)

## Monatlicher Abrechnungslauf

The billing run starts on the first day of every month at 02:00 UTC and creates one invoice per
customer from the usage records of the previous month. It runs for about two hours; invoices are
sent only after the whole run has finished, so a failed run never leaves some customers billed and
others not. Details on the invoices it creates are in [Invoices](invoices.md).

!!! note ""
    The run uses the exchange rates of the last working day of the previous month, never the
    rates of the day it runs on.

## Zahlungsläufe prüfen

After every billing run, check that the payment collection started for all invoices. The
dashboard of `billing-api` shows the number of invoices created and the number of payments
requested; the two numbers must match within an hour of the run. A gap means some payments were
not requested, and the [correction process][corrections] decides how to bill those customers.

<!--
Screenshot of the dashboard to follow once the new layout ships.
-->

![](images/dashboard.png)

???+ tip "Faster check"
    `billing-api check --run latest` compares both numbers and lists the invoices without a
    payment request.

## Who to contact

Questions about invoices go to the `#billing` channel. Customers never contact the billing team
directly; their requests reach the team through support, with a ticket that names the invoice
number. For anything that needs a correction, follow the [correction process][corrections]
instead of changing an invoice by hand.

[corrections]: invoices.md#correcting-an-invoice
