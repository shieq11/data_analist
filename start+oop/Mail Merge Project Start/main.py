
with open(r"\Users\shieq\OneDrive\Pulpit\python\udemy\data_analist\Mail Merge Project Start\Input\Names\invited_names.txt", mode="r") as f:
    names = f.readlines()

with open(r"/start+oop/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as g:
    letter = g.read()
    for nam in names:
        p = nam.strip()
        x = letter.replace("[name]", p)
        with open(f"./Output/ReadyToSend/letter_for_{p}.txt", mode="w") as data:
            data.write(x)






#
#     g.readlines()
#     letter = g.read()
#
#
# for nam in name:
#
#     x = letter.replace("[name]", nam)
#     f.write(x)
#     f.close()


