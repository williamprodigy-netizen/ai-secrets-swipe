#!/usr/bin/env python3
"""Build the AI Secrets Challenge (Russell Brunson) swipe site.

Run: python3 build_site.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/AI_SECRETS_Swipe")
tx = sorted(glob.glob(os.path.join(PKG, "Transcript/aisecrets_*.md")))

CONFIG = {
    "SITE": "AI Secrets Challenge — Russell Brunson & Todd Dickerson",
    "CREATOR": "AI Secrets Challenge",
    "ADS_KEY": "ai_secrets",
    "FUNNEL_IDS": ["F118"],
    "CAPTURED": "31 July 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/AI_SECRETS_Swipe",
    "BLURB": "The ClickFunnels founders running a five-day live challenge, Aug 3&ndash;7. "
             "A segmentation quiz gates the opt-in and then <b>personalises the VIP pitch by "
             "name of segment</b>. VIP is given away at $0 rather than sold &mdash; the whole "
             "funnel optimises for attendance, not front-end cash.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("transcripts.html", "Transcripts"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("VIP price", "$97 &rarr; $0"),
        ("Dates", "Aug 3&ndash;7"),
        ("Daily", "11:00 AM PT"),
        ("Per day", "90 min"),
        ("Registered", "2,745"),
        ("Platform", "Zoom"),
        ("VIP timer", "20 min"),
        ("Captured", "7m 01s"),
    ],

    "OFFER": [
        ("Product", "AI Secrets Challenge &rarr; his AI platform"),
        ("Hosts", "Russell Brunson &amp; Todd Dickerson, ClickFunnels co-founders"),
        ("Big idea", "&ldquo;The Future Belongs To The One-Person Company&rdquo;"),
        ("Positioning", "&ldquo;AI just made most online businesses disposable. Here's how to "
                        "build the one kind AI can't touch.&rdquo;"),
        ("Core claim", "The secret to AI is not more capability, it is <b>better constraints "
                       "and guardrails</b>"),
        ("Mechanism", "Software that executes the frameworks from DotCom Secrets, Expert "
                      "Secrets and Traffic Secrets &mdash; e.g. Dream 100 automated"),
        ("Entry", "Free. Segmentation quiz, then name / email / phone"),
        ("VIP", "<b>$97 marked to $0</b> with a 20-minute countdown"),
        ("Consent field", "<code>aisc_bot_calling_checkbox</code> &mdash; opt-in to AI-generated "
                          "voice calls, explicitly not required to attend"),
        ("Entity", "Marketing Secrets LLC, Eagle, Idaho"),
    ],

    "FINDINGS": [
        ("The quiz personalises the next video",
         "The opt-in opens with &ldquo;Which One Best Describes You?&rdquo; Brunson's VIP video "
         "then opens: <i>&ldquo;on the last page you told me that you are a bootstrap founder or "
         "CEO, kind of like me.&rdquo;</i> The segmentation answer is spoken back at the "
         "prospect inside the very next asset. Cheap to build, and it makes a recorded video "
         "feel addressed to one person."),
        ("Two identities caught a live split test",
         "Registering twice surfaced <b>two different VIP pages</b>: the first identity "
         "(31 July) was sent to <code>/vip-upgrade</code>, the second (1 August) to "
         "<code>/vip</code>. A single registration would have reported one of them as "
         "<i>the</i> page. This is the whole argument for the second-identity pass."),
        ("VIP is free, on purpose",
         "$97 struck to $0 on a 20-minute timer. Jordan Lee and Miss Affiliate both charge $27 "
         "for the same slot. Brunson is buying attendance and commitment rather than front-end "
         "cash, because the money is on day five."),
        ("Constraints, not capability",
         "&ldquo;The real secret to making AI work isn't more capability. It's better "
         "constraints, better guardrails. Without it, it's just expensive noise that changes "
         "every three months.&rdquo; He reframes the entire AI category away from tool-chasing "
         "and toward his frameworks &mdash; which conveniently he already owns."),
        ("Tool fatigue as the enemy",
         "He names the real pain precisely: learning a tool, a better one launching, switching "
         "again, and nothing in the business actually getting built. That is a far sharper "
         "villain than &ldquo;you're not using AI&rdquo;."),
        ("The books become software",
         "Every framework from his three books is turned into a platform feature. Dream 100 "
         "finds thousands of partners in seconds and pulls their contact details. He is "
         "converting a decade of owned IP into recurring software revenue."),
        ("Same operator as the Secrets of Propaganda VSL",
         "Already in the registry as F073. Worth cross-reading the two funnels for shared "
         "structure."),
    ],

    "FUNNEL": [
        ("Registration + quiz", "aisecretschallenge.com",
         "&ldquo;Which One Best Describes You?&rdquo; segments before it asks for anything."),
        ("Popup form", "aisecretschallenge.com/#open-popup",
         "Name, email, <b>phone</b>, plus <code>aisc_bot_calling_checkbox</code>."),
        ("VIP upgrade", "aisecretschallenge.com/vip-upgrade",
         "$97 &rarr; $0, 20-minute timer, 7m01s personalised pitch video."),
        ("Live sessions", "Zoom, Aug 3&ndash;7, 11:00 AM PT",
         '<span class="tag good">genuinely live</span> — registered, needs capture on the day'),
    ],

    "TRANSCRIPT_GROUPS": [("Captured video", tx)],
    "SLIDE_PAGES": [],

    "VIDEOS": [
        ("aisecrets_vip.mp4", 436, "181 MB",
         "The personalised VIP upgrade pitch. Voomly-hosted."),
    ],

    "ANALYSIS": """
