---
type: periodical
layout: periodical_old
title: "Revuo Periodical #3"
date: "2019-09-14T11:07:56-07:00"
issuenumber: 3
covering: "January 1 - June 30, 2019"
---

<h3>Table of Contents:</h3>
<ul class="contents">
    <li><a href="#welcome">Welcome</a></li>
    <li><a href="#development">Development Update</a></li>
    <li><a href="#mrl">Monero Research Lab Update</a></li>
    <li><a href="#community">Community Update</a></li>
    <li><a href="#translations">Monero Localization Update</a></li>
    <li><a href="#mobile">Third-Party Mobile Update</a></li>
    <li><a href="#thanks">Special Thanks</a></li>
    <li><a href="#pdf">Download PDF</a></li>
    <li><a href="#donate">Donate</a></li>
</ul>

<h3 id="welcome">Welcome</h3>

<p>Hello everyone, and welcome to the third issue of the Monero Revuo. We pretty much dropped the ball on the 2018 quarterlies, but we’re picking it all back up with a 2019 first-half-year special. As always, we aim to give the community an update on the major developments from the primary workgroups in the Monero Project. This issue focuses on the Development, Research Lab, GUI, Community, third-party mobile, and Localization groups.</p>

<h3 id="development">Development Update</h3>

<p>Under the hood, Monero is a powerhouse of technology and code. Work on the code base is very versatile: it concerns maintaining the current code, fixing bugs, implementing innovations, etc. It is easy to get lost in all the developments of the past six months, but we’ll take a look at a few major development highlights, and what we may expect for the upcoming October protocol upgrade.</p>

<table class="hted-head">
  <tbody><tr class="row1">
    <th>Protocol Upgrade Summary</th>
  </tr>
</tbody></table>

<p>On March 9, 2019, Monero had its scheduled upgrade on block 1788000. The scheduled network upgrade introduced four major changes. First, the dynamic block size algorithm was adjusted to better accommodate short-term spending sprees while keeping long-term growth sensible. Second, a PoW tweak (CryptoNight-R) curbed the ASICs previously present on the network. Third, an encrypted payment ID was added to each transaction to improve transaction homogeneity. Fourth, the development team simplified amount commitments by shrinking the size of amount encodings and using deterministic masks. These changes made transactions smaller and were deemed safe to apply by the Monero Research Lab. Since the update, several major focus areas have received attention.</p>

<h5>RandomX</h5>

<p>RandomX is a PoW algorithm that has been in the works for over a year, and is set to replace CryptonightR to provide further ASIC resistance. RandomX is designed to render ASICs non-competitive and be “CPU-centric.” The core of RandomX is the concept of randomized execution. To put it simply, the developers want to execute a series of random instructions to take advantage of a general-purpose CPU’s flexibility with dynamic code execution. RandomX is Monero’s best attempt yet to preserve its promise of accessible mining. RandomX has been audited by four firms: TrailOfBits, X41, Kudelski, and Quarkslab. <a href="https://github.com/hyc/RandomxAudits" target="_blank">Each of these are publicly viewable on GitHub</a>.</p>

<h5>Blockchain Pruning</h5>

<p>One of the issues blockchain is facing today concerns scalability. One such way to help solve this is through blockchain pruning, which means removing unnecessary data from the blockchain after verification. This significantly reduces the size on disk. Monero recently added blockchain pruning to its daemon software, which reduces disk use by about two-thirds. While it is best for users to run full nodes, pruned nodes nevertheless are much better than running nothing at all, and they still contribute significantly to the network.</p>

<h5>Deterministic (reproducible) builds</h5>

<p>The CLI release binaries can now be verified via the deterministic build process. That is, users can build a binary themselves and verify that the hash matches the hash of the release binary published on the website. This vastly reduces the risk of Monero contributors concealing hidden code in published binaries. <a href="https://github.com/monero-project/monero/tree/master/contrib/gitian#gitian-building" target="_blank">Instructions can be found on GitHub</a>.</p>

<h5>Tor/i2p integration</h5>

<p>Due to knaccc/jgrassie's efforts (et al.), the Monero CLI tools now has support for tor/i2p, with the GUI implementation soon to follow. There are still many challenges ahead before this can happen, however, such as coming up with an intuitive interface for the networking options, effortless switching between the present options, as well as deciding on the bundling options of the networking software.</p>

