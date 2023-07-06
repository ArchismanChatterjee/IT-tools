public class Kinematics {

    public static void main(String[] args) {
        // A simple Java code to find out the velocity and displacement of an object 
        // after 1 second. 
        // Initialize the object's initial velocity and acceleration.
        // Encoding's in UTF-8.
        float v0 = 5.0f;
        float a = 2.0f;

        // Calculate the object's velocity after 1 second.
        float v = v0 + a * 1.0f;

        // Calculate the object's displacement after 1 second.
        float Δx = v0 * 1.0f + 1/2 * a * 1.0f * 1.0f;

        // Print the object's velocity and displacement.
        System.out.println("Velocity: " + v);
        System.out.println("Displacement: " + Δx);
    }
}