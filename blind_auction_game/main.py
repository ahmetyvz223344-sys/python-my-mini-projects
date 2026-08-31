import art
print(art.logo)






data={
    "names":[],
    "bidds":[]

}
k=True
while k:
    b = input("what is your name?")
    a = int(input("what is your bidd?"))

    data["names"].append(b)
    data["bidds"].append(a)

    c = input("are there any other bidders? yes or no")
    if c == "yes":
        print("\n" * 100)


    if c == "no":
        k=False



the_most=data["bidds"]
r=max(the_most)
p=the_most.index(r)
f=data["names"][p]


print(f"the winner is {f} with a bid of ${r}")

