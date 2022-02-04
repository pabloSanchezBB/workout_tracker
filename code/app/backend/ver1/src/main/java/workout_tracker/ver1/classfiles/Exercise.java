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

        for(int i;i<this.weight_per_set.length;++i) {
            set_weight_per_set(i, 0/*Change this to the User Input*/);
        }
    }

    // Setters:
    public void set_name(String name)
    {
        this.name = name;
    }

    public void set_num_sets(int num_sets)
    {
        this.num_sets = num_sets;
    }

    public void set_min_reps(int min_reps)
    {
        this.min_reps = min_reps;
    }

    public void set_max_reps(int max_reps)
    {
        this.max_reps = max_reps;
    }

    public void set_weight_per_set(int index, int weight)
    {
        this.weight_per_set[index] = weight;
    }

    // Getters:
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

    public int get_weight_per_set(int index)
    {
        try{
            return this.weight_per_set[index];
        } catch(ArrayIndexOutOfBoundsException e){
            e.printStackTrace();
        }

    }
}
