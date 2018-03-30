"""
Checkpoint 5: Shield made of arbitrary number of materials
----------------------------------------------------------

Pass a set of material properties representing any number of materials
in a shield each with their own thickness and attenuation coefficient.
"""

import math as m

def calc_phi(phi, mat_props):
    """Calculates final flux after two shields of different thicknesses
    and attenuation coefficients given the starting flux phi_0.

    Input:
    ------
        phi: float, initial flux value (photons/cm**2-s)
        mat_props: list of tuples, each tuple represents a set of
            properties for each material in the problem in the form
            [(mu0, x0), (mu1, x1), (mu2, x2) ... (muN, xN)] for any N
            number of shields. Each shielding material (one tuple)
            should be defined by:
                mu: float, attenuation coefficient (1/cm)
                x: float, shield thickness (cm)

    Returns:
    --------
        phi: float, final flux value after all shields (photons/cm**2-s)
    """

    # iterate over each shield in the property list
    for mat in mat_props:

        # unpack current shield properties mu and x
        mu = mat[0]
        x = mat[1]

        # update phi_0 with new flux value after attenuation through
        # current shield
        phi = phi * m.exp(-mu*x)

    # return final flux value
    return(phi)


# Set properties for three different shielding types (lead, plastic, and
# tungsten:
lead_props = (.125, 5.0)
plastic_props = (.02, 15.)
tungsten_props = (.120, 7.)

# Set initial flux
phi_0 = 1.e15

# Calculate using three shields (lead, plastic, and tungsten)
mat_props = [lead_props, plastic_props, tungsten_props]
phi_final = calc_phi(phi_0, mat_props)
print(phi_final)

# Calculate using two shields (lead and tungsten)
mat_props = [lead_props, tungsten_props]
phi_final = calc_phi(phi_0, mat_props)
print(phi_final)

# Calculate using one shield (lead)
mat_props = [lead_props]
phi_final = calc_phi(phi_0, mat_props)
print(phi_final)
