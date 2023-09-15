def hofstadter_q(n):
  """
  Calculates the Hofstadter Q-sequence value for the given integer.

  Args:
    n: The integer value.

  Returns:
    The Hofstadter Q-sequence value for the given integer.
  """
  if n == 1 or n == 2:
    return 1
  else:
    return hofstadter_q(n - hofstadter_q(n - 1)) + hofstadter_q(n - hofstadter_q(n - 2))


def main():
  """
  The main function.
  """
  n = int(input("Enter an integer: "))
  print("The Hofstadter Q-sequence value for {} is {}".format(n, hofstadter_q(n)))


if _name_ == "_main_":
  main()
