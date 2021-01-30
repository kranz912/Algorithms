import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;





public class Roundrobin{
    public void  Run(){
        Queue<Tasks> tasks = new LinkedList<>();
        List<Tasks> finished = new ArrayList<>();
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number of processes:");
        int processes = scan.nextInt();
        System.out.print("Enter quantum: ");
        int quantum = scan.nextInt();
        int time = 0;

        for(int i = 0; i<processes; i++){
            System.out.print("Enter burst time:");
            int bt = scan.nextInt();
            tasks.add(new Tasks("P"+i, bt));
        }

        while(!tasks.isEmpty()){
            Tasks t = tasks.remove();
            int remaining_time =t.getRemainingTime()-quantum;
            System.out.println(remaining_time);
            if(remaining_time>0){
                time+=quantum;
                t.setRemainingTime(remaining_time);
                tasks.add(t);
            }
            else{
                time+=t.getRemainingTime();
                t.setWaitTime(time-t.getBurstTime());
                finished.add(t);
            }

        }
        finished.sort(Comparator.comparing(Tasks::getTaskName));
        int total_waiting_time = 0;
        int total_turn_around_time =0;
        for (Tasks t : finished) {
            t.print();
            total_turn_around_time += t.getTurnAroundTime();
            total_waiting_time += t.getWaitingTime();
        }

        System.out.println("Average waiting time: "+ ((float)total_waiting_time/(float)processes));
        System.out.println("Average turn around time: "+ ((float)total_turn_around_time/(float)processes));
        


        scan.close();
    }
}
class Tasks{
    private int _waitingTime;
    private String _taskName;
    private int _burstTime;
    private int _turnAroundTime;
    private int _remainingTime;
    public Tasks(String taskname, int burstTime){
        _burstTime = burstTime;
        _remainingTime = _burstTime;
        _taskName = taskname;
    }
    public int getBurstTime(){
        return _burstTime;
    }
    public int getRemainingTime(){
        return this._remainingTime;
    }
    public void setRemainingTime(int remainingTime){
        this._remainingTime = remainingTime;
    }
    public void setWaitTime(int waitingTime){
        this._waitingTime = waitingTime;
        this._turnAroundTime = _waitingTime  + _burstTime;
    }
    public String getTaskName(){
        return this._taskName;
    }

    public int getWaitingTime(){
        return this._waitingTime;
    }
    public int getTurnAroundTime(){
        return this._turnAroundTime;
    }
    public void print(){
        System.out.println(
            "Task name:\t"+_taskName+
            "\tBurst time \t"+_burstTime+
            "\tWaiting time:\t"+_waitingTime+
            "\t Turn Around time \t"+ _turnAroundTime
            );
    }
    

}
class Solution{
    public static void main(String[] args) {
        new Roundrobin().Run();
    }
}