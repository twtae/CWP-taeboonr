#!/usr/bin/python3

def famous_births(persons: dict):
    sorted_by_birth = dict(sorted(persons.items(), key = lambda p: p[1]["date_of_birth"]))
    for name, info in sorted_by_birth.items():
        print(f"{info["name"]} is a great scientist born in {info["date_of_birth"]}.")

women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)