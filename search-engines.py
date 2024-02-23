# If you're reading this, congrats on looking at a sketchy script
# to generate rulesets for specific search engines
# Everything looks bad, everything is hardcoded but we love it

orig = open('seo-garbage.txt', 'r')
domains = orig.readlines()
orig.close()

google = open('seo-garbage-google.txt', 'w')
duck = open('seo-garbage-duckduckgo.txt', 'w')

for line in domains:
    line = line.strip()

    if '||' in line: # The best detection ever
        line = line.replace('||', '')
        
        # GOOGLE
        google.write(f'google.*##.g:has(a[href*="{line}"])\n')
        google.write(f'google.*##a[href*="{line}"]:upward(1)\n')

        # DUCKDUCKGO
        duck.write(f'duckduckgo.*##li:has(a[href*="{line}"])\n')
        duck.write(f'duckduckgo.*##.results_links_deep:has(a[href*="{line}"])\n')
    else:
        if '! Title:' in line:
            google.write(f'{line}, Google edition\n')
            duck.write(f'{line}, Duckduckgo edition\n')
        else:
            google.write(f'{line}\n')
            duck.write(f'{line}\n')

google.close()
duck.close()