<table class="hted-head">
  <tbody><tr class="row1">
    <th>GUI Update</th>
  </tr>
</tbody></table>

<p>Not only has the protocol changed, but a lot of work has been done on the Graphical User Interface (GUI) worked on by volunteers and stewarded by the Core Team. We summarize the major developments below, but there is an ongoing effort to make the Monero software as user-friendly as possible.
</p>

<p>The starting screens/startup wizards were  rebuilt from scratch, with the most notable change being the inclusion of simple mode. This new startup option was created to get new users up and going as quickly as possible by utilizing a simplified UI and connecting to a remote node by default. The GUI also saw new screens, such as a merchant page, which allows the GUI to be used as a point-of-sale system, as well as support for multiple accounts (made possible by subaddresses).</p>

<p>Another major success was the added ability for users to utilize the GUI with their Trezor hardware wallets. The last major inclusion is the new white theme designed by knufflebund. Users are given the option of whether to use the standard black theme, or toggle it to a brighter alternative.</p>

<p>Aside from these major additions, there were tweaks and improvements to several other screens, such as the address book and history page, as well as dramatic performance improvements.</p>

<h3 id="mrl">Monero Research Lab Update</h3>

<p>Keeping up with advances in the space, original research, testing implementations of improvements, providing privacy recommendations, and being the front line of defense against attacks are all part of the seemingly simple job that the Monero Research Lab is tasked with: making sure Monero remains at the forefront of privacy and blockchain technologies. In this section, we take a look at what the beginning of 2019 brings us - this section is led by Mitchell P. Krawiec-Thayer.</p>


<h5>Conferences and Payment IDs</h5>

<p>Back in January 2019, Monero Research Lab and several developers attended the Stanford Blockchain Conference. This conference explores the use of formal methods, empirical analysis, and risk modeling to better understand security and systemic risk in blockchain protocols. The same month they’ve discovered patterns in Monero nonces, due to varying search strategies employed by different miners.</p>

<p>A lot of discussion took place around deprecating or eliminating Payment IDs, due to privacy impacts and confusing UX. After much discussion, wallets hid this feature for the April update, and most wallets will completely remove the feature in the October update. Exchanges, payment processors, and other services should upgrade to support Monero subaddresses as soon as possible, which offer greater privacy and a better user experience.</p>

<h5>All the algorithms</h5>

<p>In March, the developers team had a special <a href="https://repo.getmonero.org/monero-project/monero-site/blob/b87354501b6343f9146f331805ddadc45696f728/_posts/2019-03-24-logs-for-the-dev-meeting-held-on-2019-03-24.md" target="_blank">2.5 hour developer meeting</a> to discuss proof of work algorithms. The same month, a Boron Butterfly Upgrade was made ahead of schedule (v0.14) to address <a href="https://www.reddit.com/r/Monero/comments/aj21yt/big_bang_attack_on_xmr/" target="_blank">dynamic blocksize algorithm</a> and the <a href="https://www.reddit.com/r/Monero/comments/agysnf/hashrate_discussion_thread/" target="_blank">suspected presence of ASICs</a> on the network. The PoW algorithm was tweaked to the <a href="https://github.com/monero-project/monero/pull/5126" target="_blank">CryptoNightR</a> variant with ASIC-incompatible random integer math. This caused a significant decrease in the <a href="https://www.coinwarz.com/network-hashrate-charts/monero-network-hashrate-chart" target="_blank">total hashrate</a> from approximately 1 GH/s to 200 MH/s. Developers also switched decoy selection algorithm to use the “output lineup” method.</p>

<h5>Ring Signature Optimizations and Replacement Candidates</h5>

<p>A lot of work has been performed by the Research Lab team in researching several new ring signature alternatives. These schemes include the likes of: <a href="https://eprint.iacr.org/2019/550" target="_blank">Spartan</a>, <a href="https://eprint.iacr.org/2019/508" target="_blank">RingCT3.0</a>, and <a href="https://lelantus.io/lelantus.pdf" target="_blank">Lelantus</a>. They have shared an analysis of Lelantus, including prototype code for Monero-to-Lelantus output migration, and plan on reviewing <a href="https://eprint.iacr.org/2019/580.pdf" target="_blank">Omniring</a> next, which would massively improve Monero’s privacy.</p>
<p>In addition to these reviews from external sources, MRL has been working up schemes of their own, which include the likes of <a href="https://eprint.iacr.org/2019/595" target="_blank">DLSAG</a> and CLSAG. DLSAG would enable non-interactive refund transactions for interoperable payment channels which would, in turn, enable second-layer solutions on Monero such as Lightning Network and atomic swaps. CLSAG (compact linkable spontaneous anonymous group) is a similar ring signature scheme to what is presently used, but is ~25% smaller and ~20% faster to verify transactions, all as a low-impact change.</p>

