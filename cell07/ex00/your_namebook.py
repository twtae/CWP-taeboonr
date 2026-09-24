#!/usr/bin/python3

def array_of_names(persons: dict[str, str]) -> list[str]:
    return [f"{f_name.capitalize()} {l_name.capitalize()}" for f_name, l_name in persons.items()]

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_names(persons))