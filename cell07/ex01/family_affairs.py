#!/usr/bin/python3

def find_the_redheads(family_mem: dict[str, str]) -> list[str]:
    return list(dict(filter(lambda kv: kv[1] == "red", family_mem.items())).keys())

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}

print(find_the_redheads(dupont_family))