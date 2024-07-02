---
type: periodical
layout: periodical_old
title: "Revuo Periodical #5"
date: "2021-03-01T11:07:56-07:00"
issuenumber: 5
covering: "January 1 - December 31, 2024"
---

<h3>Table of Contents:</h3>
<ul class="contents">
    <li><a href="#welcome">Welcome</a></li>
    <li><a href="#coreteamupdate">Core Team & Structural Updates</a></li>
    <li><a href="#development">Development Update</a></li>
    <li><a href="#mrl">Monero Research Lab Update</a></li>
    <li><a href="#community">Community Update</a></li>
    <li><a href="#monerospace">Monero Space Update</a></li>
    <li><a href="#mobile">Third-Party Apps & Services Update</a></li>
    <li><a href="#donate">Donate</a></li>
</ul>

<h3 id="welcome">Welcome</h3>

<p>Hello everyone and welcome to the fifth Monero periodical. In this issue we summarize the major developments of Monero in 2020. It’s been another amazing year, and we feel it’s important to celebrate our accomplishments as a community. Please note this list is not comprehensive, and there were many other things accomplished. These are just what we consider the highlights. So without further ado...</p>

<h3 id="coreteamupdate">Core Team & Structural Updates</h3>

<p>In September, Justin "sgp" Ehrenhofer and dEBRUYNE <a href="https://www.getmonero.org/2020/09/01/note-scheduled-upgrades.html" target="_blank">distributed a note about Monero scheduled protocol upgrades</a>. In Monero’s early years, required protocol upgrades occurred approximately every six months. Now that Monero is a larger project with more exchanges and wallets, this frequent upgrade schedule is more straining. Thus, Monero required protocol upgrades are now expected to occur approximately every nine to twelve months. This will allow for Monero to continue upgrading to the latest and greatest technology at a rapid pace while acknowledging the importance of ecosystem stability.</p>

<p>These future protocol upgrades will *not* include mining algorithm changes. RandomX, first implemented in November 2019, remains the CPU-friendly mining algorithm. It will remain this way unless ASICs pose a significant threat to the Monero network and widely push out CPU miners. However, RandomX’s success to date at limiting ASICs on the Monero network seems to be meeting expectations over a year later.</p>

<h3 id="development">Development Update</h3>

<a href="" target="_blank"></a>

<p>Monero had two major updates in 2020 (0.16 and 0.17) and a slew of minor point release updates following 0.17.</p>

<p>Monero 0.16 “Nitrogen Nebula” was the first ever major Monero release version that did not require a protocol upgrade. This version most importantly brought Dandelion++, a more private transaction broadcast method.</p>

<p>Monero 0.17 “Oxygen Orion” required a protocol upgrade and introduced CLSAGs. CLSAGs are a more efficient ring signature construction that reduce transaction size by about 25% and verification time by about 10%. <a href="https://www.getmonero.org/2020/07/31/clsag-audit.html" target="_blank">The CLSAG code implementation was audited by JP Aumasson and Antony Vennard</a>.</p>

<p>Following the 0.17 protocol upgrade, attackers performed a series of attacks targeting Dandelion++. This resulted in an enormous amount of developer work put into further hardening the Dandelion++ transaction propagation system. These network attacks have been largely mitigated, and no Monero was ever at risk.</p>

<h3 id="mrl">Monero Research Lab Update</h3>

<p>To start the year, Justin Ehrenhofer and Dr. Sarang Noether <a href="https://web.getmonero.org/2020/01/17/auditability.html" target="_blank">released a popular blog post explaining the nuances of supply auditability</a>. This explains the specific risks associated with select tradeoffs. Riccardo “fluffypony” Spagni later also spoke on this topic, further diving into the damages that even a detectable inflation bug would have on Bitcoin if it occurred today.</p>

<p>Sarang Noether <a href="https://eprint.iacr.org/2020/312, https://web.getmonero.org/2020/08/22/triptych.html" target="_blank">released a preprint of the Triptych-2 paper</a>: efficient proofs for confidential transactions.</p>

<p>koe, Kurt M. Alonso, and Dr. Sarang Noether <a href="https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf" target="_blank">released the second edition of Zero to Monero</a>. Zero to Monero is one of the leading resources that describes the Monero protocol.</p>

<p>MAGIC Grants started a <a href="https://charity.gofundme.com/o/en/campaign/dr-sarang-noether-to-implement-bulletproofs-in-monero" target="_blank">community crowdfunding campaign to hire Dr. Sarang Noether to work on Bulletproofs+ for Monero</a>. The campaign was successful and is one of the largest Monero community project raises outside of the Community Crowdfunding System (CCS). Monero community members donated to a CCS campaign to hire auditors of Bulletproofs+, with a second audit expected to begin shortly.</p>

<p>Lastly, Monero community member h4sh3d and a small team of developers had <a href="https://ccs.getmonero.org/proposals/h4sh3d-atomic-swap-research.html" target="_blank">funded the research phase of Bitcoin-Monero Atomic Swaps</a>. The research proved successful, and they <a href="https://ccs.getmonero.org/proposals/h4sh3d-atomic-swap-implementation.html" target="_blank">opened a second CCS that is now in progress for the implementation</a>. We expect to see this effort fully materialize in late 2021.</p>

