---
type: weekly
layout: weekly

date: "2024-10-24T23:52:27-05:00"
issuenumber: 215
title: "Issue 215: October 17 - 24, 2024"
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
XMRig [v6.22.1](https://github.com/xmrig/xmrig/releases/tag/v6.22.1).
{{% /newsbyte %}}

{{% newsbyte %}}
Monero contributor jeffro256 has published a MRL issue calling for discussion on the possiblity of retroactively ignoring the `unlock_time` field of transactions past some future block height, making the migration to FCMP++ tree building easier. GitHub [issue](https://github.com/monero-project/research-lab/issues/125); Lemmy [thread](https://monero.town/post/4726596).
{{% /newsbyte %}}

{{% newsbyte %}}
Cake v4.20.1 and Monero.com [v1.17.0](https://github.com/cake-tech/cake_wallet/releases/tag/v4.20.0) with LTC mimblewimble support; BIP32 wallet groups; XMR address handling refactor; and many more improvements under the hood.
{{% /newsbyte %}}

{{% newsbyte %}}
monerod GUI [v0.1.1-rc](https://github.com/everoddandeven/monerod-gui/releases/tag/v0.1.1-rc) with autostart/start at boot; native `.deb` package; general bug fixes; and upgraded dependencies.
{{% /newsbyte %}}

{{% newsbyte %}}
[!!] In just three (3) weeks, MoneroTopia is taking place! Join us for MoneroTopia 2024 down in Roma, Mexico City, November 14-17, 2024. Check the schedule and get your tickets over at [monerotopia.com](https://monerotopia.com/). Psst! You may use discount code: **Revuo24** to get 10% off your order!
{{% /newsbyte %}}

### Upcoming Events {#events}

{{% event "October 26, 2024 (Saturday) - 17:00 UTC" %}}
Community Workgroup Meeting - [#monero-community](irc://irc.libera.chat/#monero-community) IRC channel; Matrix [room](https://matrix.to/#/#monero-community:monero.social).
{{% /event %}}

{{% event "October 27, 2024 (Sunday) - 19:00 UTC" %}}
Monero Website Workgroup Meeting - [#monero-community](irc://irc.libera.chat/#monero-community) IRC channel; Matrix [room](https://matrix.to/#/#monero-community:monero.social).
{{% /event %}}

{{% event "October 28, 2024 (Monday) - 18:00 UTC" %}}
Monero Tech Meeting - [#no-wallet-left-behind](irc://irc.libera.chat/#no-wallet-left-behind) IRC channel; Matrix [room](https://matrix.to/#/#no-wallet-left-behind:monero.social).
{{% /event %}}

{{% event "October 29, 2024 (Tuesday) - 18:00 UTC" %}}
Cuprate Workgroup Meeting - [#cuprate](irc://irc.libera.chat/#cuprate) IRC channel; Matrix [room](https://matrix.to/#/#cuprate:monero.social).
{{% /event %}}

{{% event "October 30, 2024 (Wednesday) - 18:00 UTC" %}}
Research Lab Meeting - [#monero-research-lab](irc://irc.libera.chat/#monero-research-lab) IRC channel; Matrix [room](https://matrix.to/#/#monero-research-lab:monero.social).
{{% /event %}}

### CCS Proposal Ideas {#proposals}

Below you can find some CCS proposal ideas open for discussion.

{{% ccs_item link="https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/506" author="SimplifiedPrivacy" %}}
Carrot animated video
{{% /ccs_item %}}

{{% ccs_item link="https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/495" author="DiosDelRayo" %}}
Offline Signing Library for XmrSigner Production
{{% /ccs_item %}}

### CCS Proposals Need Funding

{{% ccs_item link="https://ccs.getmonero.org/proposals/VOSTOEMISIO-FCMP-Animated-Explainer.html" author="VOSTOEMISIO" goal=20 raised=10.04 %}}
FCMP Animated Explainer Video
{{% /ccs_item %}}

### Price & Blockchain Stats {#stats}

###### Blockchain Stats

{{< bc_stats
	height="3266566"
	hashrate="2.94 GH/s"
	txs_per_block="32.10"
	avg_txs_per_day="23143"
	block_reward="0.6"

	date="October 25, 2024"
>}}

###### XMR Blocks Distribution in last 1000 blocks

![Hashrate Pool Distribution Pie Chart](./hash.png)

###### Price & Performance

{{< price_performance
	market_cap="2,925,817,960"
	street_price="155.56"

	table_date="10/25/24"
	price_usd="158.71,+0.39,-5.38,+0.94"
	price_eur="146.65,+0.54,-2.09,-1.10"
	price_btc="0.002345,+0.19,-9.98,-49.31"

	date="October 25, 2024"
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
