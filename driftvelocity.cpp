#include <iostream>

using namespace std;

double drift_velocity(double E, double m, double n) {
  /*
    This function calculates the drift velocity of electrons in a conductor.

    Args:
      E: The electric field strength.
      m: The mass of an electron.
      n: The number density of electrons.

    Returns:
      The drift velocity of electrons.
  */

  double vd = (E * m) / (n * pow(10, -19));
  return vd;
}

int main() {
  double E = 1000;
  double m = 9.11 * pow(10, -31);
  double n = 10 * pow(10, 28);
  double vd = drift_velocity(E, m, n);
  cout << "The drift velocity of electrons is " << vd << " m/s." << endl;
  return 0;
}