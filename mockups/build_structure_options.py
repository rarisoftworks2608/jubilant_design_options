"""Builds options K, L, M: the same Shaahi-style structure (6 Jubilant pages), three visual themes.
Run:  python build_structure_options.py
Reads real photos/videos from ../../jubilant-events. Only real Jubilant facts are used."""
import os, html
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..', 'structure-options'))
SITE = os.path.normpath(os.path.join(HERE, '..', '..', 'jubilant-events'))
VER = '3'
IMG = '../images/'
VID = '../videos/'

THEMES = [
    dict(key='k-boardroom', letter='K', name='Boardroom Navy', shared='boardroom.css', logo=('0.0824', '0.1843', '0.2863'),
         fonts='Plus+Jakarta+Sans:wght@400;500;600;700;800'),
    dict(key='l-gold', letter='L', name='Boardroom Gold', shared='boardroom.css', logo=('0.1098', '0.1059', '0.0980'),
         fonts='Plus+Jakarta+Sans:wght@400;500;600;700;800'),
    dict(key='m-editorial', letter='M', name='Editorial', shared=None, logo=('0.0824', '0.1843', '0.2863'),
         fonts='Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,400;1,9..144,500&family=Jost:wght@300;400;500;600'),
]
NAV = [('index.html', 'Home'), ('about.html', 'About'), ('services.html', 'Services'),
       ('projects.html', 'Projects'), ('production.html', 'Production'), ('contact.html', 'Contact')]

_dims = {}
def img(path, alt='', cls='', lazy=True):
    if path not in _dims:
        with Image.open(os.path.join(SITE, 'images', path)) as im:
            _dims[path] = im.size
    w, h = _dims[path]
    l = ' loading="lazy"' if lazy else ''
    c = f' class="{cls}"' if cls else ''
    return f'<img{c} src="{IMG}{path}" alt="{html.escape(alt)}" width="{w}" height="{h}"{l}>'

def frame(path, alt=''):
    fill = img(path, '', 'fill').replace('<img ', '<img aria-hidden="true" ')
    return f'<div class="frame">{fill}{img(path, alt)}</div>'


ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
I_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
I_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
I_CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8.5 8.5 0 0 1-12.4 7.5L3 21l1.6-5.4A8.5 8.5 0 1 1 21 12z"/></svg>'
I_IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/></svg>'
I_FB = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8.5V6.9c0-.8.2-1.2 1.3-1.2H17V2.1C16.6 2 15.7 2 14.7 2 12.2 2 10.5 3.5 10.5 6.3v2.2H8v3.6h2.5V22H14v-9.9h2.6l.4-3.6z"/></svg>'
I_IN = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.1c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7V21h-4z"/></svg>'


def _ico(inner):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{inner}</svg>'
SVC_STRIP = [
    ('Brand Promotions', _ico('<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>'), 'tone-coral'),
    ('MICE &amp; Conferences', _ico('<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 19v3"/>'), 'tone-gold'),
    ('Product Launches', _ico('<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>'), 'tone-purple'),
    ('Live Events &amp; Entertainment', _ico('<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>'), 'tone-teal'),
    ('Celebrity Management', _ico('<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>'), 'tone-coral'),
    ('Custom Fabrication', _ico('<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1-1.4-7.94l3.76 3.76z"/>'), 'tone-gold'),
]

def head(th, title, depth_css='theme.css'):
    shared = f'\n<link rel="stylesheet" href="../{th["shared"]}?v={VER}">' if th.get('shared') else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Jubilant Events &amp; Productions</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={th['fonts']}&display=swap">
<link rel="stylesheet" href="../base.css?v={VER}">{shared}
<link rel="stylesheet" href="{depth_css}?v={VER}">
</head>
<body class="t-{th['letter'].lower()}">
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><filter id="brand-logo" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0 0 0 0 {th['logo'][0]}  0 0 0 0 {th['logo'][1]}  0 0 0 0 {th['logo'][2]}  0 0 0 1 0"/></filter></svg>
<a class="sr" href="#main" style="position:absolute;left:-9999px">Skip to main content</a>
'''

def header(active):
    links = ''.join(f'<a href="{h}"{" class=on" if h == active else ""}>{n}</a>' for h, n in NAV)
    return f'''<header class="site-header"><div class="wrap nav">
  <a class="logo" href="index.html"><img src="{IMG}logo-transparent.png" alt="Jubilant Events &amp; Productions" width="615" height="199"></a>
  <button class="menu-btn" aria-label="Menu" aria-expanded="false"><span></span></button>
  <nav class="links" aria-label="Main">{links}<a class="btn btn-p" href="contact.html">Enquire now</a></nav>
</div></header>
<main id="main">
'''

def cta_block():
    return f'''<section class="sec cta s-d">
<div class="wrap">
  <span class="eyebrow">Start a conversation</span>
  <h2>Have an event <em>in mind?</em></h2>
  <p>Let's turn your idea into an experience people remember.</p>
  <div class="btns"><a class="btn btn-p" href="contact.html">Enquire now</a><a class="btn btn-o" href="https://wa.me/919545599027">WhatsApp us</a></div>
  <div class="lines">
    <div><b>Primary</b><a href="tel:+919545599027">+91 95455 99027</a></div>
    <div><b>Alternate</b><a href="tel:+919028512879">+91 90285 12879</a></div>
    <div><b>Email</b><a href="mailto:jubilantgroupindia@gmail.com">jubilantgroupindia@gmail.com</a></div>
    <div><b>Studio</b>Pune, Maharashtra, India</div>
  </div>
