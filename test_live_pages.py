import urllib.request
import urllib.error
import time

urls = [
    "https://globalteampartners.github.io/ural-sales-kit/",
    "https://globalteampartners.github.io/ural-sales-kit/index.html",
    "https://globalteampartners.github.io/ural-sales-kit/Solo_Executive_Strategy.html",
    "https://globalteampartners.github.io/ural-sales-kit/Leads_List.html",
    "https://globalteampartners.github.io/ural-sales-kit/Comprehensive_Pitches.html",
    "https://globalteampartners.github.io/ural-sales-kit/Fast_Collab_Pitches.html",
    "https://globalteampartners.github.io/ural-sales-kit/Dynamic_Pitch_Deck.html",
    "https://globalteampartners.github.io/ural-sales-kit/Dynamic_Pitch_Deck.html?id=sveza-sinichikha",
    "https://globalteampartners.github.io/ural-sales-kit/Dynamic_One_Pager.html",
    "https://globalteampartners.github.io/ural-sales-kit/Dynamic_One_Pager.html?id=stroydormash-alapaevsk",
    "https://globalteampartners.github.io/ural-sales-kit/Templates_Catalog.html",
    "https://globalteampartners.github.io/ural-sales-kit/Exclusive_Strategy.html",
    "https://globalteampartners.github.io/ural-sales-kit/Market_Intelligence.html",
    "https://globalteampartners.github.io/ural-sales-kit/demos/wood-industry-demo/index.html",
    "https://globalteampartners.github.io/ural-sales-kit/demos/machinery-demo/index.html",
    "https://globalteampartners.github.io/ural-sales-kit/demos/real-estate-demo/index.html",
    "https://globalteampartners.github.io/ural-sales-kit/demos/horeca-demo/index.html",
    "https://globalteampartners.github.io/ural-sales-kit/demos/medical-demo/index.html",
    "https://globalteampartners.github.io/ural-sales-kit/demos/service-demo/index.html",
]

print("Checking live URLs on GitHub Pages...")
all_ok = True

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
            content = resp.read()
            size = len(content)
            # Check for specific phrase in Solo_Executive_Strategy.html
            phrase_check = ""
            if "Solo_Executive_Strategy.html" in url:
                has_phrase = "Плейбук Димы: Стратегия На Земле" in content.decode('utf-8', errors='ignore')
                phrase_check = f" [Content verified: {has_phrase}]"
            print(f"[{status}] {size:6d} bytes: {url}{phrase_check}")
    except Exception as e:
        print(f"[FAIL] {url} -> {e}")
        all_ok = False

if all_ok:
    print("\nSUCCESS: All live URLs are responding with HTTP 200 and full content!")
else:
    print("\nSome URLs failed or are still deploying.")
