---
type: weekly
layout: weekly

date: "2025-03-29T14:20:46-05:00"
issuenumber: 233
title: "Issue 233: March 23 - 30, 2025"
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
Monero 0.18.4.0 'Fluorine Fermi' Release has been [tagged](https://github.com/monero-project/monero/releases/tag/v0.18.4.0). Binaries and blog post containing release notes, A.K.A. changelog, to be expected in the next few days. Reach out to your preferred node operators and wallet developers in the meantime!
{{% /newsbyte %}}

{{% newsbyte %}}
Community members mondetta and Schmidt1024 launched [monero.eco](https://monero.eco/): a map or graph of Monero Ecosystem that aims to provide a visual overview, with web links to relevant XMR projects and services. [Repository](https://gitea.pro/schmidt1024/monero-ecosystem).
{{% /newsbyte %}}

{{% newsbyte %}}
MRL contributor Rucknium wrote a gist with a simulation of the risk of OSPEAD DSA deployment without a hard fork. Preliminary results are found [here](https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee). A newer, more fine-tuned estimate is to be expected in the forthcoming weeks.
{{% /newsbyte %}}

{{% newsbyte %}}
Feather Wallet [v2.8.0](https://featherwallet.org/changelog/) with a slew of UI/UX enhancements; dependencies upgrades; and Monero v0.18.4.0. [Download](https://featherwallet.org/download/).
{{% /newsbyte %}}

{{% newsbyte %}}
Cake v4.24.0 and Monero.com v1.21.0 [released](https://github.com/cake-tech/cake_wallet/releases/tag/v4.24.0) with Monero background sync (Android-only for now) and various UI enhancements, fixes. Feedback? [Here](https://forum.cakewallet.com/t/cake-wallet-introduces-decred-and-new-background-sync-for-monero-v4-24-0/151). Reddit [thread](https://redlib.zaggy.nl/r/Monero/comments/1jjplhe/cake_wallet_v4240_introduces_new_background_sync/).
{{% /newsbyte %}}

{{% newsbyte %}}
Recently launched Monero casino website xmr.gg enters maintainance mode for 4-7 weeks. Read the full announcement [here](https://xmr.gg/read-me).
{{% /newsbyte %}}

{{% newsbyte %}}
Monero Talk had XMRFamily on to talk about his experience as a peer-to-peer trader on LocalMonero, legal issues and potential arrests of traders. They talk about Haveno's volume; MAGIC Grants; and much more. Peep it: [Video](https://iv.0x7c0.com/watch?v=UasxQiesdUo); [Audio](https://www.monerotalk.live/monerotalk-345). Kuno [fundraiser](https://kuno.anne.media/fundraiser/hqlc/).
{{% /newsbyte %}}

### Upcoming Events {#events}

{{% event "March 31, 2025 (Monday) - 18:00 UTC" %}}
Monero Tech Meeting - [#no-wallet-left-behind](irc://irc.libera.chat/#no-wallet-left-behind) IRC channel; Matrix [room](https://matrix.to/#/#no-wallet-left-behind:monero.social).
{{% /event %}}

{{% event "April 1, 2025 (Tuesday) - 18:00 UTC" %}}
Cuprate Workgroup Meeting - [#cuprate](irc://irc.libera.chat/#cuprate) IRC channel; Matrix [room](https://matrix.to/#/#cuprate:monero.social).
{{% /event %}}

{{% event "April 2, 2025 (Wednesday) - 18:00 UTC" %}}
Research Lab Meeting - [#monero-research-lab](irc://irc.libera.chat/#monero-research-lab) IRC channel; Matrix [room](https://matrix.to/#/#monero-research-lab:monero.social).
{{% /event %}}

{{% event "April 5, 2025 (Saturday) - 17:00 UTC" %}}
MoneroKon 5 Meeting - [#monerokon](irc://irc.libera.chat/#monerokon) IRC channel; Matrix [room](https://matrix.to/#/#monerokon:matrix.org).
{{% /event %}}

### CCS Proposal Ideas {#proposals}

Below you can find some CCS proposal ideas open for discussion.

{{% ccs_item link="https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555" author="spirobel" %}}
Monero Browser Wallet
{{% /ccs_item %}}

{{% ccs_item link="https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538" author="napoly" %}}
Btcpayserver plugin
{{% /ccs_item %}}

### CCS Proposals Need Funding

{{% ccs_item link="https://ccs.getmonero.org/proposals/revuo-monero-maintenance-2025-q2.html" author="rottenwheel" goal=7 raised=0.02 %}}
Revuo Monero maintenance (2025 Q2)
{{% /ccs_item %}}

### Price & Blockchain Stats {#stats}

###### Blockchain Stats

{{< bc_stats
	height="3379365"
	hashrate="4.46 GH/s"
	txs_per_block="37.87"
	avg_txs_per_day="23891"
	block_reward="0.6"

	date="March 30, 2025"
>}}

###### XMR Blocks Distribution in last 1000 blocks

![Hashrate Pool Distribution Pie Chart](./hash.png)

###### Price & Performance

{{< price_performance
	market_cap="4,021,183,232"
	street_price="239.15"

	table_date="03/30/25"
	price_usd="218.00,+1.36,+2.32,+71.20"
	price_eur="201.32,+1.24,-2.00,+70.75"
	price_btc="0.002640,+4.48,+4.18,+44.87"

	date="March 30, 2025"
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