<h3 id="community">Community Update</h3>

<p>The Monero community is global, diverse, and full of initiative. It would be impossible to recount everything done by every member of the community for the betterment of the Monero Project, so we will just highlight a few things here. The Monero Project would like to extend a huge “Thank You!” to every contributing member of the Monero community. This section will cover activity from the Monero Community Workgroup, as well as other, external happenings of Monero in the wider world.</p> 

<table class="hted-head">
  <tbody><tr class="row1">
    <th>Breaking Monero & Coffee Chats</th>
  </tr>
</tbody></table>

<p> Justin 'sgp' Ehrenhofer and Diego ‘rehrar’ Salazar hold the Monero Coffee Chat every four weeks. Here, the community contributors join a livestreamed conversation to discuss the development, community projects, and events which have happened since the last Coffee Chat. They are available for viewing on the <a href="https://www.youtube.com/channel/UCKxLNPJeEjPXOke55i5AIXA" target="_blank">Monero Community Workgroup Youtube channel</a>, and they are excellent resources for getting a summary of the month’s activities and discussions.</p>

<p>In December, a video program “Breaking Monero” was introduced. It helps newbies to understand the weaknesses and flaws of Monero. While this might seem like a strange goal on the surface, it’s important to remember that only by highlighting and discussing these flaws can we hope to overcome them, both technologically and as a community. So far, the topics covered include: a ring signatures introduction, 0-decoy and chain reactions, chain splits (key image reuse attack), input selection algorithm, unusual ringsize, remote nodes, timing attacks, poisoned outputs (EAE attack), public mining pools, input/output metadata, and blockchain explorer opsec. These are also available for viewing on the Monero Community Workgroup YouTube channel. Moreover, there is other good news: <a href="https://www.monerooutreach.org/breaking-monero/" target="_blank">Breaking Monero series is fully transcripted by the Outreach workgroup</a>.</p>

<table class="hted-head">
  <tbody><tr class="row1">
    <th>Monero Talks</th>
  </tr>
</tbody></table>

<p>Another YouTube program which has sprouted since our last issue is Monero Talk is “Monero Talk”. Led by Doug and Sunita, and based in NYC, this channel has quickly become a staple in the community for interviewing various people of interest, both involved in Monero and otherwise. They’ve also been a part of providing coverage in various conferences where Monero has had a presence. A sampling of topics and guests for the last six months include:</p>

<ul>
    <li>"OpenBazaar & Monero a shared ethos w/ Brian Hoffman and Co”</li>
    <li>"Italian government to test a Monero based online voting system with Vincenzo Di Nicola, Calogero Mandracchia & Raffaele Nicodemo"</li>
    <li>"Is Monero digital cash? w/ Riccardo Spagni aka Fluffypony"</li>
    <li>"Lightning Network on Monero with Bernhard Breytenbach"</li>
    <li>Monero Talk with Howard Chu and Sam Williams of Arweave about RandomX progress</li>
</ul>

<table class="hted-head">
  <tbody><tr class="row1">
    <th>Monero Adoption</th>
  </tr>
</tbody></table>

<p>Adoption of Monero  as a payment method is becoming more and more widespread. A sample of related news is below (note: this is not a comprehensive list, and none should be considered endorsements):</p>

<h5>Wallets</h5>

<ul>
    <li>Exodus Desktop has started to support  XMR! The Monero coin has been added to Exodus Eden version 19.2.2.</li>
    <li>Exa Wallet released a multisig-focused mobile wallet for both Android and iOS. Stagenet and Mainnet are supported.</li>
    <li>Trust Wallet has added Monero.</li>
    <li>Coinomi added Monero as well.</li>
    <li>ZelCore (Multi-Asset Wallet)- now supports XRM.</li>
    <li>WooKey wallet - a new monero wallet, fully open source, for iOS and Android, which is available now.</li>
    <li>Guarda Wallet now supports XMR.</li>