</div>
</section>
'''

def footer():
    return f'''</main>
<footer><div class="wrap">
  <div class="fgrid">
    <div><a class="logo" href="index.html"><img src="{IMG}logo-transparent.png" alt="Jubilant Events &amp; Productions" width="615" height="199"></a>
      <p>Your one-stop events management partner. Concept to completion, produced in-house in Pune.</p>
      <div class="social"><a href="#" aria-label="Instagram">{I_IG}</a><a href="#" aria-label="Facebook">{I_FB}</a><a href="#" aria-label="LinkedIn">{I_IN}</a></div></div>
    <div><h4>Navigation</h4><ul>{''.join(f'<li><a href="{h}">{n}</a></li>' for h, n in NAV)}</ul></div>
    <div><h4>Services</h4><ul><li>Brand Promotions</li><li>Product Launches</li><li>MICE &amp; Conferences</li><li>Exhibitions &amp; Stalls</li><li>Event Production</li></ul></div>
    <div><h4>Contact</h4><ul><li><a href="tel:+919545599027">+91 9545599027</a></li><li><a href="tel:+919028512879">+91 9028512879</a></li><li><a href="mailto:jubilantgroupindia@gmail.com">jubilantgroupindia@gmail.com</a></li><li>Pune, Maharashtra, India</li></ul></div>
  </div>
  <div class="fbar"><span>&copy; 2026 Jubilant Events &amp; Productions. All rights reserved.</span><span>Powered by <a href="https://rarisoftworks.com" target="_blank" rel="noopener">RaRi Softworks</a></span></div>
</div></footer>
<script src="../site.js?v={VER}"></script>
</body></html>
'''

def sec(cls, inner, extra=''):
    return f'<section class="sec {cls}"{extra}><div class="wrap">{inner}</div></section>\n'

def phero(eyebrow, h1, sub, poster, crumb, btns=''):
    return f'''<section class="phero" style="background-image:url('{IMG}{poster}')">
