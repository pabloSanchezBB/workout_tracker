package workout_tracker.ver1.classfiles;

public class Exercise
{
    private String name;
    private int num_sets;
    private int min_reps;
    private int max_reps;
    private int[] weight_per_set;

    public Exercise(String name, int num_sets, int min_reps, int max_reps)
    {
        this.name = name;
        this.num_sets = num_sets;
        this.min_reps = min_reps;
        this.max_reps = max_reps;
        this.weight_per_set = new int[num_sets];
    }

    public String get_name()
    {
        return this.name;
    }

    public int get_num_sets()
    {
        return this.num_sets;
    }

    public int get_min_reps()
    {
        return this.min_reps;
    }

    public int get_max_reps()
    {
        return this.max_reps;
    }
}