</ul>

<h5>Exchanges</h5>

<ul>
    <li>Kucoin listed Monero. Cryptocurrency wallet Coindirect added Monero, so now it is possible to buy XMR for Euro in 20 European countries.</li>
    <li>The cryptocurrency exchange Huobi added XMR for trading.</li>
    <li>Binance added XMR/BNB and XMR/USDT trading pairs.</li>
    <li>Monero listed on Tokenomy Exchange (XMR/BTC).</li>
    <li>XMR perpetual swaps with 20x leverage are now available for trading on Delta Exchange.</li>
    <li>Poloniex added fiat deposits and withdrawals - Monero included (XMR/USDC pair is available on Poloniex)</li>
    <li>VARL.com now accepts Monero.</li>
    <li>XMR is now available through Faast API.</li>
</ul>

<h5>Businesses/Other</h5>

<ul>
    <li>Trezor.io now accepts payments in XMR via Globee.</li>
    <li>CoinLoan, a P2P lending platform for crypto-to-fiat loans, is now accepting Monero as collateral. The Estonian-based startup rolled out an update allowing to use privacy oriented coin Monero (XMR) to get credit in fiat currencies (USD, EUR, GBP, RUB) or stablecoins (TUSD, GUSD, USDC).</li>
    <li>XMR is now on all Freedom Gateway Machines.</li>
    <li>Monero is live now on a crypto asset broker Voyager.</li>
    <li>Astral AR and Core Scientific announced a partnership that puts Monero mining software on high-power safety drones.</li>
    <li>Bity, a Swiss brokerage, now provides an ability to buy or sell XMR at any of their 10  ATM locations throughout major cities in Switzerland.</li>
    <li>The Tor Project, a digital anonymity-focused nonprofit, is now accepting cryptocurrency donations directly, including Monero.</li>
</ul>

<table class="hted-head">
  <tbody><tr class="row1">
    <th>Other Community Events</th>
  </tr>
</tbody></table>

<p>On June 22-23, Brandon “suraeNoether” Goodell held a Monero Konferenco in Dever, Colorado. The two days were jam-packed with quality talks, content, and networking. <a href="https://www.youtube.com/playlist?list=PLsSYUeVwrHBkJHJg_l2uDgbicDJ1PmAVW" target="_blank">All talks can be viewed on the designated playlist of the Monero Community youtube channel</a>.</p>

<p>The electronic version of <a href="https://masteringmonero.com/" target="_blank">Mastering Monero</a> was released, and freely accessible to all (although a donation is recommended). It is a comprehensive guide on the world of Monero, progressing from a beginner’s introduction all the way to the privacy tech, and details of development.</p>

<p>The beloved Forum Funding System has finally retired (may the spam rest in peace), and has been replaced by the Community Crowdfunding System (CCS), which can be viewed at <a href="https://ccs.getmonero.org" target="_blank">ccs.getmonero.org</a>. Feel free to join, comment, discuss, and donate to proposals.</p>

<h3 id="translations">Monero Localization Update</h3>

<p>The Monero Localization Workgroup formed at the end of 2017 with the goal of translating Monero's community maintained materials. In the reviewed period, ErCiccione has led the localization team to translate Monerujo in Ukrainian, Esperanto, Catalan and Serbian. Check out the <a href="https://taiga.getmonero.org/project/erciccione-monero-localization/epic/162" target="_blank">list of available languages</a>, click on the one you speak and check if there is a task labelled "Needed". If there is none: good news, that language is updated and you can just help translating something else. If you find a Needed task, take a look at the very short <a href="https://github.com/monero-ecosystem/monero-translations/blob/master/translate-monerujo.md" target="_blank">step-by-step guide to add a new translation</a>.</p>

<p>Getmonero.org is now available in German, Russian, Turkish, and Chinese, and the GUI wallet has been translated into 9 new languages: Kurdish, Bengali, Persian, Irish, Urdu, Zulu, Greek, Nepali, Esperanto and Hindi. Just take a look at the <a href="https://translate.getmonero.org/projects/monero-gui/" target="_blank">list of languages available</a> and start translating the missing phrases/words of the language you speak. Once again, a short <a href="https://github.com/monero-ecosystem/monero-translations/blob/master/pootle.md" target="_blank">step-by-step guide with screenshots</a> is provided, which explains how to add a translation and how to review one. Be sure to give it a look!</p>