<div class="wrap"><div class="crumbs"><a href="index.html">Home</a><span>/</span><span>{crumb}</span></div>
<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p>{sub}</p>{btns}</div></section>
'''

def stats(items, n3=False):
    return f'<div class="stats{" n3" if n3 else ""}">' + ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in items) + '</div>'

CLIENTS = [('aayojan-ventures.png', 'Aayojan Ventures'), ('intrepid-control-systems.png', 'Intrepid Control Systems'),
           ('shivom-enterprises.png', 'Shivom Enterprises'), ('sgs-mall.png', 'SGS Mall Pune'),
           ('nuhii.png', 'National Union of Hospitality Industry of India'), ('seasons.png', 'Seasons'),
           ('dilip-oaks-academy.png', "Dilip Oak's Academy"), ('s-monogram.png', 'Client partner'), ('hdfc-bank.png', 'HDFC Bank')]

def marquee():
    one = ''.join(f'<div class="chip">{img("clients/" + f, a, lazy=False)}</div>' for f, a in CLIENTS)
    return f'<div class="marq"><h4>Brands we\'ve worked with</h4><div class="track">{one}{one}</div></div>'

SERVICES13 = [
    ('Celebrity Management', "Securing and coordinating celebrity appearances that elevate your event's profile.", 'events/svc-celebrity-management.jpg', 'Celebrity arrival with security escort managed by Jubilant at Seasons Mall, Pune'),
    ('Artist Management', 'End-to-end artist bookings, riders and on-ground coordination, handled seamlessly.', 'events/svc-artist-management.jpg', 'Singer performing live on a Jubilant-managed mall stage'),
    ('Brand Promotions', 'Strategic on-ground activations that build lasting brand equity.', 'events/svc-brand-promotions.jpg', 'Film promotion appearance on a branded stage produced by Jubilant'),
    ('Product Launches', 'Memorable reveals engineered for maximum impact and recall.', 'stock/launch-supercars.jpg', 'Supercars displayed on a curved launch platform'),
    ('MICE', 'Meetings, incentives, conferences and exhibitions, delivered at scale.', 'events/svc-mice.jpg', 'Seated guests facing the stage at a corporate event managed by Jubilant'),
    ('Conferences', 'Seamless logistics and production for large-scale conferences.', 'stock/svc-conference-hall.jpg', 'Modern conference hall set with projection screens and round tables'),
    ('Annual Day &amp; Family Day', 'Company celebrations designed to bring teams and families together.', 'events/svc-annual-day.jpg', 'Guests arriving at a seated celebration hosted by Jubilant'),
    ('Exhibitions &amp; Stall Setup', 'Custom stalls, structures and displays that command attention.', 'stock/svc-exhibition-stalls.jpg', 'Exhibition hall filled with custom-built stalls'),
    ('Opening &amp; Inauguration Events', 'Grand openings executed with precision, spectacle and style.', 'events/svc-opening-events.jpg', 'Mall atrium dressed with balloon decor by Jubilant for an anniversary celebration'),
    ('Event Production', 'Full-scale technical production, from concept through to show day.', 'events/svc-event-production.jpg', 'LED backdrop and stage set built by Jubilant'),
    ('Custom Fabrication', 'Bespoke structures and builds, engineered and fabricated in-house.', 'events/svc-custom-fabrication.jpg', 'Illuminated floral entrance tunnel fabricated in-house by Jubilant'),
    ('Live Events &amp; Entertainment', 'Full-scale production for concerts, festivals and live shows.', 'events/svc-live-events.jpg', 'Artists performing among a packed crowd at a Jubilant-managed event'),
    ('Sports Events', 'Comprehensive production support for sporting events and tournaments.', 'stock/svc-sports-stadium.jpg', 'Floodlit cricket stadium during an evening match'),
]
SV = {s[0]: s for s in SERVICES13}

def svc_card(name, num=None):
    n, d, p, alt = SV[name]
    tag = f'<span class="num">{num:02d}</span>' if num else ''
    return f'<article class="card">{frame(p, alt)}<div class="body">{tag}<h3>{n}</h3><p>{d}</p></div></article>'

# (title, client, category label, filter key, image, alt)
PROJECTS = [
    ('Udta Teer: Film Promotion', 'Seasons Mall, Pune', 'Celebrity Management', 'celebrity', 'events/udta-teer/udta-teer-11.jpg', 'Ayushmann Khurrana and Sara Ali Khan at the Udta Teer promotion managed by Jubilant'),
    ('Awarapan 2: Star Cast Meet &amp; Greet', 'Seasons Mall, Pune', 'Celebrity Management', 'celebrity', 'events/project-awarapan-2.jpg', 'Awarapan 2 star cast meet and greet'),
    ('VIBE: Film Promotion Meet &amp; Greet', 'Seasons Mall, Pune', 'Brand Promotion', 'celebrity', 'events/project-vibe.jpg', 'VIBE star cast promotion'),
    ('Seasons Mall 13th Anniversary Celebration', 'Seasons Mall, Pune', 'Corporate Event', 'corporate', 'events/project-anniversary-felicitation.jpg', 'Anniversary felicitation on an LED stage'),
    ('DSK Toyota, Hadapsar, Pune', 'DSK Toyota', 'Flagship Project', 'automotive', 'stock/project-dsk-toyota-stage.jpg', '12-level stage built for DSK Toyota'),
    ('Intrepid Control Systems', 'Intrepid Control Systems', 'Corporate Event', 'corporate', 'stock/project-intrepid-control-systems.jpg', 'Corporate event for Intrepid Control Systems'),
    ('Renault Pune', 'Renault', 'Automotive Launch', 'automotive', 'stock/project-renault-car.jpg', 'Renault Pune event'),
    ('PPS Motor', 'PPS Motor', 'Automotive Event', 'automotive', 'stock/project-pps-motor.jpg', 'PPS Motor event'),
    ('National Union Of Hospitality Industry Of India', 'NUHII', 'Conference', 'corporate', 'stock/project-nuhii-conference.jpg', 'NUHII conference'),
    ('Siddharth Auto Engineers', 'Siddharth Auto Engineers', 'Corporate Event', 'corporate', 'stock/project-siddharth-auto.jpg', 'Siddharth Auto Engineers corporate event'),
    ("Dilip Oak's Academy", "Dilip Oak's Academy", 'Institutional Event', 'corporate', 'stock/project-dilip-oaks-academy.jpg', "Dilip Oak's Academy event"),
    ('Godrej Air, Bangalore: Marketing Campaign', 'Godrej Air', 'Marketing Campaign', 'real-estate', 'stock/project-godrej-air-campaign.jpg', 'Godrej Air campaign'),
    ('Godrej Air, Bangalore: Property Launch', 'Godrej Air', 'Property Launch', 'real-estate', 'stock/project-godrej-air-launch.jpg', 'Godrej Air property launch'),
    ('Sai Dutta Developer, Amravati', 'Sai Dutta Developer', 'Real Estate Launch', 'real-estate', 'stock/project-sai-dutta.jpg', 'Sai Dutta Developer launch'),
    ('Chintamani Developers', 'Chintamani Developers', 'Real Estate Event', 'real-estate', 'stock/project-chintamani.jpg', 'Chintamani Developers event'),
    ('Destination Wedding D&eacute;cor, Shirdi', '', 'D&eacute;cor &amp; Social Events', 'decor', 'events/decor-haldi-stage.jpg', 'Haldi stage in Shirdi'),
    ('Floral Mandap &amp; Lounge Set-up', '', 'D&eacute;cor &amp; Social Events', 'decor', 'events/decor-floral-mandap.jpg', 'Floral mandap with crystal strands'),
    ('Gala Nights / Opening Events', '', 'Social &amp; Opening Events', 'decor', 'stock/header-contact-table-setting.jpg', 'Gala night table setting'),
    ('Exhibition / Stall / Structure / Customization', '', 'Exhibition', 'exhibition', 'stock/project-exhibition-structure.jpg', 'Custom exhibition structure'),
]

def work_card(p):
    t, c, cat, key, im, alt = p
    sub = f'<p class="sub">{c}</p>' if c else ''
    return f'<article class="card" data-cat="{key}">{frame(im, alt)}<div class="body"><span class="cat">{cat}</span><h3>{t}</h3>{sub}</div></article>'

# ---------------------------------------------------------------- pages
def intro(th):
    # Shows every time the design is opened from outside (chooser, link, new tab, reload);
    # skipped only when you come back to Home from another page of the same design.
    return f'''<script>(function(){{var d=document.documentElement,r=document.referrer||'';
if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&r.indexOf('/{th['key']}/')<0)d.classList.add('intro')}})();</script>
<div class="loader" id="loader" aria-hidden="true"><div class="lg"><img src="{IMG}logo-transparent.png" alt="" width="615" height="199"><i></i><small>Event management &amp; production</small></div></div>
'''

def page_home(th):
    h = intro(th) + header('index.html')
    h += f'''<section class="hero">
  <video autoplay muted loop playsinline preload="metadata" poster="{IMG}events/reel-poster.jpg" aria-label="Highlights from celebrity and corporate events managed by Jubilant at Seasons Mall, Pune"><source src="{VID}jubilant-reel.mp4" type="video/mp4"></video>
  <div class="wrap hero-inner">
    <span class="eyebrow">Event management &amp; production &middot; Pune</span>
    <h1>We create <em>experiences</em> that people remember</h1>
    <p>From concept to completion, Jubilant Events &amp; Productions delivers seamless events, powerful experiences and professional event production.</p>
    <div class="btns"><a class="btn btn-p" href="contact.html">Enquire now</a><a class="btn btn-o" href="projects.html">Explore our work</a></div>
  </div>
