def find_synonym_groups(synonyms):

    groups = []

    visited = set()

    for phrase1, phrase2 in synonyms:

        if phrase1 in visited or phrase2 in visited:

            continue

        group = set([phrase1, phrase2])

        visited.add(phrase1)

        visited.add(phrase2)

        for phrase3, phrase4 in synonyms:

            if phrase3 in group or phrase4 in group:

                group.add(phrase3)

                group.add(phrase4)

                visited.add(phrase3)

                visited.add(phrase4)

        groups.append(group)

    return groups

synonyms = [

    {"Dg set": "Diesel generator"},

    {"Organization": "Organisation"},

    {"Group": "Organization"},

    {"Orange": "Kinnu"},

    {"Orange": "narangi"}

]

print(find_synonym_groups(synonyms))

