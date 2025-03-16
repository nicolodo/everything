
favorite_languages = {
    'jen': 'python',
    'charles': 'C',
    'Benny': 'Java',
    'House': 'Rust',
    'Mike': 'python'
}

# language = favorite_languages['jen'].title()
# print(f"Jen's favourite language is {language}")

for k,v in favorite_languages.items():
    print(k,':',v)

for name in sorted(favorite_languages):
    print(name)

for language in set(favorite_languages.values()):
    print(language)