<h3 id="mobile">Third-Party Mobile Update</h3>

<p>The Monero ecosystem has several third-party wallets, and it would be a heavy task for the Revuo to report on all of them. That said, there are a few mobile wallets that have etched their way into the hearts and minds of the community, in large part due to their initiative and significant continued investment in Monero’s ecosystem. We will focus on Monerujo, Cake Wallet, and MyMonero in this issue.</p>

<table class="hted-head">
  <tbody><tr class="row1">
    <th>Monerujo</th>
  </tr>
</tbody></table>

<p><a href="https://monerujo.io" target="_blank">Monerujo’s</a> efforts are led by m2049r. There were two releases in this time period, with many interesting and necessary features such as the “Node-omatiC” feature, which allows users to automatically scan the network for high quality remote nodes, as well as Street Mode to hide your Monero balances while in public.</p>

<p>Not content with just working on the premiere Android wallet however, the Monerujo team has released several noob friendly articles (with illustrations!) to gently explain how some of the more advanced or confusing areas of Monero’s technology works. You can read these articles <a href="https://medium.com/@anhdres" target="_blank">on the Medium account of Monerujo team member anhdres</a>.</p>

<table class="hted-head">
  <tbody><tr class="row1">
    <th>Cake Wallet</th>
  </tr>
</tbody></table>

<p><a href="https://cakewallet.io" target="_blank">Cake Wallet</a> was founded by Vikrant Sharma, who moved to Monero after realizing Bitcoin’s lack of privacy, and understanding it could no longer meet his cryptocurrency needs. At the time, there was no available wallet for iOS, and so he decided to solve that problem, not just for himself, but for the community as a whole.</p>

<p>The largest features that went live in Cake Wallet were the complete redesign of the app as well as utilizing subaddresses for separate “Accounts” to be set by the user.</p>

<p>One of the features that Cake Wallet boasts is the ability to exchange cryptocurrencies from within the app, utilizing third party services such as XMR.to and MorphToken. The aforementioned release also added ChangeNow to this list as well, so users can shop around for the best rates from within the app.</p>

<table class="hted-head">
  <tbody><tr class="row1">
    <th>MyMonero</th>
  </tr>
</tbody></table>

<p><a href="https://mymonero.com" target="_blank">MyMonero</a> has been a staple in the Monero community for many years. Starting as a simple and easy-to-use web wallet, they have built and open sourced an underlying infrastructure for light wallets, as well as maintain a Javascript implementation of the Monero protocol.</p>

<p>Early in the year, the MyMonero team launched their long-awaited new apps for Desktop followed by iOS, as well as a new, related website and redesigned web wallet.</p>

<p>Despite these big achievements, the team was not content. They realized a large problem, common to all web wallets, and indeed websites as a whole, needed to be solved in order for users to feel truly safe when using browser based cryptocurrency wallets: compromised web resources (HTML,CSS, Javascript) leading to stolen funds.</p>

<p>After deliberation, building, and iterating, the MyMonero team revealed the end result at the Magical Crypto Con: <a href="https://securebrowse.gitlab.io/securebrowse/" target="_blank">SecureBrowse</a>, a security protocol that utilizes the existing DNS infrastructure to hash and sign their client-side resources for easy verification.
</p>

<h3 id="thanks">Special Thanks</h3>

<p>The Revuo Monero would like to thank Maria Vovchok for her work in tracking down, assembling, and writing the first draft of the issue, and Justin "sgp" Ehrenhofer for his review and comments.</p>

<h3 id="pdf">Download PDF</h3>

<p>Print-friendly version of this Periodical in the PDF format will be available soon..</p>

<h3 id="donate">Donate</h3>

<p markdown="1">If you enjoy this publication and want to support it, we encourage you to donate to the Monero General Fund, using the following address:</p>

<p class="address" markdown="1">44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A</p>

<!--p><a href="monero:44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A" class="qr"><img src="/img/donate-monero.png"></a></p-->

Comments, criticism, complaints or corrections? Please contact rehrar at **rehrar** at **tuta.io**. Say rehrar sent you.
