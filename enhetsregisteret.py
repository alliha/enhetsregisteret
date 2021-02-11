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

def orgtypes_renderer(orglist, window):
    """Display the different organization types"""
    frame = tk.Frame(master=window, width=128, pady=4, bd=0)
    frame.grid()
    text_area = st.ScrolledText(master=frame, font=("serif", 12))
    for i in orglist:
        text_area.insert(tk.INSERT, i[0] + ": " + i[1] + "\n")
    text_area.grid()
    text_area.configure(state="disabled")

def specific_org_render(organization, window):
    """Displays certain information about a certain org."""
    frame1 = tk.Frame(master=window, pady=4)
    frame1.grid()

    header_label = tk.Label(master=frame1, text="Oppgåve 2:", 
        font=("serif", 12), width=87, justify="left", anchor="w")
    header_label.grid()

    navn_label = tk.Label(master=frame1, text=organization["navn"], 
        font=("serif", 16), width=64, justify="left", anchor="w")
    navn_label.grid()

    org_form_label = tk.Label(master=frame1, 
        text=(organization["organisasjonsform"]["kode"] + ": "
        + organization["organisasjonsform"]["beskrivelse"]), 
        font=("serif", 12), width=87, justify="left", anchor="w")
    org_form_label.grid()

    org_næring_label = tk.Label(master=frame1, text=("Næringsform "
        + organization["naeringskode1"]["kode"]+": "
        + organization["naeringskode1"]["beskrivelse"]),
        font=("serif", 12), width=87, justify="left", anchor="w")
    org_næring_label.grid()

    org_ansatte_label = tk.Label(master=frame1, text=("Ansatte: "
        + str(organization["antallAnsatte"])), 
        font=("serif", 12), width=87, justify="left", anchor="w")
    org_ansatte_label.grid()

    org_adress = ""
    if organization["forretningsadresse"]["adresse"]:
        org_adress = " ".join(organization["forretningsadresse"]["adresse"])\
        + ", "
    org_adresse_label = tk.Label(master=frame1, text=("Adr.: " + org_adress
        + organization["forretningsadresse"]["postnummer"] + " "
        + organization["forretningsadresse"]["poststed"]),
        font=("serif", 12), width=87, justify="left", anchor="w")
    org_adresse_label.grid()

    org_stiftelse_label = tk.Label(master=frame1, text=("Stifta: "
        + organization["stiftelsesdato"]),
        font=("serif", 12), width=87, justify="left", anchor="w")
    org_stiftelse_label.grid()


def main():
    window = tk.Tk()

    organizations = get_json("organisasjonsformer/")
    orglist = parse_organizations(organizations)
    orgtypes_renderer(orglist, window)

    some_org = get_json("enheter/956338581")
    specific_org_render(some_org, window)

    window.mainloop()

if __name__ == "__main__":
    main()