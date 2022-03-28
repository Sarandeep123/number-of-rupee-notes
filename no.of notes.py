am=int(input("Enter the amount"))
H=am//100
am=am%100
F=am//50
am=am%50
Tw=am//20
am=am%20
Te=am//10
am=am%10
Fiv=am//5
Total_notes=H+F+Tw+Te+Fiv
print("The number of notes are:",Total_notes)