</section>
'''
    # What we do: Shaahi-style split header + one slim row of 6 icon + name cells (no photos, no descriptions)
    h += sec('s-a', f'''<div class="shead"><div><span class="eyebrow">What we do</span><h2>Our <em>signature</em> services</h2></div>
<div class="right"><p class="lede">A complete suite of event management and production capabilities, tailored to every scale and occasion.</p><a class="arrow-link" href="services.html">View all services {ARROW}</a></div></div>
<div class="svc-strip">{''.join(f'<a class="svc-cell {tone}" href="services.html"><span class="svc-ico">{ico}</span><h3>{n}</h3></a>' for n, ico, tone in SVC_STRIP)}</div>''')
    # Featured work (masonry cards)
    feat = [PROJECTS[0], PROJECTS[4], PROJECTS[1], PROJECTS[12], PROJECTS[6], PROJECTS[8]]
    h += sec('s-b', f'''<div class="head row"><div><span class="eyebrow">Featured work</span><h2>Ideas in <em>action</em></h2><p>Real briefs, delivered end to end: celebrity promotions, corporate events, launches and weddings.</p></div><a class="arrow-link" href="projects.html">View all projects {ARROW}</a></div>
<div class="g3">{''.join(work_card(p) for p in feat)}</div>''')
    # Impact
    h += sec('s-d', f'''<div class="head c"><span class="eyebrow">Our impact</span><h2>Built on experience, <em>run in-house</em></h2></div>
{stats([('2017', 'Founded'), ('2018', 'Own production house'), ('100+', 'Events delivered'), ('13', 'Services')])}
{marquee()}''')
    # image band
    h += sec('s-a', f'''<div class="band">{img('events/cta-atrium-crowd.jpg', 'Every level of the Seasons Mall atrium filled with fans at a Jubilant-managed event')}<div class="cap"><b>Packed atriums. Managed end to end.</b><span>Crowd barricading, security, stage and artists, all run by our own team.</span></div></div>''')
    # Who we are
    h += sec('s-b', f'''<div class="split"><div><span class="eyebrow">Our story</span><h2>Built on experience, <em>run in-house.</em></h2>
<p>What began in 2017 as a management company fielding vendor requests became too dependent on outside vendors to guarantee quality. So by 2018 we built our own production house.</p>
<p>Today, Jubilant Events &amp; Productions works with clients from concept to completion: a dedicated in-house team engineering every stage, launch and summit.</p>
<a class="btn btn-p" href="about.html">Discover more</a></div>
<div class="bigtext"><span>Your one-stop</span><span>events management</span><span>partner.</span></div></div>''')
    # Why choose us (testimonial slot)
    why = [('Experience', 'Years of hands-on expertise across events of every size and complexity.'), ('Quality', 'Meticulous attention to detail, from concept sketches to final execution.'),
           ('End-to-end execution', 'In-house production means full control over quality, timelines and cost.'), ('Dedicated support', 'A committed team, on call and on-ground, from planning through to the last minute.')]
    h += sec('s-a', f'''<div class="head c"><span class="eyebrow">Why choose us</span><h2>Quality service by a <em>dedicated team</em></h2><p>With the expertise and vision to turn your concept into reality, we push boundaries on every project: unique ideas that inspire, and a concept that works.</p></div>
<div class="g4">{''.join(f'<article class="card"><div class="body" style="padding-top:30px"><span class="num">0{i}</span><h3>{t}</h3><p>{d}</p></div></article>' for i, (t, d) in enumerate(why, 1))}</div>''')
    # In-house capability (destinations slot)
    tiles = [('Truss', 'events/teaser-truss-lights.jpg', 'Lighting truss and smoke jets over a live stage'), ('Stages', 'events/teaser-stages-atrium.jpg', 'Stage and branded backdrop built for a mall meet and greet'),
             ('Custom fabrication', 'stock/teaser-fabrication-floral-gazebo.jpg', 'Floral-dressed gazebo structure built for a celebration'), ('Canopies', 'stock/inventory-canopy.jpg', 'White canopy tent set up on a lawn for an outdoor event')]
    h += sec('s-d', f'''<div class="head row"><div><span class="eyebrow">In-house capability</span><h2>Our own fleet. <em>Our own crew.</em></h2><p>Our own fleet of production assets means faster turnarounds, tighter quality control and total reliability.</p></div><a class="arrow-link" href="production.html">View full inventory {ARROW}</a></div>
