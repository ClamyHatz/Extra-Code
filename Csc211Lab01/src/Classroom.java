public class Classroom {
    public static void main(String[] args) {
        Student william = new Student("William");

        System.out.println("We have " + Student.studentCount + " students");
        System.out.println("his name is " + william.getName());

        System.out.println("He currently has " + william.getPoints() + " points");
        System.out.println("He did not fail his physics exam so lets give him 50 pts");
        william.setPoints(50);
        System.out.println("He now has " + william.getPoints() + " points");

        System.out.println("JK he failed so lets subtract 75 points");
        william.setPoints(william.getPoints() - 75);

        Student larry = new Student("Larry");
        System.out.println("New student enrolled, total " + Student.studentCount + " enrolled\n" +
                "His name is " + larry.getName());

        System.out.println("Larry will now tutor William");
        larry.tutorStudent(william);
        System.out.println(william.getPoints());
        
    }
}
