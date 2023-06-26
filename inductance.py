// The aforementioned code is to be used  to calculate the mutual inductance of two concentric circular coils:


import math

def mutual_inductance(r1, r2, n1, n2):
  """
  Calculates the mutual inductance of two concentric circular coils.

  Args:
    r1: The radius of the inner coil (in cm).
    r2: The radius of the outer coil (in cm).
    n1: The number of turns in the inner coil.
    n2: The number of turns in the outer coil.

  Returns:
    The mutual inductance (in Henry).
  """

  mu_0 = 4 * math.pi * 10**-7  # The permeability of free space (in Henry/m).
  l = math.log(r2 / r1)  # The length of the common flux path (in cm).
  return mu_0 * n1 * n2 * l / (2 * math.pi)  # The mutual inductance (in Henry).

if __name__ == "__main__":
  r1 = 1  # The radius of the inner coil (in cm).
  r2 = 1000  # The radius of the outer coil (in cm).
  n1 = 10  # The number of turns in the inner coil.
  n2 = 200  # The number of turns in the outer coil.

  mutual_inductance = mutual_inductance(r1, r2, n1, n2)
  print("The mutual inductance is", mutual_inductance, "Henry.")