<div class="g4">{''.join(f'<a class="tile" href="production.html">{frame(p, a)}<div class="cap"><h3>{t}</h3><span>Owned by Jubilant</span></div></a>' for t, p, a in tiles)}</div>''')
    h += cta_block()
    return h + footer()

def page_about(th):
    h = header('about.html')
    h += phero('Our story', 'From an idea to an <em>experience</em>', "The story behind Jubilant Events &amp; Productions, and how we became Pune's trusted in-house event production house.", 'events/header-about-poster.jpg', 'About',
               '<div class="btns"><a class="btn btn-p" href="contact.html">Enquire now</a></div>')
    h += sec('s-a', f'''<div class="split"><div><span class="eyebrow">Our story</span><h2>Built on experience, <em>run in-house.</em></h2>
<p>It started with the same questions, again and again: "Will you be able to do a small stage for us?" "Can you organize a launch event?" "Do you have canopies, pagoda, chairs?" As a management company founded in 2017, Dream Cast Events kept fielding these requests, and kept relying on outside vendors to deliver. We wanted quality, but with vendors in the middle, that quality was never fully in our hands.</p>
<p>The headaches of depending on other vendors pushed us to a decision: build our own production house. We spent the next year adding inventory, and by 2018 we were ready: a dedicated management team backed by our own production capability. Jubilant Group was born.</p>
<p>We make it our priority to understand our clients' objectives, working with them from concept to completion to create a unique, memorable event. We're a team of experienced event planners who pride ourselves on delivering first-class service to every client, big and small.</p></div>
<div class="photo">{img('events/header-stage-setup.jpg', 'LED stage and backdrop built in-house by Jubilant')}</div></div>''')
    h += sec('s-b', stats([('2017', 'Founded'), ('2018', 'Production house'), ('100+', 'Projects')], n3=True))
    pillars = [('100% in-house fleet', 'We own our stages, German pagodas, lighting trusses, sound reinforcement and VIP lounges. No middleman delays, no unpredictable third-party fees.'),
               ('End-to-end engineering', 'From conceptual sketches and 3D scale renders to precision load calculations and show-day stage direction, everything is engineered in-house.'),
               ('Direct accountability', 'A single dedicated point of contact on ground from initial kickoff through final venue strike. If it\'s on our stage, our reputation stands behind it.')]
    h += sec('s-a', f'''<div class="split rev"><div class="head" style="margin:0"><span class="eyebrow">Our foundation</span><h2>The three pillars of <em>Jubilant</em></h2><p>How our unique in-house model sets us apart from conventional event brokers.</p></div>