<h3 id="community">Community Update</h3>

<p>Diego “rehrar” Salazar released a sticker pack for Isabella the Monero girl. It is available on <a href="https://t.me/addstickers/MoneroGirl" target="_blank">Telegram</a>, <a href="https://signal.art/addstickers/#pack_id=c7ddbbfc53c6d4a93fb9947626b8747b&pack_key=ac2999ee373b058fec9e41f1d7f6b4bc949815cc89f8868b1ab48615ca919c5f" target="_blank">Signal</a> and Matrix. It is one of the default <a href="https://matrix.org/blog/2020/03/13/this-week-in-matrix-2020-03-13#final-thoughts-" target="_blank">Element (Matrix)</a> sticker packs!</p>

<p>Several members of the Monero community created a documentary feature film about Monero that was the #1 film in the United States box office for two days. The film primarily features Dr. Daniel Kim and a presentation that he gave at the 36c3 conference. The novelty of the success garnered the film fame, including articles in several publications including Vice. It is one of the most-watched Monero videos to date. <a href="https://youtu.be/8quGD9W7B2I" target="_blank">Monero Means Money is available for free on YouTube</a>.</p>

<p>Every year on April 18, Monero celebrates its “Moneroversary.” For 2020, this virtual event featured <a href="https://www.youtube.com/watch?v=YigNWkXJk48" target="_blank">a deep dive into Monero’s history, a coffee chat, a game of trivia, and a meme contest</a>.</p>

<p>As before, the Monero Village <a href="https://www.youtube.com/playlist?list=PLsSYUeVwrHBn43BwoeplKKdJDFJFGH-9_" target="_blank">participated at DEFCON 28</a>, though of course the virtual event was very different than years prior. Monero remained the only cryptocurrency community with its own dedicated village. The Monero Village also participated in the Grayhat cybersecurity conference for the first time.</p>

<table class="hted-head">
  <tbody><tr class="row1">
    <th>Monero Outreach Update</th>
  </tr>
</tbody></table>

<p>Monero Outreach has started a “<a href="https://www.monerooutreach.org/we-accept-monero.html" target="_blank">We Accept Monero</a>” campaign for merchant adoption. </p>

<table class="hted-head">
  <tbody><tr class="row1">
    <th>Monero Talk Update</th>
  </tr>
</tbody></table>

<p>Monero Talk released 31 episodes over the course of 2020. The most popular episodes feature Dr. Daniel Kim, Riccardo “fluffypony” Spagni, and Roger Ver. <a href="https://www.youtube.com/channel/UC3Hx81QYLoEQkm3vyl4N4eQ" target="_blank">All episodes are free to watch on the Monero Talk website and on their YouTube</a>.</p>

<h3 id="monerospace">Monero Space Update</h3>

<p>In August, two Monero Community Workgroup organizers stepped down and started a separate workgroup called Monero Space. Monero Space is an active workgroup that is focused on projects and community infrastructure.</p>

<p><a href="https://youtu.be/w5rtd3md11g" target="_blank">Their new video content</a> includes interviews with Samourai Wallet, nothingmuch speaking about Wasabi Wallet, and Dave Jevans of CipherTrace. The Monero Coffee Chats, which were previously held approximately every four weeks for the past three years, are now organized by Monero Space under the new name Monero Meet. Monero Meets still air approximately every four weeks and cover largely the same topics.</p>

<p>Monero Space began offering community infrastructure, <a href="https://forum.monero.space" target="_blank">including a Flarum forum and a Nextcloud</a>.</p>

<h3 id="mobile">Third-Party Apps & Services Update</h3>

<p>Monero counts numerous third-party applications and services, each tailored to a specific need. In this section, we will focus on the most used ones that community members consider most trustworthy.</p>

<h5>Feather Wallet</h5>

<p>Several developers in the community released a new wallet called <a href="https://featherwallet.org" target="_blank">Feather Wallet</a>, which is still in beta. It features an Electrum-style user interface and several features not available in the official Monero GUI.</p>

<h5>Cake Wallet</h5>

<p><a href="https://cakewallet.io" target="_blank">Cake Wallet</a>  released their wallet for android in early 2020. It previously was only released on iOS. They’ve also redesigned their wallet to be even more user friendly.</p>

<h5>Monerujo</h5>

<p><a href="https://monerujo.io" target="_blank">Monerujo</a> revamped their user experience in October and improved their node selection and management process.</p>

<h3 id="donate">Donate</h3>

<p markdown="1">If you enjoy this publication and want to support it, we encourage you to donate to the Monero General Fund, using the following address:</p>

<p class="address" markdown="1">44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A</p>

<!--p><a href="monero:44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A" class="qr"><img src="/img/donate-monero.png"></a></p-->

Comments, criticism, complaints or corrections? Please contact rehrar at **rehrar** at **tuta.io**. Say rehrar sent you.
