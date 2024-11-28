---
type: weekly
layout: weekly

date: "2024-11-28T12:44:39-06:00"
issuenumber: 219
title: "Issue 219: November 21 - 28, 2024"
---

### Table of Contents:

- [Recent News](#news)
- [Upcoming Events](#events)
- [CCS Proposals](#proposals)
- [Price & Blockchain Stats](#stats)
- [Volunteer Opportunities](#volunteer)
- [Support](#support)

### Recent News {#news}

{{% newsbyte %}}
Public remote nodes aggregator and monitor [xmr.ditatompel.com](https://xmr.ditatompel.com/) has implemented a slew of important changes to source code, such as: changing license from GLWTS to BSD-3-Clause, hoping to make it more accesible for others to use it and contribute to development; front-end layout improvements; support for IPv6 and I2P monitoring of remote nodes; and a hidden service for the web UI. GitHub [repository]; [.onion](http://xmrlist2ug5ypisuhsvsi2req4bc3uiv3nc24yzibbaztslqprchvcad.onion/) hidden service.
{{% /newsbyte %}}

{{% newsbyte %}}
MoneroPay [v2.7.0](https://gitlab.com/moneropay/moneropay/-/blob/master/CHANGELOG.md#270---2024-11-24) with wallet auto-creation if one has not been created while setting up; 0-confirmation fulfilled invoice support; and other miscellaneous improvements.
{{% /newsbyte %}}

{{% newsbyte %}}
Gupax [v1.3.10](https://github.com/hinto-janai/gupax/releases/tag/v1.3.10) removing some remote nodes; and making some UI enhancements.
{{% /newsbyte %}}

{{% newsbyte %}}
CypherStack published a review of the forthcoming XMR address scheme, CARROT. GitHub [repository](https://github.com/cypherstack/carrot-audit); [Carrot-final.pdf](https://github.com/cypherstack/carrot-audit/blob/main/latex/Carrot-final.pdf).
{{% /newsbyte %}}

{{% newsbyte %}}
MoneroKon C3 call for workshops/presentations is running! Deadline December 7th. Apply [today](https://pretalx.riat.at/38c3/submit/PVr4DB/info/), select *MoneroKon* as the `Track`. X [thread](https://xcancel.com/MoneroKon/status/1860321346380533986).
{{% /newsbyte %}}

### Upcoming Events {#events}

{{% event "November 30, 2024 (Saturday) - 17:00 UTC" %}}
MoneroKon 5 Meeting - [#monerokon](irc://irc.libera.chat/#monerokon) IRC channel; Matrix [room](https://matrix.to/#/#monerokon:matrix.org).
{{% /event %}}

{{% event "December 2, 2024 (Monday) - 18:00 UTC" %}}
Monero Tech Meeting - [#no-wallet-left-behind](irc://irc.libera.chat/#no-wallet-left-behind) IRC channel; Matrix [room](https://matrix.to/#/#no-wallet-left-behind:monero.social).
{{% /event %}}

{{% event "December 3, 2024 (Tuesday) - 18:00 UTC" %}}
Cuprate Workgroup Meeting - [#cuprate](irc://irc.libera.chat/#cuprate) IRC channel; Matrix [room](https://matrix.to/#/#cuprate:monero.social).
{{% /event %}}

{{% event "December 4, 2024 (Wednesday) - 18:00 UTC" %}}
Research Lab Meeting - [#monero-research-lab](irc://irc.libera.chat/#monero-research-lab) IRC channel; Matrix [room](https://matrix.to/#/#monero-research-lab:monero.social).
{{% /event %}}

### CCS Proposal Ideas {#proposals}

Below you can find some CCS proposal ideas open for discussion.

{{% ccs_item link="https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/517" author="v1docq47" %}}
monerotopia 2024 voiceovers and working on xmr.ru
{{% /ccs_item %}}

{{% ccs_item link="https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/506" author="SimplifiedPrivacy" last=1 %}}
Carrot animated video
{{% /ccs_item %}}

### CCS Proposals Need Funding

{{% ccs_item link="https://ccs.getmonero.org/proposals/monero-serai-wallet-audit.html" goal=1050 raised=752.67 %}}
Audit monero-serai and monero-wallet
{{% /ccs_item %}}

{{% ccs_item link="https://ccs.getmonero.org/proposals/gingeropolous_1TB_MRC.html" goal=20 raised=0.86 %}}
1TB MRC upgrade
{{% /ccs_item %}}

### Price & Blockchain Stats {#stats}

###### Blockchain Stats

{{< bc_stats
	height="3291468"
	hashrate="3.25 GH/s"
	txs_per_block="39.13"
	avg_txs_per_day="29381"
	block_reward="0.6"

	date="November 28, 2024"
>}}

###### XMR Blocks Distribution in last 1000 blocks

![Hashrate Pool Distribution Pie Chart](./hash.png)

###### Price & Performance

{{< price_performance
	market_cap="2,913,776,115"
	street_price="169.69"

	table_date="11/28/24"
	price_usd="157.91,-2.13,-3.41,-5.40"
	price_eur="149.63,-2.75,-1.11,-1.49"
	price_btc="0.001658,+0.65,-26.29,-62.07"

	date="November 28, 2024"
>}}

###### XMR Price Graph

![XMR Price Graph](./price.png)

Sources: [miningpoolstats.stream](https://miningpoolstats.stream/monero); [bitinfocharts.com](https://bitinfocharts.com/monero/); [coingecko.com](https://www.coingecko.com/en/coins/monero); [localmonero.co blocks](https://localmonero.co/blocks); [haveno.markets](https://haveno.markets/).

{{< volunteer >}}
{{% volunteer_item title="Test Monero Core Software" link="https://github.com/monero-project/monero" %}}
Anyone with moderate technical ability is encouraged to try to build and run Monero nightlies. Do not trust it with your Monero, but feel free to open an Issue on GitHub as problems arise. Instructions to build on your OS of choice can be found [here](https://github.com/monero-project/monero#compiling-monero-from-source). 
{{% /volunteer_item %}}
{{< /volunteer >}}

{{< support />}}
