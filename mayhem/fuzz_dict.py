#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    import pyphen

languages = list(pyphen.LANGUAGES.keys())

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    chosen_lang = languages[fdp.ConsumeIntInRange(0, len(languages)-1)]
    clkr = pyphen.Pyphen(lang=chosen_lang)
    total_str = fdp.ConsumeString(atheris.ALL_REMAINING)
    half_len = len(total_str) // 2
    clkr.inserted(total_str[:half_len])
    clkr.wrap(total_str[half_len:], fdp.ConsumeIntInRange(0, half_len))

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
