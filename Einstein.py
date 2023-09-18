import math

def threshold_frequency(work_function):
  """Calculates the threshold frequency given the work function."""
  h = 6.62607015 * 10**(-34)  # Planck constant
  return work_function / h


def stopping_potential(threshold_frequency, frequency):
  """Calculates the stopping potential given the threshold frequency and the frequency of incident radiation."""
  h = 6.62607015 * 10**(-34)  # Planck constant
  e = 1.60217662 * 10**(-19)  # Charge of an electron
  return (frequency - threshold_frequency) * h / e


# Example usage:

work_function = 2.3 * 10**(-19)  # Work function of sodium
threshold_frequency = threshold_frequency(work_function)
frequency = 5 * 10**14  # Frequency of incident radiation

# Calculate the stopping potential
stopping_potential = stopping_potential(threshold_frequency, frequency)

# Print the results
print("Threshold frequency:", threshold_frequency, "Hz")
print("Stopping potential:", stopping_potential, "V")
