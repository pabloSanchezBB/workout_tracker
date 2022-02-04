package workout_tracker.ver1.classfiles;

public class Workout
{
    private String name;
    private int num_exercises;
    private Exercise[] exercise_list;

    public Workout(String name, int num_exercises, Exercise[] exercise_list)
    {
        this.name = name;
        this.num_exercises = num_exercises;
        this.exercise_list = exercise_list;
    }

    // Getters:
    public String get_name()
    {
        return name;
    }

    public int get_num_exercises()
    {
        return num_exercises;
    }

    public Exercise[] get_exercise_list()
    {
        return exercise_list;
    }

    // Setters:
    public void set_name(String name)
    {
        this.name = name;
    }

    public void set_num_exercises(int num_exercises)
    {
        this.num_exercises = num_exercises;
    }

    public void set_exercise_list(Exercise[] exercise_list)
    {
        this.exercise_list = exercise_list;
    }
}
