#!/usr/bin/env python3
"""AI Secrets Challenge — the whole business, wired.

Run: python3 build_board.py  ->  board.html
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from boardbuild import build, X

REPO = os.path.dirname(os.path.abspath(__file__))
S = os.path.expanduser("~/UNDERGROUND_FUNNELS_SSOT/01_RAW_FUNNELS")
P = f"{S}/AI_Secrets_Challenge - AI_Secrets_Challenge_5-day - 2026-07-31/02_Pages"

CONFIG = {
    "OUT": os.path.join(REPO, "board.html"),
    "KICK": "Competitor swipe · captured 31 July 2026",
    "TITLE": "AI Secrets Challenge — the whole business, wired",
    "BLURB": "Russell Brunson and Todd Dickerson running a five-day live challenge, 3&ndash;7 "
             "August. A segmentation quiz gates the opt-in and its answer is spoken back inside "
             "the very next video. VIP is given away at <b>$0</b> &mdash; the only one of the "
             "seven that does not charge for the post-optin slot.",

    "SHOTS": {
        "reg": {
            "col": 1, "y": 120, "lane": "event", "step": "Entry · quiz first",
            "title": "Registration + segmentation quiz",
            "url": "aisecretschallenge.com",
            "img": f"{P}/01_Registration/20260731T152120Z__screenshot_fullpage.png",
            "max_h": 1100,
            "note": "&ldquo;AI just made most online businesses disposable.&rdquo; Opens with "
                    "<b>&ldquo;Which One Best Describes You?&rdquo;</b> before it asks for "
                    "anything. 2,745 registered for the live event.",
        },
        "vip": {
            "col": 3, "y": 120, "lane": "back", "step": "Upsell",
            "title": "VIP upgrade — $97 &rarr; $0",
            "url": "aisecretschallenge.com/vip-upgrade",
            "img": f"{P}/02_VIP_upgrade_97_-_0/20260731T152557Z__screenshot_fullpage.png",
            "max_h": 1100,
            "note": "&ldquo;You'll see this video once &mdash; press play now.&rdquo; "
                    "20-minute countdown on a <b>free</b> upgrade.",
        },
    },

    "DATA": {
        "form": {
            "col": 2, "y": 120, "lane": "event", "step": "Capture",
            "title": "The popup form",
            "kv": [("Name", "required"), ("Email", "required"),
                   ("Phone", "required"),
                   ("Checkbox", "<code>aisc_bot_calling</code>"),
                   ("Covers", "AI-generated voice"),
                   ("Required?", "explicitly no")],
            "note": "The consent box opts you into automated and AI-voice calls. Their own copy "
                    "says consent is not required to attend, so it was left unticked.",
        },
        "pitch": {
            "col": 4, "y": 120, "lane": "ever", "step": "VIP video",
            "title": "The personalised pitch — 7m 01s",
            "kv": [("Host", "Voomly"), ("Words", "1,701"),
                   ("Opens with", "your quiz answer"),
                   ("Villain", "tool fatigue"),
                   ("Reframe", "guardrails &gt; capability"),
                   ("Mechanism", "3 books as software")],
            "note": "&ldquo;On the last page you told me that you are a bootstrap founder or "
                    "CEO, kind of like me.&rdquo;",
        },
        "event": {
            "col": 5, "y": 120, "lane": "event", "step": "The challenge",
            "title": "Five days — not yet captured",
            "kv": [("Dates", "Mon 3 &ndash; Fri 7 Aug"),
                   ("Time", "11:00 AM PT"),
                   ("Length", "90 min/day"),
                   ("Platform", "Zoom"),
                   ("Registered", "yes"),
                   ("Price", "not yet observed")],
            "note": "Genuinely live. A cron sniff will not capture Zoom &mdash; this needs a "
                    "human on the call, or a replay.",
        },
    },

    "EDGES": [
        ("reg", "form"), ("form", "vip"), ("vip", "pitch"), ("pitch", "event"),
    ],

    "LABELS": [
        {"x": X[1], "y": 60, "t": "Challenge funnel — quiz-gated"},
        {"x": X[1], "y": 1700, "t": "Routing logic"},
    ],

    "BRANCH": [
        {"id": "b_quiz", "x": X[1] + 10, "y": 1760, "state": "yes",
         "cond": "Picks a segment → the next video names it back",
         "body": "The quiz asks &ldquo;Which One Best Describes You?&rdquo; with options like "
                 "<i>I'm a founder, coach, or consultant</i>. Brunson's VIP video then opens "
                 "<b>&ldquo;on the last page you told me that you are a bootstrap founder or "
                 "CEO, kind of like me&rdquo;</b>. Segmentation captured before the email, and "
                 "spoken back inside the very next asset. Cheap, and it makes a recording feel "
                 "addressed to one person.",
         "ev": "VERIFIED · quiz walked and VIP video transcribed 31 Jul"},
        {"id": "b_free", "x": X[3] + 10, "y": 1760, "state": "yes",
         "cond": "Registers → VIP given away at $0",
         "body": "$97 struck to $0 on a 20-minute timer. Jordan Lee and Miss Affiliate both "
                 "charge <b>$27</b> for the identical slot. Brunson is buying attendance and "
                 "commitment, not front-end cash, because the money lands on day five. Show "
                 "rate is the metric he is optimising &mdash; the same one we are.",
         "ev": "VERIFIED · captured on the VIP page 31 Jul"},
        {"id": "b_bot", "x": X[5] + 10, "y": 1760, "state": "dq",
         "cond": "Phone captured under an AI-caller consent",
         "body": "The form field is literally named <code>aisc_bot_calling_checkbox</code> and "
                 "the label covers &ldquo;automated calls, including prerecorded or "
                 "AI-generated voice messages&rdquo;. Their own copy says consent is not "
                 "required to attend, so it was left unticked and registration still completed.",
         "ev": "VERIFIED · form inspected and submitted unticked 31 Jul"},
        {"id": "b_live", "x": X[7] + 10, "y": 1760, "state": "unver",
         "cond": "The sessions are genuinely live",
         "body": "Unlike Richard Yu and Karla Marie, nothing static is exposed. Zoom is WebRTC, "
                 "so the scheduled sniffer will report &ldquo;needs a human&rdquo;. Price, offer "
                 "stack and the day-five close are all unobserved until someone attends or a "
                 "replay is posted.",
         "ev": "UNVERIFIED · registered, sessions run 3–7 Aug"},
    ],

    "LEGEND": [("event", "Challenge funnel"), ("ever", "VIP pitch"),
               ("back", "Free upgrade")],
}

if __name__ == "__main__":
    build(CONFIG)