<div>{''.join(f'<div class="feat"><i>0{i}</i><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (t, d) in enumerate(pillars, 1))}</div></div>''')
    why = [('Experience', 'Years of hands-on expertise across events of every size and complexity.'), ('Quality', 'Meticulous attention to detail, from concept sketches to final execution.'),
           ('End-to-end execution', 'In-house production means full control over quality, timelines and cost.'), ('Dedicated support', 'A committed team, on call and on-ground, from planning through to the last minute.')]
    h += sec('s-d', f'''<div class="head c"><span class="eyebrow">Why choose us</span><h2>Quality service by a <em>dedicated team</em></h2><p>With the expertise and vision to turn your concept into reality, we push boundaries on every project: unique ideas that inspire, and a concept that works.</p></div>
<div class="g4">{''.join(f'<article class="card"><div class="body" style="padding-top:30px"><span class="num">0{i}</span><h3>{t}</h3><p>{d}</p></div></article>' for i, (t, d) in enumerate(why, 1))}</div>''')
    h += cta_block()
    return h + footer()

def page_services(th):
    h = header('services.html')
    h += phero('What we do', 'Our <em>services</em>', 'A complete suite of event management and production capabilities, tailored to every scale and occasion.', 'events/header-services-poster.jpg', 'Services',
               '<div class="btns"><a class="btn btn-p" href="contact.html">Enquire now</a></div>')
    cards = ''.join(svc_card(s[0], i) for i, s in enumerate(SERVICES13, 1))
    h += sec('s-a', f'''<div class="head row"><div><span class="eyebrow">13 services</span><h2>Everything under <em>one roof</em></h2></div></div>
<div class="g3">{cards}</div>''')
    weds = [('Haldi', 'Tangerine Glow', 'A sunlit morning in marigold and citrus, with a floral stage and a rangoli floor.', 'events/theme-haldi.jpg', 'Haldi stage with floral frame and a colourful rangoli floor', ['Stage', 'Entrance', 'Props', 'Photobooth', 'Bar']),
            ('Sangeet', 'An Evening of Light', 'Glowing entrances, a performance stage and lounges built for music and dance.', 'events/theme-sangeet.jpg', 'Illuminated floral entrance tunnel lit for an evening celebration', ['Entrance', 'Stage', 'Lounge', '360&deg; Point', 'Couple Seating']),
            ('Phere', 'Framed in Florals', 'A mandap in roses and crystal strands, with a welcome aisle to match.', 'events/theme-phere.jpg', 'Floral mandap with a crystal-strand canopy and rose-wrapped pillars', ['Mandap', 'Entrance', 'Welcome Board', 'Activities', 'Artist Stage']),
            ('After Party', 'Neon Nights', 'Light installations, a DJ console and a dance floor that keeps going.', 'events/theme-afterparty.jpg', 'Neon-lit dance floor with a mirror ball at an after party', ['Dance Floor', 'DJ Console', 'Hangings', 'Photobooth', 'Bar'])]
    h += sec('s-b', f'''<div class="head c"><span class="eyebrow">Weddings &amp; celebrations</span><h2>Signature <em>wedding themes</em></h2><p>Every function gets its own look, designed, fabricated and styled by our in-house team, from the morning haldi to the last song at the after party.</p></div>
<div class="g4">{''.join(f'<article class="card">{img(p, a)}<div class="body"><span class="cat">{f}</span><h3>{t}</h3><p>{d}</p><div class="tags">{"".join(f"<span>{c}</span>" for c in ch)}</div></div></article>' for f, t, d, p, a, ch in weds)}</div>''')
    steps = [('Discovery &amp; brief', 'We analyse your brand tone, audience profile and venue parameters to shape an imaginative creative narrative.'),
             ('3D CAD &amp; visuals', 'Precise 3D renders, stage elevation models and lighting simulations ensure zero surprises before a single bolt is turned.'),
             ('In-house rigging &amp; build', 'Our fleet of aluminium trusses, custom stage levels and branding frameworks is prepared and safety-tested in our workshop.'),
             ('Live show direction', 'Dedicated on-ground technical controllers and showrunners oversee live cueing, audio-visual transitions and artist logistics.')]
    h += sec('s-a', f'''<div class="head c"><span class="eyebrow">How we work</span><h2>The four-stage <em>blueprint</em></h2><p>A structured, battle-tested method from creative inception through show-day culmination.</p></div>
<div class="steps">{''.join(f'<div class="step"><b>0{i}</b><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps, 1))}</div>''')
    h += cta_block()
    return h + footer()

def page_projects(th):
    h = header('projects.html')
    h += phero('Our work', 'Our <em>projects</em>', 'A portfolio built on trust, precision and brands who came back for more: celebrity promotions, corporate events, launches and weddings.', 'events/header-projects-poster.jpg', 'Projects',
               '<div class="btns"><a class="btn btn-p" href="#film">Watch the Udta Teer film</a></div>')
    pills = [('all', 'All work'), ('celebrity', 'Celebrity &amp; Promotions'), ('corporate', 'Corporate &amp; Summits'), ('automotive', 'Automotive &amp; Launches'),
             ('real-estate', 'Real Estate &amp; Property'), ('exhibition', 'Exhibitions &amp; Stalls'), ('decor', 'D&eacute;cor &amp; Social')]
    pillbar = '<div class="pills">' + ''.join(f'<button class="pill{" on" if k == "all" else ""}" data-f="{k}">{n}</button>' for k, n in pills) + '</div>'
    h += sec('s-a', f'''<div class="featured"><div class="photo">{img('events/udta-teer/udta-teer-11.jpg', 'Ayushmann Khurrana and Sara Ali Khan at the Udta Teer promotion managed by Jubilant')}</div>
<div><span class="eyebrow">Featured project</span><h2>Udta Teer, <em>film promotion</em></h2><p>Film promotion with <strong>Ayushmann Khurrana</strong> and <strong>Sara Ali Khan</strong>: a cinema meet &amp; greet with the stars, then a packed Seasons Mall atrium fan event with crowd barricading, felicitation and a dhol welcome.</p><a class="btn btn-p" href="#film">View project</a></div></div>
<div id="work">{pillbar}<div class="g3">{''.join(work_card(p) for p in PROJECTS)}</div></div>''')
    h += sec('s-d', stats([('100+', 'Turnkey events executed'), ('12', 'Level multi-tier stage'), ('500+', 'Guest capacity arenas'), ('100%', 'In-house fleet ownership')]))
    h += sec('s-b', f'''<div class="head row" id="film"><div><span class="eyebrow">Event film</span><h2>Udta Teer, <em>the film</em></h2></div><p style="max-width:460px;color:var(--ink2)">Ayushmann Khurrana and Sara Ali Khan at Seasons Mall, Pune: the cinema meet &amp; greet, the atrium stage and the fans. Planned and run end to end by our team.</p></div>
<div class="vid"><video controls preload="none" playsinline width="1280" height="720" poster="{IMG}events/udta-teer-film-poster.jpg"><source src="{VID}udta-teer-film.mp4" type="video/mp4">Your browser does not support video playback.</video></div>''')
    gal = ['12', '15', '06', '19', '29', '17', '10', '03', '32', '43', '50', '48']
    h += sec('s-a', f'''<div class="head c"><span class="eyebrow">Event gallery</span><h2>Udta Teer, <em>film promotion</em></h2><p>Ayushmann Khurrana and Sara Ali Khan, from the cinema meet &amp; greet to a packed Seasons Mall atrium. Every moment managed by our team.</p></div>
<div class="masonry">{''.join(f'<div class="photo">{img(f"events/udta-teer/udta-teer-{n}.jpg", "Udta Teer promotion photo " + n)}</div>' for n in gal)}</div><p class="credit">Photographs: @ketan.artwork</p>''')
    h += cta_block()
    return h + footer()

def page_production(th):
    h = header('production.html')
    h += phero('In-house capability', 'Production <em>inventory</em>', 'Our own fleet of production assets means faster turnarounds, tighter quality control and total reliability.', 'events/header-production-poster.jpg', 'Production',
               '<div class="btns"><a class="btn btn-p" href="contact.html">Enquire now</a></div>')
    h += sec('s-b', stats([('9', 'Asset categories'), ('100%', 'Owned fleet'), ('2018', 'In-house since')], n3=True))
    adv = [('Zero broker markup', 'Direct warehouse access means your budget goes 100% onto the stage, eliminating costly multi-tier vendor markups and middlemen fees.'),
           ('Certified structural rigging', 'Load-tested aluminium box trusses, certified staging joints and fire-retardant canopy fabrics engineered to strict international safety standards.'),
           ('Dedicated on-site technicians', 'From early morning load-in to post-event strike, our seasoned carpenters, master riggers and technicians oversee every technical cue.')]
    h += sec('s-a', f'''<div class="split rev"><div class="head" style="margin:0"><span class="eyebrow">Engineering rigour</span><h2>The in-house <em>technical advantage</em></h2><p>Why Pune's top agencies and corporations rely directly on our owned production assets.</p></div>
<div>{''.join(f'<div class="feat"><i>0{i}</i><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (t, d) in enumerate(adv, 1))}</div></div>''')
    fleet = [('Truss', 'stock/inventory-truss.jpg', 'Overhead lighting truss and rigging illuminating an event crowd'), ('Canopies', 'stock/inventory-canopy.jpg', 'White canopy tent set up on a lawn for an outdoor event'),
             ('Leather Sofas', 'stock/inventory-leather-sofa.jpg', 'Premium leather sofa seating for event lounges'), ('Queue Managers', 'stock/inventory-queue-managers.jpg', 'Managed queue line at an event entrance'),
             ('Flex &amp; Framing', 'stock/inventory-flex-framing.jpg', 'Branded exhibition booth with printed backdrop framing'), ('Chairs &amp; Tables', 'stock/inventory-chairs-tables.jpg', 'Elegant banquet hall set with long tables and chairs'),
             ('Stages', 'events/header-stage-setup.jpg', 'LED stage and backdrop built in-house by Jubilant'), ('Exhibition Structures', 'stock/inventory-exhibition-structures.jpg', 'Exhibition hall fitted with custom structures'),
             ('Custom Fabrication', 'stock/inventory-fabrication-workshop.jpg', 'Custom fabrication workshop for bespoke event builds')]
    h += sec('s-d', f'''<div class="head c"><span class="eyebrow">The fleet</span><h2>Nine categories, <em>all owned</em></h2></div>
<div class="g3">{''.join(f'<div class="tile">{frame(p, a)}<div class="cap"><h3>{t}</h3><span>0{i} &middot; Owned by Jubilant</span></div></div>' for i, (t, p, a) in enumerate(fleet, 1))}</div>''')
    h += cta_block()
    return h + footer()

def page_contact(th):
    h = header('contact.html')
    h += phero('Get in touch', "Let's start a <em>conversation</em>", 'Tell us about your event and our team will get back to you shortly.', 'stock/header-contact-table-setting.jpg', 'Contact')
    h += f'''<section class="sec s-a" style="padding-top:0"><div class="wrap"><div class="ccards">
<a class="ccard" href="tel:+919545599027">{I_PHONE}<div><b>Call us</b><span>+91 95455 99027</span></div></a>
<a class="ccard" href="https://wa.me/919545599027">{I_CHAT}<div><b>WhatsApp</b><span>Chat with our team</span></div></a>
<a class="ccard" href="mailto:jubilantgroupindia@gmail.com">{I_MAIL}<div><b>Email</b><span style="font-size:15px">jubilantgroupindia@gmail.com</span></div></a>
</div></div></section>
'''
    opts = ''.join(f'<option>{o}</option>' for o in ['Wedding', 'Corporate Event', 'Exhibition', 'Product Launch', 'Conference', 'Social Event', 'Other'])
    h += sec('s-a', f'''<div class="cgrid"><div><span class="eyebrow">Contact details</span><h2>We'd love to <em>hear from you</em></h2>
<p style="color:var(--ink2);margin:18px 0 30px;font-size:17px">Reach out directly, or send an enquiry and our team will be in touch shortly.</p>
<div class="dlist"><div><b>Contact person</b><span>Rohit Killekar</span></div><div><b>Phone</b><span>+91 9545599027 / +91 9028512879</span></div><div><b>Email</b><span style="font-size:16px">jubilantgroupindia@gmail.com</span></div><div><b>Location</b><span>Pune, Maharashtra, India</span></div></div></div>
<form class="enq" onsubmit="return false"><div class="full"><span class="eyebrow" style="margin:0">Send an enquiry</span></div>
<div><label>Full name *</label><input type="text"></div><div><label>Company</label><input type="text"></div>
<div><label>Email *</label><input type="email"></div><div><label>Phone *</label><input type="tel"></div>
<div><label>Event type *</label><select><option>Select event type</option>{opts}</select></div><div><label>Event date</label><input type="date"></div>
<div class="full"><label>Message *</label><textarea></textarea></div><div class="full"><button class="btn btn-p" type="submit">Send enquiry {ARROW}</button></div></form></div>''')
    faqs = [('How early should we initiate event planning?', 'For major summits, exhibitions or custom multi-level stage builds, we recommend engaging 4 to 8 weeks in advance for 3D modelling and structural planning. However, with our fully owned in-house inventory, we routinely accommodate urgent turnarounds.'),
            ('Do you manage events outside Pune?', 'Yes. While our headquarters and primary fabrication facility are based in Pune, our fleet and technical crew regularly travel across Maharashtra, Goa and pan-India for corporate summits and destination celebrations.'),
            ('Can we hire you purely for production &amp; fabrication?', 'Absolutely. We work both ways: as a complete turnkey event management agency handling every detail, or directly as a technical production partner providing stage builds, aluminium trusses, canopies and lighting.'),
            ('What is your typical turnaround time for a proposal?', 'Following an initial discovery discussion or enquiry form submission, our production directors typically deliver a comprehensive line-item scope and cost estimate within 24 to 48 hours.')]
    h += sec('s-b', f'''<div class="split rev" style="align-items:start"><div class="head" style="margin:0"><span class="eyebrow">Common queries</span><h2>Frequently asked <em>questions</em></h2><p>Quick answers regarding bookings, execution capabilities and engagement timelines.</p></div>
<div>{''.join(f'<details class="faq"{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(faqs))}</div></div>''')
    return h + footer()

PAGES = {'index.html': page_home, 'about.html': page_about, 'services.html': page_services,
         'projects.html': page_projects, 'production.html': page_production, 'contact.html': page_contact}
TITLES = {'index.html': 'Home', 'about.html': 'About', 'services.html': 'Services', 'projects.html': 'Projects', 'production.html': 'Production', 'contact.html': 'Contact'}

for th in THEMES:
    d = os.path.join(OUT, th['key'])
    os.makedirs(d, exist_ok=True)
    for fn, fnc in PAGES.items():
        body = head(th, TITLES[fn]) + fnc(th)
        body = body.replace('run in-house', '<span class="nb">run in-house</span>').replace('Your one-stop', '<span class="nb">Your one-stop</span>')
        open(os.path.join(d, fn), 'w', encoding='utf-8').write(body)
    print('built', th['key'])

# copy every photo/video the pages reference into structure-options/ so the folder is self-contained (GitHub Pages)
import re, shutil
used = set()
for root, _, files in os.walk(OUT):
    for f in files:
        if f.endswith('.html'):
            t = open(os.path.join(root, f), encoding='utf-8').read()
            used.update(re.findall(r"\.\./((?:images|videos)/[^\"'\s)]+)", t))
for rel in sorted(used):
    src = os.path.join(SITE, rel)
    dst = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
print('copied', len(used), 'assets')


# ---- chooser page
OPTS = [('k-boardroom', 'K', 'Boardroom Navy', 'White and navy with coral-to-saffron gradient buttons (the Shaahi palette). Top contact bar, square-edged cards, same-size photo cards.'),
        ('l-gold', 'L', 'Boardroom Gold', 'The same design as K in a different palette: charcoal and antique gold with copper and burgundy accents.'),
        ('m-editorial', 'M', 'Editorial', 'White and navy with coral and saffron accents. Serif headlines, a centred masthead menu and framed photos.')]
PG = [('index', 'Home'), ('about', 'About'), ('services', 'Services'), ('projects', 'Projects'), ('production', 'Production'), ('contact', 'Contact')]
cards = ''
for k, l, n, d in OPTS:
    links = ' '.join(f'<a href="{k}/{pp}.html">{tt}</a>' for pp, tt in PG)
    cards += f'<article><a class="th" href="{k}/index.html"><img src="img/{l.lower()}-home.jpg" alt="Option {l} {n} home page"></a><div><span class="tag">Option {l}</span><h2>{n}</h2><p>{d}</p><div class="lk">{links}</div></div></article>\n'
CHOOSER_CSS = """*{box-sizing:border-box;margin:0;padding:0}body{font:16px/1.6 'Segoe UI',system-ui,sans-serif;background:#f5f5f3;color:#1a1a1a}
.w{max-width:1240px;margin:0 auto;padding:56px 32px 80px}h1{font-size:clamp(30px,4vw,48px);line-height:1.1;margin-bottom:12px}
.sub{color:#555;max-width:760px;margin-bottom:44px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
article{background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 20px 40px -28px rgba(0,0,0,.4)}
.th img{width:100%;display:block}article>div{padding:22px 24px 26px}.tag{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#777;font-weight:600}
h2{font-size:26px;margin:6px 0 8px}p{color:#555;font-size:15px}.lk{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.lk a{padding:8px 14px;border:1px solid #ddd;border-radius:999px;font-size:14px;text-decoration:none;color:#222}.lk a:hover{background:#1a1a1a;color:#fff}
@media(max-width:900px){.grid{grid-template-columns:1fr}}"""
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(
    '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
    '<title>Jubilant Events | Website structure options</title>\n<style>\n' + CHOOSER_CSS + '\n</style></head><body><div class="w"><h1>Website structure options</h1>\n'
    '<p class="sub">Same section order and page structure in every option, filled with the real Jubilant content and photos. '
    'K and L are the same Boardroom design in two colour palettes; M is the Editorial design. Open any option and use its menu to browse all six pages.</p>\n'
    '<div class="grid">\n' + cards + '</div></div></body></html>')
