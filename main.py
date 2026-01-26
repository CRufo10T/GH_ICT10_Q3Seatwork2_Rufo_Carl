from pyscript import display, document


def team_checker(e):
    registration = document.getElementById("Regis").value.lower()
    clearance = document.getElementById("clinic").value.lower()
    grade = document.getElementById("grades").value.lower()
    section = document.getElementById("sections").value.lower()
    document.getElementById("output").innerHTML = ""

    if registration == "yes" and clearance == "yes" and grade in ["7", "8", "9", "10"]:
        display("You are eligible for the team", target="output")
    else:
        display("You are not eligible for the team", target="output")
        
        

    if section == "emerald":
        display("Your team is Blue Bears", target="output")
    elif section == "ruby":
        display("Your team is Red BullDogs", target="output")
    elif section == "sapphire":
        display("Your team is Yellow Tigers", target="output")
    elif section == "topaz":
        display("Your team is Green Hornets", target="output")
    else:
        display("You are NOT eligible for the team", target="output")

        