<div class="note"><b>The mechanic worth stealing.</b> A one-question segmentation quiz before
the opt-in, whose answer is then spoken back to the prospect in the next video. Our masterclass
registration asks nothing and personalises nothing.</div>

<h2 class="sec">How the VIP video is built</h2>
<div class="tablewrap"><table>
<tr><th>Time</th><th>Beat</th><th>What he is doing</th></tr>
<tr><td>00:00</td><td>Callback</td><td>Names the segment the prospect selected on the previous page</td></tr>
<tr><td>00:20</td><td>Credential</td><td>Bootstrapped ClickFunnels without outside capital &mdash; matched to that segment</td></tr>
<tr><td>01:01</td><td>Villain</td><td>Tool fatigue: learn one, a better one ships, switch, nothing gets built</td></tr>
<tr><td>01:40</td><td>Reframe</td><td>&ldquo;Not more capability &mdash; better constraints&rdquo;</td></tr>
<tr><td>02:43</td><td>Mechanism</td><td>The platform turns his three books into software that executes</td></tr>
<tr><td>03:00+</td><td>Proof</td><td>Dream 100 finds thousands of partners in seconds</td></tr>
</table></div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Segment, then speak it back</h3><p>One question on the opt-in, answer
referenced by name in the next video. Even with three recorded variants it reads as personal,
and it tells you which lane every lead is in before a setter ever opens a thread.</p></div>
<div class="card"><h3>Give the upgrade away</h3><p>He is the only one of the seven who does not
charge for VIP. Commitment without a payment barrier, and show rate is the metric he is buying.
That is the same metric we are trying to move.</p></div>
<div class="card"><h3>Name the villain precisely</h3><p>Not &ldquo;you're behind on AI&rdquo;
but &ldquo;you keep switching tools and nothing gets built.&rdquo; Ours should be equally
specific about what the creator actually keeps doing wrong.</p></div>
<div class="card"><h3>Turn owned IP into the mechanism</h3><p>Three books become platform
features. Our Hybrid Model is the equivalent asset and is currently explained rather than
operationalised.</p></div>
</div>

<h2 class="sec">Open</h2>
<p>The five sessions run 3&ndash;7 August at 11:00 AM PT on Zoom. Genuinely live, so a cron
sniff will not capture them. Price and the day-five pitch are unobserved.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
