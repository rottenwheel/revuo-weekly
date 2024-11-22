---
type: weekly
layout: weekly

date: "2024-11-22T14:47:59-06:00"
issuenumber: 218
title: "Issue 218: November 7 - 21, 2024"
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
UnstoppableSwap GUI [v1.0.0-rc1](https://github.com/UnstoppableSwap/unstoppableswap-gui/releases/tag/v1.0.0-rc.1). If you are running an ASB: please upgrade as soon as possible. The update has already been rolled out to GUI users. They will not be able to initiate swaps with you until you do, since it introduces breaking changes on the network level.
{{% /newsbyte %}}

{{% newsbyte %}}
Cake v4.21.0 and Monero.com v1.18.0 [released](https://github.com/cake-tech/cake_wallet/releases/tag/v4.21.0); as well, they've published Cupcake v0.1.0, a companion application to have the ability to set up airgapped XMR wallets; a slew of bug fixes; and a new buy/sell workflow have been implemented. Worth noting: Cupcake is in beta and should be used with caution. Feedback is more than welcome! Cupcake's GitHub [repository](https://github.com/cake-tech/cupcake).
{{% /newsbyte %}}

{{% newsbyte %}}
Haveno DEX [v1.0.14](https://github.com/haveno-dex/haveno/releases/tag/1.0.14) with a few bug fixes; and offering the ability to reopen disputes until payout has been confirmed. Haveno Reto [v1.0.14](https://github.com/retoaccess1/haveno-reto/releases/tag/v1.0.14).
{{% /newsbyte %}}

{{% newsbyte %}}
Speaking of Haveno Reto... seems like moving forward we'll know them as [Reto Swap](https://nitter.poast.org/Reto_Swap/status/1859903768164532588) and v1.0.14 was the last release as Haveno Reto? We shall see.
{{% /newsbyte %}}

{{% newsbyte %}}
Monerod-GUI 'Tenacity' [v1.0.2](https://github.com/everoddandeven/monerod-gui/releases/tag/v1.0.2) deploying UI/UX fixes and enhancements; and upgrading/installing daemons effectively.
{{% /newsbyte %}}

{{% newsbyte %}}
[MoneroTopia](https://monerotopia.com/) was a success last weekend. Thanks to everyone who made it out to Huerto Roma Verde in Mexico city; congratulations to Douglas Tuman, Sunita, volunteers and everyone involved with the event.
{{% /newsbyte %}}

### Upcoming Events {#events}

{{% event "November 23, 2024 (Saturday) - 16:00 UTC" %}}
Community Workgroup Meeting - [#monero-community](irc://irc.libera.chat/#monero-community) IRC channel; Matrix [room](https://matrix.to/#/#monero-community:monero.social).
{{% /event %}}

{{% event "November 23, 2024 (Saturday) - 17:00 UTC" %}}
MoneroKon 5 Meeting - [#monerokon](irc://irc.libera.chat/#monerokon) IRC channel; Matrix [room](https://matrix.to/#/#monerokon:matrix.org).
{{% /event %}}

{{% event "November 25, 2024 (Monday) - 18:00 UTC" %}}
Monero Tech Meeting - [#no-wallet-left-behind](irc://irc.libera.chat/#no-wallet-left-behind) IRC channel; Matrix [room](https://matrix.to/#/#no-wallet-left-behind:monero.social).
{{% /event %}}

{{% event "November 26, 2024 (Tuesday) - 18:00 UTC" %}}
Cuprate Workgroup Meeting - [#cuprate](irc://irc.libera.chat/#cuprate) IRC channel; Matrix [room](https://matrix.to/#/#cuprate:monero.social).
{{% /event %}}

{{% event "November 27, 2024 (Wednesday) - 18:00 UTC" %}}
Research Lab Meeting - [#monero-research-lab](irc://irc.libera.chat/#monero-research-lab) IRC channel; Matrix [room](https://matrix.to/#/#monero-research-lab:monero.social).
{{% /event %}}

### CCS Proposal Ideas {#proposals}

Below you can find some CCS proposal ideas open for discussion.

{{% ccs_item link="https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/517" author="v1docq47" %}}
monerotopia 2024 voiceovers and working on xmr.ru
{{% /ccs_item %}}

{{% ccs_item link="https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/516" author="gingeropolous" %}}
1TB MRC upgrade 
{{% /ccs_item %}}

{{% ccs_item link="https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/506" author="SimplifiedPrivacy" last=1 %}}
Carrot animated video
{{% /ccs_item %}}

### CCS Proposals Need Funding

{{% ccs_item link="https://ccs.getmonero.org/proposals/monero-serai-wallet-audit.html" author="kayabaNerve" goal=1050 raised=0.8 %}}
Audit monero-serai and monero-wallet
{{% /ccs_item %}}

### Price & Blockchain Stats {#stats}

###### Blockchain Stats

{{< bc_stats
	height="3287218"
	hashrate="3.16 GH/s"
	txs_per_block="39.18"
	avg_txs_per_day="28637"
	block_reward="0.6"

	date="November 22, 2024"
>}}

###### XMR Blocks Distribution in last 1000 blocks

![Hashrate Pool Distribution Pie Chart](./hash.png)

###### Price & Performance

{{< price_performance
	market_cap="2,928,975,601"
	street_price="164.19"

	table_date="11/22/24"
	price_usd="158.74,+11.60,+2.00,-2.53"
	price_eur="152.41,+12.77,+5.60,+1.89"
	price_btc="0.001602,+2.79,-31.46,-63.05"

	date="November 22, 2024"
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
