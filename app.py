import streamlit as st
import zipfile
import io
from datetime import datetime

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Kaydiem Script Lab | Enterprise Engine", layout="wide", page_icon="🧪")

# Streamlit UI Design
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4em; 
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%); 
        color: white; font-weight: 900; border: none; font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: DESIGN STUDIO ---
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=50)
    st.title("Kaydiem Lab")
    st.markdown("---")
    st.header("🎨 Visual Theme")
    p_color = st.color_picker("Brand Primary Color", "#003B73")
    s_color = st.color_picker("Accent Action Color", "#3EB489")
    font_choice = st.selectbox("Typography", ["Inter", "Poppins", "Montserrat", "Outfit"])
    st.header("⚙️ Tech SEO")
    gsc_tag = st.text_input("GSC Verification Tag", placeholder="google-site-verification=...")
    st.info("By www.kaydiemscriptlab.com")

st.title("💎 Premium Google Business Site Factory")
st.write("Generating 100% Certified, Enterprise-Grade Local SEO Assets.")

# --- 2. DATA COLLECTION TABS ---
tabs = st.tabs(["📍 Identity", "🏗️ Content & SEO", "🌟 Social Proof", "⚖️ Legal Pages"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name (NAP)", "Urban Prime Dental")
        biz_phone = st.text_input("Phone", "+91 98765 43210")
        biz_email = st.text_input("Email", "care@urbanprime.com")
    with c2:
        biz_cat = st.text_input("Category", "Dental Clinic")
        biz_hours = st.text_input("Hours", "Mon-Sat: 09:00 - 21:00")
        prod_url = st.text_input("Production URL", "https://username.github.io/repo/")
    biz_addr = st.text_area("Full Address (Exact match to Google Maps)")
    map_iframe = st.text_area("Google Map Embed Link (Paste <iframe> here)", placeholder="Go to Google Maps -> Share -> Embed -> Copy HTML")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", "World-Class Dental Care")
    seo_d = st.text_input("Meta Description", "Best dental clinic in Bengaluru...")
    biz_key = st.text_input("Keywords", "Dentist, Root Canal, Implants")
    biz_serv = st.text_area("Services (One per line)", "Painless Implants\nRoot Canal\nSmile Makeover")
    about_txt = st.text_area("About Us (Deep E-E-A-T Content)", height=300)

with tabs[2]:
    testi = st.text_area("Testimonials (Name | Comment)", "Amit | Great service!")
    faqs = st.text_area("FAQ (Question ? Answer)", "Is it safe ? Yes, it is ISO certified.")

with tabs[3]:
    priv_body = st.text_area("Privacy Policy", height=200)
    terms_body = st.text_area("Terms & Conditions", height=200)

# --- 3. THE RECTIFIED GENERATION ENGINE ---

if st.button("🚀 GENERATE PREMIUM COMPLIANT BIZ PACKAGE"):
    
    # CSS Strategy for Enterprise Look
    theme_css = f"""
    :root {{ --p: {p_color}; --s: {s_color}; --font: '{font_choice}', sans-serif; }}
    body {{ font-family: var(--font); scroll-behavior: smooth; color: #1e293b; line-height: 1.6; }}
    .bg-brand {{ background-color: var(--p); }}
    .text-brand {{ color: var(--p); }}
    .btn-accent {{ background-color: var(--s); color: white; padding: 1rem 2rem; border-radius: 99px; font-weight: 800; transition: all 0.3s; display: inline-block; }}
    .btn-accent:hover {{ transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.15); }}
    .glass {{ background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); }}
    """

    def get_layout(title, desc, content, is_index=False):
        gsc = f'<meta name="google-site-verification" content="{gsc_tag}">' if (is_index and gsc_tag) else ""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {gsc}
    <title>{title} | {biz_name}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{prod_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={font_choice.replace(' ', '+')}:wght@400;700;900&display=swap" rel="stylesheet">
    <style>{theme_css}</style>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "{biz_name}",
      "address": {{ "@type": "PostalAddress", "streetAddress": "{biz_addr}" }},
      "telephone": "{biz_phone}", "url": "{prod_url}"
    }}
    </script>
</head>
<body class="bg-white flex flex-col min-h-screen">
    <nav class="glass sticky top-0 z-50 border-b">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <a href="index.html" class="text-2xl font-black text-brand tracking-tighter uppercase">{biz_name}</a>
            <div class="hidden md:flex space-x-8 text-xs font-bold uppercase tracking-widest">
                <a href="index.html" class="hover:text-brand">Home</a>
                <a href="about.html" class="hover:text-brand">About</a>
                <a href="contact.html" class="hover:text-brand">Contact</a>
            </div>
            <a href="tel:{biz_phone}" class="bg-brand text-white px-6 py-2 rounded-full text-xs font-bold shadow-lg">Call Now</a>
        </div>
    </nav>
    <main class="flex-grow">{content}</main>
    <footer class="bg-slate-950 text-slate-400 py-20 px-6">
        <div class="max-w-7xl mx-auto grid md:grid-cols-4 gap-12">
            <div class="col-span-2">
                <h4 class="text-white font-black text-xl mb-6 tracking-widest uppercase">{biz_name}</h4>
                <p class="max-w-sm mb-6 text-slate-400">{biz_addr}</p>
                <p class="text-xs">Build By <a href="https://www.kaydiemscriptlab.com" class="text-white underline">Kaydiem Script Lab</a></p>
            </div>
            <div>
                <h4 class="text-white font-bold mb-6">Legal</h4>
                <ul class="space-y-4 text-sm">
                    <li><a href="privacy.html" class="hover:text-white">Privacy Policy</a></li>
                    <li><a href="terms.html" class="hover:text-white">Terms & Conditions</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-bold mb-6">Support</h4>
                <p class="text-sm">{biz_phone}<br>{biz_email}</p>
            </div>
        </div>
    </footer>
</body></html>"""

    # --- RECTIFIED PAGE CONTENT ---
    
    # Cleaning function to remove backticks and whitespace issues
    def clean(txt): return txt.replace("`", "").strip()

    # Grid Fix for Services
    serv_cards = "".join([f'<div class="bg-slate-50 p-8 rounded-3xl border border-slate-100 hover:shadow-xl transition"><h3 class="text-xl font-black mb-3 text-brand">{s.strip()}</h3><p class="text-slate-500 text-sm">Professional {biz_cat} care tailored for you.</p></div>' for s in biz_serv.splitlines() if s.strip()])
    
    testi_cards = "".join([f'<div class="p-6 bg-white border-l-4 border-brand shadow-sm italic mb-4">"{t.split("|")[1].strip()}"<br><span class="font-bold not-italic text-brand">- {t.split("|")[0].strip()}</span></div>' for t in testi.splitlines() if "|" in t])
    
    faq_html = "".join([f'<details class="mb-4 bg-slate-50 p-4 rounded-xl cursor-pointer"><summary class="font-bold">{f.split("?")[0].strip()}?</summary><p class="mt-2 text-slate-600">{f.split("?")[1].strip()}</p></details>' for f in faqs.splitlines() if "?" in f])

    idx_main = f"""
    <header class="relative bg-slate-50 py-32 px-6 text-center overflow-hidden">
        <div class="max-w-5xl mx-auto relative z-10">
            <h1 class="text-5xl md:text-8xl font-black text-slate-900 mb-8 tracking-tighter leading-tight">{clean(hero_h)}</h1>
            <p class="text-xl md:text-2xl text-slate-500 mb-12 max-w-2xl mx-auto">{clean(seo_d)}</p>
            <a href="tel:{biz_phone}" class="btn-accent uppercase tracking-widest text-sm shadow-xl">Book Appointment</a>
        </div>
    </header>
    
    <section class="max-w-7xl mx-auto py-24 px-6">
        <h2 class="text-4xl font-black mb-16 text-center uppercase tracking-tighter text-brand">Our Specialties</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">{serv_cards}</div>
    </section>

    <section class="bg-slate-50 py-24 px-6">
        <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-20">
            <div><h2 class="text-4xl font-black mb-12 uppercase tracking-tighter text-brand">Patient Stories</h2>{testi_cards}</div>
            <div><h2 class="text-4xl font-black mb-12 uppercase tracking-tighter text-brand">Common Queries</h2>{faq_html}</div>
        </div>
    </section>
    """

    # --- ZIP ENGINE ---
    zip_buf = io.BytesIO()
    with zipfile.ZipFile(zip_buf, "a", zipfile.ZIP_DEFLATED, False) as zf:
        zf.writestr("index.html", get_layout("Home", seo_d, idx_main, True))
        zf.writestr("about.html", get_layout("About", "Our History", f"<section class='max-w-4xl mx-auto py-32 px-6'><h1 class='text-5xl font-black mb-12 text-brand uppercase tracking-tighter'>About Us</h1><div class='text-lg leading-relaxed text-slate-700 whitespace-pre-wrap'>{clean(about_txt)}</div></section>"))
        zf.writestr("contact.html", get_layout("Contact", "Locate Us", f"<section class='max-w-5xl mx-auto py-32 px-6 text-center'><h1 class='text-6xl font-black mb-12 text-brand tracking-tighter'>VISIT CLINIC</h1><div class='bg-white p-12 md:p-20 rounded-[3rem] shadow-2xl border'><p class='text-4xl font-black mb-4 text-brand'>{biz_phone}</p><p class='text-xl mb-12 text-slate-500'>{biz_addr}</p><div class='rounded-3xl overflow-hidden shadow-inner bg-slate-100'>{map_iframe if 'iframe' in map_iframe else '<p class="p-20 text-slate-400 italic">Google Map Embed via Google Maps API</p>'}</div></div></section>"))
        zf.writestr("privacy.html", get_layout("Privacy", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-6'><h1 class='text-4xl font-bold mb-10'>Privacy Policy</h1><div class='text-slate-600'>{clean(priv_body)}</div></div>"))
        zf.writestr("terms.html", get_layout("Terms", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-6'><h1 class='text-4xl font-bold mb-10'>Terms & Conditions</h1><div class='text-slate-600'>{clean(terms_body)}</div></div>"))
        zf.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}sitemap.xml")
        zf.writestr("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{prod_url}index.html</loc></url></urlset>')

    st.success("💎 Enterprise Package Rectified & Ready!")
    st.download_button("📥 DOWNLOAD CORRECTED BIZ PACKAGE", zip_buf.getvalue(), f"{biz_name.lower()}_enterprise.zip")
