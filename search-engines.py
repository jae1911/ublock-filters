# If you're reading this, congrats on looking at a sketchy script
# to generate rulesets for specific search engines
# Everything looks bad, everything is hardcoded but we love it

original_file = open('seo-garbage.txt', 'r')
domains = original_file.readlines()
original_file.close()

variants = ['Google', 'Duckduckgo']

def google_converter(domain: str) -> str:
    converted = f'google.*##.g:has(a[href*="{domain}"])\n'
    converted += f'google.*##a[href*="{domain}"]:upward(1)\n'
    return converted

def duckduckgo_converter(domain: str) -> str:
    converted = f'duckduckgo.*##li:has(a[href*="{domain}"])\n'
    converted += f'duckduckgo.*##.results_links_deep:has(a[href*="{domain}"])\n'
    return converted

def generate_list(variant: str) -> None:
    list_file = open(f'seo-garbage-{variant}.txt', 'w')

    for line in domains:
        line = line.strip()

        if '||' in line:
            match variant:
                case 'Google':
                    list_file.write(google_converter(line.replace('||', '')))
                case 'Duckduckgo':
                    list_file.write(duckduckgo_converter(line.replace('||', '')))
        else:
            if '! Title:' in line:
                list_file.write(f'{line}, {variant} edition\n')
            else:
                list_file.write(f'{line}\n')

    list_file.close()

for version in variants:
    generate_list(version)
