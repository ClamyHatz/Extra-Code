public class Student {
    private String name;
    private int points;
    public static int studentCount;

    public Student(String nameArg) {
        this.name = nameArg;
        this.points = 0;
        this.studentCount++;
    }
    public String getName(){
        return this.name;
    }
    public int getPoints(){
        return this.points;
    }
    public void setPoints(int pointsArg){
        this.points = pointsArg;
    }
    public int tutorStudent(Student otherStudent){
        otherStudent.setPoints(otherStudent.points + 1);
        return otherStudent.points;
    }

}
