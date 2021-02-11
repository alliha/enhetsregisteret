import requests
import json
import tkinter as tk
import tkinter.scrolledtext as st

"""
Lag en oversikt over de ulike organisasjonsformene som finnes, med tilhørende kode og beskrivelse.
Lag en visuell oversikt over organisasjonsnummer 956338581 med alle relevante data. Det vil si antall ansatte, navn, organisasjonsform, næringskode osv. (Finner du ikke dette organisasjonsnummeret, velg et annet)
Skriv en kortfattet dokumentasjon av programkoden du lager.

"""


def get_json(api_endpoint):
    """Return JSON of organisation types"""
    response = requests.get("https://data.brreg.no/enhetsregisteret/api/" + api_endpoint)
    if response.status_code != 200:
        #Something went wrong
        raise Exception
    else:
        return response.json()

def parse_organizations(organizations):
    """Return list of tuples of org.-types and codes"""
    organizations_list = []
    for i in organizations["_embedded"]["organisasjonsformer"]:
        organizations_list.append((i["kode"], i["beskrivelse"]))
    return organizations_list

def orgtypes_renderer(orglist):
    """Display the different organization types"""
    window = tk.Tk()
    text_area = st.ScrolledText(window)
    for i in orglist:
        text_area.insert(tk.INSERT, i[0] + ": " + i[1] + "\n")

    text_area.grid()
    text_area.configure(state="disabled")
    window.mainloop()

def main():
    organizations = get_json("organisasjonsformer/")
    orglist = parse_organizations(organizations)
    orgtypes_renderer(orglist)

if __name__ == "__main__":
    main()