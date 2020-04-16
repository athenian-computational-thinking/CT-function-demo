# This function wil calculate the kinetic energy of an object, using parameters mass and velocity.

def kinetic_energy(m, v):
    KE =  (m * v**2) / 2
    return KE

mass = float(input("Enter the mass in kilograms: "))
velocity = float(input("Enter the velocity in m/s: "))


print(kinetic_energy(mass, velocity))

# or I can do this:
kin_en = kinetic_energy(mass, velocity)

print(kin_en)
print("The object's KE is" , kin_en, "Joules")